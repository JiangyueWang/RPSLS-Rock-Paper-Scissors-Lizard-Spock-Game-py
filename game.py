from human import Human
from ai import Ai
import time


class Game:
    # the Game class contains all methods for running the Game

    def __init__(self):
        # 0 Rock
        # 1 Paper
        # 2 Scissors
        # 3 Lizard
        # 4 Spock
        self.player1 = None
        self.player2 = None
        self.player1_gesture_index = 0
        self.player2_gesture_index = 0
        # self.gesture_list = [0, 1, 2, 3, 4]
        self.player1_wins = 0
        self.player2_wins = 0
        self.round_num = 1

    def display_game_rule(self):
        # display the game rule
        print(f"\nWelcome to Rock Paper Scissors Lizard Spock")
        print(f"Each match will be best of three games\nUse the number keys to enter your selection\n\n")
        print(f"Scissor cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\n")
        print(f"Spock smashes Scissor\nScissor decapitates Lizard\nLizard eats Paper\n")
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
        if self.human_player_number == 1:
            self.player1 = Human("Human One")
            self.player2 = Ai("AI One")
        elif self.human_player_number == 2:
            self.player1 = Human("Human One")
            self.player2 = Human("Human Two")
        elif self.human_player_number == 0:
            self.player1 = Ai("AI One")
            self.player2 = Ai("AI Two")

    def run_game(self):
        # game starts
        self.display_game_rule()
        self.human_player_number_selection()
        while True:
            if self.player1_wins == 2 or self.player2_wins == 2:
                break
            else:
                print(f"----round {self.round_num} starts----")
                # player 1 chooses gesture
                print(
                    f"----{self.player1.player_name} is choosing the gesture----")
                self.player1.select_gesture()
                # player 1 chooses gesture
                print(
                    f"\n----{self.player2.player_name} is choosing the gesture----")
                time.sleep(2)
                self.player2.select_gesture()

                if self.human_player_number == 0:
                    # two ai players
                    self.player1_gesture_index = self.player1.ai_rand_gesture_index
                    self.player2_gesture_index = self.player2.ai_rand_gesture_index
                elif self.human_player_number == 1:
                    # one human player, one ai player
                    self.player1_gesture_index = self.player1.user_select_gesture_index
                    self.player2_gesture_index = self.player2.ai_rand_gesture_index
                else:
                    # two human players
                    self.player1_gesture_index = self.player1.user_select_gesture_index
                    self.player2_gesture_index = self.player2.user_select_gesture_index

                self.determine_round_winner(
                    self.player1_gesture_index, self.player2_gesture_index)
                print(
                    f"{self.player1.player_name} wins {self.player1_wins}\n{self.player2.player_name} wins {self.player2_wins}\n\n")
                continue

        self.display_finnal_winner()
        self.play_again_check()

    def determine_round_winner(self, player1_gesture_index, player2_gesture_index):
        # display the winner for the round
        # 1. check to see if its a tie
        # 2. check to see if player one is the winner
        # 3. else player 2 is the winner
        if player1_gesture_index == player2_gesture_index:
            print("Tie, try again")
        if player1_gesture_index == 0:
            if player2_gesture_index == 1 or player2_gesture_index == 4:
                self.player2_wins += 1
            else:
                self.player1_wins += 1
        elif player1_gesture_index == 1:
            if player2_gesture_index == 0 or player2_gesture_index == 4:
                self.player1_wins += 1
            else:
                self.player2_wins += 1
        elif player1_gesture_index == 2:
            if player2_gesture_index == 1 or player2_gesture_index == 3:
                self.player1_wins += 1
            else:
                self.player2_wins += 1
        elif player1_gesture_index == 3:
            if player2_gesture_index == 1 or player2_gesture_index == 4:
                self.player1_wins += 1
            else:
                self.player2_wins += 1
        else:
            if player2_gesture_index == 0 or player2_gesture_index == 2:
                self.player1_wins += 1
            else:
                self.player2_wins += 1
        self.round_num += 1

    def display_finnal_winner(self):
        if self.player1_wins == 2:
            print(f"{self.player1.player_name} wins best of three")
        else:
            print(f"{self.player2.player_name} wins best of three")

    def play_again_check(self):
        # aks whether user wants to play again

        while True:
            print("Do you want to play again?")
            self.user_play_again_decision = input("Enter y/n:").lower()
            if self.user_play_again_decision == "y":
                self.player1_wins = 0
                self.player2_wins = 0
                self.round_num = 1
                self.run_game()
            elif self.user_play_again_decision == "n":
                self.game_end_message()
                break
            else:
                print("Invalid selection, choose again\n")
                continue

    def game_end_message(self):
        print("Thank you for playing RPSLS game, see you next time.\n")
