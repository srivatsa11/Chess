from piece import Piece


class ChessPiece(Piece):
    def __init__(self, position, color, validMoves):
        super().__init__(position, color)
        self.onBoard = False
        self.validMoves = validMoves

    def move(self, newPosition):
        pass

    def calculateValidMoves(self):
        pass

    def checkIfMoveInBounds(self, newPosition):
        x, y = newPosition
        if (x >= 0 and y >= 0) and (x <= 7 and y <= 7):
            return True
        else:
            return False

    def setInitialPosition(self, pos):
        self.position = pos

    def move(self, newPosition):
        self.calculateValidMoves()
        if self.checkIfMoveInBounds(newPosition) and newPosition in self.validMoves:
            self.position = newPosition
        else:
            print("Invalid move")


if __name__ == "__main__":
    pass
