import traceback
from typing import List
from uuid import UUID

from sqlalchemy.orm import Session

from app.database import get_db
from app.models.chat_model import Chat
from app.schemas.chat_schema import Chat as DBChat


class ChatRepo:
    db: Session

    def __init__(self) -> None:
        self.db = next(get_db())

    def _map_to_model(self, chat: DBChat) -> Chat:
        result = Chat.from_orm(chat)
        return result

    def _map_to_schema(self, chat: Chat) -> DBChat:
        data = dict(chat)
        result = DBChat(**data)
        return result

    def create_chat(self, chat: Chat) -> Chat:
        try:
            db_chat = self._map_to_schema(chat)
            self.db.add(db_chat)
            self.db.commit()
            return self._map_to_model(db_chat)
        except Exception as e:
            traceback.print_exc()
            self.db.rollback()
            raise e

    def get_all_chats(self) -> List[Chat]:
        chats = []
        for b in self.db.query(DBChat).all():
            chats.append(self._map_to_model(b))
        return chats

    def get_chat_by_id(self, chat_id: UUID) -> Chat:
        chat = self.db \
            .query(DBChat) \
            .filter(DBChat.id == chat_id) \
            .first()

        if chat is None:
            raise KeyError(f"Chat with id {chat_id} not found.")
        return self._map_to_model(chat)

    def update_chat_last_message(self, chat:Chat) -> Chat:
        try:
            db_chat = self.db \
                .query(DBChat) \
                .filter(DBChat.id == chat.id) \
                .first()
            db_chat.last_message = chat.last_message
            self.db.commit()
            return self._map_to_model(db_chat)
        except:
            traceback.print_exc()
            raise KeyError