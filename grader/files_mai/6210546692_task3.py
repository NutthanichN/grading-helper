def check_valid_input(s):
    """
    Return the boolean of user's input

    >>> check_valid_input("rock")
    True
    >>> check_valid_input("spock")
    True
    >>> check_valid_input("zombie")
    True
    >>> check_valid_input("cat")
    False

    """

    if s == "gun":
        return True
    if s == "lizard":
        return True
    if s == "rock":
        return True
    if s == "paper":
        return True
    if s == "scissors":
        return True
    if s == "spock":
        return True
    if s == "zombie":
        return True
    else:
        return False

def convert_to_num(s):

    """
     Convert an input to the number

    >>> convert_to_num("rock")
    2
    >>> convert_to_num("zombie")
    6
    >>> convert_to_num("lizard")
    1
    """
    if s == "gun":
        return 0
    if s == "lizard":
        return 1
    if s == "rock":
        return 2
    if s == "paper":
        return 3
    if s == "scissors":
        return 4
    if s == "spock":
        return 5
    if s == "zombie":
        return 6
    else:
        print("Error: should not reach this if input is a valid one")

def convert_to_string(s):

    """
    Convert a num to string

    >>> convert_to_string(1)
    'lizard'
    >>> convert_to_string(2)
    'rock'
    >>> convert_to_string(5)
    'spock'
    """

    if s == 0:
        return "gun"
    if s == 1:
        return "lizard"
    if s == 2:
        return "rock"
    if s == 3:
        return "paper"
    if s == 4:
        return "scissors"
    if s == 5:
        return "spock"
    if s == 6:
        return "zombie"
    else:
        print("Error: should not reach this if input is a valid one")


#player choice

print("task3: rock/ paper/ scissors/ spock/ zombie / gun/ lizard")
valid = False
while valid == False:
    player_choice = input("Enter you choice: ")
    valid = check_valid_input(player_choice)
    if valid == False:
        print("Invalid choice. Enter again.")

#computer choice

import random
computer_choice_num = random.randint(0,6)
computer_choice = convert_to_string(computer_choice_num)
player_choice_num = convert_to_num(player_choice)
print("player chooses", player_choice)
print("computer chooses", computer_choice)

#Rules
"""
rock       |win against| scissors   zombie  lizard
paper      |win against| rock       spock   gun
scissors   |win against| paper      zombie  lizard
spock      |win against| rock    scissors   gun
zombie     |win against| paper      spock   lizard
gun        |win against| rock    scissors   zombie
lizard     |win against| paper      spock   gun
"""
def game_decision(player_choice_num,computer_choice_num):
    """
    1.if player_choice_num equal to computer_choice_num
    it will show "BOTH TIE !"
    2.if (player_choice_num+1)%7 equal to computer_choice_num or (player_choice_num+3)%7 equal to computer_choice_num or (player_choice_num+5)%7 equal to computer_choice_num
    it will show "  "
    3.if (player_choice_num+2)%7 == computer_choice_num or (player_choice_num+4)%7 == computer_choice_num or (player_choice_num+6)%7 == computer_choice_num
    it will show "  "

    >>> game_decision(5,6)
    COMPUTER WIN !
    >>> game_decision(4,4)
    BOTH TIE !
    >>> game_decision(0,2)
    PLAYER WIN !
    """
    if player_choice_num == computer_choice_num:
        print("BOTH TIE !")
    if (player_choice_num+1)%7 == computer_choice_num or (player_choice_num+3)%7 == computer_choice_num or (player_choice_num+5)%7 == computer_choice_num :
        print("COMPUTER WIN !")
    if (player_choice_num+2)%7 == computer_choice_num or (player_choice_num+4)%7 == computer_choice_num or (player_choice_num+6)%7 == computer_choice_num:
        print("PLAYER WIN !")

#Program
game_decision(player_choice_num,computer_choice_num)