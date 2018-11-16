class Board:
    def __init__(self):
        self.board = [[""], [""], [""],
                      [""], [""], [""],
                      [""], [""], [""]]
        self.player_ones_turn = True
        self.moves_made = 0

    def player_ones_turn(self):
        return self.player_ones_turn

    def make_move(self):
        self.moves_made += 1

    def get_board(self):
        return self.board

    def check_rows(self):
        index = 0
        while index < len(self.board) - 1:
            print(self.board[index])
            index += 1

        return True

    def player_one_has_won(self):
        return check_rows(self)


t = Board()
print(t.check_rows())
