from src.board import *
import numpy as np

class Game:

    """
    A class representing the game.

    Attributes:
        board (Board): The game board object.
        max_turns (int): The maximum number of turns allowed in the game.
        turns (int): The current turn count.
    """
     
    def __init__(self, board: Board, max_turns: int):

        """
        Initializes the Game object.

        Parameters:
            board (Board): The game board object.
            max_turns (int): The maximum number of turns allowed in the game.
        """

        self.board = board
        self.max_turns = max_turns
        self.turns = 0

    def is_game_won(self):

        """
        Checks if the game is won, i.e., all cells on the board have the same color.

        Returns:
            bool: True if the game is won, False otherwise.
        """
                
        return np.all(self.board.board == self.board.board[0, 0])

    def play_turn(self, new_color: str):

        """
        Plays a turn by updating the board with the chosen color.

        Parameters:
            new_color (str): The color chosen by the player.
        """

        self.board.update_board(new_color)
        self.turns += 1

    def has_ended(self):

        """
        Checks if the game has ended (reached the maximum number of turns).

        Returns:
            bool: True if the game has ended, False otherwise.
        """

        return self.turns >= self.max_turns
