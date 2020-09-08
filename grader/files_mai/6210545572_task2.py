if __name__ == "__main__":
    import doctest

    doctest.testmod()


def this_check_valid_input(t):
    """ this function will check that if the input is True or False """

    if t == "rock":
        return True
    elif t == "paper":
        return True
    elif t == "scissors":
        return True
    elif t == "lizard":
        return True
    elif t == "spock":
        return True
    else:
        return False


def this_convert_to_num(t):
    """ this function will convert string to a number of choices

    >>> this_convert_to_num("rock")
    0
    >>> this_convert_to_num("paper")
    1
    >>> this_convert_to_num("scissors")
    2
    >>> this_convert_to_num("spock")
    3

    """

    if t == "rock":
        return 0
    elif t == "paper":
        return 1
    elif t == "scissors":
        return 2
    elif t == "spock":
        return 3
    elif t == "lizard":
        return 4
    else:
        print("Error: should not reach this if input is a valid one")


def this_convert_to_string(x):
    """ this function will convert a number of choices to string

    >>> this_convert_to_string(0)
    'rock'
    >>> this_convert_to_string(1)
    'paper'
    >>> this_convert_to_string(2)
    'scissors'
    >>> this_convert_to_string(3)
    'spock'
    """

    if x == 0:
        return "rock"
    elif x == 1:
        return "paper"
    elif x == 2:
        return "scissors"
    elif x == 3:
        return "spock"
    elif x == 4:
        return "lizard"
    else:
        print("Error: should not reach this if input is a valid one")


def this_game_decision(playchoice, comchoice):
    """ this function will get a choices from playchoice and comchoice then it will return the winner!

    >>> this_game_decision(0,0)
    Both ties!
    >>> this_game_decision(0,2)
    Player wins!
    >>> this_game_decision(2,0)
    Computer wins!
    >>> game_decision(1,1)
    Both ties!
    >>> game_decision(4,4)
    Both ties!

    """
    if playchoice == comchoice:
        print("Both ties!")
    elif ((playchoice + 1) % 5) or ((playchoice + 3) % 5) == comchoice:
        print("Computer wins!")
    else:
        print("Player wins!")


def this_is_main():
    valid = False
    while valid == False:
        this_player_choice = input("Enter your choice: ")
        valid = this_check_valid_input(this_player_choice)
        if valid == False:
            print("Invalid choice. Enter again.")
    import random

    this_computer_choice_num = random.randint(0, 2)
    this_computer_choice = this_convert_to_string(this_computer_choice_num)
    this_player_choice_num = this_convert_to_num(this_player_choice)
    print("Players chooses: ", this_player_choice)
    print("Computer chooses: ", this_computer_choice)
    this_game_decision(this_player_choice_num, this_computer_choice_num)


valid = False
# while valid == False:
#     this_player_choice = input("Enter your choice: ")
#     valid = check_valid_input(this_player_choice)
#     if valid == False:
#         print("Invalid choice. Enter again.")
# import random

# this_computer_choice_num = random.randint(0, 4)
# this_computer_choice = this_convert_to_string(this_computer_choice_num)
# this_player_choice_num = this_convert_to_num(this_player_choice)
# print("Players chooses ", this_player_choice)
# print("Computer chooses ", this_computer_choice)
# this_game_decision(this_player_choice_num, this_computer_choice_num)


