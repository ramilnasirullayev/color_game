import numpy as np
from collections import deque
from typing import List

class Board:
    def __init__(self, size: int, colors: List[str], mode: str):
        self.size = size
        self.colors = colors
        self.mode = mode
        self.board = self.initialize_board()

    def initialize_board(self):
        if self.mode == 'easy':
            # Generate a board with large contiguous regions.
            base_board = np.random.choice(self.colors, (self.size//2, self.size//2))
            board = np.repeat(np.repeat(base_board, 2, axis=0), 2, axis=1)
        elif self.mode == 'medium':
            # Generate a board with random distribution.
            board = np.random.choice(self.colors, (self.size, self.size))
        elif self.mode == 'hard':
            # Generate a board with scattered regions.
            board = np.random.choice(self.colors, (self.size, self.size))
            np.random.shuffle(board.flat)
        else:
            raise ValueError("Invalid game mode! Choose from 'easy', 'medium', or 'hard'.")
        return board

    def update_board(self, new_color: str):
        start_color = self.board[0, 0]
        visited = np.zeros((self.size, self.size), dtype=bool)
        self.dfs_fill(0, 0, start_color, new_color, visited)

    def dfs_fill(self, i: int, j: int, start_color: str, new_color: str, visited: np.ndarray):
        if i < 0 or i >= self.size or j < 0 or j >= self.size or visited[i, j] or self.board[i, j] != start_color:
            return

        visited[i, j] = True
        self.board[i, j] = new_color

        self.dfs_fill(i - 1, j, start_color, new_color, visited)  # Up
        self.dfs_fill(i + 1, j, start_color, new_color, visited)  # Down
        self.dfs_fill(i, j - 1, start_color, new_color, visited)  # Left
        self.dfs_fill(i, j + 1, start_color, new_color, visited)  # Right
