import asyncio

from fastapi import FastAPI

from app_location.app.endpoints.location_router import location_router
from app_location.app.schemas import location_schema
from app_location.app.schemas.base_schema import engine
app = FastAPI(title='App')
location_schema.Base.metadata.create_all(bind=engine)


@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()


app.include_router(location_router, prefix='/api')
