import doctest
import sys
import random

def play_choice(n):
    """
    received the int from string_to_num and print out what player chose and return int to use in calculation who is won.


    >>> play_choice(1)
    Player chooses rock
    1
    >>> play_choice(2)
    Player chooses paper
    2
    >>> play_choice(3)
    Player chooses scissors
    3
    """

    if n == 1:
        print("Player chooses rock")
        return 1
    elif n==2:
        print("Player chooses paper")
        return 2
    elif n==3:
        print("Player chooses scissors")
        return 3


def string_to_num(elp):
    """
    receive the input that player input from the start function and converts to a number to use in play_choice function.

    >>> string_to_num("paper")
    2
    >>> string_to_num("rock")
    1
    >>> string_to_num("scissors")
    3
    >>> string_to_num("rick")
    Error: Invalid input
    """

    if elp == "rock"or elp == "Rock":
        return 1
    elif elp == "paper" or elp == "Paper" :
        return 2
    elif elp == "scissors" or elp == "Scissors":
        return 3
    else:
        print("Error: Invalid input")
        sys.exit()


def com_choice(n):
    """
     received the int from computer random number variable and print out what computer chose and return int to use in calculation who is won.


    >>> com_choice(1)
    Computer chooses rock
    1
    >>> com_choice(2)
    Computer chooses paper
    2
    >>> com_choice(3)
    Computer chooses scissors
    3
    """
    if n == 1:
        print("Computer chooses rock")
        return 1
    elif n==2:
        print("Computer chooses paper")
        return 2
    elif n==3:
        print("Computer chooses scissors")
        return 3


def game_decision(player_choice,computer_choice):
    """receive player_choice and computer choice and if else case to if see who is won.
    if they both tie will return start() until we have the winner.
    >>> game_decision(1,3)
    Players wins !
    >>> game_decision(2,3)
    Computer wins !
    >>> game_decision(3,3)
    Both tie !




    """
    if player_choice == computer_choice:
         print("Both tie !")
         return start()

    elif player_choice == 1 and computer_choice == 2:
         print("Computer wins!")
    elif player_choice == 1 and computer_choice == 3:
        print("Players wins !")
    elif player_choice == 2 and computer_choice == 1:
        print("Players wins !")
    elif player_choice == 2 and computer_choice == 3:
        print("Computer wins !")
    elif player_choice == 3 and computer_choice == 1:
        print("Computer wins !")
    elif player_choice == 3 and computer_choice == 2:
        print("Players wins !")

def start():
    """start the game and receives the input from user to use in other functions.
    create variable for computer choice by random number from 1-3.

    >>>start()
    Rock-Paper-Scissors
    Enter your choice:
    Player chooses rock
    Computer chooses paper
    Computer wins!

    >>> start()
    Rock-Paper-Scissors
    Enter your choice: paper
    Player chooses paper
    Computer chooses scissors
    Computer wins !

    >>> start()
    Rock-Paper-Scissors
    Enter your choice: Scissors
    Player chooses scissors
    Computer chooses scissors
    Both tie !
    Rock-Paper-Scissors
    Enter your choice: rock
    Player chooses rock
    Computer chooses scissors
    Players wins !

    """

    computer_ran = random.randint(1, 3)
    print("Rock-Paper-Scissors")
    keyword = str(input("Enter your choice: "))
    wth = string_to_num(keyword)
    nani = play_choice(wth)
    com_choice(computer_ran)
    game_decision(nani, computer_ran)

start()
