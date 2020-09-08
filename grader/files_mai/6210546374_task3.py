def check_valid_input(s):
    """
    *Check if the user's input is valid*
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

def convert_to_num(s):

    """
    *This function convert the string that take from users to the number*

    >>> convert_to_num("rock")
    0
    >>> convert_to_num("zombie")
    4
    >>> convert_to_num("lizard")
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

def convert_to_string(s):
    """
    *This function take the number that system random from the range [0,6] to string*

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


#player choice
""" *Users Input Here!* """
print("task3: rock/ paper/ scissors/ spock/ zombie / gun/ lizard")
valid = False
while valid == False:
    player_choice = input("Enter you choice: ")
    valid = check_valid_input(player_choice)
    if valid == False:
        print("Invalid choice. Enter again.")

#computer choice
""" *Computer random number from range [0,6]* """
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
    *This is the game part or rules that consider who will win the game*
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
