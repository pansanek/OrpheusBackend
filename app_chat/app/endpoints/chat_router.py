from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app_chat.app.models.chat_model import Chat, CreateChatRequest
from app_chat.app.services.chat_service import ChatService

chat_router = APIRouter(prefix='/chats', tags=['Chats'])


@chat_router.get('/')
def get_chats(chat_service: ChatService = Depends(ChatService)) -> List[Chat]:
    return chat_service.get_all_chats()


@chat_router.post('/')
def create_chat(
        chat_info: CreateChatRequest,
        chat_service: ChatService = Depends(ChatService)
) -> Chat:
    try:
        chat = chat_service.create_chat(
            users = chat_info.users,
            last_message=chat_info.last_message,
            picture=chat_info.picture,
            name=chat_info.name,
        )
        return chat.dict()
    except KeyError:
        raise HTTPException(400, f'chat with name={chat_info.name} already exists')


@chat_router.get('/{id}')
def get_chat_by_id(id: UUID, chat_service: ChatService = Depends(ChatService)) -> Chat:
    try:
        chat = chat_service.get_chat_by_id(id)
        return chat.dict()
    except KeyError:
        raise HTTPException(404, f'chat with id={id} not found')



@chat_router.put('/{chat_id}')
def update_chat(
        chat_id: UUID,
        chat_info: CreateChatRequest,
        chat_service: ChatService = Depends(ChatService)
) -> Chat:
    try:
        updated_chat = chat_service.update_chat(
            chat_id=chat_id,
            users=chat_info.users,
            last_message=chat_info.last_message,
            picture=chat_info.picture,
            name=chat_info.name,
        )
        return updated_chat
    except KeyError:
        raise HTTPException(404, f'Chat with id={chat_id} not found')