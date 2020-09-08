def play2(player,com):
    """Print result of a game that simulates your playing Rock-Paper-Scissors-Lizard-Spock

    Args:
        player: player choose an object
        computer: randomly choose an object

    Return:
        The result of the game

        >>> play2('spock','spock')
        Computer choosed spock
        Both Tie!
        >>> play2('scissors','paper')
        Computer choosed paper
        You Win!
        >>> play2('lizard','scissors')
        Computer choosed scissors
        Computer Wins!
        >>> play2('spock','scissors')
        Computer choosed scissors
        You Win!
        >>> play2('rock','paper')
        Computer choosed paper
        Computer Wins!
        >>> play2('spock','lizard')
        Computer choosed lizard
        Computer Wins!

    Notes: I used 'a' list as differents of index of item in list that make computer wins
    such as lizard is index#3 in list 'a' and paper is index#2 in list 'a' so if rock 3 minus 2
    is 1 as in list 'a' below ,except if computer chooses rock or spock its will be in another
    condition such as spock that win scissors but index of spock is 1 but scissors is 4 which
    1 minus 4 is -3 so I use speciel condition for rock and spock that can make the value in
    'a' list different.

    """
    import random
    items = ['rock','spock','paper','lizard','scissors']
    print (f"Computer choosed {com}")
    if player in items:
        a = [1,2]
        if com == "rock":
            a = [1,-4]
        if com == "spock":
            a = [-4,-3]
        if (items.index(com) - items.index(player)) in a:
            print ("Computer Wins!")
        elif items.index(player) == items.index(com):
            print ("Both Tie!")
        else:
            print ("You Win!")
