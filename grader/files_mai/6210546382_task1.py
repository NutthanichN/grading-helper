def check_valid_input(s):
    """ function which check that the input is True or False 
    >>> check_valid_input('rock')
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
    else:
        return False


def convert_to_num(s):
    """ function which tranfer string to a number of choice 

    >>> convert_to_num("paper")
    1
    >>> convert_to_num("rock")
    0
    >>> convert_to_num("tiger")
    Error: should not reach this if input is a valid one

    """

    if s == "rock":
        return 0
    elif s == "paper":
        return 1
    elif s == "scissors":
        return 2
    else:
        print("Error: should not reach this if input is a valid one")


def convert_to_string(n):
    """ function which tranfer number of choice to string 

    >>> convert_to_string(0)
    'rock'
    >>> convert_to_string(2)
    'scissors'
    >>> convert_to_string(20)
    Error: should not reach this if input is a valid one
    """

    if n == 0:
        return "rock"
    elif n == 1:
        return "paper"
    elif n == 2:
        return "scissors"
    else:
        print("Error: should not reach this if input is a valid one")


def game_decision(player_choice_num, computer_choice_num):
    """ function which get a choice from layer and computer then return the winner 

    >>> game_decision(3,3)
    Both ties!
    >>> game_decision(0,2)
    Player wins!
    >>> game_decision(2,0)
    Computer wins!

    """

    if player_choice_num == computer_choice_num:
        print("Both ties!")
    elif ((player_choice_num+1) % 3) == computer_choice_num:
        print("Computer wins!")
    else:
        print("Player wins!")


def main():
    valid = False
    while valid == False:
        player_choice = input("Enter your choice: ")
        valid = check_valid_input(player_choice)
        if valid == False:
            print("Invalid choice. Enter again.")

    import random
    computer_choice_num = random.randint(0, 2)
    computer_choice = convert_to_string(computer_choice_num)
    player_choice_num = convert_to_num(player_choice)
    print("Players chooses ", player_choice)
    print("Computer chooses ", computer_choice)

    game_decision(player_choice_num, computer_choice_num)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
