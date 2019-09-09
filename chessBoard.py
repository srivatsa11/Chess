from board import Board
from king import King
from pawn import Pawn
from queen import Queen
from rook import Rook
from bishop import Bishop
from knight import Knight

class ChessBoard(Board):
    def __init__(self):
        self.board = [[0 for j in range(8)] for i in range(8)]
        self.pieces = []

    def showBoard(self):
        for i in range(8):
            for j in range(8):
                print("*", end="  ")
            print("")


if __name__ == "__main__":
    cb = ChessBoard()
    cb.showBoard()