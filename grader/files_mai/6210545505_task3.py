def check_valid_input(s):
    '''this func is to check input
    Example:
        >>> check_valid_input("rock")
        True
        >>> check_valid_input("rok")
        False
    '''
    if s == "rock":
        return True
    elif s == "paper":
        return True
    elif s == "scissors":
        return True
    elif s == "spock":
        return True
    elif s == "lizard":
        return True
    elif s == "zombie":
        return True
    elif s == "gun":
        return True
    else:
        return False

def convert_to_num(s):
    '''this func is to convert input to num 
    Example:
        >>> convert_to_num("rock")
        0
        >>> convert_to_num("paper")
        1
    '''
    if s == "rock":
        return 0
    elif s == "paper":
        return 1
    elif s == "scissors":
        return 2
    elif s == "spock":
        return 3
    elif s == "zombie":
        return 4
    elif s == "gun":
        return 5
    elif s == "lizard":
        return 6
    else:
        print("Error: should not reach this if input is a valid one")

def convert_to_string(n):
    '''this func is to convert input to string 
    Example:
        >>> convert_to_string(0)
        'rock'
        >>> convert_to_string(1)
        'paper'
    '''
    if n == 0:
        return "rock"
    elif n == 1:
        return "paper"
    elif n == 2:
        return "scissors"
    elif n == 3:
        return "spock"
    elif n == 4:
        return "zombie"
    elif n == 5:
        return "gun"
    elif n == 6:
        return "lizard"
    else:
        print("Error: should not reach this if input is a valid one")

def game_decision(player_choice_num, computer_choice_num):
    '''this func is to decide who win the game
    Example:
        >>> game_decision(1, 0)
        Player wins!
        >>> game_decision(1, 6)
        Computer wins!
        >>> game_decision(1, 3)
        Player wins!
        >>> game_decision(5, 3)
        Computer wins!
        >>> game_decision(0, 6)
        Player wins!
        >>> game_decision(4, 3)
        Player wins!
        >>> game_decision(2, 4)
        Player wins!
        >>> game_decision(5, 5)
        Both ties!
        >>> game_decision(0, 0)
        Both ties!
        '''
    if player_choice_num == computer_choice_num:
        print("Both ties!")
    elif (((player_choice_num + 1) % 7) == computer_choice_num) or (((player_choice_num + 3) % 7) == computer_choice_num) or (((player_choice_num + 5) % 7) == computer_choice_num):
        print("Computer wins!")
    else:
        print("Player wins!")

import random
def main():
    """get an input from a player and validate"""   
    valid = False
    while valid == False:
        player_choice = input("Enter your choice: ")
        valid = check_valid_input(player_choice)
        if valid == False:
            print("Invalid choice. Enter again.")

    # random a response from a computer and print out player and computer choices
    computer_choice_num = random.randint(0, 6)
    computer_choice = convert_to_string(computer_choice_num)
    player_choice_num = convert_to_num(player_choice)
    print("Players chooses ", player_choice)
    print("Computer chooses ", computer_choice)

    # do this
    game_decision(player_choice_num, computer_choice_num)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)