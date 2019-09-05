from board import Board

class ChessBoard(Board):
    def __init__(self):
        self.board = [[0 for j in range(8)] for i in range(8)]

    def showBoard(self):
        for i in range(8):
            for j in range(8):
                print("*", end="  ")
            print("")


if __name__ == "__main__":
    cb = ChessBoard()
    cb.showBoard()