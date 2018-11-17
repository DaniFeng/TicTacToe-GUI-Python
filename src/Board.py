def check_rows(board):
    for row in board:
        index = 1
        front = row[0]
        while index < len(board):
            if front != row[index]:
                return False
            index += 1

    return True


def check_cols(board):
    row = 0
    while row < len(board):
        front = board[row][0]
        col = 1
        while col < len(board[row]):
            if board[row][col] != front:
                return False
            col += 1

        row += 1

    return True


def check_forward_diag(board):
    front = board[0][0]
    rowcol = 1
    while rowcol < len(board):
        if board[rowcol][rowcol] != front:
            return False
        rowcol += 1

    return True


def check_back_diag(board):
    front = board[0][len(board[0]) - 1]
    row = 1
    col = len(board[0]) - 1
    while row < len(board[0]):
        if front != board[row][col]:
            return False
        row += 1
        col -= 1

    return True


class Board:
    def __init__(self):
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.player_ones_turn = True
        self.moves_made = 0

    def player_ones_turn(self):
        return self.player_ones_turn

    def make_move(self):
        self.moves_made += 1

    def get_board(self):
        return self.board

    def player_one_has_won(self):
        if self.moves_made < 5:
            return False

        return check_rows(self.board) and check_cols(self.board) and check_forward_diag(self.board) and check_back_diag(
            self.board)
