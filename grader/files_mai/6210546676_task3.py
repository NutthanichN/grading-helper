import random
def compu_check(n): 
    """
    >>> compu_check(0)
    Computer chooses: rock
    >>> compu_check(1)
    Computer chooses: paper
    >>> compu_check(2)
    Computer chooses: scissors
    >>> compu_check(3)
    Computer chooses: spock
    >>> compu_check(4)
    Computer chooses: zombie
    >>> compu_check(5)
    Computer chooses: gun
    >>> compu_check(6)
    Computer chooses: lizard
    """
    List = ["rock", "paper", "scissors", "spock", "zombie", "gun", "lizard"]
    for i in range(7):
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
    >>> player_check("zombie")
    4
    >>> player_check("gun")
    5
    >>> player_check("lizard")
    6
    """
    List = ["rock", "paper", "scissors", "spock", "zombie", "gun", "lizard"]
    for i in range(7):
        if n == List[i]:
            return i
    print("System Error!")
    SystemExit

def convert_to_num(v):
    if v   == "rock":
        return 0
    elif v == "paper":
        return 1
    elif v == "scissors":
        return 2
    elif v == "spock":
        return 3
    elif v == "zombie":
        return 4
    elif v == "gun":
        return 5
    elif v == "lizard":
        return 6
    else:
        print("Error: should not reach this if input is a valid one")
    
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


def check_valid_input(v):
    if  v == "rock":
        return True
    elif v == "paper":
        return True
    elif v == "scissors":
        return True
    elif v == "spock":
        return True
    elif v == "zombie":
        return True
    elif v == "gun":
        return True
    elif v == "lizard":
        return True
    else:
        return False
    

def winner_check(player_choice_number, computer_choice_number): 
    """
    >>> winner_check(2,1)
    Player wins!
    >>> winner_check(1,3)
    Player wins!
    >>> winner_check(4,5)
    Computer wins!
    >>> winner_check(4,4)
    Both ties!
    >>> winner_check(6,3)
    Player wins!
    """ 
    if player_choice_number == computer_choice_number:
        print("Both ties!")
    elif((player_choice_number + 1) %7 ) == computer_choice_number or ((player_choice_number +3) %7) == computer_choice_number or ((player_choice_number +5) %7) == computer_choice_number:
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
    computer_choice_number = random.randint(0,6)
    computer_choice = convert_to_string(computer_choice_number)
    player_choice_number = convert_to_num(player_choice)
    print("Player chooses ", player_choice) 
    print("Computer chooses ", computer_choice)
    winner_check(player_choice_number, computer_choice_number)  

if __name__ == '__main__':
    import doctest
    doctest.testmod()


