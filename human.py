from player import Player


class Human(Player):
    # Each Human player has a name inheritated from Player class
    # Each Human player selects gesture themselves via overwritted select_gesture
    def __init__(self, name):
        super().__init__(name)

    def check_user_input(self, range):
        while True:
            self.user_select_gesture_index = input(
                f'Enter valid integer from 0 to {range}: ')
            try:
                self.user_select_gesture_index = int(
                    self.user_select_gesture_index)
                break
            except ValueError:
                print("Invalid input, please enter a valid integer number again.")
                continue
        return self.user_select_gesture_index

    def select_gesture(self):
        for i in range(0, len(self.gesture_list), 1):
            print(f"Choose {i} for {self.gesture_list[i]}\n")
        self.user_select_gesture_index = self.check_user_input(
            len(self.gesture_list)-1)
        print(
            f"\n{self.player_name} chose {self.gesture_list[self.user_select_gesture_index]}")


# human_one = Human("player 1")

# human_one.select_gesture()
