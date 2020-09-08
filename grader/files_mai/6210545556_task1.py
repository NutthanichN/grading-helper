def check_valid_input(s):
    if s == "rock":
        return True
    elif s == "paper":
        return True
    elif s == "scissors":
        return True
    else:
        return False

def convert_to_num(s):
    """ transfer a player answer which is string to integer
    >>> convert_to_num('rock')
    0
    >>> convert_to_num('paper')
    1
    """
    if s == "rock":
        return 0
    if s == "paper":
        return 1
    if s == "scissors":
        return 2
    else:
        print("Error : should not reach this if input is a valid one")

def convert_to_string(n):
    """ transfer a random computer answer which is integer to string
    >>> convert_to_string(0)
    'rock'
    >>> convert_to_string(1)
    'paper'
    """

    if n == 0:
        return "rock"
    elif n == 1:
        return "paper"
    elif n == 2:
        return "scissors"
    else:
        print("Error: should not reach this if input is a valid one")

def game_decision(player_choice_num,computer_choice_num):
    """ function which determine games result
    >>> game_decision(0,0)
    Both ties!
    >>> game_decision(1,0)
    Player wins!
    >>> game_decision(2,0)
    Computer wins!
    """
    if player_choice_num == computer_choice_num:
        print ("Both ties!")
    elif ((player_choice_num + 1) % 3) == computer_choice_num:
        print ("Computer wins!")
    else:
        print ("Player wins!")




def main():
    valid = False
    while valid == False:
        player_choice = input("Enter your choice: ")
        valid = check_valid_input(player_choice)
        if valid == False:
            print("Invalid choice, Enter again.")

    import random
    computer_choice_num = random.randint(0, 2)
    player_choice_num = convert_to_num(player_choice)
    print(f"Player chooses {player_choice}")
    print(f"Computer chooses {convert_to_string(computer_choice_num)}")
    game_decision(player_choice_num, computer_choice_num)

if __name__ == '__main__':
    import doctest
    doctest.testmod()