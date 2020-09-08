def check_valid_input(s):
    """
    Reture True if the input is in choices, and return False otherwise.
    >>> check_valid_input('paper')
    True
    >>> check_valid_input('cake')
    False
    >>> check_valid_input('rock')
    True
    >>> check_valid_input('spock')
    True
    >>> check_valid_input('lisa')
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
    Return number instead of the input in words.
    >>> convert_to_num('rock')
    2
    >>> convert_to_num('scissors')
    0
    >>> convert_to_num('cake')
    Error: should not reach this if input is a valid one
    >>> convert_to_num('lizard')
    3
    >>> convert_to_num('spock')
    6
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
    Return the opposite of convert to num function.
    >>> convert_to_string(1)
    'paper'
    >>> convert_to_string(2)
    'rock'
    >>> convert_to_string(7)
    Error: should not reach this if input is a valid one
    >>> convert_to_string(3)
    'lizard'
    >>> convert_to_string(4)
    'gun'
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
    Return game result from player and computer choice.
    >>> game_decision(1, 1)
    Both ties!
    >>> game_decision(2, 3)
    Player wins!
    >>> game_decision(0, 1)
    Player wins!
    >>> game_decision(4, 0)
    Player wins!
    >>> game_decision(3, 1)
    Player wins!
    """
    if player_choice_num == computer_choice_num:
        print("Both ties!")
    elif player_choice_num == 0:
        if computer_choice_num ==1 or computer_choice_num == 3 or computer_choice_num == 5:
            print("Player wins!")
    elif player_choice_num == 1:
        if computer_choice_num ==6 or computer_choice_num == 4 or computer_choice_num == 2:
            print("Player wins!")
    elif player_choice_num == 2:
        if computer_choice_num ==0 or computer_choice_num == 5 or computer_choice_num == 3:
            print("Player wins!")
    elif player_choice_num == 3:
        if computer_choice_num ==1 or computer_choice_num == 6 or computer_choice_num == 4:
            print("Player wins!")
    elif player_choice_num == 4:
        if computer_choice_num ==2 or computer_choice_num == 0 or computer_choice_num == 5:
            print("Player wins!")
    elif player_choice_num == 5:
        if computer_choice_num ==3 or computer_choice_num == 1 or computer_choice_num == 6:
            print("Player wins!")
    elif player_choice_num == 6:
        if computer_choice_num ==0 or computer_choice_num == 2 or computer_choice_num == 4:
            print("Player wins!")
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
computer_choice_num = random.randint(0, 6)
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

if __name__ == '__main__':
    import doctest
    doctest.testmod()

