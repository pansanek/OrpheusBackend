from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app_musician.app.models.musician_model import Musician, CreateMusicianRequest
from app_musician.app.services.musician_service import MusicianService

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
            user=musician_info.user,
            genre=musician_info.genre,
            instrument=musician_info.instrument
        )
        return musician.dict()
    except KeyError:
        raise HTTPException(400, f'Musician with id={musician_info.user} already exists')


@musician_router.get('/{id}')
def get_musician_by_id(id: UUID, musician_service: MusicianService = Depends(MusicianService)) -> Musician:
    try:
        musician = musician_service.get_musician_by_id(id)
        return musician.dict()
    except KeyError:
        raise HTTPException(404, f'Musician with id={id} not found')

@musician_router.put('/{musician_id}')
def update_musician(
        musician_id: UUID,
        musician_info: CreateMusicianRequest,
        musician_service: MusicianService = Depends(MusicianService)
) -> Musician:
    try:
        updated_musician = musician_service.update_musician(
            musician_id=musician_id,
            user=musician_info.user,
            genre=musician_info.genre,
            instrument=musician_info.instrument
        )
        return updated_musician
    except KeyError:
        raise HTTPException(404, f'Musician with id={musician_id} not found')