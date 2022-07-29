import random


class Utility:
    def __init__(self):
        pass

    def rand_index(self, list_length):
        # return a random index from a list
        self.rand_list_index = random.randint(0, list_length)
        return self.rand_list_index
