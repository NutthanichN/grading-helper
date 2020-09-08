def check_valid_input(s):

    """
    Return the boolean of user's input

    >>> check_valid_input("rock")
    True
    >>> check_valid_input("spock")
    True
    >>> check_valid_input("scissors")
    True
    >>> check_valid_input("spock")
    True
    >>> check_valid_input("lizard")
    True
    >>> check_valid_input("cat")
    False

    """

    if s == "rock":
        return True
    if s == "paper":
        return True
    if s == "scissors":
        return True
    if s == "spock":
        return True
    if s == "lizard":
        return True
    else:
        return False

def convert_to_num(s):

    """
    Convert an input to the number

    >>> convert_to_num("rock")
    0
    >>> convert_to_num("paper")
    1
    >>> convert_to_num("scissors")
    2
    >>> convert_to_num("spock")
    3
    >>> convert_to_num("lizard")
    4

    """

    if s == "rock":
        return 0
    if s == "paper":
        return 1
    if s == "scissors":
        return 2
    if s == "spock":
        return 3
    if s == "lizard":
        return 4

def convert_to_string(s):

    """
    Convert a num to string

    >>> convert_to_string(1)
    'paper'
    >>> convert_to_string(4)
    'lizard'
    >>> convert_to_string(0)
    'rock'
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
        return "lizard"

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
    1.if player_choice_num equal to computer_choice_num
    it will show "BOTH TIE!!"
    2.if (player_choice_num+1)%5 equal to computer_choice_num or (player_choice_num+3)%5 equal to computer_choice_num
    it will show "COMPUTER WIN !"
    3.if (player_choice_num+2)%5 equal to computer_choice_num or (player_choice_num+4)%5 equal to computer_choice_num
    it will show "PLAYER WIN !"

    >>> game_decision(0,1)
    COMPUTER WIN !
    >>> game_decision(1,1)
    BOTH TIE !
    >>> game_decision(0,3)
    COMPUTER WIN !
    """

    if player_choice_num == computer_choice_num:
        print("BOTH TIE !")
    elif (player_choice_num+1)%5 == computer_choice_num or (player_choice_num+3)%5 == computer_choice_num:
        print("COMPUTER WIN !")
    elif (player_choice_num+2)%5 == computer_choice_num or (player_choice_num+4)%5 == computer_choice_num:
        print("PLAYER WIN !")

game_decision(player_choice_num,computer_choice_num)