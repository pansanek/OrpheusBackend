from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.models.user_model import CreateUserRequest
from app.models.user_model import User
from app.services.user_service import UserService

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
            user_type=user_info.user_type
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


@user_router.get('/auth')
def authorize(login: str, password: str, user_service: UserService = Depends(UserService)) -> str:
    try:
        response = user_service.authorize(login,password)
        return response
    except KeyError:
        raise HTTPException(404, f'User with id={id} not found')