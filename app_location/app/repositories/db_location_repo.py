import traceback
from typing import List
from uuid import UUID

from sqlalchemy.orm import Session

from app_location.app.database import get_db
from app_location.app.models.location_model import Location
from app_location.app.schemas.location_schema import Location as DBLocation


class LocationRepo:
    db: Session

    def __init__(self) -> None:
        self.db = next(get_db())

    def _map_to_model(self, location: DBLocation) -> Location:
        result = Location.from_orm(location)
        return result

    def _map_to_schema(self, location: Location) -> DBLocation:
        data = dict(location)
        result = DBLocation(**data)
        return result

    def create_location(self, location: Location) -> Location:
        try:
            db_location = self._map_to_schema(location)
            self.db.add(db_location)
            self.db.commit()
            return self._map_to_model(db_location)
        except Exception as e:
            traceback.print_exc()
            self.db.rollback()
            raise e

    def get_all_locations(self) -> List[Location]:
        locations = []
        for l in self.db.query(DBLocation).all():
            locations.append(self._map_to_model(l))
        return locations

    def get_location_by_id(self, location_id: UUID) -> Location:
        location = self.db \
            .query(DBLocation) \
            .filter(DBLocation.id == location_id) \
            .first()

        if location is None:
            raise KeyError(f"Location with id {location_id} not found.")
        return self._map_to_model(location)
