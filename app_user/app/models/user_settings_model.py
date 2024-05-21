from pydantic import BaseModel, ConfigDict


class UserSettings(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    can_receive_messages_for_new_chats: bool
    can_receive_band_invitations: bool
