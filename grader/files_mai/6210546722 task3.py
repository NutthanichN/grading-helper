

#check if input is valid
def check_valid_input(s):
    """
    >>> check_valid_input("rock")
    True
    >>> check_valid_input("spock")
    True
    >>> check_valid_input("Human")
    False
    """

    if s == "rock":
        return True
    if s == "paper":
        return True
    if s == "scrissors":
        return True
    if s == "spock":
        return True
    if s == "zombie":
        return True
    if s == "gun":
        return True
    if s == "lizard":
        return True
    else:
        return False
#converting input to number
def convert_to_number(s):

    """
    >>> convert_to_number("rock")
    0
    >>> convert_to_number("zombie")
    4
    >>> convert_to_number("lizard")
    6
    """
    if s == "rock":
        return 0
    if s == "paper":
        return 1
    if s == "scissors":
        return 2
    if s == "spock":
        return 3
    if s == "zombie":
        return 4
    if s == "gun":
        return 5
    if s == "lizard":
        return 6
    else:
        print("Error: should not reach this if input is a valid one")

#converting number to string
def convert_to_string(s):
    """
    >>> convert_to_string(1)
    'paper'
    >>> convert_to_string(2)
    'scissors'
    >>> convert_to_string(5)
    'gun'
    """

    if s == 0:
        return "rock"
    if s == 1:
        return "paper"
    if s == 2:
        return "scissors"
    if s == 3:
        return "spock"
    if s == 4:
        return "zombie"
    if s == 5:
        return "gun"
    if s == 6:
        return "lizard"
    else:
        print("Error: should not reach this if input is a valid one")


# #input from player / choice

# print("task3 : rock/ paper/ scissors/ spock/ zombie / gun/ lizard")
# valid = False
# while valid == False:
#     player_choice = input("Enter you choice: ")
#     valid = check_valid_input(player_choice)
#     if valid == False:
#         print("Invalid choice. Enter again.")

# #random output / computer choice

# import random
# computer_choice_number = random.randint(0, 6)
# computer_choice = convert_to_string(computer_choice_number)
# player_choice_number = convert_to_number(player_choice)
# print("player chooses", player_choice)
# print("computer chooses", computer_choice)

#rock, paper, scissors, spock, lizard, zombie, gun. rules
"""
lizard     |win against| paper      spock   gun
rock       |win against| scissors   zombie  lizard
paper      |win against| rock       spock   gun
zombie     |win against| paper      spock   lizard
gun        |win against| rock    scissors   zombie
scissors   |win against| paper      zombie  lizard
spock      |win against| rock    scissors   gun
"""
def game_decision(player_choice_number,computer_choice_number):
    """
    >>> game_decision(5, 6)
    COMPUTER WIN !!!
    >>> game_decision(4, 4)
    BOTH TIE !!!
    >>> game_decision(0, 2)
    PLAYER WIN !!!

    >>> game_decision(2, 1)
    PLAYER WIN !!!
    >>> game_decision(2, 0)
    COMPUTER WIN !!!
    >>> game_decision(2, 6)
    PLAYER WIN !!!
    >>> game_decision(2, 5)
    COMPUTER WIN !!!
    >>> game_decision(2, 4)
    PLAYER WIN !!!
    >>> game_decision(2, 3)
    COMPUTER WIN !!!
    >>> game_decision(1, 0)
    PLAYER WIN !!!
    >>> game_decision(1, 6)
    COMPUTER WIN !!!
    >>> game_decision(1, 5)
    PLAYER WIN !!!
    >>> game_decision(1, 4)
    COMPUTER WIN !!!
    >>> game_decision(1, 3)
    PLAYER WIN !!!
    >>> game_decision(0, 6)
    PLAYER WIN !!!
    >>> game_decision(0, 5)
    COMPUTER WIN !!!
    >>> game_decision(0, 4)
    PLAYER WIN !!!
    >>> game_decision(0, 3)
    COMPUTER WIN !!!
    >>> game_decision(6, 5)
    PLAYER WIN !!!
    >>> game_decision(6, 4)
    COMPUTER WIN !!!
    >>> game_decision(6, 3)
    PLAYER WIN !!!
    >>> game_decision(5, 4)
    PLAYER WIN !!!
    >>> game_decision(5, 3)
    COMPUTER WIN !!!
    >>> game_decision(4, 3)
    PLAYER WIN !!!
    >>> game_decision(1, 2)
    COMPUTER WIN !!!
    >>> game_decision(0, 2)
    PLAYER WIN !!!
    >>> game_decision(6, 2)
    COMPUTER WIN !!!
    >>> game_decision(5, 2)
    PLAYER WIN !!!
    >>> game_decision(4, 2)
    COMPUTER WIN !!!
    >>> game_decision(3, 2)
    PLAYER WIN !!!
    >>> game_decision(0, 1)
    COMPUTER WIN !!!
    >>> game_decision(6, 1)
    PLAYER WIN !!!
    >>> game_decision(5, 1)
    COMPUTER WIN !!!
    >>> game_decision(4, 1)
    PLAYER WIN !!!
    >>> game_decision(3, 1)
    COMPUTER WIN !!!
    >>> game_decision(6, 0)
    COMPUTER WIN !!!
    >>> game_decision(5, 0)
    PLAYER WIN !!!
    >>> game_decision(4, 0)
    COMPUTER WIN !!!
    >>> game_decision(3, 0)
    PLAYER WIN !!!
    >>> game_decision(5, 6)
    COMPUTER WIN !!!
    >>> game_decision(4, 6)
    PLAYER WIN !!!
    >>> game_decision(3, 6)
    COMPUTER WIN !!!
    >>> game_decision(4, 5)
    COMPUTER WIN !!!
    >>> game_decision(3, 5)
    PLAYER WIN !!!
    >>> game_decision(3, 4)
    COMPUTER WIN !!!
    >>> game_decision(0, 0)
    BOTH TIE !!!
    >>> game_decision(2, 2)
    BOTH TIE !!!
    >>> game_decision(1, 1)
    BOTH TIE !!!
    >>> game_decision(6, 6)
    BOTH TIE !!!
    >>> game_decision(5, 5)
    BOTH TIE !!!
    >>> game_decision(4, 4)
    BOTH TIE !!!
    >>> game_decision(3, 3)
    BOTH TIE !!!
    """
    if player_choice_number == computer_choice_number:
        print("BOTH TIE !!!")
    if (player_choice_number  + 1 ) % 7 == computer_choice_number or (player_choice_number + 3 ) % 7 == computer_choice_number or (player_choice_number + 5 ) % 7 == computer_choice_number :
        print("COMPUTER WIN !!!")
    if (player_choice_number + 2 ) % 7 == computer_choice_number or (player_choice_number + 4 ) % 7 == computer_choice_number or (player_choice_number + 6 ) % 7 == computer_choice_number:
        print("PLAYER WIN !!!")

# #Program
# game_decision(player_choice_number,computer_choice_number)
import doctest
doctest.testmod()
