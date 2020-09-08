import random, sys


def computer_try(num):
    """Return a number that recieved from random.randint
    >>> computer_try(0)
    0
    >>> computer_try(1)
    1
    >>> computer_try(2)
    2
    >>> computer_try(3)
    3
    >>> computer_try(4)
    4
    """
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 3
    elif num == 4:
        return 4


def player_try(num_p):
    """Changing player str into int and return it
    >>> player_try("rock")
    0
    >>> player_try("paper")
    1
    >>> player_try("scissors")
    2
    >>> player_try("spock")
    3
    >>> player_try("lizard")
    4
    """
    if num_p == "rock":
        return 0
    if num_p == "paper":
        return 1
    if num_p == "scissors":
        return 2
    if num_p == "spock":
        return 3
    if num_p == "lizard":
        return 4


def com_str(num_c):
    """Changing computer int into str and return it
    >>> com_str(0)
    'rock'
    >>> com_str(1)
    'paper'
    >>> com_str(2)
    'scissors'
    >>> com_str(3)
    'spock'
    >>> com_str(4)
    'lizard'
    """
    if num_c == 0:
        return "rock"
    if num_c == 1:
        return "paper"
    if num_c == 2:
        return "scissors"
    if num_c == 3:
        return "spock"
    if num_c == 4:
        return "lizard"

def main() -> None:
    while True:
        choose = input("Player chooses ")
        choose.lower()
        if choose != "paper" and choose != "scissors" and choose != "rock" and choose != "spock" and choose != "lizard":
            print("Invalid choice")
            sys.exit()
        com = random.randint(0,4)
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
