import random

# 3.Rock-Paper-Scissors-Lizard-Spock-Gun-Zombie


def check_valid_input(input):
    """Return True in string that have in game choice, an game choice is (Rock, Paper, Scissors, Lizard, Spock, Gun, Zombie)
    >>> check_valid_input("Rock")
    True
    >>> check_valid_input("Gun")
    True
    >>> check_valid_input("Spock")
    True
    >>> check_valid_input("Paper")
    True
    >>> check_valid_input("Zombie")
    True
    >>> check_valid_input("Lizard")
    True
    >>> check_valid_input("Scissors")
    True
    >>> check_valid_input("yay")
    False
    """
    if input == "Rock":
        return True
    elif input == "Gun":
        return True
    elif input == "Spock":
        return True
    elif input == "Paper":
        return True
    elif input == "Zombie":
        return True
    elif input == "Lizard":
        return True
    elif input == "Scissors":
        return True
    else:
        return False


def convert_to_num(String):
    """Return the intergers 0, 1, 2, 3, 4, 5, 6 to assign instead of string, string have only in game choice
    >>> convert_to_num("Rock")
    0
    >>> convert_to_num("Gun")
    1
    >>> convert_to_num("Spock")
    2
    >>> convert_to_num("Paper")
    3
    >>> convert_to_num("Lizard")
    4
    >>> convert_to_num("Zombie")
    5
    >>> convert_to_num("Scissors")
    6
    >>> convert_to_num("skynet")
    Error: Should not reach this if input is a valid one
    """
    if String == "Rock":
        return 0
    elif String == "Gun":
        return 1
    elif String == "Spock":
        return 2
    elif String == "Paper":
        return 3
    elif String == "Lizard":
        return 4
    elif String == "Zombie":
        return 5
    elif String == "Scissors":
        return 6
    else:
        print("Error: Should not reach this if input is a valid one")


def convert_to_string(num):
    """Return the string that have in game choice, from number that use to assign
    >>> convert_to_string(0)
    Rock
    >>> convert_to_string(1)
    Gun
    >>> convert_to_string(2)
    Spock
    >>> convert_to_string(3)
    Paper
    >>> convert_to_string(4)
    Lizard
    >>> convert_to_string(5)
    Zombie
    >>> convert_to_string(6)
    Scissors
    >>> convert_to_string(7)
    Error: Should not reach this if input is a valid one
    """
    if num == 0:
        return "Rock"
    elif num == 1:
        return "Gun"
    elif num == 2:
        return "Spock"
    elif num == 3:
        return "Paper"
    elif num == 4:
        return "Lizard"
    elif num == 5:
        return "Zombie"
    elif num == 6:
        return "Scissors"
    else:
        print("Error: Should not reach this if input is a valid one")


def game_decision(player_choice_num, computer_choice_num):
    """return game that have win lose and both ties, for use with number that select by user and random by computer
    >>> games_desion(0, 0)
    Both Ties!!!
    >>> games_desion(0, 1)
    Oh no!, This is Skynet?!
    >>> games_desion(0, 2)
    Oh no!, This is Skynet?!
    >>> games_desion(0, 3)
    Oh no!, This is Skynet?!
    >>> games_desion(0, 4)
    Yeah!, I found John Conner.
    >>> games_desion(0, 5)
    Yeah!, I found John Conner.
    >>> games_desion(0, 6)
    Yeah!, I found John Conner.
    >>> games_desion(1, 1)
    Both Ties!!!
    >>> games_desion(2, 2)
    Both Ties!!!
    >>> games_desion(3, 3)
    Both Ties!!!
    >>> games_desion(4, 4)
    Both Ties!!!
    >>> games_desion(5, 5)
    Both Ties!!!
    >>> games_desion(6, 6)
    Both Ties!!!
    """
    if player_choice_num == computer_choice_num:
        print("Both Ties!!!")
    elif ((player_choice_num + 3) % 7) >= computer_choice_num:
        print("Oh no!, This is skynet?!!")
    else:
        print("Yeah!, I found John Conner.")


def main() -> None:
    valid = False
    while valid == False:
        player_choice = input(
            "Enter your choice(Rock, Gun, Spock, Paper, Lizard, Zombie, Scissors): ")
        valid = check_valid_input(player_choice)
        if valid == False:
            print("Invalid choice. Enter again.")

    computer_choice_num = random.randint(0, 6)
    computer_choice = convert_to_string(computer_choice_num)
    player_choice_num = convert_to_num(player_choice)
    print("Skynet take control of your computer")
    print(f"Player choose {player_choice}")
    print(f"Skynet choose {computer_choice}")

    game_decision(player_choice_num, computer_choice_num)


if __name__ == '__main__':
    main()
