from enum import IntEnum


class ResponseStatusCode(IntEnum):
    SUCCESS = 0,
    INTERNAL_ERROR = 1,
    USER_ALREADY_EXISTS = 2,
    USER_NOT_FOUND = 3,
    CITY_ALREADY_ADDED = 4,
    CITY_NOT_ADDED = 5,
    INVALID_CITY = 6,
    FUZZY_CITY = 7,
    TRACKS_LIST_ALREADY_ADDED = 8,
    TRACKS_LIST_NOT_ADDED = 9,
    INVALID_TRACK_LIST = 10
