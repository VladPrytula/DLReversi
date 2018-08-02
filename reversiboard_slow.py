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

        self.placed_stones = {Point(4, 4): Player.white,
                              Point(4, 5): Player.black,
                              Point(5, 4): Player.white,
                              Point(5, 5): Player.black}

        # This should be extracted to the separate functions, since it is used during the game
        self.extended_placed_stones = set()
        self.available_positions = set()
        self.update_extended_placed_stones()
        self.update_available_positions()

        print("placed stone positions are {}".format(self.placed_stones))
        print("placed stone and eighbours are {}".format(
            self.extended_placed_stones))
        print("available places {}".format(self.available_positions))

    def place_stone(self, player, point):
        assert self.is_on_grid(point)
        if self.can_be_placed(point):
            self.placed_stones[point] = player
            logging.debug("new placed stones {}".format(self.placed_stones))
            self.update_available_positions()
            self.update_placed_stones(player, point)
            return True
        return False

    def is_on_grid(self, point):
        logging.debug("point  ({}, {}) is on the grid".format(
            point.row, point.col))
        return 1 <= point.row <= self.num_rows and \
            1 <= point.col <= self.num_cols

    def can_be_placed(self, point):
        logging.debug("Placing  ({}, {})".format(point.row, point.col))
        print(self.available_positions)
        if point in self.available_positions:
            return True
        return False

    def update_available_positions(self):
        logging.debug("updating available positions")
        self.available_positions = self.extended_placed_stones - \
            set(self.placed_stones.keys())

    def update_extended_placed_stones(self):
        self.extended_placed_stones = set(itertools.chain.from_iterable(
            [s.neighbours() for s in self.placed_stones.keys()]))

    def update_placed_stones(self, player, point):
        pass
        def up():
            pass

        def down():
            pass
        
        def left():
            pass

        def right():
            pass
        
        def up_right():
            pass

        def up_left():
            pass

        def down_left():
            pass

        def down_right():
            pass
        
        # TODO: this thing looks BAD!
        # from enum import Enum
        # Directions = Enum('left',
        #                   'right',
        #                   'up',
        #                   'down',
        #                   'left-up',
        #                   'left-down',
        #                   'right-up',
        #                   'right-down')

        # def check_in_direction(direction):
        #     for col in range()
        #     pass

        # def check_horizontal():
        #     """
        #     check if among the stones on the board there exists one with the same 
        #     y coordinat
        #     """
        #     print("check horizontal start")
        #     horizontal_sorted_player = [x for x in sorted(
        #         self.placed_stones.items(), key=lambda k: k[0].col) if x[1] == player]
        #     horizontal_sorted_other = [x for x in sorted(
        #         self.placed_stones.items(), key=lambda k: k[0].col) if x[1] != player]
        #     print(horizontal_sorted_player)
        #     print(horizontal_sorted_other)
        #     print("check horizontal end")
        #     """
        #     TODO: here it might make sense to store sorted ony with coords, since it was split by color already
        #     """
        # check_horizontal()
