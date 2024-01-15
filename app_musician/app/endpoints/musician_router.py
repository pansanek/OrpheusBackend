from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException

from app_musician.app.models.musician_model import Musician, CreateMusicianRequest
from app_musician.app.services.musician_service import MusicianService
from app_musician.app.models.musician_model import GenreTypes, InstrumentTypes

musician_router = APIRouter(prefix='/musicians', tags=['Musicians'])

@musician_router.get('/')
def get_musicians(musician_service: MusicianService = Depends(MusicianService)) -> list[Musician]:
    return musician_service.get_all_musicians()

@musician_router.post('/')
def create_musician(
    musician_info: CreateMusicianRequest,
    musician_service: MusicianService = Depends(MusicianService)
) -> Musician:
    try:
        musician = musician_service.create_musician(
            user_id=musician_info.user_id,
            genre=musician_info.genre,
            instrument=musician_info.instrument
        )
        return musician.dict()
    except KeyError:
        raise HTTPException(400, f'Musician with id={musician_info.id} already exists')

@musician_router.get('/{id}')
def get_musician_by_id(id: UUID, musician_service: MusicianService = Depends(MusicianService)) -> Musician:
    try:
        musician = musician_service.get_musician_by_id(id)
        return musician.dict()
    except KeyError:
        raise HTTPException(404, f'Musician with id={id} not found')
