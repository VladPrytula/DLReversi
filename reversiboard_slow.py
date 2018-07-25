import itertools
import copy
from reversitypes import Player, Point
import logging

logging.basicConfig(level=logging.DEBUG)


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
    def __init__(self, num_rows=10, num_cols=10):
        self.num_rows = num_rows
        self.num_cols = num_cols
        """
        grid = {Point: color}
        """
        self.__grid = {}  # a dcitionary where we store stones

        # a set of available coord for stones
        # This is wrong. TODO: redo the whole thing.
        #self.init_positions = list(itertools.chain.from_iterable([Point(4,4).neighbours(), 
        #                                Point(5,5).neighbours(), 
        #                                Point(4,5).neighbours(), 
        #                                Point(5,4).neighbours()]))
        self.placed_stones = {Point(4,4) : "white", 
                             Point(4,5) : "black",
                             Point(5,4) : "white",
                             Point(5,5) : "black"}

        self.extended_placed_stones = set(itertools.chain.from_iterable([s.neighbours() for s in self.placed_stones.keys()]))
        self.available_positions = self.extended_placed_stones -set(self.placed_stones.keys())

        #print("placed stones are {}".format(self.placed_stones))
        #print("placed stone positions are {}".format(list(self.placed_stones.keys())))
        #print("placed stone neighbours are {}".format([s.neighbours() for s in self.placed_stones.keys()]))
        print("placed stone positions are {}".format(self.placed_stones))
        print("placed stone and eighbours are {}".format(self.extended_placed_stones))
        print("available places {}".format(self.available_positions))


                            

    def place_stone(self, player, point):
        assert self.is_on_grid(point)
        assert self.can_be_placed(point)
        return False

    def is_on_grid(self, point):
        logging.debug("point  ({}, {}) is on the grid".format(point.row, point.col))
        return 1 <= point.row <= self.num_rows and \
            1 <= point.col <= self.num_cols

    def can_be_placed(self, point):
        logging.debug("Placing  ({}, {})".format(point.row, point.col))
        print(self.available_positions)
        if point in self.available_positions: 
            self.update_available_positions(point)
            return True
        return False

    def check_connected_component(self, player, point):
        pass

    def update_available_positions(self, point):
        logging.debug("checking available positions")
        return self
