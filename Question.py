

class Question:
    def __init__(self, message, right, wrong):
        self.message = message
        self.right = right
        self.wrong = wrong

    def jsonable(self):
        return self.__dict__
