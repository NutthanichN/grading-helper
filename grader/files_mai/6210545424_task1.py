import random

def convert_to_num(player):
    """
    >>> convert_to_num("scissors")
    0
    >>> convert_to_num("rock")
    2
    >>> convert_to_num("paper")
    1

    """
    if player == "scissors":
        return 0
    elif player == "paper":
        return 1
    elif player == "rock":
        return 2
    else:
        print("Invalid input")

def convert_to_string(n):
    """
    >>> convert_to_string(0)
    'scissors'
    >>> convert_to_string(1)
    'paper'
    >>> convert_to_string(2)
    'rock'

    """
    if n == 0:
        return "scissors"
    elif n == 1:
        return "paper"
    elif n == 2:
        return "rock"
    else:
        print("Invalid input")

def game_decision(number,computer):
        """
        >>> game_decision(0,0)
        Both ties!
        >>> game_decision(1,0)
        Computer wins!
        >>> game_decision(1,2)
        Player wins!
        >>> game_decision(2,1)
        Computer wins!
        >>> game_decision(0,1)
        Player wins!

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
    computer = random.randint(0,2)

    print(f"Player chooses {player}")
    print(f"Computer chooses {convert_to_string(computer)}")

    number = convert_to_num(player)
    result = game_decision(number,computer)

