from chessPiece import ChessPiece
import utilities

class Queen(ChessPiece):
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

        for i in range(0, 8):
            if (i != x):
                self.validMoves.append((i, y))

        for j in range(0, 8):
            if (j != y):
                self.validMoves.append((x, j))


if __name__ == "__main__":
    cp = Queen()
    cp.setInitialPosition((3, 4))
    cp.calculateValidMoves()
    utilities.printBoard(cp.validMoves)