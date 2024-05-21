import asyncio

from fastapi import FastAPI

from app_notification.app.endpoints.notification_router import notification_router
from app_notification.app.schemas import notification_schema
from app_notification.app.schemas.base_schema import engine
app = FastAPI(title='App')
notification_schema.Base.metadata.create_all(bind=engine)


@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()


app.include_router(notification_router, prefix='/api')
