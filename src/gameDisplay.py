import os
from termcolor import colored
from src.game import *

class GameDisplay:
    def __init__(self, game: Game):
        self.game = game
        self.color_map = {
            'red': 'red',
            'blue': 'blue',
            'green': 'green',
            'yellow': 'yellow',
            # Add more colors here if necessary.
            # The keys should match the colors used in your game.
        }

    def print_board(self):
        for row in self.game.board.board:
            for color in row:
                print(colored('██', self.color_map[color]), end=' ')
            print()

    def play_game(self):
        print('Game Start!')
        while not self.game.has_ended():
            os.system('cls' if os.name == 'nt' else 'clear')  # Clears the console
            self.print_board()
            color_choice = input(f"Turn {self.game.turns + 1}. Choose a color from {self.game.board.colors}: ").strip().lower()
            while color_choice not in self.game.board.colors:
                color_choice = input(f"Invalid color! Choose a color from {self.game.board.colors}: ").strip().lower()
            self.game.play_turn(color_choice)
            if self.game.is_game_won():
                print("Congratulations, you've won!")
                return
        print("Game Over. You've lost.")
