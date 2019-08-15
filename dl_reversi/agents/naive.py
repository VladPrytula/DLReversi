import random
from .base import Agent
from ..reversitypes import Point
from ..move import Move
from ..game_state import GameState


class RandomBot(Agent):
    def select_move(self, game_state):
        """Choose a random valid move from all available moves."""
        candidates = []
        for row in range(game_state.board.num_rows+1):
            for col in range(game_state.board.num_cols+1):
                candidate_point = Point(row=row, col=col)
                if game_state.is_valid_move(Move.play(candidate_point)):
                    candidates.append(candidate_point)

        if not candidates:
            return Move.pass_turn()
        return Move.play(random.choice(candidates)) #here we actually do a random choice
