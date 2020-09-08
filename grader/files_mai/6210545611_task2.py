def check_valid_input(s):
    """
    Validate input string if the input is match of raock scissors paper
    :param s: s is a input string choice
    :return: true or false

    """
    if s == "rock":
        return True
    elif s == "paper":
        return True
    elif s == "scissors":
        return True
    elif s == 'lizard':
        return True
    elif s == 'spock':
        return True
    else:
        return False


def convert_to_num(s):
    """
    convert string to number
    :param s: input string ex. rock paper scissors
    :return: number

    """
    if s == "rock":
        return 0
    elif s == "paper":
        return 2
    elif s == "scissors":
        return 4
    elif s == 'lizard':
        return 3
    elif s == 'spock':
        return 1
    else:
        print("Error: should not reach this if input is a valid one")


def convert_to_string(n):
    """
    convert number back to string
    :param n: number
    :return: string ex. rock paper scissors

    """
    if n == 0:
        return "rock"
    elif n == 2:
        return "paper"
    elif n == 4:
        return "scissors"
    elif n == 3:
        return 'lizard'
    elif n == 1:
        return 'spock'
    else:
        print("Error: should not reach this if input is a valid one")


def game_decision(player_choice_num, computer_choice_num):
    """
    This function is to check who will win between computer and human player

    :param player_choice_num: the number represent player choice string
    :param computer_choice_num: the number represent computer choice string
    :return: No

    >>> game_decision( 0, 1)
    Computer wins!
    >>> game_decision( 1, 0)
    Player wins!
    >>> game_decision( 1, 1)
    Both ties!

    """

    if player_choice_num == computer_choice_num:
        print("Both ties!")
    elif (computer_choice_num - player_choice_num)%5 == 3:
        print("Player wins!")
    elif (computer_choice_num - player_choice_num)%5 == 4:
        print("Player wins!")
    # elif (computer_choice_num - player_choice_num)%5 == 1 or 2:
    #     print("Computer wins!")
    else:
        print("Computer wins!")



# get an input from a player and validate
valid = False
while valid == False:
    player_choice = input("Enter your choice: ")
    valid = check_valid_input(player_choice)
    if valid == False:
        print("Invalid choice. Enter again.")

# random a response from a computer and print out player and computer choices
import random

computer_choice_num = random.randint(0, 4)
computer_choice = convert_to_string(computer_choice_num)
player_choice_num = convert_to_num(player_choice)
print("Players chooses ", player_choice)
print("Computer chooses ", computer_choice)


game_decision(player_choice_num, computer_choice_num)

