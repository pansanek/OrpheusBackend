import traceback
from typing import List
from uuid import UUID

from sqlalchemy.orm import Session

from app.database import get_db
from app.models.message_model import Message
from app.schemas.message_schema import Message as DBMessage


class MessageRepo:
    db: Session

    def __init__(self) -> None:
        self.db = next(get_db())

    def _map_to_model(self, message: DBMessage) -> Message:
        result = Message.from_orm(message)
        return result

    def _map_to_schema(self, message: Message) -> DBMessage:
        data = dict(message)
        result = DBMessage(**data)
        return result

    def create_message(self, message: Message) -> Message:
        try:
            db_message = self._map_to_schema(message)
            self.db.add(db_message)
            self.db.commit()
            return self._map_to_model(db_message)
        except Exception as e:
            traceback.print_exc()
            self.db.rollback()
            raise e

    def get_all_messages(self) -> List[Message]:
        messages = []
        for b in self.db.query(DBMessage).all():
            messages.append(self._map_to_model(b))
        return messages

    def get_message_by_id(self, message_id: UUID) -> Message:
        message = self.db \
            .query(DBMessage) \
            .filter(DBMessage.id == message_id) \
            .first()

        if message is None:
            raise KeyError(f"Message with id {message_id} not found.")
        return self._map_to_model(message)

    def get_messages_by_chat_id(self, chat_id: UUID) -> List[Message]:
        messages = self.db.query(DBMessage).filter(DBMessage.chat_id == chat_id).all()

        if not messages:
            raise KeyError(f"Messages with chat_id {chat_id} not found.")

        return [self._map_to_model(message) for message in messages]
