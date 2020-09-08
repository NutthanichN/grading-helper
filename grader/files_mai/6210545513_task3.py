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


if __name__ == '__main__':
    import doctest

    doctest.testmod()
valid = False


def check_valid_input(s):
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

def check_convert_to_num():
    """ change a random answer which is string to number
    >> convert_to_num('gun')
    5
    >>> convert_to_num('spock')
    3
    >>> convert_to_num('paper')
    1
    >>> convert_to_num('lizard')
    6
    >> convert_to_num('rock')
    0
    >> convert_to_num('scissors')
    2
    >> convert_to_num('zombie')
    4
    """


def convert_to_num(s):
    if s == "rock":
        return 0
    elif s == "paper":
        return 1
    elif s == "scissors":
        return 2
    elif s == "spock":
        return 3
    elif s == "zombie":
        return 4
    elif s == "gun":
        return 5
    elif s == "lizard":
        return 6
    else:
        print("Error: should not reach this if input is a valid one")


def check_convert_to_string():
    """change number to string
    >>> convert_to_string(6)
    "lizard"
    >>> convert_to_string(1)
    "paper"
    >>> convert_to_string(4)
    "zombie"
    >>> convert_to_string(0)
    "rock"
    >>> convert_to_string(3)
    "spock"
    >>> convert_to_string(2)
    "scissors"
    """


def convert_to_string(n):
    if n == 0:
        return "rock"
    elif n == 1:
        return "paper"
    elif n == 2:
        return "scissors"
    elif n == 3:
        return "spock"
    elif n == 4:
        return "zombie"
    elif n == 5:
        return "gun"
    elif n == 6:
        return "lizard"
    else:
        print("Error: should not reach this if input is a valid one")



def check_game_dicision():
    """ function that decide the game result
    >>> game_decision(1,0)
    Player wins!
    >>> game_decision(6,6)
    Both ties!
    >>> game_decision(0,1)
    Computer wins!

    """


def game_decision(player_choice_num, computer_choice_num):
    if player_choice_num == computer_choice_num:
        print("Both ties!")
    elif ((player_choice_num + 1) % 7) == computer_choice_num or ((player_choice_num + 3) % 7) == computer_choice_num or ((player_choice_num + 5) % 7) == computer_choice_num:
        print("Computer wins!")
    else:
        print("Player wins!")


# get an input from a player and validate
valid = False
while valid == False:
    player_choice = input("Enter your choice: ")
    valid = check_valid_input(player_choice)
    if valid == False:
        print("Invalid choice. Enter again.")

# random a response from a computer and print out player and computer choices
import random

computer_choice_num = random.randint(0, 6)
computer_choice = convert_to_string(computer_choice_num)
player_choice_num = convert_to_num(player_choice)
print("Players chooses ", player_choice)
print("Computer chooses ", computer_choice)

# apply the rules of rock-paper-scissors
# rock-0 ; paper-1 ; scissors-2

# do this
game_decision(player_choice_num, computer_choice_num)

