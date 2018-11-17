def check_row(board):
    front = board[0]
    for number in board:
        if number != front:
            return False
    return True


def check_col(board, col):
    front = board[0][col]
    row = 1
    while row < len(board):
        if board[row][col] != front:
            return False
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
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.player_ones_turn = True
        self.moves_made = 0

    def player_ones_turn(self):
        if self.player_ones_turn:
            return True
        return False

    def make_move(self, row, col):
        if self.board[row][col] != '-':
            raise TypeError

        self.moves_made += 1
        if self.player_ones_turn:
            self.board[row][col] = "x"
        else:
            self.board[row][col] = "o"

        self.player_ones_turn = not self.player_ones_turn

    def get_board(self):
        return self.board

    def game_over(self):
        if self.moves_made < 5:
            return False

        for row in self.board:
            if check_row(row):
                return True

        col = 0
        while col < len(self.board[col]):
            if check_col(self.board, col):
                return True
            col += 1

        return check_forward_diag(self.board) and check_back_diag(self.board)
