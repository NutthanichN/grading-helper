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
    else:
        return False
def convert_to_num(s):
    """
    >>> convert_to_num('rock')
    0
    >>> convert_to_num('paper')
    2
    >>> convert_to_num('scissors')
    4
    >>> convert_to_num("lizard")
    3
    >>> convert_to_num("spock")
    1
    >>> convert_to_num('ashjdg')
    Error: should not reach this if input is a valid one
    """
    if s == "rock":
        return 0
    elif s == "spock":
        return 1
    elif s == "paper":
        return 2
    elif s == "lizard":
        return 3
    elif s == "scissors":
        return 4
    else:
        print("Error: should not reach this if input is a valid one")
def convert_to_string(n):
    """
    >>> convert_to_string(0)
    'rock'
    >>> convert_to_string(1)
    'spock'
    >>> convert_to_string(2)
    'paper'
    >>> convert_to_string(3)
    'lizard'
    >>> convert_to_string(4)
    'scissors'
    >>> convert_to_string(5)
    Error: should not reach this if input is a valid one
    """
    if n == 0:
        return "rock"
    elif n == 1:
        return "spock"
    elif n == 2:
        return "paper"
    elif n == 3:
        return "lizard"
    elif n == 4:
        return "scissors"
    else:
        print("Error: should not reach this if input is a valid one")
def game_decision(player_choice_num, computer_choice_num):
    """
    ##########
    0=rock
    1=spock
    2=paper
    3=lizard
    4=scissors
    ###########
    >>> game_decision(0,0)
    Both ties!
    >>> game_decision(0,1)
    Computer wins!
    >>> game_decision(0,2)
    Computer wins!
    >>> game_decision(0,3)
    Player wins!
    >>> game_decision(0,4)
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
    >>> game_decision(3,0)
    Computer wins!
    >>> game_decision(3,1)
    Player wins!
    >>> game_decision(3,2)
    Player wins!
    >>> game_decision(3,3)
    Both ties!
    >>> game_decision(3,4)
    Computer wins!
    >>> game_decision(4,0)
    Computer wins!
    >>> game_decision(4,1)
    Computer wins!
    >>> game_decision(4,2)
    Player wins!
    >>> game_decision(4,3)
    Player wins!
    >>> game_decision(4,4)
    Both ties!
    """
    if player_choice_num == computer_choice_num:
        print("Both ties!")
    elif ((player_choice_num + 1) % 5) == computer_choice_num or ((player_choice_num + 2) % 5) == computer_choice_num:
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
        computer_choice_num = random.randint(0, 4)
        computer_choice = convert_to_string(computer_choice_num)
        player_choice_num = convert_to_num(player_choice)
        print("Players chooses ", player_choice)
        print("Computer chooses ", computer_choice)
        game_decision(player_choice_num, computer_choice_num)
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)