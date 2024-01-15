
import asyncio
from fastapi import FastAPI

from app_musician.app.endpoints.musician_router import musician_router
from app_post.app.endpoints.post_router import post_router

app = FastAPI(title='App')

@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()


app.include_router(musician_router, prefix='/api')

