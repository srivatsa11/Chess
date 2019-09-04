from chessPiece import ChessPiece
import utilities


class King(ChessPiece):
    def __init__(self):
        super().__init__((-1, -1), -1, [])

    def calculateValidMoves(self):
        x, y = self.position
        self.validMoves = []
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if (i >= 0 and j >= 0) and (i <= 7 and j <= 7) and (i, j) != self.position:
                    self.validMoves.append((i, j))


if __name__ == "__main__":
    cp = King()
    cp.setInitialPosition((3, 4))
    cp.calculateValidMoves()
    utilities.printBoard(cp.validMoves)


