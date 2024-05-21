import asyncio

from fastapi import FastAPI

from app_message.app.endpoints.message_router import message_router
from app_message.app.schemas import message_schema
from app_message.app.schemas.base_schema import engine
app = FastAPI(title='App')
message_schema.Base.metadata.create_all(bind=engine)


@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()


app.include_router(message_router, prefix='/api')
