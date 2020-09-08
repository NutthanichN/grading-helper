def check_valid_input(s):
    """
        >>> check_valid_input('rock')
        True
        >>> check_valid_input('paper')
        True
        >>> check_valid_input('scissors')
        True
        >>> check_valid_input("lizard")
        True
        >>> check_valid_input("spock")
        True
        >>> check_valid_input("gun")
        True
        >>> check_valid_input("zombie")
        True
        >>> check_valid_input('asjdh')
        False
        """
    if s == "rock":
        return True
    elif s == "paper":
        return True
    elif s == "scissors":
        return True
    elif s== "lizard":
        return True
    elif s=="spock":
        return True
    elif s=="gun":
        return True
    elif s=="zombie":
        return True
    else:
        return False
def convert_to_num(s):
    """
        >>> convert_to_num('rock')
        0
        >>> convert_to_num('gun')
        1
        >>> convert_to_num('spock')
        2
        >>> convert_to_num("paper")
        3
        >>> convert_to_num("lizard")
        4
        >>> convert_to_num("zombie")
        5
        >>> convert_to_num("scissors")
        6
        >>> convert_to_num('ashjdg')
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
    >>> convert_to_string(0)
    'rock'
    >>> convert_to_string(1)
    'gun'
    >>> convert_to_string(2)
    'spock'
    >>> convert_to_string(3)
    'paper'
    >>> convert_to_string(4)
    'lizard'
    >>> convert_to_string(5)
    'zombie'
    >>> convert_to_string(6)
    'scissors'
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
    elif n==5:
        return "zombie"
    elif n==6:
        return "scissors"
    else:
        print("Error: should not reach this if input is a valid one")
def game_decision(player_choice_num, computer_choice_num):
    """
    >>> game_decision(0,0)
    Both ties!
    >>> game_decision(0,1)
    Computer wins!
    >>> game_decision(0,2)
    Computer wins!
    >>> game_decision(0,3)
    Computer wins!
    >>> game_decision(0,4)
    Player wins!
    >>> game_decision(0,5)
    Player wins!
    >>> game_decision(0,6)
    Player wins!
    >>> game_decision(1,0)
    Player wins!
    >>> game_decision(1,1)
    Both ties!
    >>> game_decision(1,2)
    Computer wins!
    >>> game_decision(1,3)
    Computer wins!
    >>> game_decision(1,4)
    Computer wins!
    >>> game_decision(1,5)
    Player wins!
    >>> game_decision(1,6)
    Player wins!
    >>> game_decision(2,0)
    Player wins!
    >>> game_decision(2,1)
    Player wins!
    >>> game_decision(2,2)
    Both ties!
    >>> game_decision(2,3)
    Computer wins!
    >>> game_decision(2,4)
    Computer wins!
    >>> game_decision(2,5)
    Computer wins!
    >>> game_decision(2,6)
    Player wins!
    >>> game_decision(3,0)
    Player wins!
    >>> game_decision(3,1)
    Player wins!
    >>> game_decision(3,2)
    Player wins!
    >>> game_decision(3,3)
    Both ties!
    >>> game_decision(3,4)
    Computer wins!
    >>> game_decision(3,5)
    Computer wins!
    >>> game_decision(3,6)
    Computer wins!
    >>> game_decision(4,0)
    Computer wins!
    >>> game_decision(4,1)
    Player wins!
    >>> game_decision(4,2)
    Player wins!
    >>> game_decision(4,3)
    Player wins!
    >>> game_decision(4,4)
    Both ties!
    >>> game_decision(4,5)
    Computer wins!
    >>> game_decision(4,6)
    Computer wins!
    >>> game_decision(5,0)
    Computer wins!
    >>> game_decision(5,1)
    Computer wins!
    >>> game_decision(5,2)
    Player wins!
    >>> game_decision(5,3)
    Player wins!
    >>> game_decision(5,4)
    Player wins!
    >>> game_decision(5,5)
    Both ties!
    >>> game_decision(5,6)
    Computer wins!
    >>> game_decision(6,0)
    Computer wins!
    >>> game_decision(6,1)
    Computer wins!
    >>> game_decision(6,2)
    Computer wins!
    >>> game_decision(6,3)
    Player wins!
    >>> game_decision(6,4)
    Player wins!
    >>> game_decision(6,5)
    Player wins!
    >>> game_decision(6,6)
    Both ties!
    """
    if player_choice_num == computer_choice_num:
        print("Both ties!")
    elif ((player_choice_num + 1) % 7) == computer_choice_num or ((player_choice_num + 2) % 7) == computer_choice_num or ((player_choice_num + 3) % 7) == computer_choice_num:
        print("Computer wins!")
    else:
        print("Player wins!")

def main():
    while True:
        valid = False
        while valid == False:
            player_choice = input("Enter your choice: ").lower()

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
    doctest.testmod(verbose=True)
