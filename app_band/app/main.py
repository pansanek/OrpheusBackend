
import asyncio
from fastapi import FastAPI

from app_band.app.endpoints.band_router import band_router
from app_post.app.endpoints.post_router import post_router

app = FastAPI(title='App')

@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()


app.include_router(band_router, prefix='/api')

