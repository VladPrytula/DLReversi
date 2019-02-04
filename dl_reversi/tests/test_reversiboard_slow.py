import unittest
from ..reversitypes import Player, Point
from ..reversiboard_slow import ReversiBoard


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.reversi_board = ReversiBoard(10, 10)

"""     def test_place_stone(self):
        assert self.reversi_board.place_stone(
            Player.white, point=Point(row=2, col=3)) == False
        assert self.reversi_board.place_stone(
            Player.white, point=Point(row=1, col=1)) == False
        assert self.reversi_board.place_stone(
            Player.white, point=Point(row=3, col=4)) == True
        assert self.reversi_board.place_stone(
            Player.white, point=Point(row=4, col=4)) == False
        assert self.reversi_board.place_stone(
            Player.white, point=Point(row=4, col=5)) == False """