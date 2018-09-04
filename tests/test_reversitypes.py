import unittest
from reversitypes import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player.black

    def test_other_player(self):
        print(self.player.other)
        assert self.player.other == Player.white
