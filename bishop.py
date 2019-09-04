from chessPiece import ChessPiece
import utilities


class Bishop(ChessPiece):
    def __init__(self):
        super().__init__((-1, -1), -1, [])

    def calculateValidMoves(self):
        x, y = self.position
        self.validMoves = []

        u = y
        for v in range(x - 1, -1, -1):
            u = u - 1
            if self.checkIfMoveInBounds((v, u)):
                self.validMoves.append((v, u))

        u = y
        for v in range(x + 1, 8):
            u = u + 1
            if self.checkIfMoveInBounds((v, u)):
                self.validMoves.append((v, u))

        u = y
        for v in range(x + 1, 8):
            u = u - 1
            if self.checkIfMoveInBounds((v, u)):
                self.validMoves.append((v, u))

        u = y
        for v in range(x - 1, -1, -1):
            u = u + 1
            if self.checkIfMoveInBounds((v, u)):
                self.validMoves.append((v, u))


if __name__ == "__main__":
    cp = Bishop()
    cp.setInitialPosition((3, 4))
    cp.calculateValidMoves()
    utilities.printBoard(cp.validMoves)