import random

class Board:
    def __init__(self, size, colors):
        self.size = size
        self.colors = colors
        self.board = self.initialize_board()

    def initialize_board(self):
        board = [[random.choice(self.colors) for _ in range(self.size)] for _ in range(self.size)]
        return board

    def update_board(self, new_color):
        start_color = self.board[0][0]
        visited = [[False for _ in range(self.size)] for _ in range(self.size)]
        queue = [(0, 0)]
        while queue:
            i, j = queue.pop(0)
            if (i < 0 or i >= self.size or j < 0 or j >= self.size or
                    visited[i][j] or self.board[i][j] != start_color):
                continue
            self.board[i][j] = new_color
            visited[i][j] = True
            queue.extend([(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)])