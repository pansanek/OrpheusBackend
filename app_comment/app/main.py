import asyncio

from fastapi import FastAPI

from app_comment.app.endpoints.comment_router import comment_router
from app_comment.app.schemas import comment_schema
from app_comment.app.schemas.base_schema import engine
app = FastAPI(title='App')
comment_schema.Base.metadata.create_all(bind=engine)


@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()


app.include_router(comment_router, prefix='/api')
