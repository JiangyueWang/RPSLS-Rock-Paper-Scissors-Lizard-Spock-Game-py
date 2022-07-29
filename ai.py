from player import Player
from utility import rand_index


class Ai(Player):
    # Each Ai class has a name inherirated from Player class
    # Each Ai generates gestures randomly
    def __init__(self, name):
        super().__init__(name)
        self.ai_rand_gesture_index = 0

    def select_gesture(self):
        self.ai_rand_gesture_index = rand_index(len(self.gesture_list)-1)
        print(
            f"\n{self.player_name} chose {self.gesture_list[self.ai_rand_gesture_index]}\n")


# ai_one = Ai("AI one")
# ai_one.select_gesture()
