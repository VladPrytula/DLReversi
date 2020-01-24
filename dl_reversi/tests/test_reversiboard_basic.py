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
        assert self.reversi_board.grid_array[4, 5] == Player.black.value
        assert self.reversi_board.grid_array[2, 2] == 0
        assert self.reversi_board.grid_array[0, 8] == 8

    def test_convert_left(self):
        self.setUp()
        self.reversi_board.grid_array = np.array(
            [
                [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, -1, 1, 0, 1, 0, 0, 8],
                [8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
            ]
        )
        assert self.reversi_board.place_stone(
            Point(8, 7), Player.white) == False
        pprint(self.reversi_board.grid_array)

        self.reversi_board.grid_array = np.array(
            [
                [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0,-1, 1,-1, 1, 0, 0, 8],
                [8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
            ]
        )
        assert self.reversi_board.place_stone(
            Point(8, 7), Player.white) == True
        pprint(self.reversi_board.grid_array)


    def test_convert_right(self):
        self.setUp()
        self.reversi_board.grid_array = np.array(
            [
                [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0,-1, 1, 0, 1,-1, 0, 8],
                [8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
            ]
        )
        assert self.reversi_board.place_stone(
            Point(8, 1), Player.black) == False
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(8, 2), Player.black) == True
        pprint(self.reversi_board.grid_array)
        self.reversi_board.grid_array = np.array(
            [
                [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, -1, -1, -1, 1,-1, 0, 8],
                [8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
            ]
        )
        assert self.reversi_board.place_stone(
            Point(8, 1), Player.black) == False
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(8, 2), Player.black) == True
        pprint(self.reversi_board.grid_array)        
"""
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
            Point(3, 6), Player.black) == True
        pprint(self.reversi_board.grid_array)

        assert self.reversi_board.place_stone(
            Point(4, 7), Player.white) == False
        pprint(self.reversi_board.grid_array)

        assert self.reversi_board.place_stone(
            Point(3, 5), Player.white) == True
        pprint(self.reversi_board.grid_array)

        assert self.reversi_board.place_stone(
            Point(5, 6), Player.black) == True
        pprint(self.reversi_board.grid_array)

    def test_is_valid_place(self):
        self.setUp()
        # modify the state to check the right border
        #  8  .  .  .  .  .  .  .  .
        #  7  .  .  .  W  B  B  B  .
        #  6  .  .  .  W  W  B  B  .
        #  5  W  W  W  W  B  W  B  .
        #  4  W  W  W  W  B  B  B  .
        #  3  B  B  B  B  B  B  B  .
        #  2  B  W  W  W  W  W  W  .
        #  1  B  .  .  .  .  .  .  .
        #     A  B  C  D  E  F  G  H
        self.reversi_board.grid_array = np.array(
            [
                [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
                [8, 1, -1, -1, -1, -1, -1, -1, 0, 8],
                [8, 1, -1, -1, -1, -1, -1, -1, 0, 8],
                [8, 1, -1, -1, -1, -1, -1, -1, 0, 8],
                [8, 1, -1, -1, -1, -1, -1, -1, 0, 8],
                [8, 1, -1, -1, -1, -1, -1, -1, 0, 8],
                [8, 1, -1, -1, -1, -1, -1, -1, 0, 8],
                [8, 1, -1, -1, -1, -1, -1, -1, 0, 8],
                [8, 1, -1, -1, -1, -1, -1, -1, 0, 8],
                [8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
            ]
        )

        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.grid_array[1, 8] == 0
        assert self.reversi_board.place_stone(
            Point(1, 8), Player.black) == True
        pprint(self.reversi_board.grid_array)

        assert self.reversi_board.place_stone(
            Point(8, 8), Player.black) == True
        pprint(self.reversi_board.grid_array)

    def test_convert_generic(self):
        self.setUp()
        self.reversi_board.grid_array = np.array(
            [
                [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 1, 1, 0, 0, 0, 8],
                [8, 0, 0, 1, 0, 1, 0, 0, 0, 8],
                [8, 0, 1, 0, 0, 1, 0, 0, 0, 8],
                [8,-1, 0, 0, 0, 1, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 1, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 1, 0, 0, 0, 8],
                [8, 0, 0, 1, 1, 1, 1, 0, 0, 8],
                [8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
            ]
        )

        assert self.reversi_board.place_stone(
            Point(1, 5), Player.white) == True
        pprint(self.reversi_board.grid_array)


        self.reversi_board.grid_array = np.array(
            [
                [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 1, 1, 0, 0, 0, 8],
                [8, 0, 0, 1, 0, 1, 0, 0, 0, 8],
                [8, 0, 1, 0, 0, 1, 0, 0, 0, 8],
                [8,-1, 0, 0, 0, 1, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 1, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 1, 0, 0, 0, 8],
                [8, 0, 0, 1, 1,-1, 1, 0, 0, 8],
                [8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
            ]
        )
        assert self.reversi_board.place_stone(
            Point(1, 5), Player.white) == True
        pprint(self.reversi_board.grid_array)
        
        self.reversi_board.grid_array = np.array(
            [
                [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 1, 1, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 1, 0, 0, 0, 8],
                [8, 0, 1, 0, 0, 0, 0, 0, 0, 8],
                [8,-1, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 1, 0, 0, 0, 8],
                [8, 0, 0, 1, 1,-1, 1, 0, 0, 8],
                [8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
            ]
        )
        pprint(self.reversi_board.grid_array)
        assert self.reversi_board.place_stone(
            Point(1, 5), Player.white) == True
        pprint(self.reversi_board.grid_array)


    def test_convert_down(self):
        self.setUp()
        self.reversi_board.grid_array = np.array(
            [
                [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 1, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 1, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 1, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 1, 0, 0, 0, 8],
                [8, 0, 0, 0, 0,-1, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 1, 0, 0, 0, 8],
                [8, 0, 0, 1, 1, 1, 1, 0, 0, 8],
                [8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
            ]
        )

        assert self.reversi_board.place_stone(
            Point(1, 5), Player.white) == True
        pprint(self.reversi_board.grid_array)
        logging.debug("testing down with gap")
        self.reversi_board.grid_array = np.array(
            [
                [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 1, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 1, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 1, 0, 0, 0, 8],
                [8, 0, 0, 0, 0,-1, 0, 0, 0, 8],
                [8, 0, 0, 0, 0, 1, 0, 0, 0, 8],
                [8, 0, 0, 1, 1, 1, 1, 0, 0, 8],
                [8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
            ]
        )
        assert self.reversi_board.place_stone(
            Point(1, 5), Player.white) == True
        pprint(self.reversi_board.grid_array)
"""

"""
Player.black E2
 0  .  .  .  .  .  .  .  . 
 1  .  .  .  .  .  .  .  . 
 2  .  .  .  .  B  .  .  . 
 3  .  .  .  .  B  .  B  . 
 4  .  .  B  B  B  W  B  . 
 5  .  .  .  B  B  .  W  . 
 6  .  .  .  .  B  .  .  W 
 7  .  .  .  .  .  .  .  . 
    A  B  C  D  E  F  G  H
Player.white
bot is working
[Point(row=2, col=4), Point(row=2, col=7), Point(row=2, col=8), Point(row=4, col=2), Point(row=4, col=8), Point(row=5, col=3), Point(row=6, col=4)]
bot is working
Point(row=6, col=4)
Player.white D6
 0  .  .  .  .  .  .  .  . 
 1  .  .  .  .  .  .  .  . 
 2  .  .  .  .  B  .  .  . 
 3  .  .  .  .  B  .  B  . 
 4  .  .  B  B  B  W  B  . 
 5  .  .  .  B  W  .  W  . 
 6  .  .  .  W  W  W  W  W 
 7  .  .  .  .  .  .  .  . 
    A  B  C  D  E  F  G  H
"""
