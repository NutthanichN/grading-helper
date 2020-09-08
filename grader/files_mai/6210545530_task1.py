def check_valid_input(s):
    """"
    Check the input (valid or not)

    Args:
        s (str): The parameter, which is the input from the player.

    Returns:
        bool: The return value. True for valid input, False for invalid.

    >>>check_valid_input("paperrr")
    False
    >>>check_valid_input("scissors")
    True
    >>>check_valid_input("mermaid")
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
    Convert string to integer

    Args:
        s (str): The parameter, which is the player's choice.

    Returns:
        int: The return value. Convert str to int by returning the right value for each parameter.

    >>>convert_to_num("paper")
    1
    >>>convert_to_num("boat")
    Error: should not reach this if input is a valid one
    >>>convert_to_num("scissors")
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
    Convert integer to string

    Args:
        n (int): The parameter, take the computer's choice in an int form.

    Returns:
        str: The return value. Convert int to str by returning the right value for each parameter.

    >>>convert_to_string(1)
    paper
    >>>convert_to_string(200)
    Error: should not reach this if input is a valid one
    >>>convert_to_string(5.4)
    Error: should not reach this if input is a valid one
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
    Use two integers (from player and computer) to calculate the result

    Args:
        player_choice_num (int): The first parameter. Get the player's choice in an int form.
        computer_choice_num (int): The second parameter. Get the computer's choice in an int form.

    Returns:
        str: The return value. Return the right result for each conditions.

    >>>game_decision(2, 1)
    Player wins!
    >>>game_decision(0, 0)
    Both ties!
    >>>game_decision(2, 0)
    Computer wins!
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
