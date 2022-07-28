from player import Player
import random


class Ai(Player):

    def __init__(self, name):
        super().__init__(name)

    def rand_index(self, list_length):
        self.rand_list_index = random.randint(0, list_length)
        return self.rand_list_index

    def select_gesture(self):
        self.ai_rand_gesture_index = self.rand_index(len(self.gesture_list)-1)
        print(
            f"\n{self.player_name} chose {self.gesture_list[self.ai_rand_gesture_index]}")


# ai_one = Ai("AI one")
# ai_one.select_gesture()
