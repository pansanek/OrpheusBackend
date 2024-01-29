from datetime import datetime
from typing import List
from uuid import UUID, uuid4

from fastapi import Depends

from app.models.message_model import Message, Chat, User
from app.repositories.db_message_repo import MessageRepo


class MessageService:
    message_repo: MessageRepo

    def __init__(self, message_repo: MessageRepo = Depends(MessageRepo)) -> None:
        self.message_repo = message_repo

    def get_all_messages(self) -> List[Message]:
        return self.message_repo.get_all_messages()

    def get_message_by_id(self, message_id: UUID) -> Message:
        return self.message_repo.get_message_by_id(message_id)

    def create_message(self, chat: Chat,
                       from_user: User,
                       content: str) -> Message:
        message = Message(id=uuid4(), chat=chat, from_user=from_user, content=content,
                          timestamp=datetime.utcnow())
        return self.message_repo.create_message(message)
