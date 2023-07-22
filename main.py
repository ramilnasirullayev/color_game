from src.board import *
from src.game import *
from src.gameDisplay import *



if __name__ == "__main__":
    board = Board(size=18, colors=['r', 'b', 'g', 'y'])
    game = Game(board=board, max_turns=21)
    display = GameDisplay(game=game)
    display.play_game()
