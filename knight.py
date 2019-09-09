from chessPiece import ChessPiece
import utilities

class Knight(ChessPiece):
    def __init__(self):
        super().__init__((-1, -1), -1, [])

    def calculateValidMoves(self):
        x, y = self.position
        self.validMoves = []

        rowOptions = [-1, -2, -2, -1, +1, +2, +2, +1]
        colOptions = [-2, -1, +1, +2, +2, +1, -1, -2]

        for i in range(8):
            r = x + rowOptions[i]
            c = y + colOptions[i]
            if (r >= 0 and r <= 7) and (c >= 0 and c <= 7):
                self.validMoves.append((r, c))

if __name__ == "__main__":
    cp = Knight()
    cp.setInitialPosition((1, 1))
    cp.calculateValidMoves()
    utilities.printBoard(cp.validMoves)