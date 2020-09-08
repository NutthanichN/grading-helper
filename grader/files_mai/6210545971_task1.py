import random
choice = ['scissors', 'paper', 'rock']
scissors_win =  [1]
paper_win =     [2]
rock_win =      [0]


def check_win(x, y):
    """Check if x win y.

    >>> check_win(0,0)
    False
    >>> check_win(0,1)
    True
    >>> check_win(0,2)
    False
    >>> check_win(1,0)
    False
    >>> check_win(1,1)
    False
    >>> check_win(1,2)
    True
    >>> check_win(2,0)
    True
    >>> check_win(2,1)
    False
    >>> check_win(2,2)
    False
    """
    if x == 0 and y in scissors_win:
        return True
    elif x == 1 and y in paper_win:
        return True
    elif x == 2 and y in rock_win:
        return True
    else:
        return False


def str_to_num(x):
    """change string to number sort according to list

    >>> str_to_num('rock')
    2
    >>> str_to_num('paper')
    1
    >>> str_to_num('scissors')
    0
    >>> str_to_num('ROCK')
    Error: should not reach this if input is a valid one
    """
    if x == 'scissors':
        return 0
    if x == 'paper':
        return 1
    if x == 'rock':
        return 2
    else:
        print("Error: should not reach this if input is a valid one")


def check_valid_input(x):
    """check if player input is valid

    >>> check_valid_input('x')
    False
    >>> check_valid_input('rock')
    True
    >>> check_valid_input('scissors')
    True
    >>> check_valid_input('paper')
    True
    >>> check_valid_input(0)
    False
    """
    if x in choice:
        return True
    else:
        return False


def game_decision(x,y):
    """check and display winner

    >>> game_decision(0,0)
    Both tie!
    >>> game_decision(0,1)
    Player win!
    >>> game_decision(0,2)
    Computer win!
    >>> game_decision(1,0)
    Computer win!
    >>> game_decision(1,1)
    Both tie!
    >>> game_decision(1,2)
    Player win!
    >>> game_decision(2,0)
    Player win!
    >>> game_decision(2,1)
    Computer win!
    >>> game_decision(2,2)
    Both tie!
    """
    if x == y:
        print("Both tie!")
    elif check_win(x, y):
        print("Player win!")
    elif check_win(y, x):
        print("Computer win!")
    else:
        print("Error: should not reach this if input is a valid one")


########################################################################################################################
def main() -> None:
    # get an input from a player and validate
    valid = False
    while valid != True:
        player = input("Player chooses ").lower()
        valid = check_valid_input(player)
        if valid == False:
            print("Invalid choice. Enter again.")
# random a response from a computer and print out computer choices
    com = choice[random.randint(0, 2)]
    print(f'Computer chooses {com}')
# convert string to number
    player = str_to_num(player)
    com = str_to_num(com)
# apply the rules of game, check and display winner
    game_decision(player, com)

if __name__ == '__main__':
    main()