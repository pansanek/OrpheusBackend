from pydantic import BaseModel


class UserSettings(BaseModel):
    can_receive_messages_for_new_chats: bool
    can_receive_band_invitations: bool
