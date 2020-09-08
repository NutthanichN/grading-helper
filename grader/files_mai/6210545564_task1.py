import random


def check_valid_input(s):
    """
    check if the input is one of the choice, if it is return true, if not return false
    >>> check_valid_input(1)
    False
    >>> check_valid_input('rock')
    True
    >>> check_valid_input('apple')
    False
    >>> check_valid_input('paper')
    True
    >>> check_valid_input('scissors')
    True
    """
    if s == 'rock':
        return True
    elif s == 'paper':
        return True
    elif s == 'scissors':
        return True
    else:
        return False


def string_to_num(s):
    '''
    change string to a number
    >>> string_to_num('rock')
    0
    >>> string_to_num('paper')
    1
    >>> string_to_num('scissors')
    2
    >>> string_to_num(12345)

    '''
    if s == 'rock':
        return 0
    elif s == 'paper':
        return 1
    elif s == 'scissors':
        return 2



def num_to_string(num):
    '''
    change number to string
    >>> num_to_string(0)
    'rock'
    >>> num_to_string(2)
    'scissors'
    >>> num_to_string(1)
    'paper'
    >>> num_to_string(89)

    '''
    if num == 0:
        return 'rock'
    elif num == 1:
        return "paper"
    elif num == 2:
        return "scissors"


def rule(player, com):
    '''
    compute the value of computer choice and player with (player+1)%3) == computer's number  if the result is >= computer's number return computer wins
    other results will makes the player wins
    >>> rule(0,0)
    Both ties!
    >>> rule(5,6)
    Player wins!
    >>> rule(2,0)
    Computer wins!
    >>> rule(1,0)
    Player wins!
    '''
    if player == com:
        print('Both ties!')
    elif ((player+1)%3) == com:
        print("Computer wins!")
    else:
        print("Player wins!")


valid = False
while valid == False:
    player_choice = input("Enter your choice: ")
    valid = check_valid_input(player_choice)
    if valid == False:
        print("Invalid choice. Enter again")

com_num = random.randint(0, 2)
com_choose = num_to_string(com_num)
print(f"player chooses {player_choice}")
print(f"computer chooses {com_choose}")
player_num = string_to_num(player_choice)
rule(player_num, com_num)

input()







