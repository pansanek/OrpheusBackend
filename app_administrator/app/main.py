import asyncio

from fastapi import FastAPI

from app_administrator.app.endpoints.administrator_router import administrator_router

app = FastAPI(title='App')


@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()


app.include_router(administrator_router, prefix='/api')
