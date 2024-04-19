from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.models.chat_model import chat, CreateChatRequest
from app.services.chat_service import chatService

chat_router = APIRouter(prefix='/chats', tags=['Chats'])


@chat_router.get('/')
def get_chats(chat_service: chatService = Depends(chatService)) -> List[chat]:
    return chat_service.get_all_chats()


@chat_router.post('/')
def create_chat(
        chat_info: CreateChatRequest,
        chat_service: chatService = Depends(chatService)
) -> chat:
    try:
        chat = chat_service.create_chat(
            creator=chat_info.creator,
            second_user=chat_info.second_user,
            last_message=chat_info.last_message,
            picture=chat_info.picture,
            name=chat_info.name,
        )
        return chat.dict()
    except KeyError:
        raise HTTPException(400, f'chat with name={chat_info.name} already exists')


@chat_router.get('/{id}')
def get_chat_by_id(id: UUID, chat_service: chatService = Depends(chatService)) -> chat:
    try:
        chat = chat_service.get_chat_by_id(id)
        return chat.dict()
    except KeyError:
        raise HTTPException(404, f'chat with id={id} not found')


@chat_router.post('/{id}/update')
def update_chat_last_message(
        id: UUID,
        lastMessage: str,
        chat_service: chatService = Depends(chatService)
) -> chat:
    try:
        chat = chat_service.update_chat_last_message(
            id=id,
            last_message=lastMessage
        )
        return chat.dict()
    except KeyError:
        raise HTTPException(400, f'Error')
