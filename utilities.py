import enum


class pieceColor(enum.Enum):
    BLACK = 0
    WHITE = 1


def printBoard(validMoves):
    for i in range(0, 8):
        for j in range(0 , 8):
            if (i, j) in validMoves:
                print("(*, *)", end="  ")
            else:
                print("({}, {})".format(i, j), end="  ")
        print("")