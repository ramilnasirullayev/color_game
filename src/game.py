from src.board import *
import numpy as np

class Game:
    def __init__(self, board: Board, max_turns: int):
        self.board = board
        self.max_turns = max_turns
        self.turns = 0

    def is_game_won(self):
        return np.all(self.board.board == self.board.board[0, 0])

    def play_turn(self, new_color: str):
        self.board.update_board(new_color)
        self.turns += 1

    def has_ended(self):
        return self.turns >= self.max_turns
