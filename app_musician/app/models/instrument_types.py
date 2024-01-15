from enum import Enum


class InstrumentTypes(str, Enum):
    METAL = "Metal"
    METALCORE = "Metalcore"
    ROCK = "Rock"
    ELSE = "Else"