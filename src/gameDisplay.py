import os
from termcolor import colored
from src.game import *

class GameDisplay:    
    
    """
    A class representing the game display and user interface.

    Attributes:
        game (Game): The game object.
        color_map (dict): A dictionary mapping color names to corresponding colored text codes.
    """

    def __init__(self, game: Game):

        """
        Initializes the GameDisplay object.

        Parameters:
            game (Game): The game object.
        """

        self.game = game
        self.color_map = {
            'r': 'red',
            'b': 'blue',
            'g': 'green',
            'y': 'yellow',
            # Add more colors here if necessary.
            # The keys should match the colors used in your game.
        }

    def print_board(self):

        """
        Prints the game board with colored cells to the console.
        """
                
        for row in self.game.board.board:
            for color in row:
                print(colored('██', self.color_map[color]), end=' ')
            print()

    def play_game(self):

        """
        Starts the game and handles the user input and turn execution.
        """
                
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
