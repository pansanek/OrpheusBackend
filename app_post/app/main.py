import asyncio

from fastapi import FastAPI

from app.endpoints.post_router import post_router

app = FastAPI(title='App')


@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()


app.include_router(post_router, prefix='/api')
