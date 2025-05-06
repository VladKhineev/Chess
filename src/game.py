from src.figure import EmptyСage


class Game:
    pass


class Player:
    def __init__(self, color, board):
        self.color = color
        self.board = board

    def make_move(self):
        print(self.board)
        figure, x, y = self.choose_figure(self.board)
        possible_moves = figure.get_possible_moves(x, y, self.board)
        self.finish_move(x, y, possible_moves, figure)

    def choose_figure(self, board):
        x = 4  # int(input('x: '))
        y = 4  # int(input('y: '))
        return board[y][x], x, y

    def finish_move(self, x, y, possible_moves, figure):
        print(possible_moves)

        cage_player_x, cage_player_y = self.choose_move(possible_moves)

        self.update_board(x, y, cage_player_x, cage_player_y, figure)

        print(self.board)

    def choose_move(self, possible_moves):
        move_player = int(input('move: '))

        cage_player_x = possible_moves[move_player][1]
        cage_player_y = possible_moves[move_player][0]

        return cage_player_x, cage_player_y

    def update_board(self, x, y, cage_player_x, cage_player_y, figure):
        self.board[y][x] = EmptyСage()
        self.board[cage_player_y][cage_player_x] = figure


class Color:
    WHITE = 0
    BLACK = 1
