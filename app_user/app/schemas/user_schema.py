from sqlalchemy import Column, String, Enum, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship

from app_user.app.models.user_model import UserTypes
from app_user.app.schemas.base_schema import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, unique=True, nullable=False)
    login = Column(String, index=True, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, index=True, unique=True, nullable=False)
    about = Column(String, nullable=True)
    user_type = Column(Enum(UserTypes), nullable=False)
    profile_picture = Column(JSON, nullable=True)
    background_picture = Column(JSON, nullable=True)
    settings = Column(JSON, nullable=False)
