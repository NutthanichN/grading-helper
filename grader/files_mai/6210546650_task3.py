# Chanathip Thumkanon
# 6210546650
import random

NUMOFSYM = 7


def check_valid_input(s):
    return convert_to_num(s) >= 0


def convert_to_num(s):
    if s == 'rock':
        return 0
    elif s == 'gun':
        return 1
    elif s == 'Spock':
        return 2
    elif s == 'paper':
        return 3
    elif s == 'lizard':
        return 4
    elif s == 'zombie':
        return 5
    elif s == 'scissors':
        return 6
    return -1


def convert_to_string(n):
    if n == 0:
        return 'rock'
    elif n == 1:
        return 'gun'
    elif n == 2:
        return 'Spock'
    elif n == 3:
        return 'paper'
    elif n == 4:
        return 'lizard'
    elif n == 5:
        return 'zombie'
    elif n == 6:
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
    >>> game_result('rock','gun')
    Player chooses rock
    Computer chooses gun
    Computer wins!
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
    >>> game_result('rock','zombie')
    Player chooses rock
    Computer chooses zombie
    Player wins!
    >>> game_result('rock','scissors')
    Player chooses rock
    Computer chooses scissors
    Player wins!
    >>> game_result('gun','rock')
    Player chooses gun
    Computer chooses rock
    Player wins!
    >>> game_result('gun','gun')
    Player chooses gun
    Computer chooses gun
    Both Tie!
    >>> game_result('gun','Spock')
    Player chooses gun
    Computer chooses Spock
    Computer wins!
    >>> game_result('gun','paper')
    Player chooses gun
    Computer chooses paper
    Computer wins!
    >>> game_result('gun','lizard')
    Player chooses gun
    Computer chooses lizard
    Computer wins!
    >>> game_result('gun','zombie')
    Player chooses gun
    Computer chooses zombie
    Player wins!
    >>> game_result('gun','scissors')
    Player chooses gun
    Computer chooses scissors
    Player wins!
    >>> game_result('Spock','rock')
    Player chooses Spock
    Computer chooses rock
    Player wins!
    >>> game_result('Spock','gun')
    Player chooses Spock
    Computer chooses gun
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
    >>> game_result('Spock','zombie')
    Player chooses Spock
    Computer chooses zombie
    Computer wins!
    >>> game_result('Spock','scissors')
    Player chooses Spock
    Computer chooses scissors
    Player wins!
    >>> game_result('paper','rock')
    Player chooses paper
    Computer chooses rock
    Player wins!
    >>> game_result('paper','gun')
    Player chooses paper
    Computer chooses gun
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
    >>> game_result('paper','zombie')
    Player chooses paper
    Computer chooses zombie
    Computer wins!
    >>> game_result('paper','scissors')
    Player chooses paper
    Computer chooses scissors
    Computer wins!
    >>> game_result('lizard','rock')
    Player chooses lizard
    Computer chooses rock
    Computer wins!
    >>> game_result('lizard','gun')
    Player chooses lizard
    Computer chooses gun
    Player wins!
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
    >>> game_result('lizard','zombie')
    Player chooses lizard
    Computer chooses zombie
    Computer wins!
    >>> game_result('lizard','scissors')
    Player chooses lizard
    Computer chooses scissors
    Computer wins!
    >>> game_result('zombie','rock')
    Player chooses zombie
    Computer chooses rock
    Computer wins!
    >>> game_result('zombie','gun')
    Player chooses zombie
    Computer chooses gun
    Computer wins!
    >>> game_result('zombie','Spock')
    Player chooses zombie
    Computer chooses Spock
    Player wins!
    >>> game_result('zombie','paper')
    Player chooses zombie
    Computer chooses paper
    Player wins!
    >>> game_result('zombie','lizard')
    Player chooses zombie
    Computer chooses lizard
    Player wins!
    >>> game_result('zombie','zombie')
    Player chooses zombie
    Computer chooses zombie
    Both Tie!
    >>> game_result('zombie','scissors')
    Player chooses zombie
    Computer chooses scissors
    Computer wins!
    >>> game_result('scissors','rock')
    Player chooses scissors
    Computer chooses rock
    Computer wins!
    >>> game_result('scissors','gun')
    Player chooses scissors
    Computer chooses gun
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
    >>> game_result('scissors','zombie')
    Player chooses scissors
    Computer chooses zombie
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


print("Rock, Paper, Scissors, Lizard, Spock, Zombie, Gun Game")
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