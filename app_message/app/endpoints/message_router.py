from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app_message.app.models.message_model import Message, CreateMessageRequest
from app_message.app.services.message_service import MessageService

message_router = APIRouter(prefix='/messages', tags=['Messages'])


@message_router.get('/')
def get_messages(message_service: MessageService = Depends(MessageService)) -> List[Message]:
    return message_service.get_all_messages()


@message_router.post('/')
def create_message(
        message_info: CreateMessageRequest,
        message_service: MessageService = Depends(MessageService)
) -> Message:
    try:
        message = message_service.create_message(
            chat_id=message_info.chat_id,
            from_user=message_info.from_user,
            timestamp = message_info.timestamp,
            content = message_info.content
        )
        return message.dict()
    except KeyError:
        raise HTTPException(400, f'message with name={message_info.name} already exists')


@message_router.get('/{id}')
def get_message_by_id(id: UUID, message_service: MessageService = Depends(MessageService)) -> Message:
    try:
        message = message_service.get_message_by_id(id)
        return message.dict()
    except KeyError:
        raise HTTPException(404, f'message with id={id} not found')


@message_router.put('/{message_id}')
def update_message(
        message_id: UUID,
        message_info: CreateMessageRequest,
        message_service: MessageService = Depends(MessageService)
) -> Message:
    try:
        updated_message = message_service.update_message(
            message_id=message_id,
            chat_id=message_info.chat_id,
            from_user=message_info.from_user,
            timestamp=message_info.timestamp,
            content=message_info.content
        )
        return updated_message
    except KeyError:
        raise HTTPException(404, f'Message with id={message_id} not found')