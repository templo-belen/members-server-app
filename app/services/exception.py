
class LogicConstraintViolationException(Exception):
    def __init__(self, msg):
        super().__init__(self, msg)
        self.message = msg

class NotFoundException(Exception):
    def __init__(self, msg):
        super().__init__(self, msg)
        self.message = msg
