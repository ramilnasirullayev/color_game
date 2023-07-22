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
