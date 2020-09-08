import random

# list = ["rock", "scissors", "paper", "Spock", "lizard", "gun", "zombie"]
# player = random.choice(list)#input("Play chooses: ")
# com = random.choice(list)
# print(f"Computer choose {com}")


def strnum(player):
    '''
    :param player: [str]
    :return: [int]
    '''
    if player == "Scissors":
        return 1
    if player == "Paper":
        return 2
    if player == "Rock":
        return 3
    if player == "Lizard":
        return 4
    if player == "Gun":
        return 5
    if player == "Zombie":
        return 6
    if player == "Spock":
        return 7
def more7(x):
    '''
    :param x: x
    :return: return x%7 if x > 7, return x if x <= 7
    '''
    if x > 7:
        return x % 7
    else:
        return x
def play(player,com):
    """
        >>> play('Spock','Paper')
        Computer Wins!
        >>> play('Spock','Scissors')
        Player Win!
        >>> play('Lizard','Lizard')
        Both tie!
        >>> play('Paper','Scissors')
        Computer Wins!
        >>> play('Zombie','Paper')
        Player Win!
        >>> play('Gun','Rock')
        Player Win!
        >>> play('Rock','Rock')
        Both tie!
        >>> play('Gun','Paper')
        Computer Wins!
        >>> play('Paper','Zombie')
        Computer Wins!
    """
    p = strnum(player)
    c = strnum(com)
    # Ex.1 scissor(1) win: paper(2), lizard(4), zombie(6)
    # Ex.2 paper(2) win: rock(3), gun(5), spock(7)
    # Ex.3 rock(3) win: scissor(1), lizard(4), zombie(6)
    # So we got pattern is if you choose num and you got win
    # computer need to choose num+1, num+3, num+5 and
    # we need more7 function because in Ex.3 if rock(3)+5 = 8%7 = scissor(1)
    if c == more7(int(p)+1) or c == more7(int(p)+3) or c == more7(int(p)+5):
        print("Player Win!")
    elif p - c == 0:
        print("Both tie!")
    else:
        print("Computer Wins!")


