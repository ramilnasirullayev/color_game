class Game:
    def __init__(self, board, max_turns):
        self.board = board
        self.max_turns = max_turns
        self.turns = 0

    def is_game_won(self):
        return all(self.board.board[i][j] == self.board.board[0][0] for i in range(self.board.size) for j in range(self.board.size))

    def play_turn(self, new_color):
        self.board.update_board(new_color)
        self.turns += 1

    def has_ended(self):
        return self.turns >= self.max_turns