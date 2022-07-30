import random
from tabnanny import check


def rand_index(list_length):
    # return a random index from a list
    rand_list_index = random.randint(0, list_length)
    return rand_list_index


def check_user_input(range):
    while True:
        user_input = input(f"Enter valid integer from 0 to 4: {range}")
        try:
            user_input = int(user_input)
            if user_input in range(0, 4):
                break
            else:
                print("Check your entry again")
                continue
        except ValueError:
            print("Invalid input, please enter a valid integer number again.")
            continue

    return user_input


check_user_input()
