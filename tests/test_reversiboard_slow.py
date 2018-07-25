import unittest
from reversiboard_slow import ReversiBoard
from reversitypes import Player, Point


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.reversi_board = ReversiBoard(10, 10)
        
    def test_place_stone(self):
        assert self.reversi_board.place_stone(Player(1), point=Point(row=1, col=1))
