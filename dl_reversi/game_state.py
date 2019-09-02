from .reversitypes import Player, Point
import copy
from .basic_reversiboard_slow import BasicReversiBoard as Board


class GameState():
    def __init__(self, board, next_player, previous, move):
        self.board = board
        self.next_player = next_player
        self.previous_state = previous
        self.last_move = move

    def apply_move(self, move):
        if move.is_play:
            next_board = copy.deepcopy(self.board)
            next_board.place_stone(move.point, self.next_player)
        else:
            next_board = self.board
        # TODO: this is actually a dumb thing to return a new object!
        return GameState(next_board, self.next_player.other, self, move)

    @classmethod
    def new_game(cls, board_size):
        if isinstance(board_size, int):
            board_size = (board_size, board_size)
        board = Board(*board_size)
        return GameState(board, Player.black, None, None)

    def is_over(self):
        if self.last_move is None:
            return False
        if self.last_move.is_resign:
            return True
        second_last_move = self.previous_state.last_move
        if second_last_move is None:
            return False
        return self.last_move.is_pass and second_last_move.is_pass

    # TODO: must cover with tests
    def is_valid_move(self, move):
        if self.is_over():
            return False
        if move.is_pass or move.is_resign:
            return True

        return self.board.is_valid_place(move.point, self.next_player)



#  8  .  .  .  .  .  .  .  . 
#  7  .  .  .  W  B  B  B  . 
#  6  .  .  .  W  W  B  B  . 
#  5  W  W  W  W  B  W  B  . 
#  4  W  W  W  W  B  B  B  . 
#  3  B  B  B  B  B  B  B  . 
#  2  B  W  W  W  W  W  W  . 
#  1  B  .  .  .  .  .  .  . 
#     A  B  C  D  E  F  G  H

# This configuration does not work