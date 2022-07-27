
class Game:
    # the Game class contains all methods for running the Game

    def __init__(self):
        pass

    def display_game_rule(self):
        # display the game rule
        print("Welcome to Rock Paper Scissors Lizard Spock")
        print(f"Each match will be best of three games\nUse the number keys to enter your selection")
        print(f"Scissor cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock")
        print(f"Spock smashes Scissor\nScissor decapitates Lizard\nLizard eats Paper")
        print(f"Paper disproves Spock\nSpock vaporizes Rock\nRock crushes Scissors\n")

    def human_player_selection(self):
        # ask how many human players will paly
        pass

    def ai_player_selection(self):
        # ask how mamy ai will play
        pass

    def run_game(self):
        # game starts
        # game ends when one play has two wins
        pass

    def display_winner_for_the_round(self):
        # display the winner for the round
        pass

    def display_finnal_winner(self):
        pass

    def play_again(self):
        # aks whether user wants to play again
        pass

    def game_end(self):
        # print game ends message
        pass
