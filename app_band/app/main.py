import asyncio

from fastapi import FastAPI

from app.endpoints.band_router import band_router

app = FastAPI(title='App')


@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()


app.include_router(band_router, prefix='/api')
