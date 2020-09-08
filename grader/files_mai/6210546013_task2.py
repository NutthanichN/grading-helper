import random

# 2.Rock-Paper-Scissors-Lizard-Spock


def check_valid_input(input):
    """Return True in string that have in game choice, an game choice is (Rock, Paper, Scissors, Lizard, Spock)
    >>> check_valid_input("Rock")
    True
    >>> check_valid_input("Spock")
    True
    >>> check_valid_input("Paper")
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
    elif input == "Spock":
        return True
    elif input == "Paper":
        return True
    elif input == "Lizard":
        return True
    elif input == "Scissors":
        return True
    else:
        return False


def convert_to_num(String):
    """Return the intergers 0, 1, 2, 3, 4 to assign instead of string, string have only in game choice
    >>> convert_to_num("Rock")
    0
    >>> convert_to_num("Spock")
    1
    >>> convert_to_num("Paper")
    2
    >>> convert_to_num("Lizard")
    3
    >>> convert_to_num("Scissors")
    4
    >>> convert_to_num("skynet")
    Error: Should not reach this if input is a valid one
    """
    if String == "Rock":
        return 0
    elif String == "Spock":
        return 1
    elif String == "Paper":
        return 2
    elif String == "Lizard":
        return 3
    elif String == "Scissors":
        return 4
    else:
        print("Error: Should not reach this if input is a valid one")


def convert_to_string(num):
    """Return the string that have in game choice, from number that use to assign
    >>> convert_to_string(0)
    Rock
    >>> convert_to_string(1)
    Spock
    >>> convert_to_string(2)
    Paper
    >>> convert_to_string(3)
    Lizard
    >>> convert_to_string(4)
    Scissors
    >>> convert_to_string(5)
    Error: Should not reach this if input is a valid one
    """
    if num == 0:
        return "Rock"
    elif num == 1:
        return "Spock"
    elif num == 2:
        return "Paper"
    elif num == 3:
        return "Lizard"
    elif num == 4:
        return "Scissors"
    else:
        print("Error: Should not reach this if input is a valid one")


def game_decision(player_choice_num, computer_choice_num):
    """return game that have win lose and both ties, for use with number that select by user and random by computer
    >>> game_decision(0, 0)
    Both Ties!!!
    >>> game_decision(0, 1)
    Oh no!, This is Skynet?!
    >>> game_decision(0, 2)
    Oh no!, This is Skynet?!
    >>> game_decision(0, 3)
    Yeah!, I found John Conner.
    >>> game_decision(0, 4)
    Yeah!, I found John Conner.
    >>> game_decision(1, 0)
    Yeah!, I found John Conner.
    >>> game_decision(1, 1)
    Both Ties!!!
    >>> game_decision(1, 2)
    Oh no!, This is Skynet?!
    >>> game_decision(1, 3)
    Oh no!, This is Skynet?!
    >>> game_decision(1, 4)
    Yeah!, I found John Conner.
    >>> game_decision(2, 0)
    Yeah!, I found John Conner.
    >>> game_decision(2, 1)
    Yeah!, I found John Conner.
    >>> game_decision(2, 2)
    Both Ties!!!
    >>> game_decision(2, 3)
    Oh no!, This is Skynet?!
    >>> game_decision(2, 4)
    Oh no!, This is Skynet?!
    >>> game_decision(3, 0)
    Oh no!, This is Skynet?!
    >>> game_decision(3, 1)
    Yeah!, I found John Conner.
    >>> game_decision(3, 2)
    Yeah!, I found John Conner.
    >>> game_decision(3, 3)
    Both Ties!!!
    >>> game_decision(3, 4)
    Oh no!, This is Skynet?!
    >>> game_decision(4, 0)
    Oh no!, This is Skynet?!
    >>> game_decision(4, 1)
    Oh no!, This is Skynet?!
    >>> game_decision(4, 2)
    Yeah!, I found John Conner.
    >>> game_decision(4, 3)
    Yeah!, I found John Conner.
    >>> game_decision(4, 4)
    Both Ties!!!
    """
    if player_choice_num == computer_choice_num:
        print("Both Ties!!!")
    elif ((player_choice_num + 2) % 5) >= computer_choice_num:
        print("Oh no!, This is Skynet?!")
    else:
        print("Yeah!, I found John Conner.")


def main() -> None:
    valid = False
    while valid == False:
        player_choice = input(
            "Enter your choice(Rock, Paper, Scissors, Lizard, Spock): ")
        valid = check_valid_input(player_choice)
        if valid == False:
            print("Invalid choice. Enter again.")

    """ main program """
    computer_choice_num = random.randint(0, 4)
    computer_choice = convert_to_string(computer_choice_num)
    player_choice_num = convert_to_num(player_choice)
    print("Skynet take control of your computer")
    print(f"Player choose {player_choice}")
    print(f"Skynet choose {computer_choice}")

    game_decision(player_choice_num, computer_choice_num)


if __name__ == '__main__':
    main()
