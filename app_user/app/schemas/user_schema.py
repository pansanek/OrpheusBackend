from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, unique=True, nullable=False)
    login = Column(String, index=True, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, index=True, unique=True, nullable=False)
    about = Column(String, nullable=True)
    user_type = Column(String, nullable=False)
