from chessPiece import ChessPiece
import utilities


class Pawn(ChessPiece):
    def __init__(self):
        super().__init__((-1, -1), -1, [])

    def calculateValidMoves(self):
        x, y = self.position
        self.validMoves = []
        if x == 1 and self.color == utilities.pieceColor.WHITE:
            self.validMoves.append((x + 1, y))
            self.validMoves.append((x + 2, y))
        elif self.color == utilities.pieceColor.WHITE and x < 7:
            print("reached cond 2")
            self.validMoves.append((x + 1, y))
        elif x == 6 and self.color == utilities.pieceColor.BLACK:
            self.validMoves.append((x - 1), y)
            self.validMoves.append((x - 2), y)
        elif self.color == utilities.pieceColor.BLACK and x > 0:
            self.validMoves.append((x - 1, y))


if __name__ == "__main__":
    cp = Pawn()
    cp.setInitialPosition((3, 4))
    cp.setColor(utilities.pieceColor.BLACK)
    cp.calculateValidMoves()
    utilities.printBoard(cp.validMoves)
    input("Press enter to try the other side")
    cp.setColor(utilities.pieceColor.WHITE)
    cp.calculateValidMoves()
    utilities.printBoard(cp.validMoves)

