import asyncio

from fastapi import FastAPI

from app_band.app.endpoints.band_router import band_router
from app_band.app.schemas import band_schema
from app_band.app.schemas.base_schema import engine
app = FastAPI(title='App')
band_schema.Base.metadata.create_all(bind=engine)


@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()


app.include_router(band_router, prefix='/api')
