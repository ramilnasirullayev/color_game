from src.board import *

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

class GameDisplay:
    def __init__(self, game):
        self.game = game
        self.color_map = {
            'r': 'red',
            'b': 'blue',
            'g': 'green',
            'y': 'yellow',
        }

    def print_board(self):
        for row in self.game.board.board:
            for color in row:
                print('██', self.color_map[color], end=' ')
            print()

    def play_game(self):
        print('Game Start!')
        while not self.game.has_ended():
            self.print_board()
            color_choice = input(f"Turn {self.game.turns + 1}. Choose a color from {', '.join(self.game.board.colors)}: ").strip().lower()
            while color_choice not in self.game.board.colors:
                color_choice = input(f"Invalid color! Choose a color from {', '.join(self.game.board.colors)}: ").strip().lower()
            self.game.play_turn(color_choice)
            if self.game.is_game_won():
                print("Congratulations, you've won!")
                return
        print("Game Over. You've lost.")

if __name__ == "__main__":
    board = Board(size=18, colors=['r', 'b', 'g', 'y'])
    game = Game(board=board, max_turns=21)
    display = GameDisplay(game=game)
    display.play_game()
