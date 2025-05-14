import game


class EmptyСage:
    IMG = ' □ '

    def __str__(self):
        return self.IMG


class Figure:
    IMG = None

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.IMG[self.color]

    def get_horizontal_and_vertical_moves(self, x, y, board):

        range_move = self.determine_range_move()

        def get_moves_one_axis(axis, axis_num):
            for step in range(1, range_move):
                move_axis = side[0] * step + axis_num

                if self.check_board_exits(1, move_axis):
                    break
                if axis == 'x':
                    cycle_stop, cell = self.add_possible_cell(y, move_axis, board)
                else:
                    cycle_stop, cell = self.add_possible_cell(move_axis, x, board)

                if cell:
                    res.append(cell)
                if cycle_stop:
                    break

        side_movement = ((1, 0), (-1, 0), (0, 1), (0, -1))
        res = []
        for side in side_movement:
            get_moves_one_axis('x', x)
            get_moves_one_axis('y', y)

        return res

    def get_diagonal_moves(self, x, y, board):
        side_movement = ((1, 1), (-1, 1), (1, -1), (-1, -1))
        res = []

        range_move = self.determine_range_move()

        for side in side_movement:
            for step in range(1, range_move):
                move_x = side[0] * step + x
                move_y = side[1] * step + y

                if self.check_board_exits(2, move_x, move_y):
                    break

                cycle_stop, cell = self.add_possible_cell(move_y, move_x, board)
                if cell:
                    res.append(cell)
                if cycle_stop:
                    break

        return res

    def determine_range_move(self):
        if type(self) == King:
            res = 2
        else:
            res = 7

        return res

    def check_board_exits(self, count_axis, *axis):
        if count_axis == 1:
            return (axis[0] > 7) | (axis[0] < 0)
        else:
            return (axis[0] > 7) | (axis[0] < 0) | (axis[1] > 7) | (axis[1] < 0)

    def add_possible_cell(self, axis1, axis2, board):
        cycle_stop = False

        cage = board[axis1][axis2]

        if type(cage) == EmptyСage:
            return cycle_stop, (axis1, axis2)
        else:
            cycle_stop = True
            if self.color != cage.color:
                return cycle_stop, (axis1, axis2)
            return cycle_stop, None


class Rook(Figure):
    IMG = (' ♜ ', ' ♖ ')

    def get_possible_moves(self, x, y, board):
        return self.get_horizontal_and_vertical_moves(x, y, board)


class Bishop(Figure):
    IMG = (' ♝ ', ' ♗ ')

    def get_possible_moves(self, x, y, board):
        return self.get_diagonal_moves(x, y, board)


class Queen(Figure):
    IMG = (' ♛ ', ' ♕ ')

    def get_possible_moves(self, x, y, board):
        res = self.get_horizontal_and_vertical_moves(x, y, board)

        res += self.get_diagonal_moves(x, y, board)

        return res


class King(Figure):
    IMG = (' ♚ ', ' ♔ ')

    def get_possible_moves(self, x, y, board):
        res = self.get_horizontal_and_vertical_moves(x, y, board)

        res += self.get_diagonal_moves(x, y, board)

        return res


class Knight(Figure):
    IMG = (' ♞ ', ' ♘ ')

    def get_possible_moves(self, x, y, board):
        side_movement = ((2, -1), (2, 1), (-1, 2), (1, 2), (-2, -1), (-2, 1), (-1, -2), (1, -2))
        res = []

        for side in side_movement:
            move_x = side[0] + x
            move_y = side[1] + y

            if self.check_board_exits(2, move_x, move_y):
                continue

            cycle_stop, cell = self.add_possible_cell(move_y, move_x, board)
            if cell:
                res.append(cell)
            if cycle_stop:
                continue

        return res


class Pawn(Figure):
    IMG = (' ♟ ', ' ♙ ')

    def get_possible_moves(self, x, y, board):
        res = []

        move_y = self.get_move_from_color(y)

        if self.check_board_exits(1, move_y):
            return

        cycle_stop, cell = self.add_possible_cell(move_y, x, board)
        if cell:
            res.append(cell)

        cycle_stop2, cell = self.get_first_move(y, x, board)
        if cycle_stop and cycle_stop2 and cell:
            res.append(cell)

        res += self.get_moves_from_kill(y, x, board)

        return res

    def get_move_from_color(self, y):
        if self.color == game.Color.WHITE:
            move_y = y - 1
        else:
            move_y = y + 1

        return move_y

    def get_first_move(self, y, x, board):
        move_y, move_x = self.get_first_move_from_color(y, x)
        if move_y:
            return self.add_possible_cell(move_y, move_x, board)
        else:
            return False, None

    def get_first_move_from_color(self, y, x):
        if self.color == game.Color.WHITE and y == 6:
            return y - 2, x
        elif self.color == game.Color.BLACK and y == 1:
            return y + 2, x
        else:
            return None, None

    def add_possible_cell(self, axis1, axis2, board):
        cycle_stop = False

        cage = board[axis1][axis2]

        if type(cage) == EmptyСage:
            cycle_stop = True
            return cycle_stop, (axis1, axis2)
        else:
            return cycle_stop, None

    def get_moves_from_kill(self, y, x, board):
        res = []
        if self.color == game.Color.WHITE:
            kill_movement = ((-1, -1), (-1, 1))
        else:
            kill_movement = ((1, -1), (1, 1))

        for kill_step in kill_movement:
            move_y = kill_step[0] + y
            move_x = kill_step[1] + x

            if self.check_board_exits(2, move_x, move_y):
                continue

            cycle_stop, cell = self.add_possible_cell_with_figure(move_y, move_x, board)
            if cell:
                res.append(cell)
            if cycle_stop:
                continue

        return res

    def add_possible_cell_with_figure(self, axis1, axis2, board):
        cycle_stop = False

        cage = board[axis1][axis2]

        if type(cage) == EmptyСage:
            return cycle_stop, None
        else:
            cycle_stop = True
            if self.color != cage.color:
                return cycle_stop, (axis1, axis2)
            return cycle_stop, None
