import itertools
import copy
from reversitypes import Player, Point
import logging
import numpy as np

fmt = "%(funcName)s():%(lineno)i: %(message)s %(levelname)s"
logging.basicConfig(level=logging.DEBUG, format=fmt)

"""
Currently Working with this Class
"""


class BasicReversiBoard():
    def __init__(self, num_rows=8, num_cols=8):
        # it is actually would be better to pad the desk wiht 1,1 and fill with
        # "border" value
        self.num_rows = num_rows
        self.num_cols = num_cols
        # we are actaully using padding here
        self.grid_array = np.zeros(
            (self.num_rows+1) * (self.num_cols+1), dtype=int).reshape(num_rows+1, num_cols+1)

        # 8 is used to define the padded board
        self.grid_array[0, :] = 8
        self.grid_array[-1, :] = 8
        self.grid_array[:, 0] = 8
        self.grid_array[:, -1] = 8

        # logging.debug(np.matrix(self.grid_array))

        # setting up initial board configuration
        # TODO: center of the board should not be hardcoded
        # currently it is only for 8x8 board
        self.grid_array[3, 3] = Player.white.value
        self.grid_array[3, 4] = Player.black.value
        self.grid_array[4, 3] = Player.black.value
        self.grid_array[4, 4] = Player.white.value

    # TODO: this shoudl be renamed so that the function returns bool and
    # idx, idy of the stones for turn directions
    def place_stone(self, point, player):
        logging.debug("placing {} {}".format(point.row, point.col))
        """
        Here we check if in the neighbourhood there is at least one 
        connected line of stone of the other color followed by our color
        """
        # first we will check if the stone is on the board
        if point.row < 0 or point.row >= self.num_rows \
                or point.col < 0 or point.col >= self.num_cols:
            logging.debug(
                "wrong point coords, attempting to place outside the board")
            return False
        # check if the slot is already occupied
        logging.debug(
            "checking the validity for point {} and player {}".format(point, player))
        logging.debug("the grid value is {}".format(
            self.grid_array[point.row, point.col]))
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
        logging.debug(
            "the Other player color value is {}".format(player.other.value))
        # TODO: we do not need other_idx
        other_idx = np.where(self.grid_array == player.other.value)
        logging.debug(other_idx)
        logging.debug(self.grid_array[other_idx])
        # TODO: we do not need other_idx

        # checking left
        if self.grid_array[point.row, point.col-1] != player.other.value:
            logging.debug(
                'there is no opponnent stone immediately to the left')
            return False
        else:
            logging.info('there is an other stone to the left of {} {}'.format(
                point.row, point.col-1))
            # get the coordinates of the other on the left
            idy = np.where(self.grid_array[point.row, point.col:])[0][0]
            logging.debug('first Other to the left is {}'.format(idy))
            # actually here we have to update the board
            logging.info('reversing stones to the left')
            # we place the stone at the same time
            self.grid_array[point.row, idy:point.col+1] = player.value
            print(np.matrix(self.grid_array))
            return True

        # checking right
        if self.grid_array[point.row, point.col+1] != player.other.value:
            logging.debug(
                'there is no opponnent stone immediately to the right')
            # TODO: actually it makes sense to update the state at this point of time
            # TODO: the function should be renamed respecitvely
            return False
        else:
            # get the coordinates of the other on the left
            pass
        # checking up
        # checking down
        # checking left-up
        # checking right-up
        # checking left-down
        # checking right-down
        return False
