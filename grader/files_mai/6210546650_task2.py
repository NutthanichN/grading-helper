# Chanathip Thumkanon
# 6210546650
import random

NUMOFSYM = 5


def check_valid_input(s):
    return convert_to_num(s) >= 0


def convert_to_num(s):
    if s == 'rock':
        return 0
    elif s == 'Spock':
        return 1
    elif s == 'paper':
        return 2
    elif s == 'lizard':
        return 3
    elif s == 'scissors':
        return 4
    return -1


def convert_to_string(n):
    if n == 0:
        return 'rock'
    elif n == 1:
        return 'Spock'
    elif n == 2:
        return 'paper'
    elif n == 3:
        return 'lizard'
    elif n == 4:
        return 'scissors'
    return 'Error'


def judgement(a,b):
    c = a-b
    if abs(c) > NUMOFSYM//2:
        return -c
    return c


def game_result(player_choice,computer_choice):
    """ 
    >>> game_result('rock','rock')
    Player chooses rock
    Computer chooses rock
    Both Tie!
    >>> game_result('rock','Spock')
    Player chooses rock
    Computer chooses Spock
    Computer wins!
    >>> game_result('rock','paper')
    Player chooses rock
    Computer chooses paper
    Computer wins!
    >>> game_result('rock','lizard')
    Player chooses rock
    Computer chooses lizard
    Player wins!
    >>> game_result('rock','scissors')
    Player chooses rock
    Computer chooses scissors
    Player wins!
    >>> game_result('Spock','rock')
    Player chooses Spock
    Computer chooses rock
    Player wins!
    >>> game_result('Spock','Spock')
    Player chooses Spock
    Computer chooses Spock
    Both Tie!
    >>> game_result('Spock','paper')
    Player chooses Spock
    Computer chooses paper
    Computer wins!
    >>> game_result('Spock','lizard')
    Player chooses Spock
    Computer chooses lizard
    Computer wins!
    >>> game_result('Spock','scissors')
    Player chooses Spock
    Computer chooses scissors
    Player wins!
    >>> game_result('paper','rock')
    Player chooses paper
    Computer chooses rock
    Player wins!
    >>> game_result('paper','Spock')
    Player chooses paper
    Computer chooses Spock
    Player wins!
    >>> game_result('paper','paper')
    Player chooses paper
    Computer chooses paper
    Both Tie!
    >>> game_result('paper','lizard')
    Player chooses paper
    Computer chooses lizard
    Computer wins!
    >>> game_result('paper','scissors')
    Player chooses paper
    Computer chooses scissors
    Computer wins!
    >>> game_result('lizard','rock')
    Player chooses lizard
    Computer chooses rock
    Computer wins!
    >>> game_result('lizard','Spock')
    Player chooses lizard
    Computer chooses Spock
    Player wins!
    >>> game_result('lizard','paper')
    Player chooses lizard
    Computer chooses paper
    Player wins!
    >>> game_result('lizard','lizard')
    Player chooses lizard
    Computer chooses lizard
    Both Tie!
    >>> game_result('lizard','scissors')
    Player chooses lizard
    Computer chooses scissors
    Computer wins!
    >>> game_result('scissors','rock')
    Player chooses scissors
    Computer chooses rock
    Computer wins!
    >>> game_result('scissors','Spock')
    Player chooses scissors
    Computer chooses Spock
    Computer wins!
    >>> game_result('scissors','paper')
    Player chooses scissors
    Computer chooses paper
    Player wins!
    >>> game_result('scissors','lizard')
    Player chooses scissors
    Computer chooses lizard
    Player wins!
    >>> game_result('scissors','scissors')
    Player chooses scissors
    Computer chooses scissors
    Both Tie!
    """
    computer_num = convert_to_num(computer_choice)
    player_num = convert_to_num(player_choice)
    print(f"Player chooses {player_choice}")
    print(f"Computer chooses {computer_choice}")
    c = judgement(player_num,computer_num)
    if c == 0:
        print("Both Tie!")
    elif c > 0:
        print("Player wins!")
    else:
        print("Computer wins!")


print("Rock, Paper, Scissors, Lizard, Spock Game")
while True:
    player_choice = input("Type 'quit' to exit or enter your choice: ")
    computer_num = random.randint(0,NUMOFSYM-1)
    computer_choice = convert_to_string(computer_num)
    if player_choice == 'quit':
        print("Program exits")
        break
    if not check_valid_input(player_choice):
        print("Invalid choice. Enter again.")
        continue
    game_result(player_choice,computer_choice)