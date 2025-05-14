from figure import EmptyСage, Rook, Bishop, Queen, King, Knight, Pawn
from game import Color


class Board:
    def __init__(self):
        self.LENGHT_BOARD = 8
        self.board = [[EmptyСage()] * self.LENGHT_BOARD for _ in range(self.LENGHT_BOARD)]

        self.board[1][5] = Rook(Color.BLACK)
        self.board[1][2] = Rook(Color.WHITE)
        self.board[3][5] = Rook(Color.BLACK)
        self.board[5][4] = Bishop(Color.WHITE)
        self.board[4][4] = Queen(Color.BLACK)
        self.board[7][4] = King(Color.WHITE)
        self.board[4][2] = Knight(Color.BLACK)
        self.board[1][6] = Pawn(Color.WHITE)
        self.board[5][1] = Pawn(Color.BLACK)

    def __str__(self):
        res = ''

        for cell in range(self.LENGHT_BOARD):
            res += ''.join(map(str, self.board[cell])) + '\n'

        return res

    def __getitem__(self, item):
        return self.board[item]
