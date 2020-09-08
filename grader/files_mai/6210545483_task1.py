def play1(player,com):
    """Print result of a game that simulates your playing Rock-Paper-Scissors

    Args:
        player: player choose an object
        computer: randomly choose an object

    Return:
        The result of the game

        >>> play1('paper','scissors')
        Computer choosed scissors
        Computer win!
        >>> play1('rock','scissors')
        Computer choosed scissors
        Player win!
        >>> play1('scissors','scissors')
        Computer choosed scissors
        Both Ties
    """
    import random
    print(f"Computer choosed {com}")
    items = ['rock','paper','scissors']
    if player in items:
        if (items.index(com) - items.index(player)) == 1 and -2:
            print ("Computer win!")
        elif (items.index(com) - items.index(player)) == 2 and -1:
            print ("Player win!")
        else:
            print ("Both Ties")
