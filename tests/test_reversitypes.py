import unittest
from reversitypes import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player(1)

    def test_other_player(self):
        print(self.player.other)
        assert self.player.other == Player.white
        pass



