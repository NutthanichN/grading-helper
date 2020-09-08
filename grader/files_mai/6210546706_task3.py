import random
def convert_to_num(x):
    """ convert str to num for runthe program in def game

    >>> convert_to_num('rock')
    0
    >>> convert_to_num('paper')
    1
    >>> convert_to_num('scissors')
    2
    """
    if x == 'rock':
        return 0
    elif x == 'paper':
        return 1
    elif x == 'scissors':
        return 2
    elif x == 'spock':
        return 3
    elif x == 'zombie':
        return 4
    elif x == 'gun':
        return 5
    elif x == 'lizard':
        return 6
    else:
        print("Error: should not reach this if input is a valid one")

def convert_to_str(y):
    """convert num to str for display

    >>> convert_to_str(0)
    rock
    >>> convert_to_str(1)
    paper
    >>> convert_to_str(2)
    scissors
    """
    if y == 0:
        return 'rock'
    elif y == 1:
        return 'paper'
    elif y == 2:
        return 'scissors'
    elif y == 3:
        return 'spock'
    elif y == 4:
        return 'zombie'
    elif y == 5:
        return 'gun'
    elif y == 6:
        return 'lizard'
    else:
        print("Error: should not reach this if input is a valid one")


def game(com,player):
    """ run the game by num

    >>> game(0,0)
    Both ties!
    >>> game(0,2)
    Player win!
    """
    if player == com:
        print('Both ties!')
    elif ((player + 3)%7) == com:
        print('Com win!')
    else:
        print('Player wins!')


def check_choice(choose):
    """check choice for running program

    >>> check_choice(rock)
    True
    >>> check_choice(1)
    False
    """
    if choose == 'rock':
        return True
    elif choose == 'paper':
        return True
    elif choose == 'scissors':
        return True
    elif choose == 'lizard':
        return True
    elif choose == 'spock':
        return True
    elif choose == 'gun':
        return True
    elif choose == 'zombie':
        return True
    else:
        return False


check = False
while check == False:
    player_choice = input(f'Enter your choice: ')
    check = check_choice(player_choice)
    if check == False:
        print('Invalid choice. Enter again.')


com = random.randint(0,6)
com_str = convert_to_str(com)
print(f'Computer chooses: {com_str}')

player_num = convert_to_num(player_choice)

game(com,player_num)