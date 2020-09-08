def check_valid_input(s):
    if s == "rock":
        return True
    elif s == "paper":
        return True
    elif s == "scissors":
        return True
    elif s == "lizard":
        return True
    elif s == "Spock":
        return True
    elif s == "zombie":
        return True
    elif s == "gun":
        return True
    else:
        return False

def convert_to_num(s):
    """
    change input to num
    >>> convert_to_num("rock")
    0
    >>> convert_to_num("gun")
    1
    >>> convert_to_num("spock")
    2
    >>> convert_to_num("paper")
    3
    >>> convert_to_num("lizard")
    4
    >>> convert_to_num("zombie")
    5
    >>> convert_to_num("scissors")
    6
    >>> convert_to_num("krub")
    Error: should not reach this if input is a valid one

    """
    if s == "rock":
        return 0
    elif s == "gun":
        return 1
    elif s == "spock":
        return 2
    elif s == "paper":
        return 3
    elif s == "lizard":
        return 4
    elif s == "zombie":
        return 5
    elif s == "scissors":
        return 6
    else:
        print("Error: should not reach this if input is a valid one")

def convert_to_string(n):
    """ 
    change num to string
    >>> convert_to_string(0)
    "rock"
    >>> convert_to_string(1)
    "gun"
    >>> convert_to_string(2)
    "spock"
    >>> convert_to_string(3)
    "paper"
    >>> convert_to_string(4)
    "lizard"
    >>> convert_to_string(5)
    "zombie"
    >>> convert_to_string(6)
    "scissors"
    >>> convert_to_string(7)
    Error: should not reach this if input is a valid one

    """
    if n == 0:
        return "rock"
    elif n == 1:
        return "gun"
    elif n == 2:
        return "spock"
    elif n == 3:
        return "paper"
    elif n == 4:
        return "lizard"
    elif n == 5:
        return "zombie"
    elif n == 6:
        return "scissors"
    else:
        print("Error: should not reach this if input is a valid one")

def game_decision(player_choice_num, computer_choice_num):
    """
    calculate the result
    >>> game_decision(5,1)
    Computer wins!
    >>> game_decision(6,4)
    Player wins!
    >>> game_decision(4,4)
    Both ties!
    """
    g = player_choice_num - computer_choice_num
    g = g % 7   
    if g == 0:
        print("Both ties!")
    elif g == 1 or g == 2 or g == 3:
        print("Player wins!")
    else:
        print("Computer wins!")

def main():
    valid = False
    while valid == False:
        player_choice = input("Enter your choice: ")
        valid = check_valid_input(player_choice)
        if valid == False:
            print("Invalid choice. Enter again.")

    import random
    computer_choice_num = random.randint(0, 6)
    computer_choice = convert_to_string(computer_choice_num)
    player_choice_num = convert_to_num(player_choice)
    print("Players chooses ", player_choice)
    print("Computer chooses ", computer_choice)
    game_decision(player_choice_num, computer_choice_num)

if __name__ == '__main__':
    import doctest
    doctest.testmod()