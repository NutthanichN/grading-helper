import random

def convert_to_num(x):
    '''
        Change string into a number so that it could be calculated in another function
        :param x: [string]
        :return: [int]
    '''
    if x == 'Scissors':
        return 1
    elif x == 'Paper':
        return 2
    elif x == "Rock":
        return 3

player = str(input('Player chooses: ')) #receive information from the player
choice = ['Scissors','Paper','Rock'] #set of information
com = random.choice(choice) #pick one string randomly from list named choice
print (f'Computer chooses: {com}')

def play(player,com):
    """
        >>> play('Rock','Paper')
        Computer Wins!
        >>> play('Rock','Scissors')
        You Win!
        >>> play('Paper','Paper')
        Both Tie!
        >>> play('Paper','Scissors')
        Computer Wins!
        >>> play('Paper','Rock')
        You Win!
        >>> play('Rock','Rock')
        Both Tie!

    """
    player1 = convert_to_num(player)#receive variable names player that is converted in to a number with a new name
    com1 = convert_to_num(com)#receive variable names com that is converted in to a number with a new name
    if com1 == player1: #if com and player pick the same number print"Both Tie!"
        print('Both Tie!')
    elif player1+1 == com1 or player1-2 == com1:#it's a position from a cycle that it's gonna win 1 step forward or 2 steps backward
        print('You Win!')
    else:
        print('Computer Wins!')
play(player,com) #Calling function for doing all the calculation in the function

if __name__ == '__main__': #Check doctests whether they are correct or not
    import doctest
    doctest.testmod(verbose=True)