from colorama import init, Fore, Style

class GameDisplay:
    def __init__(self, game):
        self.game = game
        self.color_map = {
            'r': Fore.RED,
            'b': Fore.BLUE,
            'g': Fore.GREEN,
            'y': Fore.YELLOW,
        }
        init(autoreset=True)  # Initialize colorama

    def print_board(self):
        for row in self.game.board.board:
            for color in row:
                print(f'{Style.BRIGHT}██{self.color_map[color]}██', end=' ')
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
                print(Fore.GREEN + "Congratulations, you've won!")
                return
        print(Fore.RED + "Game Over. You've lost.")