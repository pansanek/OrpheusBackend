import asyncio

from fastapi import FastAPI

from app.endpoints.musician_router import musician_router

app = FastAPI(title='App')


@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()


app.include_router(musician_router, prefix='/api')
