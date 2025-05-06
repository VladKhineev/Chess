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

        def get_moves_one_axis(axis, axis_num):
            for step in range(1, 7):
                move_axis = side[0] * step + axis_num
                if self.check_board_exits(1, move_axis):
                    break
                if axis == 'x':
                    cycle_stop, cell = self.add_possible_moves(y, move_axis, board)
                else:
                    cycle_stop, cell = self.add_possible_moves(move_axis, x, board)

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
        a = 5
        for side in side_movement:
            for step in range(1, 7):
                move_x = side[0] * step + x
                move_y = side[1] * step + y

                if self.check_board_exits(2, move_x, move_y):
                    break

                cycle_stop, cell = self.add_possible_moves(move_y, move_x, board)
                if cell:
                    res.append(cell)
                if cycle_stop:
                    break

        return res

    def check_board_exits(self, count_axis, *axis):
        if count_axis == 1:
            return (axis[0] > 7) | (axis[0] < 0)
        else:
            return (axis[0] > 7) | (axis[0] < 0) | (axis[1] > 7) | (axis[1] < 0)

    def add_possible_moves(self, axis1, axis2, board):
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
    IMG = (' ♖ ', ' ♜ ')

    def get_possible_moves(self, x, y, board):
        return self.get_horizontal_and_vertical_moves(x, y, board)


class Bishop(Figure):
    IMG = (' ♗ ', ' ♝ ')

    def get_possible_moves(self, x, y, board):
        return self.get_diagonal_moves(x, y, board)


class Queen(Figure):
    IMG = (' ♕ ', ' ♛ ')

    def get_possible_moves(self, x, y, board):
        res = self.get_horizontal_and_vertical_moves(x, y, board)

        res += self.get_diagonal_moves(x, y, board)

        return res
