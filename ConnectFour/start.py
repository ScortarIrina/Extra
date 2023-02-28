from time import sleep

from board import Board
from game import Game


class GameUI:
    def __init__(self):
        self._board = Board()
        self._game = Game(self._board)

    def print_board(self):
        print(str(self._game.get_board))

    @staticmethod
    def read_position_player():
        print('\n\tYour turn!')
        column = int(input('Column = '))
        return column - 1

    def start(self):
        ongoing_game = 1
        is_human_turn = True
        delay = 1
        print("\nConnect4 game starts...")
        sleep(delay)
        print('...NOW!\n')
        sleep(delay/2)

        while ongoing_game:
            print(str(self._game.get_board))

            try:
                if is_human_turn:
                    try:
                        user_option_column = self.read_position_player()
                        self._game.move_human(user_option_column)

                    except ValueError as ve:
                        print(str(ve))

                else:
                    try:
                        sleep(delay)
                        print('Computer moves now...')
                        sleep(delay)
                        row, column = self._game.move_computer()
                        self._game.get_board.set_position(row, column, '#')
                        print('Computer moves on column ' + str(column + 1) + ', row ' + str(row + 1) + '\n')
                    except ValueError as ve:
                        print(str(ve))

                if self._board.is_full():
                    print('\nThere is no winner!\n')
                    break

                elif self._board.is_won():
                    if not is_human_turn:
                        print(str(self._game.get_board))
                        print('\n\tComputer won!')
                        sleep(delay)
                        ongoing_game = 0
                        break
                    else:
                        print(str(self._game.get_board))
                        print('\n\tCongratulations! You won!')
                        sleep(delay)
                        ongoing_game = 0
                        break

                is_human_turn = not is_human_turn

            except ValueError as ve:
                print(str(ve))


ui = GameUI()
ui.start()
