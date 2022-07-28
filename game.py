from human import Human
from ai import Ai


class Game:
    # the Game class contains all methods for running the Game

    def __init__(self):
        # 0 Rock
        # 1 Paper
        # 2 Scissors
        # 3 Lizard
        # 4 Spock
        self.player1 = ""
        self.player2 = ""
        self.player1_gesture_index = 0
        self.player2_gesture_index = 0
        # self.gesture_list = [0, 1, 2, 3, 4]
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
            # self.player1 = ai_player1
            # self.player2 = ai_player2
            # self.player1_gesture
            # self.player2_gesture
        elif self.human_player_number == 1:
            print(
                f"----Human Player {self.human_player_number} is choosing the gesture----")
            self.player1 = Human("Human One")
            self.player1.select_gesture()
            print(
                f"\n----AI player {self.human_player_number} is generating the gesture----")

            self.player2 = Ai("AI One")
            self.player2.select_gesture()
        else:
            print("multiple human players selected")
            print(
                f"----Human Player {self.human_player_number - 1} is choosing the gesture----")
            print(
                f"----Human Player {self.human_player_number} is choosing the gesture----")

        self.play_again_check()

    def determine_winner_for_the_round(self, player1_gesture_index, player2_gesture_index):
        # display the winner for the round
        if player1_gesture_index == 0:
            if player2_gesture_index == 0:
                print("tie, try again")
            elif player2_gesture_index == 1 or player2_gesture_index == 4:
                print(f"{self.player2.name} wins")
                self.player2_wins += 1
            else:
                print(f"{self.player1.name} wins")
                self.player1_wins += 1
        elif player1_gesture_index == 1:
            if player2_gesture_index == 1:
                print("tie, try again")
            elif player2_gesture_index == 0 or player2_gesture_index == 4:
                print(f"{self.player1.name}wins")
                self.player1_wins += 1
            else:
                print(f"{self.player2.name} wins")
                self.player2_wins += 1

        elif player1_gesture_index == 2:
            if player2_gesture_index == 2:
                print("tie, try again")
            elif player2_gesture_index == 1 or player2_gesture_index == 3:
                print(f"{self.player1.name}wins")
                self.player1_wins += 1
            else:
                print(f"{self.player2.name} wins")
                self.player2_wins += 1
        elif player1_gesture_index == 3:
            if player2_gesture_index == 3:
                print("tie, try again")
            elif player2_gesture_index == 1 or player2_gesture_index == 4:
                print(f"{self.player1.name}wins")
                self.player1_wins += 1
            else:
                print(f"{self.player2.name} wins")
                self.player2_wins += 1
        else:
            if player2_gesture_index == 4:
                print("tie, try again")
            elif player2_gesture_index == 0 or player2_gesture_index == 2:
                print(f"{self.player1.name}wins")
                self.player1_wins += 1
            else:
                print(f"{self.player2.name} wins")
                self.player2_wins += 1

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
