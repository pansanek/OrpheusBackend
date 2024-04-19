from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.models.user_model import CreateNotificationRequest
from app.models.user_model import Notification
from app.services.user_service import NotificationService

user_router = APIRouter(prefix='/users', tags=['Notifications'])


@user_router.get('/')
def get_users(user_service: NotificationService = Depends(NotificationService)) -> list[Notification]:
    return user_service.get_all_users()


@user_router.post('/')
def create_user(
        user_info: CreateNotificationRequest,
        user_service: NotificationService = Depends(NotificationService)
) -> Notification:
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
        raise HTTPException(400, f'Notification with login={user_info.login} already exists')


@user_router.get('/{id}')
def get_user_by_id(id: UUID, user_service: NotificationService = Depends(NotificationService)) -> Notification:
    try:
        user = user_service.get_user_by_id(id)
        return user.dict()
    except KeyError:
        raise HTTPException(404, f'Notification with id={id} not found')


@user_router.get('/auth')
def authorize(login: str, password: str, user_service: NotificationService = Depends(NotificationService)) -> str:
    try:
        response = user_service.authorize(login,password)
        return response
    except KeyError:
        raise HTTPException(404, f'Notification with id={id} not found')