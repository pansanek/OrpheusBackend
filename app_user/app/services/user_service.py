from typing import List
from uuid import UUID, uuid4

from fastapi import Depends

from app.models.user_model import User
from app.repositories.user_repo import UserRepo


class UserService:
    user_repo: UserRepo

    def __init__(self, user_repo: UserRepo = Depends(UserRepo)) -> None:
        self.user_repo = user_repo

    def get_all_users(self) -> List[User]:
        return self.user_repo.get_users()

    def get_user_by_id(self, user_id: UUID) -> User:
        return self.user_repo.get_user_by_id(user_id)


    def create_user(self, login: str, name: str, password: str, email: str, about: str, user_type: str,
                    profile_picture: str,
                    background_picture: str,
                    settings: str) -> User:
        user = User(id=uuid4(), login=login, name=name, password=password, email=email, about=about,
                    user_type=user_type,
                    profile_picture=profile_picture, background_picture=background_picture, settings=settings)
        return self.user_repo.create_user(user)
