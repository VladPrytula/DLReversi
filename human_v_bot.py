from dl_reversi.agents import naive
from dl_reversi.basic_reversiboard_slow import BasicReversiBoard
from dl_reversi.game_state import GameState
from dl_reversi.move import Move
import dl_reversi.reversitypes
from dl_reversi.utils import print_board, print_move, point_from_cords
from pprint import pprint
import time


def main():
    board_size = 8
    game = GameState.new_game(board_size)
    bot = naive.RandomBot()

    while not game.is_over():
        #print(chr(27) + "[2J")
        print_board(game.board)
        # pprint(game.board.grid_array)
        print(game.next_player)
        if game.next_player == dl_reversi.reversitypes.Player.black:
            candidates = []
            for row in range(game.board.num_rows+1):
                for col in range(game.board.num_cols+1):
                    candidate_point = dl_reversi.reversitypes.Point(
                        row=row, col=col)
                    if game.is_valid_move(Move.play(candidate_point)):
                        candidates.append(candidate_point)
            print(candidates)
            human_move = input('-- ')
            point = point_from_cords(human_move.strip())
            print(point)
            time.sleep(3)
            if point in candidates:
                move = Move.play(point)
            else:
                print("you can't do that")
                print("skippingj")
                move=None

        else:
            print('bot is working')
            #time.sleep(3)
            move = bot.select_move(game)
            print('bot is working')
            time.sleep(3)
        print(move.point)
        # time.sleep(10)
        print_move(game.next_player, move)
        # time.sleep(3)
        game = game.apply_move(move)


if __name__ == '__main__':
    main()
