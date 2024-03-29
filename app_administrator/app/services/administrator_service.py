from typing import List
from uuid import UUID, uuid4

from fastapi import Depends

from app.models.administrator_model import Administrator, User
from app.repositories.db_administrator_repo import AdministratorRepo


class AdministratorService:
    admin_repo: AdministratorRepo

    def __init__(self, admin_repo: AdministratorRepo = Depends(AdministratorRepo)) -> None:
        self.admin_repo = admin_repo

    def get_all_administrators(self) -> List[Administrator]:
        return self.admin_repo.get_all_administrators()

    def get_administrator_by_id(self, admin_id: UUID) -> Administrator:
        return self.admin_repo.get_administrator_by_id(admin_id)

    def create_administrator(self, user: User, location_id: UUID) -> Administrator:
        administrator = Administrator(id=uuid4(), user=user, location_id=location_id)
        return self.admin_repo.create_administrator(administrator)
