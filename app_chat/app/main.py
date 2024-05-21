import asyncio

from fastapi import FastAPI

from app_chat.app.endpoints.chat_router import chat_router
from app_chat.app.schemas import chat_schema
from app_chat.app.schemas.base_schema import engine
app = FastAPI(title='App')
chat_schema.Base.metadata.create_all(bind=engine)


@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()


app.include_router(chat_router, prefix='/api')
