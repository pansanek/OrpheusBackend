
import asyncio
from fastapi import FastAPI

from app_comment.app.endpoints.comment_router import comment_router
from app_post.app.endpoints.post_router import post_router

app = FastAPI(title='App')

@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()


app.include_router(comment_router, prefix='/api')

