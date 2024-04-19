from typing import List
from uuid import UUID, uuid4

from fastapi import Depends

from app.models.chat_model import Chat, User
from app.repositories.chat_repo import ChatRepo


class ChatService:
    chat_repo: ChatRepo

    def __init__(self, chat_repo: ChatRepo = Depends(ChatRepo)) -> None:
        self.chat_repo = chat_repo

    def get_all_chats(self) -> List[Chat]:
        return self.chat_repo.get_chats()

    def get_chat_by_id(self, chat_id: UUID) -> Chat:
        return self.chat_repo.get_chat_by_id(chat_id)

    def create_chat(self, creator: dict, second_user: dict, picture=dict,last_message=str,
                    name=str) -> Chat:
        users = []
        users.append(creator.__dict__)
        users.append(second_user.__dict__)
        chat = Chat(id=uuid4(), users=users, last_message=last_message,name=name,picture=picture)
        return self.chat_repo.create_chat(chat)

    def update_chat_last_message(self, chat_id: UUID, last_message: str) -> Chat:
        chat = self.chat_repo.get_chat_by_id(chat_id)
        chat.last_message = last_message
        return self.chat_repo.update_chat_last_message(chat)
