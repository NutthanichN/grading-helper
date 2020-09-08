import random

def convert_to_num(player):
    """
    >>> convert_to_num("scissors")
    0
    >>> convert_to_num("rock")
    2
    >>> convert_to_num("paper")
    1
    >>> convert_to_num("lizard")
    3
    >>> convert_to_num("spock")
    4

    """
    if player == "scissors":
        return 0
    elif player == "paper":
        return 1
    elif player == "rock":
        return 2
    elif player == "lizard":
        return 3
    elif player == "spock":
        return 4
    else:
        print("Invalid input")

def convert_to_string(n):
    """
    >>> convert_to_string(0)
    'scissors'
    >>> convert_to_string(2)
    'rock'
    >>> convert_to_string(4)
    'spock'
    >>> convert_to_string(1)
    'paper'
    >>> convert_to_string(3)
    'lizard'

    """
    if n == 0:
        return "scissors"
    elif n == 1:
        return "paper"
    elif n == 2:
        return "rock"
    elif n == 3:
        return "lizard"
    elif n == 4:
        return "spock"
    else:
        print("Invalid input")


def game_decision(number,computer):
        """
        >>> game_decision(3,4)
        Player wins!
        >>> game_decision(2,3)
        Player wins!
        >>> game_decision(4,2)
        Player wins!
        >>> game_decision(4,1)
        Computer wins!
        >>> game_decision(0,2)
        Computer wins!

        """
        if computer == number:
            print("Both ties!")
        elif computer - number > 0:
            if (computer - number)%2 != 0:
                print("Player wins!")
            else:
                print("Computer wins!")
        elif computer - number < 0:
            if (number - computer)%2 != 0:
                print("Computer wins!")
            else:
                print("Player wins!")
        else:
            print("Invalid input")


def main():
    player = input("Enter your choice: ")
    computer = random.randint(0,4)

    print(f"Player chooses {player}")
    print(f"Computer chooses {convert_to_string(computer)}")

    number = convert_to_num(player)
    result = game_decision(number,computer)


