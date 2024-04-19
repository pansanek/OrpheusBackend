import asyncio

from fastapi import FastAPI

from app.endpoints.user_router import user_router

app = FastAPI(title='App')


@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()


app.include_router(user_router, prefix='/api')
