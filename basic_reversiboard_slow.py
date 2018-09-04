import itertools
import copy
from reversitypes import Player, Point
import logging
import numpy as np

fmt="%(funcName)s():%(lineno)i: %(message)s %(levelname)s"
logging.basicConfig(level=logging.DEBUG, format=fmt)


class BasicReversiBoard():
    def __init__(self, num_rows=8, num_cols=8):
        # it is actually would be better to pad the desk wiht 1,1 and fill with
        # "border" value
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.grid_array = np.zeros(
            (self.num_rows+1) * (self.num_cols+1), dtype=int).reshape(num_rows+1, num_cols+1)

        self.grid_array[0, :] = 8
        self.grid_array[-1, :] = 8
        self.grid_array[:, 0] = 8
        self.grid_array[:, -1] = 8

        # print(np.matrix(self.grid_array))

        self.grid_array[3, 3] = Player.white.value
        self.grid_array[3, 4] = Player.black.value
        self.grid_array[4, 3] = Player.black.value
        self.grid_array[4, 4] = Player.white.value

    def is_valid_place(self, point, player):
        """
        Here we check if in the neighbourhood there is at least one 
        connected line of stone of the other color followed by our color
        """
        # first we will check if the stone is on the board
        if point.row < 0 or point.row >= self.num_rows \
                or point.col < 0 or point.col >= self.num_cols:
            logging.debug("wrong point coords")
            return False
        # check if the slot is already occupied
        logging.debug("checking the validity for {}".format(point))
        logging.debug("the grid value is {}".format(self.grid_array[point.row, point.col]))
        if self.grid_array[point.row, point.col] != 0:
            logging.debug("point {} is occupied".format(point))
            return False
        # then in all directions check and rotate if possible
        """
        You can play a disc when you flank one or more opponents discs between your 
        new disc and any other of your own discs, in the same horizontal, 
        vertical or diagonal line. 
        The opponents discs that are flanked will be turned upside-down and change colour. 
        This turning is called flipping. In figure 2, e5 will be flipped when 
        playing a disc at f5.
        """
        # get the coordinates of the "other"
        logging.debug("getting the indexes of the Other")
        print(np.matrix(self.grid_array))
        logging.debug("the Other player color is {}".format(player.other)) 
        logging.debug("the Other player color value is {}".format(player.other.value)) 
        other_idx = np.where(self.grid_array == player.other.value)
        print(other_idx)
        print(self.grid_array[other_idx])

        # checking left
        if self.grid_array[point.row, point.col-1] != player.other.value:
            return False
        else:
            # get the coordinates of the other on the left
            pass

        # checking right
        # checking up
        # checking down
        # checking left-up
        # checking right-up
        # checking left-down
        # checking right-down

        pass

    def place_stone(self, point, player):
        logging.debug("placing {} {}".format(point.row, point.col))
        if not self.is_valid_place(point, player):
            logging.debug("this is not a valid place")
            logging.debug("the point is {} {}".format(point.row, point.col))
            return False
        self.grid_array[point.row, point.column] = player.value
        self.update_board(point, player)
        pass

    def update_board(self, point, player):
        pass
