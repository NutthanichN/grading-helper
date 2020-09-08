def play3(player,com):
    """Print result of a game that simulates your playing Rock-Paper-Scissors-Lizard-Spock-Zombie-Gun

    Args:
        player: player choose an object
        computer: randomly choose an object

    Return:
        The result of the game

        >>> play3('spock','spock')
        Computer choosed spock
        Both Tie!
        >>> play3('scissors','paper')
        Computer choosed paper
        You Win!
        >>> play3('gun','zombie')
        Computer choosed zombie
        You Win!
        >>> play3('lizard','scissors')
        Computer choosed scissors
        Computer Wins!
        >>> play3('rock','gun')
        Computer choosed gun
        Computer Wins!
        >>> play3('spock','scissors')
        Computer choosed scissors
        You Win!
        >>> play3('zombie','rock')
        Computer choosed rock
        Computer Wins!
        >>> play3('rock','paper')
        Computer choosed paper
        Computer Wins!
        >>> play3('spock','lizard')
        Computer choosed lizard
        Computer Wins!

    Notes: a = differents of index of items in list that make player win.

    """
    import random
    items = ['scissors', 'paper', 'rock', 'lizard', 'gun', 'zombie', 'spock']
    print (f"Computer choosed {com}")
    a = [1,3,5,-2,-4,-6]
    if player in items:
        if (items.index(com) - items.index(player)) in a:
            print ("You Win!")
        elif items.index(player) == items.index(com):
            print ("Both Tie!")
        else:
            print ("Computer Wins!")
