import random


class Game:
    def __init__(self, board):
        self._board = board
        self._strategy = MoveStrategy(self._board)

    @property
    def get_board(self):
        return self._board

    def move_computer(self):
        return self._strategy.move_prevent_human_win()

    def move_human(self, column):
        if column > 7 or column < 0:
            raise ValueError('Be careful! That move not inside the board! You lost your turn.')

        for row in range(5, -1, -1):
            if self._board.get_board()[row][column] == 0:
                self._board.set_position(row, column, '%')
                break


class MoveStrategy:
    def __init__(self, board):
        self._board = board

    def column_is_full(self, column):
        """ Returns True if the given column if full, False otherwise """
        if self._board.get_board()[0][column] != 0 and self._board.get_board()[1][column] != 0 and \
                self._board.get_board()[2][column] != 0 and self._board.get_board()[3][column] != 0 and \
                self._board.get_board()[4][column] != 0 and self._board.get_board()[5][column] != 0:
            return True
        return False

    def get_random_column_not_full(self):
        """
        This function returns a random (not full) column
        :return:
        """
        while True:
            column = random.randint(0, 6)
            if not self.column_is_full(column):
                return column

    def get_column_with_3_pieces_of_player(self):
        """
         If there is a column on which the player has placed 3 pieces, this function returns it.
         Otherwise, it returns None
        :return:
        """
        for column in range(7):
            if not self.column_is_full(column) and (self._board.get_board()[5][column] ==
                                                    self._board.get_board()[4][column] == self._board.get_board()[3][
                                                        column] == '   %   ' or
                                                    self._board.get_board()[4][column] == self._board.get_board()[3][
                                                        column] ==
                                                    self._board.get_board()[2][column] == '   %   ' or
                                                    self._board.get_board()[3][column] == self._board.get_board()[2][
                                                        column] ==
                                                    self._board.get_board()[1][column] == '   %   '):
                return column

        return None

    def move_prevent_human_win(self):
        """
        The computer prevents the human from winning on columns.
        :return:
        """
        valid_move = False
        while not valid_move:
            column = self.get_column_with_3_pieces_of_player()
            if column is None:
                column = self.get_random_column_not_full()
            for row in range(5, -1, -1):
                if self._board.get_position(row, column) == 0:
                    return row, column
