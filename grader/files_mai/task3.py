import random, sys


def computer_try(num):
    """Return a number that recieved from random.randint
    >>> computer_try(1)
    1
    >>> computer_try(2)
    2
    >>> computer_try(3)
    3
    >>> computer_try(4)
    4
    >>> computer_try(5)
    5
    >>> computer_try(6)
    6
    >>> computer_try(7)
    7
    """
    if num == 1:
        return num
    elif num == 2:
        return num
    elif num == 3:
        return num
    elif num == 4:
        return num
    elif num == 5:
        return num
    elif num == 6:
        return num
    elif num == 7:
        return num

def player_try(num_p):
    """Changing player str into int and return it
    >>> player_try("rock")
    1
    >>> player_try("paper")
    2
    >>> player_try("scissors")
    3
    >>> player_try("spock")
    4
    >>> player_try("zombie")
    5
    >>> player_try("gun")
    6
    >>> player_try("lizard")
    7
    """
    if num_p == "rock":
        return 1
    if num_p == "paper":
        return 2
    if num_p == "scissors":
        return 3
    if num_p == "spock":
        return 4
    if num_p == "zombie":
        return 5
    if num_p == "gun":
        return 6
    if num_p == "lizard":
        return 7


def com_str(num_c):
    """Changing computer int into str and return it
    >>> com_str(1)
    'rock'
    >>> com_str(2)
    'paper'
    >>> com_str(3)
    'scissors'
    >>> com_str(4)
    'spock'
    >>> com_str(5)
    'zombie'
    >>> com_str(6)
    'gun'
    >>> com_str(7)
    'lizard'
    """
    if num_c == 1:
        return "rock"
    if num_c == 2:
        return "paper"
    if num_c == 3:
        return "scissors"
    if num_c == 4:
        return "spock"
    if num_c == 5:
        return "zombie"
    if num_c == 6:
        return "gun"
    if num_c == 7:
        return "lizard"


def main() -> None:
    """Main program"""
    while True:
        choose = input("Player chooses ")
        choose.lower()
        if choose != "paper" and choose != "scissors" and choose != "rock" and choose != "spock" and choose != "zombie" and choose != "lizard" and choose != "gun":
            print("Invalid choice")
            sys.exit()
        com = random.randint(1,7)
        player = player_try(choose)
        computer = computer_try(com)
        com_change = com_str(computer)
        print(f"Computer chooses {com_change}")
        set1 = computer - player


        if set1 == 0:
            print("Both tie!")
        elif set1 > 0:
            if set1 % 2 == 0:
                print("Player wins!")
            elif set1 % 2 != 0:
                print("Computer wins!")
        elif set1 < 0:
            if set1 % 2 == 0:
                print("Computer wins!")
            elif set1 % 2 != 0:
                print("Player wins!")

if __name__ == '__main__':
    main()