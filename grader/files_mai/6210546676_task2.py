import random

def computer_check(n): 
    """
    >>> computer_check(0)
    Computer chooses: rock
    >>> computer_check(1)
    Computer chooses: paper
    >>> computer_check(2)
    Computer chooses: scissors
    >>> computer_check(3)
    Computer chooses: spock
    >>> computer_check(4)
    Computer chooses: lizard
    """
    List = ["rock", "paper", "scissors", "spock", "lizard"]
    for i in range(5):
        if n == i:
            print(f"Computer chooses: {List[i]}")

def player_check(n): 
    """
    >>> player_check("rock")
    0
    >>> player_check("paper")
    1
    >>> player_check("scissors")
    2
    >>> player_check("spock")
    3
    >>> player_check("lizard")
    4
    """
    List = ["rock", "paper", "scissors", "spock", "lizard"]
    for i in range(5):
        if n == List[i]:
            return i
    print("System Error!")
    SystemExit
        
def check_valid_input(v):
    if v == "rock":
        return True
    elif v == "paper":
        return True
    elif v == "scissors":
        return True
    elif v == "spock":
        return True
    elif v == "lizard":
        return True
    else:
        return False
    
def convert_to_num(v):
    if v == "rock":
        return 0
    elif v == "paper":
        return 1
    elif v == "scissors":
        return 2
    elif v == "spock":
        return 3
    elif v == "lizard":
        return 4
    else:
        print("Error: should not reach this if input is a valid one")
    
def convert_to_str(n):
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



def winner_check(player_choice_number, computer_choice_number): 
    """
    >>> winner_check(2,2)
    Both ties!
    >>> winner_check(3,1)
    Computer wins!
    >>> winner_check(4,1)
    Player wins!
    >>> winner_check(3,3)
    Both ties!
    """ 
    if player_choice_number == computer_choice_number:
        print("Both ties!")
    elif ((player_choice_number + 1) %5 ) == computer_choice_number or ((player_choice_number +3) %5 ) == computer_choice_number:
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
    computer_choice_number = random.randint(0,4)
    computer_choice = convert_to_str(computer_choice_number)
    player_choice_number = convert_to_num(player_choice)
    print("Player chooses ", player_choice) 
    print("Computer chooses ", computer_choice)
    winner_check(player_choice_number, computer_choice_number)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
