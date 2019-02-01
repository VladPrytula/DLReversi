import itertools
import copy
from reversitypes import Player, Point
import logging
import numpy as np
from pprint import pprint


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

    def _is_on_board(self, point, player) -> bool:
        # first we will check if the stone is on the board
        if point.row < 0 or point.row >= self.num_rows \
                or point.col < 0 or point.col >= self.num_cols:
            logging.debug(
                "wrong point coords, attempting to place outside the board")
            return False
        else:
            return True

    def _is_occupied(self, point, player) -> bool:
        logging.debug(
            "checking the validity for point {} and player {}".format(point, player))
        logging.debug("the grid value is {}".format(
            self.grid_array[point.row, point.col]))
        if self.grid_array[point.row, point.col] != 0:
            logging.debug("point {} is occupied".format(point))
            return True

    def place_stone(self, point, player) -> bool:
        logging.debug("placing {} {}".format(point.row, point.col))
        """
        Here we check if in the neighbourhood there is at least one 
        connected line of stone of the other color followed by our color
        """

        neaby_other = {"left": False, "right": False,
                       "down": False, "up": False, "up_left": False, "up_right": False}

        if not self._is_on_board(point, player):
            return False

        if self._is_occupied(point, player):
            return False

        # then in all directions check and rotate if possible
        """
        You can play a disc when you flank one or more opponents discs between your 
        new disc and any other of your own discs, in the same horizontal, 
        vertical or diagonal line. 
        The opponents discs that are flanked will be turned upside-down and change colour. 
        This turning is called flipping. In figure 2, will be flipped when 
        playing a disc at f5.
        """
        # get the coordinates of the "other"
        logging.debug("getting the indexes of the Other")
        pprint(self.grid_array)
        logging.debug("the Other player color is {}".format(player.other))
        logging.debug(
            "the Other player color value is {}".format(player.other.value))
        # TODO: we do not need other_idx
        # other_idx = np.where(self.grid_array == player.other.value)
        # logging.debug(other_idx)
        # logging.debug(self.grid_array[other_idx])
        # # TODO: we do not need other_idx

        # checking left
        logging.info('checking left')
        if self.grid_array[point.row, point.col-1] != player.other.value:
            logging.debug(
                'there is no opponnent stone immediately to the left')
        elif np.where(self.grid_array[point.row, :point.col] == player.value)[0].size == 0:
            logging.debug('there are no our stones to the left')
            logging.debug(
                np.where(self.grid_array[point.row, :point.col] == player.value)[0])
        else:
            # get the index of the first stone of our color to the left
            idY = np.where(
                self.grid_array[point.row, :point.col] == player.value)[0][0]
            print(idY)
            self.grid_array[point.row, idY:point.col+1] = player.value
            neaby_other["left"] = True

        # checking right
        logging.info('checking right')
        if self.grid_array[point.row, point.col+1] != player.other.value:
            logging.debug(
                'there is no opponnent stone immediately to the right')
        elif np.where(self.grid_array[point.row, point.col+1:] == player.value)[0].size == 0:
            logging.debug('there are no our stones to the right')
            logging.debug(
                np.where(self.grid_array[point.row, point.col+1:] == player.value)[0])
        else:
            # get the index of the first stone of our color to the right
            idY = np.where(
                self.grid_array[point.row, point.col+1:] == player.value)[0][0]
            print(idY)
            self.grid_array[point.row,
                            point.col:point.col+idY+1] = player.value
            neaby_other["right"] = True

        # checking down
        logging.info('checking down')
        if self.grid_array[point.row+1, point.col] != player.other.value:
            logging.debug(
                'there is no opponnent stone immediately to the down')
        elif np.where(self.grid_array[point.row+1:, point.col] == player.value)[0].size == 0:
            logging.debug('there are no our stones to the down')
            logging.debug(
                np.where(self.grid_array[point.row+1:, point.col] == player.value)[0])
        else:
            # get the index of the first stone of our color to the down
            idY = np.where(
                self.grid_array[point.row+1:, point.col] == player.value)[0][0]
            print(idY)
            self.grid_array[point.row:point.row +
                            idY+1, point.col] = player.value
            neaby_other["down"] = True
        # checking up
        logging.info('checking up')
        if self.grid_array[point.row-1, point.col] != player.other.value:
            logging.debug(
                'there is no opponnent stone immediately to the up')
        elif np.where(self.grid_array[:point.row, point.col] == player.value)[0].size == 0:
            logging.debug('there are no our stones to the left')
            logging.debug(
                np.where(self.grid_array[:point.row, point.col] == player.value)[0])
        else:
            # get the index of the first stone of our color to the left
            idY = np.where(
                self.grid_array[:point.row, point.col] == player.value)[0][0]
            print(idY)
            self.grid_array[idY:point.row+1, point.col] = player.value
            neaby_other["up"] = True

        # checking up-left

        """
        ----- diagonals are wrong due to the incorrect iteration is loops
        """

        logging.info('checking up-left')

        def _find_closest_stone_up_left()->(int, int):
            closest_stone_row, closest_stone_col = -2, -2
            for row in reversed(range(point.row-1)):
                for col in reversed(range(point.col-1)):
                    if self.grid_array[row, col] == player.value:
                        return (row, col)
                    break
            return (closest_stone_row, closest_stone_col)

        closest_stones = _find_closest_stone_up_left()
        logging.debug(
            "closest stones our stone checking up-left is {}".format(closest_stones))
        if self.grid_array[point.row-1, point.col-1] != player.other.value:
            logging.debug(
                'there is no opponnent stone immediately to the up-left')
        elif closest_stones == (-2, -2):
            logging.debug('there are no our stones to the up-left')
        else:
            for row in range(closest_stones[0], point.row):
                for col in range(closest_stones[1], point.col):
                    self.grid_array[row, col] = player.value
                    break
            neaby_other["up_left"] = True

        # checking up-right
        logging.info('checking up-right')

        def _find_closest_stone_up_right()->(int, int):
            closest_stone_row, closest_stone_col = -2, -2
            for row in reversed(range(point.row-1)):
                for col in range(point.col, self.num_cols+1):
                    logging.debug("(row={}, col={})".format(row, col))
                    if self.grid_array[row, col] == player.value:
                        return (row, col)
                    break
            return (closest_stone_row, closest_stone_col)

        closest_stones = _find_closest_stone_up_right()
        logging.debug(
            "closest stones our stone checking up-right is {}".format(closest_stones))
        if self.grid_array[point.row-1, point.col+1] != player.other.value:
            logging.debug(
                'there is no opponnent stone immediately to the up-right')
        elif closest_stones == (-2, -2):
            logging.debug('there are no our stones to the up-right')
        else:
            for row in range(closest_stones[0], point.row):
                for col in range(point.col, closest_stones[1]):
                    self.grid_array[row, col] = player.value
                    break
            neaby_other["up_right"] = True
        # checking left-down
        # checking right-down

        return any(value == True for value in neaby_other.values())
