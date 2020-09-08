def check_valid_input(s):
    """Check if it's correct input.
    >>> check_valid_input('scissors')
    True
    >>> check_valid_input('house')
    False
    >>> check_valid_input('rock')
    True
    >>> check_valid_input('paper')
    True
    >>> check_valid_input('lizard')
    True
    """
    if s == "rock" or s == "paper" or s == "scissors" or s == "spock" or s == "lizard":
        return True
    else:
        return False


def convert_to_num(s):
    if s == "rock":
        return 0
    elif s == "paper":
        return 1
    elif s == "scissors":
        return 2
    elif s == "spock":
        return 3
    elif s == "lizard":
        return 4
    else:
        print("Error: should not reach this if input is a valid one")


def convert_to_string(n):
    if n == 0:
        return "rock"
    elif n == 1:
        return "paper"
    elif n == 2:
        return "scissors"
    elif n == 3:
        return "spock"
    elif n == 4:
        return "lizard"
    else:
        print("Error: should not reach this if input is a valid one")


def game_decision(player_choice_num, computer_choice_num):
    """
    Check the games result
    >>> game_decision(0, 1)
    Computer wins!
    >>> game_decision(0, 2)
    Player wins!
    >>> game_decision(0,0)
    Both ties!
    >>> game_decision(1,0)
    Player wins!
    >>> game_decision(1,2)
    Computer wins!
    >>> game_decision(2,1)
    Player wins!
    >>> game_decision(3,1)
    Computer wins!
    >>> game_decision(3,2)
    Player wins!
    >>> game_decision(4,1)
    Player wins!
    >>> game_decision(4,4)
    Both ties!
    """
    if player_choice_num == computer_choice_num:
        print("Both ties!")
    elif ((player_choice_num + 1) % 3) == computer_choice_num:
        print("Computer wins!")
    else:
        print("Player wins!")


# get an input from a player and validate
def display():
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