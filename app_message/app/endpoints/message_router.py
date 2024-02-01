from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.models.message_model import message, CreateMessageRequest
from app.services.message_service import messageService

message_router = APIRouter(prefix='/messages', tags=['Messages'])


@message_router.get('/')
def get_messages(message_service: messageService = Depends(messageService)) -> List[message]:
    return message_service.get_all_messages()


@message_router.post('/')
def create_message(
        message_info: CreateMessageRequest,
        message_service: messageService = Depends(messageService)
) -> message:
    try:
        message = message_service.create_message(
            chat=message_info.chat,
            from_user=message_info.from_user,
            content = message_info.content
        )
        return message.dict()
    except KeyError:
        raise HTTPException(400, f'message with name={message_info.name} already exists')


@message_router.get('/{id}')
def get_message_by_id(id: UUID, message_service: messageService = Depends(messageService)) -> message:
    try:
        message = message_service.get_message_by_id(id)
        return message.dict()
    except KeyError:
        raise HTTPException(404, f'message with id={id} not found')


@message_router.get('/chat/{id}')
def get_message_by_chat_id(id: UUID, message_service: messageService = Depends(messageService)) -> List[message]:
    try:
        return message_service.get_message_by_chat_id(id)
    except KeyError:
        raise HTTPException(404, f'chat with id={id} not found')

