class Piece:
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def move(self):
        pass

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color


