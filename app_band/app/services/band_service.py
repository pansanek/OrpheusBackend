from typing import List
from uuid import UUID, uuid4
from fastapi import Depends

from app_band.app.models.band_model import Band
from app_band.app.models.genre_types import GenreTypes
from app_band.app.models.photo_url_model import PhotoUrl
from app_band.app.repositories.db_band_repo import BandRepo


class BandService:
    band_repo: BandRepo

    def __init__(self, band_repo: BandRepo = Depends(BandRepo)) -> None:
        self.band_repo = band_repo

    def get_all_bands(self) -> List[Band]:
        return self.band_repo.get_all_bands()

    def get_band_by_id(self, band_id: UUID) -> Band:
        return self.band_repo.get_band_by_id(band_id)

    def create_band(self, name: str, member: UUID, genre: GenreTypes, photo: PhotoUrl) -> Band:
        members = []
        members.append(member.__dict__)
        band = Band(id=uuid4(), name=name, members=members, genre=genre, photo=photo.__dict__)
        return self.band_repo.create_band(band)