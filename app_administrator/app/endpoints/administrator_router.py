from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException

from app_administrator.app.models.administrator_model import CreateAdministratorRequest, Administrator
from app_administrator.app.services.administrator_service import AdministratorService

administrator_router = APIRouter(prefix='/administrators', tags=['Administrators'])


@administrator_router.get('/')
def get_administrators(administrator_service: AdministratorService = Depends(AdministratorService)) -> list[
    Administrator]:
    return administrator_service.get_all_administrators()


@administrator_router.post('/')
def create_administrator(
        administrator_info: CreateAdministratorRequest,
        administrator_service: AdministratorService = Depends(AdministratorService)
) -> Administrator:
    try:
        administrator = administrator_service.create_administrator(
            user_id=administrator_info.user_id,
            location_id=administrator_info.location_id
        )
        return administrator.dict()
    except KeyError:
        raise HTTPException(400, f'Administrator with user_id={administrator_info.user_id} already exists')


@administrator_router.get('/{id}')
def get_administrator_by_id(id: UUID, administrator_service: AdministratorService = Depends(
    AdministratorService)) -> Administrator:
    try:
        administrator = administrator_service.get_administrator_by_id(id)
        return administrator.dict()
    except KeyError:
        raise HTTPException(404, f'Administrator with id={id} not found')
