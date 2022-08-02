class Player:
    # Each player has a name
    # Each player can select gesture,
    # human players ask to choose the gesture
    # ai player generate gesture randomly

    def __init__(self, name):
        self.player_name = name
        self.player_chosen_gesture_index = 0
        # 0 Rock
        # 1 Paper
        # 2 Scissors
        # 3 Lizard
        # 4 Spock
        self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

    def select_gesture(self):
        pass
