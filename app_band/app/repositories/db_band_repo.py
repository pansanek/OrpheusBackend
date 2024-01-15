import traceback
from typing import List
from uuid import UUID
from sqlalchemy.orm import Session

from app_band.app.database import get_db
from app_band.app.models.band_model import Band
from app_band.app.schemas.band_schema import Band as DBBand

class BandRepo:
    db: Session

    def __init__(self) -> None:
        self.db = next(get_db())

    def _map_to_model(self, band: DBBand) -> Band:
        result = Band.from_orm(band)
        return result

    def _map_to_schema(self, band: Band) -> DBBand:
        data = dict(band)
        result = DBBand(**data)
        return result

    def create_band(self, band: Band) -> Band:
        try:
            db_band = self._map_to_schema(band)
            self.db.add(db_band)
            self.db.commit()
            return self._map_to_model(db_band)
        except Exception as e:
            traceback.print_exc()
            self.db.rollback()
            raise e

    def get_all_bands(self) -> List[Band]:
        bands = []
        for b in self.db.query(DBBand).all():
            bands.append(self._map_to_model(b))
        return bands

    def get_band_by_id(self, band_id: UUID) -> Band:
        band = self.db \
            .query(DBBand) \
            .filter(DBBand.id == band_id) \
            .first()

        if band is None:
            raise KeyError(f"Band with id {band_id} not found.")
        return self._map_to_model(band)
