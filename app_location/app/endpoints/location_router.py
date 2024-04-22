from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app_location.app.models.location_model import Location, CreateLocationRequest
from app_location.app.services.location_service import LocationService

location_router = APIRouter(prefix='/locations', tags=['Locations'])


@location_router.get('/')
def get_locations(location_service: LocationService = Depends(LocationService)) -> list[Location]:
    return location_service.get_all_locations()


@location_router.post('/')
def create_location(
        location_info: CreateLocationRequest,
        location_service: LocationService = Depends(LocationService)
) -> Location:
    try:
        location = location_service.create_location(
            admin=location_info.admin,
            name=location_info.name,
            address=location_info.address,
            about=location_info.about,
            profile_picture=location_info.profile_picture
        )
        return location.dict()
    except KeyError:
        raise HTTPException(400, f'Location with admin_id={location_info.admin_id} already exists')


@location_router.get('/{id}')
def get_location_by_id(id: UUID, location_service: LocationService = Depends(LocationService)) -> Location:
    try:
        location = location_service.get_location_by_id(id)
        return location.dict()
    except KeyError:
        raise HTTPException(404, f'Location with id={id} not found')
