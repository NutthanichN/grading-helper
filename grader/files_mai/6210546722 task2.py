def check_valid_input(s):

    """
    >>> check_valid_input("rock")
    True
    >>> check_valid_input("spock")
    True
    >>> check_valid_input("scissors")
    True
    >>> check_valid_input("paper")
    True
    >>> check_valid_input("lizard")
    True
    """

    if s == "rock":
        return True
    if s == "spock":
        return True
    if s == "paper":
        return True
    if s == "lizard":
        return True
    if s == "scissors":
        return True
    else:
        return False

#converting input to number
def convert_to_number(s):

    """
    >>> convert_to_number("rock")
    0
    >>> convert_to_number("spock")
    1
    >>> convert_to_number("paper")
    2
    >>> convert_to_number("lizard")
    3
    >>> convert_to_number("scissors")
    4
    """

    if s == "rock":
        return 0
    if s == "spock":
        return 1
    if s == "paper":
        return 2
    if s == "lizard":
        return 3
    if s == "scissors":
        return 4

#converting number to string
def convert_to_string(s):
    """
    >>> convert_to_string(0)
    'rock'
    >>> convert_to_string(1)
    'spock'
    >>> convert_to_string(2)
    'paper'
    >>> convert_to_string(3)
    'lizard'
    >>> convert_to_string(4)
    'scissors'
    """

    if s == 0:
        return "rock"
    if s == 1:
        return "spock"
    if s == 2:
        return "paper"
    if s == 3:
        return "lizard"
    if s == 4:
        return "scissors"

# #input from player / choice
# print("task2: rock/ paper/ scissors/ spock/ lizard ")
# valid = True
# while valid == False:
#     player_choice = input("Enter you choice: ")
#     valid = check_valid_input(player_choice)
#     if valid == False:
#         print("Invalid choice. Please Enter again.")

# #random output / computer choice
# import random
# computer_choice_number = random.randint(0, 4)
# computer_choice = convert_to_string(computer_choice_number)
# player_choice_number = convert_to_number(player_choice)

# print("player chooses", player_choice)
# print("computer chooses", computer_choice)

def game_decision(player_choice_number,computer_choice_number):

    """
    >>> game_decision(0, 1)
    COMPUTER WIN !!!
    >>> game_decision(1, 1)
    BOTH TIE !!!
    >>> game_decision(0, 3)
    PLAYER WIN !!!

    >>> game_decision(4, 2)
    PLAYER WIN !!!
    >>> game_decision(4, 0)
    COMPUTER WIN !!!
    >>> game_decision(4, 3)
    PLAYER WIN !!!
    >>> game_decision(4, 1)
    COMPUTER WIN !!!
    >>> game_decision(2, 0)
    PLAYER WIN !!!
    >>> game_decision(2, 3)
    COMPUTER WIN !!!
    >>> game_decision(2, 1)
    PLAYER WIN !!!
    >>> game_decision(0, 3)
    PLAYER WIN !!!
    >>> game_decision(0, 1)
    COMPUTER WIN !!!
    >>> game_decision(3, 1)
    PLAYER WIN !!!
    >>> game_decision(2, 4)
    COMPUTER WIN !!!
    >>> game_decision(0, 4)
    PLAYER WIN !!!
    >>> game_decision(3, 4)
    COMPUTER WIN !!!
    >>> game_decision(1, 4)
    PLAYER WIN !!!
    >>> game_decision(0, 2)
    COMPUTER WIN !!!
    >>> game_decision(3, 2)
    PLAYER WIN !!!
    >>> game_decision(1, 2)
    COMPUTER WIN !!!
    >>> game_decision(3, 0)
    COMPUTER WIN !!!
    >>> game_decision(1, 0)
    PLAYER WIN !!!
    >>> game_decision(1, 3)
    COMPUTER WIN !!!
    >>> game_decision(0, 0)
    BOTH TIE !!!
    >>> game_decision(4, 4)
    BOTH TIE !!!
    >>> game_decision(2, 2)
    BOTH TIE !!!
    >>> game_decision(3, 3)
    BOTH TIE !!!
    >>> game_decision(1, 1)
    BOTH TIE !!!
    """
    # game output system
    if player_choice_number == computer_choice_number:
        print("BOTH TIE !!!")
    if (player_choice_number + 1 ) % 5 == computer_choice_number or (player_choice_number + 2) % 5 == computer_choice_number:
        print("COMPUTER WIN !!!")
    if (player_choice_number + 3 ) % 5 == computer_choice_number or (player_choice_number + 4) % 5 == computer_choice_number:
        print("PLAYER WIN !!!")

# game_decision(player_choice_number,computer_choice_number)

import doctest
doctest.testmod()
