import random
import sys


def convert_to_num(s):
    """This function convert your choice into number.
    >>> convert_to_num('gun')
    5
    >>> convert_to_num('zombie')
    4
    >>> convert_to_num('spock')
    3
    """
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


def check_input(p1) :
    """This function check whether your input is valid or not.
    >>> check_input('gun')
    True
    >>> check_input('test')
    False
    """
    if p1=='rock' or p1=='paper' or p1=='scissors' or p1=='spock' or p1=='lizard' or p1=='gun' or p1=='zombie':
        return True
    else :
        return False


def result(p1,ai) :
    """This function return the result.
    >>> result('gun','gun')
    Both ties!
    >>> result('gun','zombie')
    Player wins!
    >>> result('zombie','scissors')
    Computer wins!
    """
    if convert_to_num(p1) == convert_to_num(ai):
        print("Both ties!")
    elif ((convert_to_num(p1) + 1) % 7) == convert_to_num(ai) or ((convert_to_num(p1) + 3) % 7) == convert_to_num(ai) or ((convert_to_num(p1) + 5) % 7) == convert_to_num(ai):
        print("Computer wins!")
    else:
        print("Player wins!")


def choose(ai) :
    """This function print what the ai choose.
    >>> choose('gun')
    Computer chooses gun
    >>> choose('zombie')
    Computer chooses zombie
    """
    print(f'Computer chooses {ai}')

def main():
    """
    This is your main program
    """
    while True :
        list1 = ['rock','paper','scissors','spock','lizard','gun','zombie']
        ai = random.choice(list1)
        p1 = input('Player chooses ')
        print()
        if check_input(p1) == False :
            print('Invalid input.')
            sys.exit()
        choose(ai)
        result(p1,ai)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
