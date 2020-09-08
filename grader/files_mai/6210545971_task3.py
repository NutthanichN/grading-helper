import random
choice = ['scissors', 'paper', 'rock', 'lizard', 'gun', 'zombie', 'spock']
scissors_win =  [1, 3, 5]
paper_win =     [2, 4, 6]
rock_win =      [3, 5, 0]
lizard_win =    [4, 6, 1]
gun_win =       [5, 0, 2]
zombie_win =    [6, 1, 3]
spock_win =     [0, 2, 4]


def check_win(x, y):
    """Check if x win y.

    >>> check_win(0,0)
    False
    >>> check_win(0,1)
    True
    >>> check_win(0,2)
    False
    >>> check_win(0,3)
    True
    >>> check_win(0,4)
    False
    >>> check_win(0,5)
    True
    >>> check_win(0,6)
    False
    >>> check_win(1,0)
    False
    >>> check_win(1,1)
    False
    >>> check_win(1,2)
    True
    >>> check_win(1,3)
    False
    >>> check_win(1,4)
    True
    >>> check_win(1,5)
    False
    >>> check_win(1,6)
    True
    >>> check_win(2,0)
    True
    >>> check_win(2,1)
    False
    >>> check_win(2,2)
    False
    >>> check_win(2,3)
    True
    >>> check_win(2,4)
    False
    >>> check_win(2,5)
    True
    >>> check_win(2,6)
    False
    >>> check_win(3,0)
    False
    >>> check_win(3,1)
    True
    >>> check_win(3,2)
    False
    >>> check_win(3,3)
    False
    >>> check_win(3,4)
    True
    >>> check_win(3,5)
    False
    >>> check_win(3,6)
    True
    >>> check_win(4,0)
    True
    >>> check_win(4,1)
    False
    >>> check_win(4,2)
    True
    >>> check_win(4,3)
    False
    >>> check_win(4,4)
    False
    >>> check_win(4,5)
    True
    >>> check_win(4,6)
    False
    >>> check_win(5,0)
    False
    >>> check_win(5,1)
    True
    >>> check_win(5,2)
    False
    >>> check_win(5,3)
    True
    >>> check_win(5,4)
    False
    >>> check_win(5,5)
    False
    >>> check_win(5,6)
    True
    >>> check_win(6,0)
    True
    >>> check_win(6,1)
    False
    >>> check_win(6,2)
    True
    >>> check_win(6,3)
    False
    >>> check_win(6,4)
    True
    >>> check_win(6,5)
    False
    >>> check_win(6,6)
    False
    >>> check_win(7,0)
    False
    >>> check_win(7,7)
    False
    """
    if x == 0 and y in scissors_win:
        return True
    elif x == 1 and y in paper_win:
        return True
    elif x == 2 and y in rock_win:
        return True
    elif x == 3 and y in lizard_win:
        return True
    elif x == 4 and y in gun_win:
        return True
    elif x == 5 and y in zombie_win:
        return True
    elif x == 6 and y in spock_win:
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
    >>> str_to_num('lizard')
    3
    >>> str_to_num('spock')
    6
    >>> str_to_num('zombie')
    5
    >>> str_to_num('gun')
    4
    >>> str_to_num('Rock')
    Error: should not reach this if input is a valid one
    >>> str_to_num('alien')
    Error: should not reach this if input is a valid one
    >>> str_to_num(6)
    Error: should not reach this if input is a valid one
    >>> str_to_num(4)
    Error: should not reach this if input is a valid one
    """
    if x == 'scissors':
        return 0
    if x == 'paper':
        return 1
    if x == 'rock':
        return 2
    if x == 'lizard':
        return 3
    if x == 'gun':
        return 4
    if x == 'zombie':
        return 5
    if x == 'spock':
        return 6
    else:
        print("Error: should not reach this if input is a valid one")


def check_valid_input(x):
    """check if player input is valid

    >>> check_valid_input('rock')
    True
    >>> check_valid_input('paper')
    True
    >>> check_valid_input('scissors')
    True
    >>> check_valid_input('lizard')
    True
    >>> check_valid_input('spock')
    True
    >>> check_valid_input('zombie')
    True
    >>> check_valid_input('gun')
    True
    >>> check_valid_input('Rock')
    False
    >>> check_valid_input('alien')
    False
    >>> check_valid_input(6)
    False
    >>> check_valid_input(4)
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
    >>> game_decision(0,3)
    Player win!
    >>> game_decision(0,4)
    Computer win!
    >>> game_decision(0,5)
    Player win!
    >>> game_decision(0,6)
    Computer win!
    >>> game_decision(1,0)
    Computer win!
    >>> game_decision(1,1)
    Both tie!
    >>> game_decision(1,2)
    Player win!
    >>> game_decision(1,3)
    Computer win!
    >>> game_decision(1,4)
    Player win!
    >>> game_decision(1,5)
    Computer win!
    >>> game_decision(1,6)
    Player win!
    >>> game_decision(2,0)
    Player win!
    >>> game_decision(2,1)
    Computer win!
    >>> game_decision(2,2)
    Both tie!
    >>> game_decision(2,3)
    Player win!
    >>> game_decision(2,4)
    Computer win!
    >>> game_decision(2,5)
    Player win!
    >>> game_decision(2,6)
    Computer win!
    >>> game_decision(3,0)
    Computer win!
    >>> game_decision(3,1)
    Player win!
    >>> game_decision(3,2)
    Computer win!
    >>> game_decision(3,3)
    Both tie!
    >>> game_decision(3,4)
    Player win!
    >>> game_decision(3,5)
    Computer win!
    >>> game_decision(3,6)
    Player win!
    >>> game_decision(4,0)
    Player win!
    >>> game_decision(4,1)
    Computer win!
    >>> game_decision(4,2)
    Player win!
    >>> game_decision(4,3)
    Computer win!
    >>> game_decision(4,4)
    Both tie!
    >>> game_decision(4,5)
    Player win!
    >>> game_decision(4,6)
    Computer win!
    >>> game_decision(5,0)
    Computer win!
    >>> game_decision(5,1)
    Player win!
    >>> game_decision(5,2)
    Computer win!
    >>> game_decision(5,3)
    Player win!
    >>> game_decision(5,4)
    Computer win!
    >>> game_decision(5,5)
    Both tie!
    >>> game_decision(5,6)
    Player win!
    >>> game_decision(6,0)
    Player win!
    >>> game_decision(6,1)
    Computer win!
    >>> game_decision(6,2)
    Player win!
    >>> game_decision(6,3)
    Computer win!
    >>> game_decision(6,4)
    Player win!
    >>> game_decision(6,5)
    Computer win!
    >>> game_decision(6,6)
    Both tie!
    >>> game_decision(7,0)
    Error: should not reach this if input is a valid one
    >>> game_decision(7,1)
    Error: should not reach this if input is a valid one
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
    com = choice[random.randint(0, 6)]
    print(f'Computer chooses {com}')
# convert string to number
    player = str_to_num(player)
    com = str_to_num(com)
# apply the rules of game, check and display winner
    game_decision(player, com)

if __name__ == '__main__':
    main()