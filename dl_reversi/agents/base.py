from abc import ABC


class Agent(ABC):
    def __init__(self):
        pass

    def select_move(self, game_state):
        raise NotImplementedError()
