from chessPiece import ChessPiece
import utilities


class Rook(ChessPiece):
    def __init__(self):
        super().__init__((-1, -1), -1, [])

    def calculateValidMoves(self):
        x, y = self.position
        self.validMoves = []

        for i in range(0, 8):
            if (i != x):
                self.validMoves.append((i, y))

        for j in range(0, 8):
            if (j != y):
                self.validMoves.append((x, j))


if __name__ == "__main__":
    cp = Rook()
    cp.setInitialPosition((3, 4))
    cp.calculateValidMoves()
    utilities.printBoard(cp.validMoves)
