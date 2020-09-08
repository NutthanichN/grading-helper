def check_valid_input(s):
    """
    >>> check_valid_input("rock")
    True
    >>> check_valid_input("jojo")
    False
    """
    if s == "rock":
        return True
    elif s == "paper":
        return True
    elif s == "scissors":
        return True
    elif s == "lizard":
        return True
    elif s == "spock":
        return True
    elif s == "zombie":
        return True
    elif s == "gun":
        return True
    else:
        return False

def convert_to_num(s):
    """
    >>> convert_to_num("rock")
    2
    >>> convert_to_num("zombie")
    5
    """
    if s == "scissors":
        return 0
    elif s == "paper":
        return 1
    elif s == "rock":
        return 2
    elif s == "lizard":
        return 3
    elif s == "gun":
        return 4
    elif s == "zombie":
        return 5
    elif s == "spock":
        return 6
    else:
        print("Error: should not reach this if input is a valid one")

def convert_to_string(n):
    """
    >>> convert_to_string(4)
    'gun'
    >>> convert_to_string(3000)
    Error: should not reach this if input is a valid one
    """
    if n == 0:
        return "scissors"
    elif n == 1:
        return "paper"
    elif n == 2:
        return "rock"
    elif n == 3:
        return "lizard"
    elif n == 4:
        return "gun"
    elif n == 5:
        return "zombie"
    elif n == 6:
        return "spock"
    else:
        print("Error: should not reach this if input is a valid one")

def game_decision(player_choice_num, computer_choice_num):
    """
    >>> game_decision(3, 0)
    Computer wins!
    >>> game_decision(6, 2)
    Player wins!
    """
    dif = (computer_choice_num-player_choice_num)
    if player_choice_num == computer_choice_num:
        print("Both ties!")
    elif dif > 0:
        if dif%2 == 0:
            print("Computer wins!")
        else:
            print("Player wins!")
    elif dif < 0:
        if dif%2 == 0:
            print("Player wins!")
        else:
            print("Computer wins!")


valid = False
while valid == False:
    player_choice = input("Enter your choice: ")
    valid = check_valid_input(player_choice)
    if valid == False:
        print("Invalid choice. Enter again.")

import random
computer_choice_num = random.randint(0, 6)
computer_choice = convert_to_string(computer_choice_num)
player_choice_num = convert_to_num(player_choice)
print("Players chooses ", player_choice)
print("Computer chooses ", computer_choice)

game_decision(player_choice_num, computer_choice_num)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
