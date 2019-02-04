from dl_reversi.agents import naive
from dl_reversi.basic_reversiboard_slow import BasicReversiBoard
from dl_reversi.game_state import GameState
import dl_reversi.reversitypes
from dl_reversi.utils import print_board, print_move
import time


def main():
    board_size = 8
    game = GameState.new_game(board_size)
    bots = {
        dl_reversi.reversitypes.Player.black: naive.RandomBot(),
        dl_reversi.reversitypes.Player.white: naive.RandomBot(),
    }
    while not game.is_over():
        time.sleep(3)

        print(chr(27) + "[2J")
        # print(chr(27))
        print_board(game.board)
        bot_move = bots[game.next_player].select_move(game)
        print_move(game.next_player, bot_move)
        game = game.apply_move(bot_move)


if __name__ == '__main__':
    main()
