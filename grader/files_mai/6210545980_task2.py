def check_valid_input(a): # Check input that must be only rock, paper, scissors, lizard and spock.
    """
    >>> check_valid_input("rock")
    True
    >>> check_valid_input("paper")
    True
    >>> check_valid_input("scissors")
    True
    >>> check_valid_input("lizard")
    True
    >>> check_valid_input("spock")
    True
    >>> check_valid_input("a")
    False
    """
    if a == "rock":
        return True
    elif a == "paper":
        return True
    elif a == "scissors":
        return True
    elif a == "lizard":
        return True
    elif a == "spock":
        return True
    else :
        return False

def convert_to_num(s): # Convert string to number.
    """
    >>> convert_to_num("rock")
    0
    >>> convert_to_num("paper")
    1
    >>> convert_to_num("scissors")
    2
    >>> convert_to_num("lizard")
    3
    >>> convert_to_num("spock")
    4
    >>> convert_to_num("rook")
    Error: should not reach this if input is a valid one
    >>> convert_to_num("456213")
    Error: should not reach this if input is a valid one
    """
    if s == "rock":
        return 0
    elif s == "paper":
        return 1
    elif s == "scissors":
        return 2
    elif s == "lizard":
        return 3
    elif s == "spock":
        return 4
    else:
        print("Error: should not reach this if input is a valid one")

def convert_to_string(n): # Convert number to string.
    """
    >>> convert_to_string(0)
    'rock'
    >>> convert_to_string(1)
    'spock'
    >>> convert_to_string(2)
    'paper'
    >>> convert_to_string(3)
    'lizard'
    >>> convert_to_string(4)
    'scissors'
    >>> convert_to_string("rock")
    Error: should not reach this if input is a valid one
    """
    if n == 0:
        return "rock"
    elif n == 1:
        return "spock"
    elif n == 2:
        return "paper"
    elif n == 3:
        return "lizard"
    elif n == 4:
        return "scissors"
    else:
        print("Error: should not reach this if input is a valid one")

def game_decision(player_choice_num, computer_choice_num): # Calculate result of game.
    """
    >>> game_decision(4,1)
    Computer wins!
    >>> game_decision(3,0)
    Computer wins!
    >>> game_decision(2,4)
    Computer wins!
    >>> game_decision(4,2)
    Player wins!
    >>> game_decision(0,3)
    Player wins!
    """
    win_lose = (computer_choice_num - player_choice_num) % 5
    if win_lose == 0:
        print("Both ties!")
    elif win_lose == 1 or win_lose == 2:
        print("Computer wins!")
    else:
        print("Player wins!")

valid = False
while valid == False:
    player_choice = input("Enter your choice: ")
    valid = check_valid_input(player_choice)
    if valid == False:
        print("Invalid choice. Enter again.")

import random
computer_choice_num = random.randint(0, 4)
computer_choice = convert_to_string(computer_choice_num)
player_choice_num = convert_to_num(player_choice)
print("Players chooses ", player_choice)
print("Computer chooses ", computer_choice)
game_decision(player_choice_num, computer_choice_num)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
