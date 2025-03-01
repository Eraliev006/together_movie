class RoomNotFoundException(Exception):
    def __init__(self, message: str):
        self.message = message


class RoomAlreadyExists(Exception):
    def __init__(self, message: str):
        self.message = message


