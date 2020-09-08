import random

scissors = 1
paper = 2
rock = 3
lizard = 4
gun = 5
zombie = 6
spock = 7
com_choose = random.randint(1,7)
def turn_to(com_choose):
    """Check turn to value
       >>> turn_to(7)
       'spock'
       >>> turn_to(2)
       'paper'
       >>> turn_to(3)
       'rock'
       >>> turn_to(4)
       'lizard'
       >>> turn_to(5)
       'gun'
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
        return 'gun'
    elif com_choose == 6:
        return 'zombie'
    elif com_choose == 7:
        return 'spock'
def take_value(player):
    """Check take value
        >>> take_value('scissors')
        1
        >>> take_value('spock')
        7
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
    elif player == 'gun':
        return 5
    elif player == 'zombie':
        return 6
    elif player == 'spock':
        return 7
    else:
        print( "Invalid input" )

def who_win(com_choose,player):
    """Check who is win
    >>> who_win(2,1)
    Player wins
    >>> who_win(5,2)
    Player wins
    >>> who_win(1,2)
    Computer wins
    >>> who_win(3,2)
    Player wins
    >>> who_win(7,1)
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
def woww():
    player = take_value(input("What is yours?: "))
    print(f"Com choose {turn_to(com_choose)}.")
    who_win(com_choose,player)