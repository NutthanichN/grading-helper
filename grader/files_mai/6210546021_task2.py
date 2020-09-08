import random

scissors = 1
paper = 2
rock = 3
lizard = 4
spock = 5
com_choose = random.randint(1,5)

def turn_to(com_choose):
    """Check turn to value
    >>> turn_to(1)
    'scissors'
    >>> turn_to(2)
    'paper'
    >>> turn_to(3)
    'rock'
    >>> turn_to(4)
    'lizard'
    >>> turn_to(5)
    'spock'
    """
    if com_choose == 1:
        return 'scissors'
    elif com_choose == 2:
        return 'paper'
    elif com_choose == 3:
        return 'rock'
    elif com_choose == 4:
        return 'lizard'
    elif com_choose == 5:
        return 'spock'
def take_value(player):
    """Check take value
    >>> take_value('scissors')
    1
    >>> take_value('spock')
    5
    >>> take_value('rock')
    3
    >>> take_value('lizard')
    4
    >>> take_value('paper')
    2
    """
    if player == 'scissors':
        return 1
    elif player == 'paper':
        return 2
    elif player == 'rock':
        return 3
    elif player == 'lizard':
        return 4
    elif player == 'spock':
        return 5
    else:
        print("Invalid input")


def who_win(com_choose,player):
    """Check who is winner
    >>> who_win(2,1)
    Player wins
    >>> who_win(2,2)
    Both tie!
    >>> who_win(1,2)
    Computer wins
    >>> who_win(3,2)
    Player wins
    >>> who_win(2,3)
    Computer wins
    """
    if com_choose == player:
        print("Both tie!")
    elif player - com_choose > 0:
        if (player - com_choose)%2 == 0:
            print("Player wins")
        else:
            print("Computer wins")
    else:
        if (player - com_choose)%2 == 0:
            print("Computer wins")
        else:
            print("Player wins")
def main():
    player = take_value(input("What is yours?: "))
    print(f"Com choose {turn_to(com_choose)}.")
    who_win(com_choose,player)

