import copy
from reversitypes import Player


class Move():
    """
    A structure that represent the actions a player can take on a turn.
    Normally, a turn imnplies placing a stone on the board, but a player 
    can also pass or resign at any time

    Here we make a distinction that play() refers to placing a stone and 
    move means any of the above mentioned actions

    To play, user has to pass a point, location, of the stone

    client is supposed not to call the Move constructor but call 
    Move.play, Move.pass_turn, Move.resign to cunstruct the instance of a move.
    """

    def __init__(self, point=None, is_pass=False, is_resign=False):
        assert (point is not None) ^ is_pass ^ is_resign
        self.point = point
        self.is_play = (self.point is not None)
        self.is_pass = is_pass
        self.is_resign = is_resign

    @classmethod
    def play(cls, point):
        return Move(point=point)

    @classmethod
    def pass_turn(cls):
        return Move(is_pass=True)

    @classmethod
    def resign(cls):
        return Move(is_resign=True)


class ReversiString():
    """
    Perhaps while this is sutibale for GO, it is overcomplicated for Reversi
    """

    def __init(self, color, stones, slots):
        self.color = color
        self.stones = set(stones)
        self.slots = set(slots)


class ReversiBoard():
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        """
        grid = {Point: color}
        """
        self.__grid = {}  # a dcitionary where we store stones

        # a set of available coord for stones
        self.__available_positions = set()

    def place_stone(self, player, point):
        assert self.is_on_grid(point)
        assert self.can_be_placed(point)
        return False

    def is_on_grid(self, point):
        return 1 <= point.row <= self.num_rows and \
            1 <= point.col <= self.num_cols

    def can_be_placed(self, point):
        if not self.occupied(point):
            pass
        return False

    def occupied(self, point):
        return False

    def check_connected_component(self, player, point):
        pass

    def update_available_positions(self):
        return self
