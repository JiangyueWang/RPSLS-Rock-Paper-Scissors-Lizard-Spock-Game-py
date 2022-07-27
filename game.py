
class Game:
    # the Game class contains all methods for running the Game

    def __init__(self):
        # 0 Rock
        # 1 Paper
        # 2 Scissors
        # 3 Lizard
        # 4 Spock
        self.player1_gesture = 0
        self.gesture_list = [0, 1, 2, 3, 4]
        self.player1_wins = 0
        self.player2_wins = 0

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

    def human_player_number_selection(self):
        # ask how many human players will paly
        print("how many human player? ")
        self.human_player_number = self.check_user_input(2)
        print(f"{self.human_player_number} human player(s) have selected\n")

    def ai_player_selection(self):
        # ask how mamy ai will play
        pass

    def run_game(self):
        # game starts
        self.display_game_rule()
        self.human_player_number_selection()
        if self.human_player_number == 0:
            print("----No human players----")
            print("----AI players are generating gestures----")
            # ai_player_selection
            # display player_1_gesture
            # display player_2_gesture
        elif self.human_player_number == 1:
            print(
                f"----Human Player {self.human_player_number} is choosing the gesture----")
            print(
                f"----AI player {self.human_player_number} is generating the gesture----")
            # ai_player generates gesture
        else:
            print("multiple human players selected")
            print(
                f"----Human Player {self.human_player_number - 1} is choosing the gesture----")
            print(
                f"----Human Player {self.human_player_number} is choosing the gesture----")

        self.play_again_check()

    def determine_winner_for_the_round(self):
        # display the winner for the round
        if self.player1_gesture == 0:
            for self.player2_gesture in self.gesture_list:
                if self.player2_gesture == 0:
                    print("tie, try again")
                elif self.player2_gesture == 1 or self.player2_gesture == 4:
                    print("player2 wins")
                    self.player2_wins += 1
                else:
                    print("player1 wins")
                    self.player1_wins += 1

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
