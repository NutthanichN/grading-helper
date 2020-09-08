import random

# 1.Rock-Paper-Scissors


def check_valid_input(input):
    """Return True in string that have in game choice, an game choice is (Rock, Paper, Scissors)
    >>> check_valid_input("Rock")
    True
    >>> check_valid_input("Paper")
    True
    >>> check_valid_input("Scissors")
    True
    >>> check_valid_input("yay")
    False
    """
    if input == "Rock":
        return True
    elif input == "Paper":
        return True
    elif input == "Scissors":
        return True
    else:
        return False


def convert_to_num(String):
    """Return the intergers 0, 1, 2 to assign instead of string, string have only in game choice
    >>> convert_to_num("Rock")
    0
    >>> convert_to_num("Paper")
    1
    >>> convert_to_num("Scissors")
    2
    >>> convert_to_num("skynet")
    Error: Should not reach this if input is a valid one
    """
    if String == "Rock":
        return 0
    elif String == "Paper":
        return 1
    elif String == "Scissors":
        return 2
    else:
        print("Error: Should not reach this if input is a valid one")


def convert_to_string(num):
    """Return the string that have in game choice, from number that use to assign
    >>> convert_to_string(0)
    Rock
    >>> convert_to_string(1)
    Paper
    >>> convert_to_string(2)
    Scissors
    >>> convert_to_string(3)
    Error: Should not reach this if input is a valid one
    """
    if num == 0:
        return "Rock"
    elif num == 1:
        return "Paper"
    elif num == 2:
        return "Scissors"
    else:
        print("Error: Should not reach this if input is a valid one")


def game_decision(player_choice_num, computer_choice_num):
    """return game that have win lose and both ties, for use with number that select by user and random by computer
    >>> game_decision(0, 0)
    Both Ties!!!
    >>> games_decision(0, 1)
    Oh no!, Skynet is take over the World
    """
    if player_choice_num == computer_choice_num:
        print("Both Ties!!!")
    elif ((player_choice_num + 1) % 3) == computer_choice_num:
        print("Oh no!, Skynet is take over the World")
    else:
        print("Yeah!, I found John Conner.")


def main() -> None:
    """ main program """
    valid = False
    while valid == False:
        player_choice = input("Enter your choice(Rock, Paper, Scissors): ")
        valid = check_valid_input(player_choice)
        if valid == False:
            print("Invalid choice. Enter again.")

    computer_choice_num = random.randint(0, 2)
    computer_choice = convert_to_string(computer_choice_num)
    player_choice_num = convert_to_num(player_choice)
    print("Skynet take control of your computer")
    print(f"Player chooses {player_choice}")
    print(f"Skynet chooses {computer_choice}")

    game_decision(player_choice_num, computer_choice_num)

if __name__ == '__main__':
    main()
