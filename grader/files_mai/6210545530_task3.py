import random


def check_valid_input(s):
    """
    Check the input (valid or not)

    Args:
        s (str): The parameter, which is the input from the player.

    Returns:
        bool: The return value. True for valid input, False for invalid.

    >>>check_valid_input("GUN")
    False
    >>>check_valid_input("paper")
    True
    >>>check_valid_input("zombee")
    False
    """
    if s == "gun":
        return True
    elif s == "zombie":
        return True
    elif s == "spock":
        return True
    elif s == "scissors":
        return True
    elif s == "paper":
        return True
    elif s == "lizard":
        return True
    elif s == "rock":
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

    >>>convert_to_num("spock")
    2
    >>>convert_to_num("Scissors")
    Error: should not reach this if input is a valid one
    >>>convert_to_num("octopus")
    Error: should not reach this if input is a valid one
    """
    if s == "gun":
        return 0
    elif s == "zombie":
        return 1
    elif s == "spock":
        return 2
    elif s == "scissors":
        return 3
    elif s == "paper":
        return 4
    elif s == "lizard":
        return 5
    elif s == "rock":
        return 6
    else:
        print("Error: should not reach this if input is a valid one")


def convert_to_string(n):
    """
    Convert integer to string

    Args:
        n (int): The parameter, take the computer's choice in an int form.

    Returns:
        str: The return value. Convert int to str by returning the right value for each parameter.

    >>>convert_to_string(3)
    spock
    >>>convert_to_string(60)
    Error: should not reach this if input is a valid one
    >>>convert_to_string(0.5)
    Error: should not reach this if input is a valid one
    """
    if n == 0:
        return "gun"
    elif n == 1:
        return "zombie"
    elif n == 2:
        return "spock"
    elif n == 3:
        return "scissors"
    elif n == 4:
        return "paper"
    elif n == 5:
        return "lizard"
    elif n == 6:
        return "rock"
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

    >>>game_decision(1, 0)
    Computer wins!
    >>>game_decision(3, 3)
    Both ties!
    >>>game_decision(4, 2)
    Player wins!
    """
    if player_choice_num == computer_choice_num:
        print("Both ties!")
    elif ((player_choice_num + 1) % 3) == computer_choice_num:
        print("Player wins!")
    else:
        print("Computer wins!")


valid = False
while valid == False:
    player_choice = input("Enter your choice: ")
    valid = check_valid_input(player_choice)
    if valid == False:
        print("Invalid choice. Enter again.")


computer_choice_num = random.randint(0, 2)
computer_choice = convert_to_string(computer_choice_num)
player_choice_num = convert_to_num(player_choice)
print("Players chooses ", player_choice)
print("Computer chooses ", computer_choice)

game_decision(player_choice_num, computer_choice_num)
