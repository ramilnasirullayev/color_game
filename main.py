from src.board import *
from src.game import *
from src.gameDisplay import *


def get_board_size():
    while True:
        try:
            size = int(input("Enter the board size (an integer greater than 0): "))
            if size <= 0:
                print("Please enter a valid board size greater than 0.")
            else:
                return size
        except ValueError:
            print("Invalid input. Please enter a valid board size (an integer greater than 0).")

def get_game_mode():
    while True:
        mode = input("Enter the game mode ('easy', 'medium', or 'hard'): ").strip().lower()
        if mode in ['easy', 'medium', 'hard']:
            return mode
        else:
            print("Invalid game mode! Choose from 'easy', 'medium', or 'hard'.")

def get_max_turns():
    while True:
        try:
            max_turns = int(input("Enter the maximum number of turns (an integer greater than 0): "))
            if max_turns <= 0:
                print("Please enter a valid maximum number of turns greater than 0.")
            else:
                return max_turns
        except ValueError:
            print("Invalid input. Please enter a valid maximum number of turns (an integer greater than 0).")

if __name__ == "__main__":
    size = get_board_size()
    colors = ['r', 'b', 'g', 'y']
    mode = get_game_mode()
    max_turns = get_max_turns()

    board = Board(size=size, colors=colors, mode=mode)
    game = Game(board=board, max_turns=max_turns)
    display = GameDisplay(game=game)
    display.play_game()
