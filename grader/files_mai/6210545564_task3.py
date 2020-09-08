import random

def check_input(s):
    """
    check if the input is one of the choice, if it is return true, if not return false
    >>> check_input('zombie')
    True
    >>> check_input('lizard')
    True
    >>> check_input('rock')
    True
    >>> check_input('abc')
    False
    """
    if s == 'rock':
        return True
    elif s == 'scissors':
        return True
    elif s == 'paper':
        return True
    elif s == 'spock':
        return True
    elif s == 'lizard':
        return True
    elif s == 'zombie':
        return True
    elif s == 'gun':
        return True
    else:
        return False


def num_to_string(n):
    """
    change number to string
    >>> num_to_string(3)
    'paper'
    >>> num_to_string(2)
    'spock'
    >>> num_to_string(9)

    >>> num_to_string(4)
    'lizard'
    """
    if n == 0:
        return 'rock'
    elif n == 1:
        return 'gun'
    elif n == 2:
        return 'spock'
    elif n == 3:
        return 'paper'
    elif n == 4:
        return 'lizard'
    elif n == 5:
        return 'zombie'
    elif n == 6:
        return 'scissors'

def string_to_num(s):
    """
    change string to a number
    >>> string_to_num('scissors')
    6
    >>> string_to_num('spock')
    2
    >>> string_to_num('rock')
    0
    >>> string_to_num('hello')

    >>> string_to_num('zombie')
    5
    >>> string_to_num('gun')
    1
    """
    if s == 'rock':
        return 0
    elif s == 'gun':
        return 1
    elif s == 'spock':
        return 2
    elif s == 'paper':
        return 3
    elif s == 'lizard':
        return 4
    elif s == 'zombie':
        return 5
    elif s == 'scissors':
        return 6

def rule(p,c):
    """
    compute the value of computer choice and player with (p + 3)%7 >= computer's number  if the result is >= computer's number return computer wins
    other results will makes the player wins
    >>> rule(0,6)
    Player wins!
    >>> rule(2,5)
    Computer wins!
    >>> rule(1,1)
    Both ties!
    """
    if p == c:
        print('Both ties!')
    elif (p + 3)%7 >= c:
        print('Computer wins!')
    else:
        print('Player wins!')



valid = False
while valid == False:
    player_choose = input("Enter your choice: ")
    valid = check_input(player_choose)
    if valid == False:
        print("Invalid choice. Enter again")

player_num = string_to_num(player_choose)
com_num = random.randint(0,4)
com_choose = num_to_string(com_num)
print(f'Player chooses {player_choose}')
print(f'Computer chooses {com_choose}')
rule(player_num,com_num)