import copy


class Board:
    def __init__(self):
        self.__board = [[0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]]

    def get_position(self, row, column):
        if row < 0 or row > 5 or column < 0 or column > 6:
            raise ValueError("Position outside board")
        return self.__board[row][column]

    def get_board(self):
        return copy.deepcopy(self.__board)

    def __getitem__(self, item):
        return self.__board[item]

    def __len__(self):
        return len(self.__board)

    def set_position(self, row, column, symbol):
        """
        Set a # or a % on the board
        Raises ValueError if necessary
        """
        if not (symbol in ['#', '%']):
            raise ValueError('Oops...you can only place a  "#"  or a  "%"  on the board!')
        if not (row in (0, 1, 2, 3, 4, 5)) or not (column in (0, 1, 2, 3, 4, 5, 6)):
            raise ValueError('Be careful! That move is outside the board')
        if self.get_board()[row][column] != 0:
            raise ValueError('Oops...you cannot overwrite the other player!')

        self.__board[row][column] = '   ' + symbol + '   '

    def is_full(self):
        """ Checks if the board is full"""
        for row in range(6):
            for column in range(7):
                if self.get_position(row, column) == 0:
                    # Found the first empty position => board not full
                    return False
        return True

    def is_won(self):
        # Check rows for winner
        for row in range(6):
            for column in range(3):
                if (self.__board[row][column] == '   %   ' or self.__board[row][column] == '   #   ') and \
                        (self.__board[row][column] == self.__board[row][column + 1] == self.__board[row][column + 2] ==
                         self.__board[row][column + 3]):
                    return True

        # Check columns for winner
        for column in range(6):
            for row in range(3):
                if (self.__board[row][column] == '   %   ' or self.__board[row][column] == '   #   ') and \
                        (self.__board[row][column] == self.__board[row + 1][column] == self.__board[row + 2][column] ==
                         self.__board[row + 3][column]):
                    return True

        # Check diagonal (top-left to bottom-right) for winner
        for row in range(3):
            for column in range(4):
                if (self.__board[row][column] == '   %   ' or self.__board[row][column] == '   #   ') and \
                        (self.__board[row][column] == self.__board[row + 1][column + 1] ==
                         self.__board[row + 2][column + 2] == self.__board[row + 3][column + 3]):
                    return True

        # Check diagonal (bottom-left to top-right) for winner
        for row in range(5, 2, -1):
            for column in range(3):
                if (self.__board[row][column] == '   %   ' or self.__board[row][column] == '   #   ') and \
                        (self.__board[row][column] == self.__board[row - 1][column + 1] ==
                         self.__board[row - 2][column + 2] == self.__board[row - 3][column + 3]):
                    return True

        return False

    def __str__(self):
        """ Convert board to string representation """
        result = "       1      2      3      4      5      6      7\n\n"
        for row in range(0, 6):
            result += str(row + 1)
            result += '   '
            for column in range(0, 7):
                if self.get_position(row, column) == 0:
                    result += '  ---  '
                else:
                    result += self.get_position(row, column)
            result += '\n\n'
        return result
