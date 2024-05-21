import asyncio

from fastapi import FastAPI

from app_user.app.schemas.base_schema import engine
from app_user.app.endpoints.user_router import user_router
from app_user.app.schemas import user_schema
app = FastAPI(title='App')
user_schema.Base.metadata.create_all(bind=engine)

@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()


app.include_router(user_router, prefix='/api')
