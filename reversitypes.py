import enum
from collections import namedtuple

class Player(enum.Enum):
    black = 1
    white = 2

    @property
    def other(self):
        return Player.black if self == Player.white else Player.white


# TODO: not sure if I have to use named tuple here or define properties
class Point(namedtuple('Point', 'row col')):
    def neighbours(self):
        return [
            Point(self.row - 1, self.col),
            Point(self.row + 1, self.col), 
            Point(self.row, self.col - 1),
            Point(self.row, self.col + 1) 
        ]