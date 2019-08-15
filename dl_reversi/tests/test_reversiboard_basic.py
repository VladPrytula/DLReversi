import unittest
from ..reversitypes import Player, Point
from ..basic_reversiboard_slow import BasicReversiBoard
import logging
import numpy as np
from pprint import pprint


fmt = "%(funcName)s():%(lineno)i: %(message)s %(levelname)s"
logging.basicConfig(level=logging.DEBUG, format=fmt)


class TestBasicBoard(unittest.TestCase):

    def setUp(self):
        self.reversi_board = BasicReversiBoard()

    def test_init_position(self):
        self.setUp()
        assert self.reversi_board.grid_array[4, 4] == Player.white.value
        assert self.reversi_board.grid_array[0, 8] == 8

    def test_place_stone_path1(self):
        self.setUp()
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(4, 6), Player.white) == True
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(4, 7), Player.black) == False
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(5, 6), Player.black) == True
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(7, 4), Player.black) == False
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(7, 6), Player.black) == False
        assert self.reversi_board.place_stone(
            Point(3, 4), Player.black) == True
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(2, 4), Player.white) == False
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(4, 7), Player.black) == True

        pprint(self.reversi_board.grid_array)

        # print(np.matrix(self.reversi_board.grid_array))
        # assert self.reversi_board.place_stone(
        #     Point(4, 5), Player.black) == True
        # print(np.matrix(self.reversi_board.grid_array))

    def test_place_stone_path2(self):
        self.setUp()
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(7, 4), Player.white) == False
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(5, 3), Player.white) == True
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(4, 3), Player.black) == True
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(3, 3), Player.white) == True
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(6, 5), Player.black) == True
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(6, 6), Player.white) == True
        pprint(self.reversi_board.grid_array)

    def test_place_stone_path3(self):
        self.setUp()
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(7, 4), Player.white) == False
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(6, 3), Player.white) == False
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(3, 5), Player.white) == True
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(6, 3), Player.white) == True
        pprint(self.reversi_board.grid_array)

    def test_place_stone_path4(self):
        self.setUp()
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(7, 4), Player.white) == False
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(6, 3), Player.white) == False
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(3, 5), Player.white) == True
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(3, 6), Player.black) == True
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(4, 6), Player.white) == True
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(5, 6), Player.black) == True
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(6, 7), Player.white) == True
        pprint(self.reversi_board.grid_array)

    def test_place_stone_path5(self):
        self.setUp()
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(7, 4), Player.white) == False
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(6, 3), Player.white) == False
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(3, 5), Player.white) == True
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(3, 6), Player.black) == True
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(4, 6), Player.white) == True
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(5, 6), Player.black) == True
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(6, 7), Player.white) == True
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(5, 7), Player.black) == True
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(3, 4), Player.black) == True
        pprint(self.reversi_board.grid_array)