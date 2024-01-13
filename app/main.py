

import asyncio
from fastapi import FastAPI

from app import rabbitmq
from app.endpoints.user_router import printing_router, metrics_router
import logging
from logging_loki import LokiHandler

app = FastAPI(title='App')

@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(rabbitmq.consume(loop))


app.include_router(printing_router, prefix='/api')

