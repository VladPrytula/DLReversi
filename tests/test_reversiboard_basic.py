import unittest
from reversitypes import Player, Point
from basic_reversiboard_slow import BasicReversiBoard


class TestBasicBoard(unittest.TestCase):

    def setUp(self):
        self.reversi_board = BasicReversiBoard()

    def test_init_position(self):
        self.setUp()
        assert self.reversi_board.grid_array[3, 3] == Player.white.value
        assert self.reversi_board.grid_array[0, 8] == 8

    def test_place_stone(self):
        assert self.reversi_board.place_stone(
            Point(1, 1), Player.white) == False
        assert self.reversi_board.place_stone(
            Point(-1, 1), Player.white) == False
        assert self.reversi_board.place_stone(
            Point(1, 8), Player.white) == False
        assert self.reversi_board.place_stone(
            Point(1, 7), Player.white) == False
        assert self.reversi_board.place_stone(
            Point(3, 4), Player.black) == False
        assert self.reversi_board.place_stone(
            Point(1, 8), Player.white) == False
        assert self.reversi_board.place_stone(
            Point(3, 2), Player.black) == False
