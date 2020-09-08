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
        return 1
    elif s == "scissors":
        return 2
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
    elif n == 1:
        return "paper"
    elif n == 2:
        return "scissors"
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

