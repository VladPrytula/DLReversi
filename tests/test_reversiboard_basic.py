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
    

    def test_place_stone_no_immediate_neighbour(self):
        self.setUp()
        print('----1------')
        assert self.reversi_board.is_valid_place(Point(3,2), Player.white) == False
        print('----2------')
        assert self.reversi_board.is_valid_place(Point(3,5), Player.white) == True
        print('----3------')
        assert self.reversi_board.is_valid_place(Point(3,5), Player.black) == False
        print('----4------')
        assert self.reversi_board.is_valid_place(Point(3,2), Player.white) == False
