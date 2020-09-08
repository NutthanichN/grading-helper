def check_valid_input(s):
    """ function which check that the input is True or False 
    >>> check_valid_input('spock')
    True
    >>> check_valid_input('dragon')
    False
    >>> check_valid_input('paper')
    True
    """

    if s == "rock":
        return True
    elif s == "paper":
        return True
    elif s == "scissors":
        return True
    elif s == "lizard":
        return True
    elif s == "spock":
        return True
    elif s == "zombie":
        return True
    elif s == "gun":
        return True
    else:
        return False


def convert_to_num(s):
    """ function which tranfer string to a number of choice 

    >>> convert_to_num("paper")
    2
    >>> convert_to_num("rock")
    0
    >>> convert_to_num("tiger")
    Error : should not reach this if input is a valid one

    """

    if s == "rock":
        return 0
    if s == "zombie":
        return 1
    if s == "paper":
        return 2
    if s == "gun":
        return 3
    if s == "scissors":
        return 4
    if s == "lizard":
        return 5
    if s == "spock":
        return 6
    else:
        print("Error : should not reach this if input is a valid one")


def convert_to_string(n):
    """ function which tranfer number of choice to string 

    >>> convert_to_string(0)
    'rock'
    >>> convert_to_string(3)
    'gun'
    >>> convert_to_string(10)
    Error: should not reach this if input is a valid one
    """

    if n == 0:
        return "rock"
    elif n == 1:
        return "zombie"
    elif n == 2:
        return "paper"
    elif n == 3:
        return "gun"
    elif n == 4:
        return "scissors"
    elif n == 5:
        return "lizard"
    elif n == 6:
        return "spock"
    else:
        print("Error: should not reach this if input is a valid one")


def game_decision(player_choice_num, computer_choice_num):
    """ function which get a choice from layer and computer then return the winner 

    >>> game_decision(0,0)
    Both ties!
    >>> game_decision(4,2)
    Player wins!
    >>> game_decision(5,4)
    Computer wins!

    """
    differ = (computer_choice_num-player_choice_num) % 7
    if differ == 6 or differ == 2 or differ == 3:
        print("Computer wins!")
    elif differ == 4 or differ == 5 or differ == 1:
        print("Player wins!")
    else:
        print("Both ties!")


def main():
    valid = False
    while valid == False:
        player_choice = input("Enter your choice: ")
        valid = check_valid_input(player_choice)
        if valid == False:
            print("Invalid choice. Enter again.")

    import random
    computer_choice_num = random.randint(0, 4)
    computer_choice = convert_to_string(computer_choice_num)
    player_choice_num = convert_to_num(player_choice)
    print("Players chooses ", player_choice)
    print("Computer chooses ", computer_choice)

    game_decision(player_choice_num, computer_choice_num)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
