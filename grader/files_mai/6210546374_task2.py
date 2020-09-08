
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

def convert_to_num(s):

    """
    *This function convert the string that take from users to the number*

    >>> convert_to_num("rock")
    0
    >>> convert_to_num("paper")
    2
    >>> convert_to_num("lizard")
    3
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

def convert_to_string(s):

    """
    *This function take the number that system random from the range [0,4] to string*

    >>> convert_to_string(1)
    'spock'
    >>> convert_to_string(4)
    'scrissors'
    >>> convert_to_string(0)
    'rock'
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

#player choice

""" *Users Input Here!* """

print("task2: rock/ paper/ scissors/ spock/ lizard ")
valid = False
while valid == False:
    player_choice = input("Enter you choice: ")
    valid = check_valid_input(player_choice)
    if valid == False:
        print("Invalid choice. Enter again.")

#computer choice
""" *Computer random number from range [0,4]* """
import random
computer_choice_num = random.randint(0,4)
computer_choice = convert_to_string(computer_choice_num)
player_choice_num = convert_to_num(player_choice)

print("player chooses", player_choice)
print("computer chooses", computer_choice)

def game_decision(player_choice_num,computer_choice_num):

    """
    *This is the game part or rules that consider who will win the game*
    >>> game_decision(0,1)
    COMPUTER WIN !
    >>> game_decision(1,1)
    BOTH TIE !
    >>> game_decision(0,3)
    PLAYER WIN !
    """
    
    if player_choice_num == computer_choice_num:
        print("BOTH TIE !")
    if (player_choice_num+1)%5 == computer_choice_num or (player_choice_num+2)%5 == computer_choice_num:
        print("COMPUTER WIN !")
    if (player_choice_num+3)%5 == computer_choice_num or (player_choice_num+4)%5 == computer_choice_num:
        print("PLAYER WIN !")

game_decision(player_choice_num,computer_choice_num)