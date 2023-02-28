import unittest

from board import Board
from game import Game, MoveStrategy


class BoardTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__board = Board()

    def tearDown(self) -> None:
        pass

    def test_get_position__position_outside_board__value_error(self):
        with self.assertRaises(ValueError):
            self.__board.get_position(-1, -1)

    def test_get_position__valid_input__returns_value(self):
        self.assertEqual(self.__board.get_position(1, 2), 0)

    def test_get_board(self):
        self.assertEqual(len(self.__board.get_board()), 6)

    def test_getitem(self):
        self.assertEqual(len(self.__board.__getitem__(1)), 7)

    def test_is_full__board_is_full__True(self):
        for row in range(6):
            for column in range(7):
                self.__board.set_position(row, column, '%')
        self.assertTrue(self.__board.is_full())

    def test_is_full__board_is_not_full__False(self):
        self.assertFalse(self.__board.is_full())

    def test_set_position__invalid_symbol__value_error(self):
        with self.assertRaises(ValueError):
            self.__board.set_position(1, 1, '^')

    def test_set_position__invalid_row__value_error(self):
        with self.assertRaises(ValueError):
            self.__board.set_position(8, 1, '$')

    def test_set_position__invalid_column__value_error(self):
        with self.assertRaises(ValueError):
            self.__board.set_position(1, 8, '%')

    def test_set_position__cell_is_taken__value_error(self):
        self.__board.set_position(1, 1, '%')
        with self.assertRaises(ValueError):
            self.__board.set_position(1, 1, '%')

    def test_is_won__won_on_second_diagonal__true(self):
        self.__board.set_position(5, 0, '%')
        self.__board.set_position(4, 1, '%')
        self.__board.set_position(3, 2, '%')
        self.__board.set_position(2, 3, '%')
        self.assertTrue(self.__board.is_won())

    def test_is_won__won_on_first_diagonal__true(self):
        self.__board.set_position(0, 0, '%')
        self.__board.set_position(1, 1, '%')
        self.__board.set_position(2, 2, '%')
        self.__board.set_position(3, 3, '%')
        self.assertTrue(self.__board.is_won())

    def test_is_won__won_on_row__true(self):
        self.__board.set_position(0, 0, '%')
        self.__board.set_position(0, 1, '%')
        self.__board.set_position(0, 2, '%')
        self.__board.set_position(0, 3, '%')
        self.assertTrue(self.__board.is_won())

    def test_is_won__won_on_column__true(self):
        self.__board.set_position(0, 0, '%')
        self.__board.set_position(1, 0, '%')
        self.__board.set_position(2, 0, '%')
        self.__board.set_position(3, 0, '%')
        self.assertTrue(self.__board.is_won())

    def test_is_won__not_won__false(self):
        self.assertFalse(self.__board.is_won())

    def test_str(self):
        self.__board.set_position(0, 0, '%')
        self.assertEqual(len(self.__board.__str__()), 382)


class GameTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__board = Board()
        self.__game = Game(self.__board)

    def tearDown(self) -> None:
        pass

    def test_move_computer(self):
        self.__game.move_computer()
        self.assertEqual(len(self.__board.get_board()), 6)

    def test_move_human__valid_column__successful_move(self):
        self.__game.move_human(2)
        self.assertEqual(len(self.__board.get_board()), 6)

    def test_move_human__invalid_column__value_error(self):
        with self.assertRaises(ValueError):
            self.__game.move_human(9)

    def test_get_board(self):
        self.assertEqual(len(self.__game.get_board), 6)


class MoveStrategyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__board = Board()
        self.__move = MoveStrategy(self.__board)

    def tearDown(self) -> None:
        pass

    def test_column_is_full__full_column__true(self):
        self.__board.set_position(0, 0, '%')
        self.__board.set_position(1, 0, '#')
        self.__board.set_position(2, 0, '%')
        self.__board.set_position(3, 0, '%')
        self.__board.set_position(4, 0, '#')
        self.__board.set_position(5, 0, '%')
        self.assertTrue(self.__move.column_is_full(0))

    def test_get_column_with_3_pieces_of_player(self):
        self.__board.set_position(3, 0, '%')
        self.__board.set_position(4, 0, '%')
        self.__board.set_position(5, 0, '%')
        self.assertEqual(self.__move.get_column_with_3_pieces_of_player(), 0)
