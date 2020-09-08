def check_valid_input(s):

    """
    Return the boolean of user's input

    >>> check_valid_input("rock")
    True
    >>> check_valid_input("paper")
    True
    >>> check_valid_input("scissors")
    True
    >>> check_valid_input("rat")
    False
    """

    if s == "rock":
        return True
    elif s == "paper":
        return True
    elif s == "scissors":
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

    """

    if s == "rock":
        return 0
    elif s == "paper":
        return 1
    elif s == "scissors":
        return 2
    else:
        print("Error: should not reach this if input is a valid one")


def convert_to_string(n):
    """
    Convert a num to string

    >>> convert_to_string("rock")
    0
    >>> convert_to_string("paper")
    1
    >>> convert_to_string("scissors")
    2

    """
    if n == 0:
        return "rock"
    elif n == 1:
        return "paper"
    elif n == 2:
        return "scissors"
    else:
        print("Error: should not reach this if input is a valid one")


def game_decision(player_choice_num, computer_choice_num):
    """

    Compare the values of player_choice_num with computer_choice_num
    First if player_choice_num equal to computer_choice_num.The output will show "Both ties!",
    second if the values of (player_choice_num + 1) % 3 equal to computer_choice_num.It will show
    "Computer win".Other than if out of first two cases, it will show "Player win!"

    """
    if player_choice_num == computer_choice_num:
        print("Both ties!")
    elif ((player_choice_num + 1) % 3) == computer_choice_num:
        print("Computer wins!")
    else:
        print("Player wins!")


# get an input from a player and validate
valid = False
while valid == False:
    player_choice = input("Enter your choice: ")
    valid = check_valid_input(player_choice)
    if valid == False:
        print("Invalid choice. Enter again.")

# random a response from a computer and print out player and computer choices
import random

computer_choice_num = random.randint(0, 2)
computer_choice = convert_to_string(computer_choice_num)
player_choice_num = convert_to_num(player_choice)
print("Players chooses ", player_choice)
print("Computer chooses ", computer_choice)

# apply the rules of rock-paper-scissors
# rock-0 ; paper-1 ; scissors-2

# do this
game_decision(player_choice_num, computer_choice_num)

# instead of this ugly if-elif-else nested block
"""
if player_choice_num == 0:
    if computer_choice_num == 0:
        print("Both ties!")
    elif computer_choice_num == 1:
        print("Computer wins!")
    else:
        print("Player wins!")
elif player_choice_num == 1:
    if computer_choice_num == 1:
        print("Both ties!")
    elif computer_choice_num == 2:
        print("Computer wins!")
    else:
        print("Player wins!")
else:
    if computer_choice_num == 2:
        print("Both ties!")
    elif computer_choice_num == 0:
        print("Computer wins!")
    else:
        print("Player wins!")
"""


