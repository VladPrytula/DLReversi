from . import reversitypes

COLS = 'ABCDEFGHJKLMNOPQRST'
STONE_TO_CHAR = {
    None: ' . ',
    reversitypes.Player.black: ' B ',
    reversitypes.Player.white: ' W ',
}


def print_move(player, move):
    if move.is_pass:
        move_str = 'passes'
    elif move.is_resign:
        move_str = 'resigns'
    else:
        move_str = '%s%d' % (COLS[move.point.col - 1], move.point.row)
    print('%s %s' % (player, move_str))

def point_from_cords(coords):
    col = COLS.index(coords[0]) + 1
    row = int(coords[1:])
    return reversitypes.Point(row, col)


def print_board(board):
    for row in range(0, board.num_rows): #, 0, -1):
        bump = " " if row <= 9 else ""
        line = []
        for col in range(1, board.num_cols+1):
            stone = board.get(reversitypes.Point(row=row, col=col))
            line.append(STONE_TO_CHAR[stone])
        print('%s%d %s' % (bump, row, ''.join(line)))
    print('    ' + '  '.join(COLS[:board.num_cols]))