
import sys
import random

def play_choice(n):
    """
        received the int from string_to_num and print out what player chose and return int to use in calculation who is won.


        >>> play_choice(0)
        Player chooses rock
        0
        >>> play_choice(1)
        Player chooses spock
        1
        >>> play_choice(3)
        Player chooses lizard
        3
        """
    if n == 0:
        print("Player chooses rock")
        return 0
    elif n==1:
        print("Player chooses spock")
        return 1
    elif n==2:
        print("Player chooses paper")
        return 2
    elif n == 3:
        print("Player chooses lizard")
        return 3
    elif n ==4:
        print("Player chooses scissors")
        return 4


def string_to_num(elp):
    """
    receive the input that player input from the start function and converts to a number to use in play_choice function.

    >>> string_to_num("paper")
    2
    >>> string_to_num("rock")
    0
    >>> string_to_num("scissors")
    4
    >>> string_to_num("rick")
    Error: Invalid input
    """

    if elp == "rock"or elp == "Rock":
        return 0
    elif elp == "spock" or elp == "Spock":
        return 1
    elif elp == "paper" or elp == "Paper" :
        return 2
    elif elp == "lizard" or elp == "Lizard":
        return 3
    elif elp == "scissors" or elp == "Scissors":
        return 4
    else:
        print("Error: Invalid input")
        sys.exit()


def com_choice(n):
    """
     received the int from computer random number variable and print out what computer chose and return int to use in calculation who is won.


    >>> com_choice(0)
    Computer chooses rock
    0
    >>> com_choice(2)
    Computer chooses paper
    2
    >>> com_choice(3)
    Computer chooses lizard
    3
    """
    if n == 0:
        print("Computer chooses rock")
        return 0
    elif n==1:
        print("Computer chooses spock")
        return 1
    elif n==2:
        print("Computer chooses paper")
        return 2
    elif n == 3:
        print("Computer chooses lizard")
        return 3
    elif n == 4:
        print("Computer chooses scissors")
        return 4



def game_decision(player_choice,computer_choice):
    """receive player_choice and computer choice and different number from choices to find the winner.
    if they both tie will return start() until we have the winner.
    >>> game_decision(1,3)
    Players wins !
    >>> game_decision(2,3)
    Computer wins !
    >>> game_decision(3,3)
    Both tie !
    """
    diff = ((player_choice - computer_choice) % 5)
    if player_choice == computer_choice:
        print("Both tie !")
        start()
    elif (diff == 1 or diff == 2):
        print("Computer wins!")
    elif (diff == 4 or diff == 3):
        print("Player wins!")

def start():
    """start the game and receives the input from user to use in other functions.
    create variable for computer choice by random number from 0-4.

    >>>start()
    Rock-Paper-Scissors-Lizard-Spock
    Enter your choice: Paper
    Player chooses paper
    Computer chooses spock
    Computer wins!
    >>> start()
    Rock-Paper-Scissors-Lizard-Spock
    Enter your choice: spock
    Player chooses spock
    Computer chooses spock
    Both tie !
    Rock-Paper-Scissors-Lizard-Spock
    Enter your choice: spock
    Player chooses spock
    Computer chooses spock
    Both tie !
    Rock-Paper-Scissors-Lizard-Spock
    Enter your choice: spock
    Player chooses spock
    Computer chooses spock
    Both tie !
    Rock-Paper-Scissors-Lizard-Spock
    Enter your choice: spock
    Player chooses spock
    Computer chooses paper
    Player wins!
    >>> start()
    Rock-Paper-Scissors-Lizard-Spock
    Enter your choice: Lizard
    Player chooses lizard
    Computer chooses spock
    Computer wins!
    """
    computer_ran = random.randint(0,4)
    print("Rock-Paper-Scissors-Lizard-Spock")
    keyword = str(input("Enter your choice: "))
    wth = string_to_num(keyword)
    nani = play_choice(wth)
    com_choice(computer_ran)
    game_decision(nani,computer_ran)

start()

