import asyncio

from fastapi import FastAPI

from app_post.app.endpoints.post_router import post_router
from app_post.app.schemas import post_schema
from app_post.app.schemas.base_schema import engine
app = FastAPI(title='App')
post_schema.Base.metadata.create_all(bind=engine)


@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()


app.include_router(post_router, prefix='/api')
