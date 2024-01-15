from typing import List
from uuid import UUID, uuid4

from fastapi import Depends

from app_location.app.models.location_model import Location
from app_location.app.repositories.db_location_repo import LocationRepo


class LocationService:
    location_repo: LocationRepo

    def __init__(self, location_repo: LocationRepo = Depends(LocationRepo)) -> None:
        self.location_repo = location_repo

    def get_all_locations(self) -> List[Location]:
        return self.location_repo.get_all_locations()

    def get_location_by_id(self, location_id: UUID) -> Location:
        return self.location_repo.get_location_by_id(location_id)

    def create_location(self, admin_id: UUID, name: str, address: str, about: str) -> Location:
        location = Location(id=uuid4(), admin_id=admin_id, name=name, address=address, about=about, profile_picture={})
        return self.location_repo.create_location(location)
