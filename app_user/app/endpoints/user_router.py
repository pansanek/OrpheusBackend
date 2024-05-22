import os
import datetime
from io import BytesIO

import jwt
from typing import Annotated

from dateutil.relativedelta import relativedelta
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException,UploadFile, File, Form

from MinioHandler import MinioHandler, UploadFileResponse, CustomException
from app_user.app.models.user_model import CreateUserRequest
from app_user.app.models.user_model import User
from app_user.app.services.user_service import UserService

user_router = APIRouter(prefix='/users', tags=['Users'])


@user_router.get('/')
def get_users(user_service: UserService = Depends(UserService)) -> list[User]:
    return user_service.get_all_users()


@user_router.post('/')
def create_user(
        user_info: CreateUserRequest,
        user_service: UserService = Depends(UserService)
) -> User:
    try:
        user = user_service.create_user(
            login=user_info.login,
            name=user_info.name,
            password=user_info.password,
            email=user_info.email,
            about=user_info.about,
            user_type=user_info.user_type,
            profile_picture=user_info.profile_picture ,
            background_picture=user_info.background_picture ,
            settings=user_info.settings
        )
        return user.dict()
    except KeyError:
        raise HTTPException(400, f'User with login={user_info.login} already exists')


@user_router.get('/{id}')
def get_user_by_id(id: UUID, user_service: UserService = Depends(UserService)) -> User:
    try:
        user = user_service.get_user_by_id(id)
        return user.dict()
    except KeyError:
        raise HTTPException(404, f'User with id={id} not found')

@user_router.put('/{user_id}')
def update_user(
        user_id: UUID,
        user_info: CreateUserRequest,
        user_service: UserService = Depends(UserService)
) -> User:
    try:
        updated_user = user_service.update_user(
            user_id=user_id,
            login=user_info.login,
            name=user_info.name,
            password=user_info.password,
            email=user_info.email,
            about=user_info.about,
            user_type=user_info.user_type,
            profile_picture=user_info.profile_picture,
            background_picture=user_info.background_picture,
            settings=user_info.settings
        )
        return updated_user
    except KeyError:
        raise HTTPException(404, f'User with id={user_id} not found')


@user_router.post('/upload')
async def upload(file: Annotated[UploadFile, Form()]):
    MinioHandler().get_instance().upload_file(file.filename, file.file, file.size)
    return {
        "status": "uploaded",
        "name": file.filename
    }


@user_router.get('/list')
async def list_files():
    return MinioHandler().get_instance().list()


@user_router.get('/link/{file}')
async def link(file: str):
    obj = MinioHandler().get_instance().stats(file)
    payload = {
        "filename": obj.object_name,
        "valid_til": str(datetime.datetime.utcnow() + relativedelta(minutes=int(os.getenv('LINK_VALID_MINUTES', 10))))
    }
    encoded_jwt = jwt.encode(payload, os.getenv('JWT_SECRET'), algorithm="HS256")

    return {
        "link": f"/download/{encoded_jwt}"
    }






@user_router.post("/upload/minio", response_model=UploadFileResponse)
async def upload_file_to_minio(file: UploadFile = File(...)):
    try:
        data = file.file.read()

        file_name = " ".join(file.filename.strip().split())

        data_file = MinioHandler().get_instance().put_object(
            file_name=file_name,
            file_data=BytesIO(data),
            content_type=file.content_type
        )
        return data_file
    except CustomException as e:
        raise e
    except Exception as e:
        if e.__class__.__name__ == 'MaxRetryError':
            raise CustomException(http_code=400, code='400', message='Can not connect to Minio')
        raise CustomException(code='999', message='Server Error')
