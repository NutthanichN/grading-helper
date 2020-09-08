def check_valid_input(s):
    if s == "scissors":
        return True
    elif s == "paper":
        return True
    elif s == "rock":
        return True
    elif s == "lizard":
        return True
    elif s == "gun":
        return True
    elif s == "zombie":
        return True
    elif s == "spock":
        return True
    else:
        return False

def convert_to_num(s):
    """ transfer a player answer which is string to integer
        >>> convert_to_num('rock')
        3
        >>> convert_to_num('paper')
        2
        >>> convert_to_num('scissors')
        1
        >>> convert_to_num('gun')
        5
        >>> convert_to_num('lizard')
        4
        >>> convert_to_num('spock')
        7
        >>> convert_to_num('zombie')
        6
    """
    if s == "scissors":
        return 1
    if s == "paper":
        return 2
    if s == "rock":
        return 3
    if s == "lizard":
        return 4
    if s == "gun":
        return 5
    if s == "zombie":
        return 6
    if s == "spock":
        return 7
    else:
        print("Error : should not reach this if input is a valid one")

def convert_to_string(n):
    """ transfer a random computer answer which is integer to string
        >>> convert_to_string(4)
        'lizard'
        >>> convert_to_string(7)
        'spock'
        >>> convert_to_string(3)
        'rock'
        >>> convert_to_string(1)
        'scissors'
        >>> convert_to_string(5)
        'gun'
        >>> convert_to_string(6)
        'zombie'
        >>> convert_to_string(2)
        'paper'
    """
    if n == 1:
        return "scissors"
    elif n == 2:
        return "paper"
    elif n == 3:
        return "rock"
    elif n == 4:
        return "lizard"
    elif n == 5:
        return "gun"
    elif n == 6:
        return "zombie"
    elif n == 7:
        return "spock"
    else:
        print("Error: should not reach this if input is a valid one")

def game_decision(player_choice_num,computer_choice_num):
    """ function which determine games result
        >>> game_decision(4,4)
        Both ties!
        >>> game_decision(4,5)
        Player wins!
        >>> game_decision(7,6)
        Computer wins!
        >>> game_decision(2,5)
        Player wins!
        >>> game_decision(5,2)
        Computer wins!
        >>> game_decision(6,7)
        Player wins!
        >>> game_decision(3,7)
        Computer wins!
    """
    if player_choice_num == computer_choice_num:
        print ("Both ties!")
    elif(computer_choice_num - player_choice_num)%2 == 0 or (computer_choice_num - player_choice_num) < 0 :
        print ("Computer wins!")
    elif(computer_choice_num - player_choice_num)%2 != 0:
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
