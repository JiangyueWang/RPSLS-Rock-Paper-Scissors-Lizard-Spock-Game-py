from player import Player


class human(Player):

    def __init__(self, name):
        super().__init__(name)

    def check_user_input(self, range):
        while True:
            self.user_input = input(f'enter valid integer from 0 to {range}: ')
            try:
                self.user_input = int(self.user_input)
            except ValueError:
                print("invalid input, please enter a valid integer number again.")
            return self.user_input

    def select_gesture(self):
        for i in range(0, len(self.gesture_list), 1):
            print(f"Choose {i} for {self.gesture_list[i]}\n")
        self.user_select_gesture_index = self.check_user_input(
            len(self.gesture_list)-1)
        print(
            f"\n{self.player_name} chose {self.gesture_list[self.user_select_gesture_index]}")

        return self.user_select_gesture_index


# human_one = human("player 1")

# human_one.select_gesture()
