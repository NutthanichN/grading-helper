# import random
# list = ["rock","scissors","paper","Spock","lizard"]
# player = input("Play chooses: ")
# com = random.choice(list)
# print(f"Computer choose {com}")
def strnum(player):
    '''
    :param player: [str]
    :return: [int]
    '''
    if player == "scissors":
        return 1
    if player == "paper":
        return 2
    if player == "rock":
        return 3
    if player == "lizard":
        return 4
    if player == "Spock":
        return 5
def play(player,com):

    """
    >>> play('Spock','paper')
    Computer Wins!
    >>> play('rock','scissors')
    Player Wins!
    >>> play('lizard','lizard')
    Both Tie!
    >>> play('paper','scissors')
    Computer Wins!
    """
    p = strnum(player)
    c = strnum(com)
    if (p-c)%2 != 0:
        print("Computer Wins!")
    elif p == c:
        print("Both Tie!")
    else:
        print("Player Wins!")
    # we got a pattern when we minus strnum(player), strnum(com)
    # if computer win the result must be odd.
    # and player win the result must be even.

