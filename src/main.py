from src.board import Board
from src.game import Player, Color

board = Board()
vlad = Player(Color.WHITE, board)
sasha = Player(Color.BLACK, board)

vlad.make_move()
