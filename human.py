from player import Player
from utility import check_user_input


class Human(Player):
    # Each Human player has a name inheritated from Player class
    # Each Human player selects gesture themselves via overwritted select_gesture
    def __init__(self, name):
        super().__init__(name)

    def select_gesture(self):
        for i in range(0, len(self.gesture_list), 1):
            print(f"Choose {i} for {self.gesture_list[i]}\n")
        self.player_chosen_gesture_index = check_user_input(
            len(self.gesture_list)-1)
        print(
            f"\n{self.player_name} chose {self.gesture_list[self.player_chosen_gesture_index]}")


# human_one = Human("player 1")

# human_one.select_gesture()
