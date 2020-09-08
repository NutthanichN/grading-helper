import random

def check_input(s):
    """
    check if the input is one of the choice, if it is return true, if not return false
    >>> check_input('rock')
    True
    >>> check_input('lizard')
    True
    >>> check_input('paper')
    True
    >>> check_input('zebra')
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
    else:
        return False


def num_to_string(n):
    """
    change number to string
    >>> num_to_string(3)
    'lizard'
    >>> num_to_string(2)
    'paper'
    >>> num_to_string(5)

    """
    if n == 0:
        return 'rock'
    elif n == 1:
        return 'spock'
    elif n == 2:
        return 'paper'
    elif n == 3:
        return 'lizard'
    elif n == 4:
        return 'scissors'

def string_to_num(s):
    """
    change string to a number
    >>> string_to_num('scissors')
    4
    >>> string_to_num('spock')
    1
    >>> string_to_num('rock')
    0
    >>> string_to_num('hello')

    """
    if s == 'rock':
        return 0
    elif s == 'spock':
        return 1
    elif s == 'paper':
        return 2
    elif s == 'lizard':
        return 3
    elif s == 'scissors':
        return 4

def rule(p,c):
    """
    compute the value of computer choice and player with (p + 2)%5 >= computer's number  if the result is >= computer's number return computer wins
    other results will makes the player wins
    >>> rule(4,2)
    Player wins!
    >>> rule(1,3)
    Computer wins!
    >>> rule(0,0)
    Both ties!
    """
    if p == c:
        print('Both ties!')
    elif (p + 2)%5 >= c:
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




