from typing import List
from uuid import uuid4

from app_band.app.models.band_model import Band
from app_band.app.models.genre_types import GenreTypes

from app_band.app.models.photo_url_model import PhotoUrl
from app_band.app.models.user_model import User, UserTypes
from app_band.app.models.user_settings_model import UserSettings

members = [
    {
        "id": str(uuid4()),
        "login": "pansanek",
        "name": "Alex",
        "password": "1234",
        "email": "1@gmail.com",
        "about": "Hehe",
        "user_type": "MUSICIAN",
        "profile_picture": {
            "id": str(uuid4()),
            "url": "https://sun1-88.userapi.com/impg/SsYpAAyxKG2SXIKXfY8iBvf2BTxZH9XYP2PFmA/lSVeMDXQuDM.jpg?size=1435x1435&quality=95&sign=c2dff2cc261588cb4a712c853c116199&type=album"
        },
        "background_picture": {
            "id": str(uuid4()),
            "url": "https://sun1-88.userapi.com/impg/SsYpAAyxKG2SXIKXfY8iBvf2BTxZH9XYP2PFmA/lSVeMDXQuDM.jpg?size=1435x1435&quality=95&sign=c2dff2cc261588cb4a712c853c116199&type=album"
        },
        "settings": {
            "can_receive_messages_for_new_chats": True,
            "can_receive_band_invitations": True
        }
    },
    {
        "id": str(uuid4()),
        "login": "pansanek",
        "name": "Alex",
        "password": "1234",
        "email": "1@gmail.com",
        "about": "Hehe",
        "user_type": "MUSICIAN",
        "profile_picture": {
            "id": str(uuid4()),
            "url": "https://sun1-88.userapi.com/impg/SsYpAAyxKG2SXIKXfY8iBvf2BTxZH9XYP2PFmA/lSVeMDXQuDM.jpg?size=1435x1435&quality=95&sign=c2dff2cc261588cb4a712c853c116199&type=album"
        },
        "background_picture": {
            "id": str(uuid4()),
            "url": "https://sun1-88.userapi.com/impg/SsYpAAyxKG2SXIKXfY8iBvf2BTxZH9XYP2PFmA/lSVeMDXQuDM.jpg?size=1435x1435&quality=95&sign=c2dff2cc261588cb4a712c853c116199&type=album"
        },
        "settings": {
            "can_receive_messages_for_new_chats": True,
            "can_receive_band_invitations": True
        }
    }
]
bands: list[Band] = [
    Band(
        id=uuid4(),
        name="pansanek",
        members=members,
        genre=GenreTypes.METALCORE,
        photo=dict(PhotoUrl(
            id=uuid4(),
            url="https://sun1-88.userapi.com/impg/SsYpAAyxKG2SXIKXfY8iBvf2BTxZH9XYP2PFmA/lSVeMDXQuDM.jpg?size=1435x1435&quality=95&sign=c2dff2cc261588cb4a712c853c116199&type=album"
        )),
    )
]


class BandRepo:
    def get_bands(self) -> list[Band]:
        return bands

    def create_band(self, band) -> Band:
        bands.append(band)
        return band

    def get_bands_by_id(self, id):
        for i in bands:
            if i.id == id:
                return i
        raise KeyError

    def update_band(self, band: Band) -> Band:
        for index, existing_band in enumerate(bands):
            if existing_band.id == band.id:
                bands[index] = band
                return band
        raise KeyError("Band not found")
