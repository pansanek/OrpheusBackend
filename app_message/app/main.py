import asyncio

from fastapi import FastAPI

from app.endpoints.message_router import message_router

app = FastAPI(title='App')


@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()


app.include_router(message_router, prefix='/api')
