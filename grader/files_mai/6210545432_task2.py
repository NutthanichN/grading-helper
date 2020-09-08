def check_valid_input(s):
    """ function to check that the input is True or False """
    if s == "rock":
        return True
    elif s == "paper":
        return True
    elif s == "scissors":
        return True
    elif s== "lizard":
        return True
    elif s== "spock":
        return True
    else:
        return False

def convert_to_num(s):
    """ function to convert string to a number of choice 
    
    >>> convert_to_num("lizard")
    4
    >>> convert_to_num("scissors")
    2
    """
    if s == "rock":
        return 0
    elif s == "paper":
        return 1
    elif s == "scissors":
        return 2
    elif s == "spock":
        return 3
    elif s == "lizard":
        return 4
    else:
        print("Error: should not reach this if input is a valid one")

def convert_to_string(n):
    """ function to convert number of choice to string 
    
    >>> convert_to_string(4)
    'lizard'
    >>> convert_to_string(0)
    'rock'
    
    """
    if n == 0:
        return "rock"
    elif n == 1:
        return "paper"
    elif n == 2:
        return "scissors"
    elif n == 3:
        return "spock"
    elif n == 4:
        return "lizard"
    else:
        print("Error: should not reach this if input is a valid one")

def game_decision(playerchoice, computerchoice):
    """ function to get a choice from playerchoice and computerchoice then return the winner 
    
    >>> game_decision(2,2)
    Both ties!
    >>> game_decision(1,1)
    Both ties!
    >>> game_decision(4,4)
    Both ties!
    >>> game_decision(3,3)
    Both ties!
    >>> game_decision(0,0)
    Both ties!
    """
    if playerchoice == computerchoice:
        print("Both ties!")
    elif ((playerchoice + 1) % 5)  or ((playerchoice + 3)%5) == computerchoice:
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
# while valid == False:
#     player_choice = input("Enter your choice: ")
#     valid = check_valid_input(player_choice)
#     if valid == False:
#         print("Invalid choice. Enter again.")
# import random
# computer_choice_num = random.randint(0, 4)
# computer_choice = convert_to_string(computer_choice_num)
# player_choice_num = convert_to_num(player_choice)
# print("Players chooses ", player_choice)
# print("Computer chooses ", computer_choice)
# game_decision(player_choice_num, computer_choice_num)