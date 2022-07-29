import random


def rand_index(list_length):
    # return a random index from a list
    rand_list_index = random.randint(0, list_length)
    return rand_list_index


def check_user_input(range):
    while True:
        user_input = input(f"Enter valid integer from 0 to {range}: ")
        try:
            user_input = int(user_input)
            break
        except ValueError:
            print("Invalid input, please enter a valid integer number again.")
            continue
        else:
            print(f"Check your input again, ensure it is from 0 to {range}")
            continue
    return user_input
