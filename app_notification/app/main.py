import asyncio

from fastapi import FastAPI

from app_notification.app.endpoints.notification_router import notification_router

app = FastAPI(title='App')


@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()


app.include_router(notification_router, prefix='/api')
