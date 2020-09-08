def check_valid_input(s):

    """
    Return the boolean of input

    >>> check_valid_input("paper")
    True
    >>> check_valid_input("lizard")
    True
    >>> check_valid_input("rubber")
    False
    >>> check_valid_input("gun")
    False
    """

    if s == "rock":
        return True
    if s == "lizard":
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
    >>> convert_to_num("scissors")
    3
    >>> convert_to_num("paper")
    4
    """

    if s == "rock":
        return 0
    if s == "lizard":
        return 1
    if s == "spock":
        return 2
    if s == "scissors":
        return 3
    if s == "paper":
        return 4

def convert_to_string(s):

    """
    Change input(number) to string

    >>> convert_to_string(4)
    'paper'
    >>> convert_to_string(3)
    'scissors'
    >>> convert_to_string(1)
    'lizard'
    >>> convert_to_string(0)
    'rock'
    """

    if s == 0:
        return "rock"
    if s == 1:
        return "lizard"
    if s == 2:
        return "spock"
    if s == 3:
        return "scissors"
    if s == 4:
        return "paper"

#player choice
print("task2: rock/ paper/ scissors/ spock/ lizard ")
valid = False
while valid == False:
    player_choice = input("Enter you choice: ")
    valid = check_valid_input(player_choice)
    if valid == False:
        print("Invalid choice. Enter again.")

#computer choice
import random
computer_choice_num = random.randint(0,4)
computer_choice = convert_to_string(computer_choice_num)
player_choice_num = convert_to_num(player_choice)

print("player chooses", player_choice)
print("computer chooses", computer_choice)

def game_decision(player_choice_num,computer_choice_num):

    """
    Compare the input(player_choice_num,computer_choice_num) to find who will win

    >>> game_decision(1,1)
    Both tie!
    >>> game_decision(1,0)
    Computer win!
    >>> game_decision(0,3)
    Player win!
    >>> game_decision(4,0)
    Player win!
    """

    if player_choice_num == computer_choice_num:
        print("Both tie!")
    if (player_choice_num+2)%5 == computer_choice_num or (player_choice_num+4)%5 == computer_choice_num:
        print("Computer win!")
    if (player_choice_num+1)%5 == computer_choice_num or (player_choice_num+3)%5 == computer_choice_num:
        print("Player win!")

game_decision(player_choice_num,computer_choice_num)