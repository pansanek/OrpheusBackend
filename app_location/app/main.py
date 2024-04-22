import asyncio

from fastapi import FastAPI

from app_location.app.endpoints.location_router import location_router

app = FastAPI(title='App')


@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()


app.include_router(location_router, prefix='/api')
