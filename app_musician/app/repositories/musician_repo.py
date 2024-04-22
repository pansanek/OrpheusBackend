from typing import List
from uuid import uuid4

from app_musician.app.models.genre_types import GenreTypes
from app_musician.app.models.instrument_types import InstrumentTypes
from app_musician.app.models.musician_model import Musician

from app_musician.app.models.photo_url_model import PhotoUrl
from app_musician.app.models.user_model import UserTypes, User
from app_musician.app.models.user_settings_model import UserSettings

musicians: list[Musician] = [
    Musician(
        id=uuid4(),
        user=dict(User(
            id=uuid4(),
            login="pansanek",
            name="Alex",
            password="1234",
            email="1@gmail.com",
            about="Hehe",
            user_type=UserTypes.MUSICIAN,
            profile_picture=dict(PhotoUrl(
                id=uuid4(),
                url="https://sun1-88.userapi.com/impg/SsYpAAyxKG2SXIKXfY8iBvf2BTxZH9XYP2PFmA/lSVeMDXQuDM.jpg?size=1435x1435&quality=95&sign=c2dff2cc261588cb4a712c853c116199&type=album"
            )),
            background_picture=dict(PhotoUrl(
                id=uuid4(),
                url="https://sun1-88.userapi.com/impg/SsYpAAyxKG2SXIKXfY8iBvf2BTxZH9XYP2PFmA/lSVeMDXQuDM.jpg?size=1435x1435&quality=95&sign=c2dff2cc261588cb4a712c853c116199&type=album"
            )),
            settings=dict(UserSettings(can_receive_messages_for_new_chats=True,
                                  can_receive_band_invitations=True)),
        )),
        genre=GenreTypes.METALCORE,
        instrument=InstrumentTypes.DRUMS
    )
]


class MusicianRepo:
    def get_musicians(self) -> list[Musician]:
        return musicians

    def create_musician(self, musician) -> Musician:
        musicians.append(musician)
        return musician

    def get_musicians_by_id(self, id):
        for i in musicians:
            if i.id == id:
                return i
        raise KeyError

    def update_musician(self, musician: Musician) -> Musician:
        for index, existing_musician in enumerate(musicians):
            if existing_musician.id == musician.id:
                musicians[index] = musician
                return musician
        raise KeyError("Musician not found")