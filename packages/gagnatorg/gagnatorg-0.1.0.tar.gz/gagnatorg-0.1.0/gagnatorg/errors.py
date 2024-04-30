class GagnatorgException(Exception):

    def __init__(self, message):
        self.message = message

class GagnatorgNotFoundException(Exception):

    def __init__(self, message):
        self.message = message
