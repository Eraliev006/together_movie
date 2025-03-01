class UserNotFoundException(Exception):
    def __init__(
            self,
            message: str
    ):
        self.message = message

class UserAlreadyExistsException(Exception):
    def __init__(self, message: str):
        self.message = message



