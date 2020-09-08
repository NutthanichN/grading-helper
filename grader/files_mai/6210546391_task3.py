def check_valid_input(s):

    """
     Return the boolean of input

    >>> check_valid_input("rock")
    True
    >>> check_valid_input("paper")
    True
    >>> check_valid_input("rubber")
    False
    >>> check_valid_input("bread")
    False
    """

    if s == "rock":
        return True
    if s == "lizard":
        return True
    if s == "gun":
        return True
    if s == "zombie":
        return True
    if s == "spock":
        return True
    if s == "scissors":
        return True
    if s == "paper":
        return True
    else:
        return False

def convert_to_num(s):

    """
    Change input(string) to number

    >>> convert_to_num("rock")
    0
    >>> convert_to_num("lizard")
    1
    >>> convert_to_num("paper")
    6
    >>> convert_to_num("spock")
    4
    """
    if s == "rock":
        return 0
    if s == "lizard":
        return 1
    if s == "gun":
        return 2
    if s == "zombie":
        return 3
    if s == "spock":
        return 4
    if s == "scissors":
        return 5
    if s == "paper":
        return 6
    else:
        print("Error: should not reach this if input is a valid one")

def convert_to_string(s):
    """
    Change input(number) to string

    >>> convert_to_string(6)
    'paper'
    >>> convert_to_string(0)
    'rock'
    >>> convert_to_string(1)
    'lizard'
    >>> convert_to_string(3)
    'zombie'
    """

    if s == 0:
        return "rock"
    if s == 1:
        return "lizard"
    if s == 2:
        return "gun"
    if s == 3:
        return "zombie"
    if s == 4:
        return "spock"
    if s == 5:
        return "scissors"
    if s == 6:
        return "paper"
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


def game_decision(player_choice_num,computer_choice_num):
    """
    Compare the input(player_choice_num,computer_choice_num) to find who will win

    >>> game_decision(2,2)
    Both tie!
    >>> game_decision(1,0)
    Computer win!
    >>> game_decision(6,0)
    Player win!
    >>> game_decision(4,5)
    Player win!
    """
    if player_choice_num == computer_choice_num:
        print("Both tie!")
    if (player_choice_num+2)%7 == computer_choice_num or (player_choice_num+4)%7 == computer_choice_num or (player_choice_num+6)%7 == computer_choice_num :
        print("Computer win!")
    if (player_choice_num+1)%7 == computer_choice_num or (player_choice_num+3)%7 == computer_choice_num or (player_choice_num+5)%7 == computer_choice_num:
        print("Player win!")

#Program
game_decision(player_choice_num,computer_choice_num)