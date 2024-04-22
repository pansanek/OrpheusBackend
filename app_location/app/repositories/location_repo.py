from typing import List
from uuid import uuid4

from app_location.app.models.location_model import Location

from app_location.app.models.photo_url_model import PhotoUrl
from app_location.app.models.user_model import UserTypes, User
from app_location.app.models.user_settings_model import UserSettings

locations: list[Location] = [
    Location(
        id=uuid4(),
        admin=dict(User(
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
                                       can_receive_band_invitations=True))
        )),
        address="DOM 4",
        name="Hello!",
        about="ABOUT",
        profile_picture=dict(PhotoUrl(
            id=uuid4(),
            url="https://sun1-88.userapi.com/impg/SsYpAAyxKG2SXIKXfY8iBvf2BTxZH9XYP2PFmA/lSVeMDXQuDM.jpg?size=1435x1435&quality=95&sign=c2dff2cc261588cb4a712c853c116199&type=album"
        ))
    )
]


class LocationRepo:
    def get_locations(self) -> list[Location]:
        return locations

    def create_location(self, location) -> Location:
        locations.append(location)
        return location

    def get_locations_by_id(self, id):
        for i in locations:
            if i.id == id:
                return i
        raise KeyError

    def update_location(self, location: Location) -> Location:
        for index, existing_location in enumerate(locations):
            if existing_location.id == location.id:
                locations[index] = location
                return location
        raise KeyError("Location not found")