def check_valid_input(s):
    """Check that input is wrong or not

    >>> check_valid_input("rock")
    True
    >>> check_valid_input("paper")
    True
    >>> check_valid_input("scissors")
    True
    >>> check_valid_input("stand")
    False
    >>> check_valid_input("hamon")
    False
    >>> check_valid_input("vampire")
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
    """Convert input to number

    >>> convert_to_num("rock")
    0
    >>> convert_to_num("paper")
    1
    >>> convert_to_num("scissors")
    2
    >>> convert_to_num("stand")
    Error: should not reach this if input is a valid one
    >>> convert_to_num("hamon")
    Error: should not reach this if input is a valid one
    >>> convert_to_num("vampire")
    Error: should not reach this if input is a valid one

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
    """Convert number to string

    >>> convert_to_string(0)
    rock
    >>> convert_to_string(2)
    scissors
    >>> convert_to_string(1)
    paper
    >>> convert_to_string(4)
    Error: should not reach this if input is a valid one
    >>> convert_to_string(44)
    Error: should not reach this if input is a valid one
    >>> convert_to_string(444)
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
    """Check the winner

    >>> game_decision(0, 0)
    Both ties!
    >>> game_decision(0, 1)
    Computer wins!
    >>> game_decision(0, 2)
    Player wins!
    >>> game_decision(1, 0)
    Player wins!
    >>> game_decision(1, 1)
    Both ties!
    >>> game_decision(1, 2)
    Computer wins!
    >>> game_decision(2, 0)
    Computer wins!
    >>> game_decision(2, 1)
    Player wins!
    >>> game_decision(2, 2)
    Both ties!

    """
    if player_choice_num == computer_choice_num:
        print("Both ties!")
    elif ((player_choice_num + 1) % 3) == computer_choice_num:
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
computer_choice_num = random.randint(0, 2)
computer_choice = convert_to_string(computer_choice_num)
player_choice_num = convert_to_num(player_choice)
print("Players chooses ", player_choice)
print("Computer chooses ", computer_choice)


game_decision(player_choice_num, computer_choice_num)





