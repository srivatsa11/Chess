from chessPiece import ChessPiece
import utilities

class Knight(ChessPiece):
    def __init__(self):
        super().__init__((-1, -1), -1, [])

    def calculateValidMoves(self):
        x, y = self.position
        self.validMoves = []

        row_options = [-1, -2, -2, -1, +1, +2, +2, +1]
        col_options = [-2, -1, +1, +2, +2, +1, -1, -2]

        for i in range(8):
            r = x + row_options[i]
            c = y + col_options[i]
            if (r in range(0, 8)) and (c in range(0, 8)):
                self.validMoves.append((r, c))


if __name__ == "__main__":
    cp = Knight()
    cp.setInitialPosition((1, 1))
    cp.calculateValidMoves()
    utilities.printBoard(cp.validMoves)
