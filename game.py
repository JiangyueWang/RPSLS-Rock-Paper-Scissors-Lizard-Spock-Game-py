
class Game:
    # the Game class contains all methods for running the Game

    def __init__(self):
        pass

    def display_game_rule(self):
        # display the game rule
        print(f"\nWelcome to Rock Paper Scissors Lizard Spock")
        print(f"Each match will be best of three games\nUse the number keys to enter your selection\nupdated ")
        print(f"Scissor cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock")
        print(f"Spock smashes Scissor\nScissor decapitates Lizard\nLizard eats Paper")
        print(f"Paper disproves Spock\nSpock vaporizes Rock\nRock crushes Scissors\n")

    def check_user_input(self, range):
        while True:
            self.user_input = input(f'enter valid integer from 0 to {range}: ')
            try:
                self.user_input = int(self.user_input)
            except ValueError:
                print("invalid input, please enter a valid integer number again.")
            else:
                print("valid entry")
                break
        return self.user_input

    def human_player_selection(self):
        # ask how many human players will paly
        print("how many human player? ")
        self.human_player_number = self.check_user_input(2)
        print(f"{self.human_player_number} human player(s) have selected\n")
        # if self.human_player_number == 0:
        # no human players
        # ai_player_selection
        # if self.human_player_numer == 1:
        # ai_player generates gesture
        # if self.human_player_number == 2:
        # human_1 choose gesture
        # human_2 choose gesture

    def ai_player_selection(self):
        # ask how mamy ai will play
        pass

    def run_game(self):
        # game starts
        self.display_game_rule()
        self.human_player_selection()
        # game ends when one play has two wins
        self.play_again_check()

    def display_winner_for_the_round(self):
        # display the winner for the round
        pass

    def display_finnal_winner(self):
        pass

    def play_again_check(self):
        # aks whether user wants to play again

        while True:
            print("Do you want to play again?")
            self.user_play_again_decision = input("Enter y/n:").lower()
            if self.user_play_again_decision == "y":
                self.run_game()
            elif self.user_play_again_decision == "n":
                self.game_end_message()
                break
            else:
                print("invalid selection, choose again")

    def game_end_message(self):
        print("Thank you for playing RPSLS game, see you next time.")
