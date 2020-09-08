import random
import sys


def convert_to_num(s):
    """This function convert your choice into number.
    >>> convert_to_num('rock')
    0
    >>> convert_to_num('paper')
    1
    >>> convert_to_num('scissors')
    2
    """
    if s == "rock":
        return 0
    elif s == "paper":
        return 1
    elif s == "scissors":
        return 2


def check_input(p1) :
    """This function check whether your input is valid or not.
    >>> check_input('scissors')
    True
    >>> check_input('test')
    False
    """
    if p1=='rock' or p1=='paper' or p1=='scissors':
        return True
    else :
        return False


def result(p1,ai) :
    """This function return the result.
    >>> result('rock','rock')
    'Both ties!'
    >>> result('paper','rock')
    'Player wins!'
    >>> result('scissors','rock')
    'Computer wins!'
    """
    if convert_to_num(p1) == convert_to_num(ai):
        return "Both ties!"
    elif ((convert_to_num(p1) + 1) % 3) == convert_to_num(ai):
        return "Computer wins!"
    else:
        return "Player wins!"


def choose(ai) :
    """This function print what the ai choose.
    >>> choose('rock')
    Computer chooses rock
    >>> choose('paper')
    Computer chooses paper
    """
    print(f'Computer chooses {ai}')

def main():
    """
    This is your main program
    """
    while True :
        list1 = ['rock','paper','scissors']
        ai = random.choice(list1)
        p1 = input('Player chooses ')
        if check_input(p1) == False :
            print('Invalid input.')
            sys.exit()
        choose(ai)
        print(result(p1,ai))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
