import asyncio

from fastapi import FastAPI

from app_musician.app.endpoints.musician_router import musician_router
from app_musician.app.schemas import musician_schema
from app_musician.app.schemas.base_schema import engine
app = FastAPI(title='App')
musician_schema.Base.metadata.create_all(bind=engine)


@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()


app.include_router(musician_router, prefix='/api')
