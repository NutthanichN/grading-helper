def check_valid_input(s):
    """ function which check that the input is True or False """
    
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
    else:
        return False

def convert_to_num(s):
    """ function which tranfer string to a number of choice 
    
    >>> convert_to_num("paper")
    2
    >>> convert_to_num("rock")
    0
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
    """ function which tranfer number of choice to string 
    
    >>> convert_to_string(0)
    'rock'
    >>> convert_to_string(3)
    'lizard'
    
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

def game_decision(player, com):
    """ function which get a choice from layer and computer then return the winner 
    
    >>> game_decision(0,0)
    Both tie!
    >>> game_decision(0,4)
    Player wins!
    >>> game_decision(1,2)
    Computer wins!
    
    """
    d=(com - player)%5
    if d == 1 or d == 2:
       print("Computer wins!")
    elif d == 3 or d == 4:
       print("Player wins!")
    elif d == 0:
       print("Both tie!")

    

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

