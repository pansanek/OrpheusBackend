import asyncio

from fastapi import FastAPI

from app_chat.app.endpoints.chat_router import chat_router

app = FastAPI(title='App')


@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()


app.include_router(chat_router, prefix='/api')
