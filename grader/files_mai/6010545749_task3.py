

import sys
import random

def play_choice(n):
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
    elif n == 5:
        print("Player chooses gun")
        return 5
    elif n == 6:
        print("Player chooses zombie")
        return 6


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
    elif elp == "gun" or elp =="Gun":
        return 5
    elif elp =="zombie" or elp =="Zombie":
        return 6
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
    elif n == 5:
        print("Computer chooses gun")
        return 5
    elif n == 6:
        print("Computer chooses zombie")
        return 6

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
    diff = ((player_choice - computer_choice) % 7)
    if player_choice == computer_choice:
        print("Both tie !")
        start()
    elif (diff == 1 or diff == 2 or diff == 6):
        print("Computer wins!")
    elif (diff == 4 or diff == 3 or diff ==5):
        print("Player wins!")

def start():
    """start the game and receives the input from user to use in other functions.
       create variable for computer choice by random number from 0-6.


    >>> start()
    Rock-Paper-Scissors-Lizard-Spock-Gun-Zombie
    Enter your choice: rock
    Player chooses rock
    Computer chooses rock
    Both tie !
    Rock-Paper-Scissors-Lizard-Spock-Gun-Zombie
    Enter your choice: rock
    Player chooses rock
    Computer chooses scissors
    Player wins!
    >>> start()
    Rock-Paper-Scissors-Lizard-Spock-Gun-Zombie
    Enter your choice: gun
    Player chooses gun
    Computer chooses gun
    Both tie !
    Rock-Paper-Scissors-Lizard-Spock-Gun-Zombie
    Enter your choice: gun
    Player chooses gun
    Computer chooses paper
    Player wins!
    >>> start()
    Rock-Paper-Scissors-Lizard-Spock-Gun-Zombie
    Enter your choice: zombie
    Player chooses zombie
    Computer chooses spock
    Player wins!




    """
    computer_ran = random.randint(0,6)
    print("Rock-Paper-Scissors-Lizard-Spock-Gun-Zombie")
    keyword = str(input("Enter your choice: "))
    wth = string_to_num(keyword)
    player_ops = play_choice(wth)
    com_choice(computer_ran)
    game_decision(player_ops,computer_ran)

start()

