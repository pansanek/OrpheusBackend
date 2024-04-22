from datetime import datetime
from typing import List
from uuid import UUID, uuid4

from fastapi import Depends

from app_message.app.models.message_model import Message
from app_message.app.repositories.message_repo import MessageRepo


class MessageService:
    message_repo: MessageRepo

    def __init__(self, message_repo: MessageRepo = Depends(MessageRepo)) -> None:
        self.message_repo = message_repo

    def get_all_messages(self) -> List[Message]:
        return self.message_repo.get_messages()

    def get_message_by_id(self, message_id: UUID) -> Message:
        return self.message_repo.get_message_by_id(message_id)

    def create_message(self, chat_id: UUID,
                       from_user:dict,
                       timestamp:str,
                       content: str) -> Message:
        message = Message(id=uuid4(), chat_id=chat_id, from_user=from_user, content=content,
                          timestamp=timestamp)
        return self.message_repo.create_message(message)

    def update_message(self, message_id: UUID, chat_id: UUID,
                       from_user:dict,
                       timestamp:str,
                       content: str) -> Message:
        message = Message(id=message_id, chat_id=chat_id, from_user=from_user, content=content,
                          timestamp=timestamp)
        return self.message_repo.update_message(message)
