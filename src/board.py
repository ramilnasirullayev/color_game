import random

class Board:
    def __init__(self, size, colors):
        self.size = size
        self.colors = colors
        self.board = self.initialize_board()

    def initialize_board(self):
        board = [[random.choice(self.colors) for _ in range(self.size)] for _ in range(self.size)]
        return board

    def dfs_fill(self, i, j, start_color, new_color, visited):
        if i < 0 or i >= self.size or j < 0 or j >= self.size or visited[i][j] or self.board[i][j] != start_color:
            return

        visited[i][j] = True
        self.board[i][j] = new_color

        self.dfs_fill(i - 1, j, start_color, new_color, visited)  # Up
        self.dfs_fill(i + 1, j, start_color, new_color, visited)  # Down
        self.dfs_fill(i, j - 1, start_color, new_color, visited)  # Left
        self.dfs_fill(i, j + 1, start_color, new_color, visited)  # Right
