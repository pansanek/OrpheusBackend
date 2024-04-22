from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app_band.app.models.band_model import Band, CreateBandRequest
from app_band.app.services.band_service import BandService

band_router = APIRouter(prefix='/bands', tags=['Bands'])


@band_router.get('/')
def get_bands(band_service: BandService = Depends(BandService)) -> List[Band]:
    return band_service.get_all_bands()


@band_router.post('/')
def create_band(
        band_info: CreateBandRequest,
        band_service: BandService = Depends(BandService)
) -> Band:
    try:
        band = band_service.create_band(
            name=band_info.name,
            members=band_info.members,
            genre=band_info.genre,
            photo = band_info.photo
        )
        return band.dict()
    except KeyError:
        raise HTTPException(400, f'Band with name={band_info.name} already exists')


@band_router.get('/{id}')
def get_band_by_id(id: UUID, band_service: BandService = Depends(BandService)) -> Band:
    try:
        band = band_service.get_band_by_id(id)
        return band.dict()
    except KeyError:
        raise HTTPException(404, f'Band with id={id} not found')


@band_router.put('/{band_id}')
def update_band(
        band_id: UUID,
        band_info: CreateBandRequest,
        band_service: BandService = Depends(BandService)
) -> Band:
    try:
        updated_band = band_service.update_band(
            band_id=band_id,
            name=band_info.name,
            members=band_info.members,
            genre=band_info.genre,
            photo=band_info.photo
        )
        return updated_band
    except KeyError:
        raise HTTPException(404, f'Band with id={band_id} not found')