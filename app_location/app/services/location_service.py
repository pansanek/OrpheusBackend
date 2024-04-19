from typing import List
from uuid import UUID, uuid4

from fastapi import Depends

from app.models.location_model import Location
from app.repositories.location_repo import LocationRepo


class LocationService:
    location_repo: LocationRepo

    def __init__(self, location_repo: LocationRepo = Depends(LocationRepo)) -> None:
        self.location_repo = location_repo

    def get_all_locations(self) -> List[Location]:
        return self.location_repo.get_locations()

    def get_location_by_id(self, location_id: UUID) -> Location:
        return self.location_repo.get_location_by_id(location_id)

    def create_location(self, admin: dict, name: str, address: str, about: str,profile_picture:dict) -> Location:
        location = Location(id=uuid4(), admin=admin, name=name, address=address, about=about, profile_picture=profile_picture)
        return self.location_repo.create_location(location)
