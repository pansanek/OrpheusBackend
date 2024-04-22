from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app_notification.app.models.notification_model import CreateNotificationRequest
from app_notification.app.models.notification_model import Notification
from app_notification.app.services.notification_service import NotificationService

notification_router = APIRouter(prefix='/notifications', tags=['Notifications'])


@notification_router.get('/')
def get_notifications(notification_service: NotificationService = Depends(NotificationService)) -> list[Notification]:
    return notification_service.get_all_notifications()


@notification_router.post('/')
def create_notification(
        notification_info: CreateNotificationRequest,
        notification_service: NotificationService = Depends(NotificationService)
) -> Notification:
    try:
        notification = notification_service.create_notification(
            type=notification_info.type,
            title=notification_info.title,
            contentDescription=notification_info.contentDescription,
            date=notification_info.date,
            fromUser=notification_info.fromUser,
            toUser=notification_info.toUser,
            postItem=notification_info.postItem,
            bandItem=notification_info.bandItem,
        )
        return notification.dict()
    except KeyError:
        raise HTTPException(400, f'Notification with title={notification_info.title} already exists')


@notification_router.get('/{id}')
def get_notification_by_id(id: UUID,
                           notification_service: NotificationService = Depends(NotificationService)) -> Notification:
    try:
        notification = notification_service.get_notification_by_id(id)
        return notification.dict()
    except KeyError:
        raise HTTPException(404, f'Notification with id={id} not found')


