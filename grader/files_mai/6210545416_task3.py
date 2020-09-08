import random
def computer_checking(n): #Getting a number that was random by the random function.
    """
    DOCTEST
    >>> computer_checking(0)
    Computer chooses: rock
    >>> computer_checking(1)
    Computer chooses: paper
    >>> computer_checking(2)
    Computer chooses: scissors
    >>> computer_checking(3)
    Computer chooses: spock
    >>> computer_checking(4)
    Computer chooses: zombie
    >>> computer_checking(5)
    Computer chooses: gun
    >>> computer_checking(6)
    Computer chooses: lizard
    """
    List = ["rock", "paper", "scissors", "spock", "zombie", "gun", "lizard"]
    for i in range(7):
        if n == i:
            print(f"Computer chooses: {List[i]}")

def player_checking(n): #Getting the result from the user and return the associate number.
    """
    DOCTEST
    >>> player_checking("rock")
    0
    >>> player_checking("paper")
    1
    >>> player_checking("scissors")
    2
    >>> player_checking("spock")
    3
    >>> player_checking("zombie")
    4
    >>> player_checking("gun")
    5
    >>> player_checking("lizard")
    6
    """
    List = ["rock", "paper", "scissors", "spock", "zombie", "gun", "lizard"]
    for i in range(7):
        if n == List[i]:
            return i
    print("System Error!")
    SystemExit
        
def check_valid_input(t):
    if t == "rock":
        return True
    elif t == "paper":
        return True
    elif t == "scissors":
        return True
    elif t == "spock":
        return True
    elif t == "zombie":
        return True
    elif t == "gun":
        return True
    elif t == "lizard":
        return True
    else:
        return False
    
def convert_to_num(t):
    if t == "rock":
        return 0
    elif t == "paper":
        return 1
    elif t == "scissors":
        return 2
    elif t == "spock":
        return 3
    elif t == "zombie":
        return 4
    elif t == "gun":
        return 5
    elif t == "lizard":
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

def winner_checking(player_choice_num, computer_choice_num): #Getting the result from the user and check if the computer or the user won.
    """
    DOCTEST
    >>> winner_checking(0,2)
    Player wins!
    >>> winner_checking(1,1)
    Both ties!
    >>> winner_checking(2,2)
    Both ties!
    >>> winner_checking(3,3)
    Both ties!
    >>> winner_checking(3,1)
    Computer wins!
    >>> winner_checking(4,5)
    Computer wins!
    >>> winner_checking(5,5)
    Both ties!
    >>> winner_checking(6,3)
    Player wins!
    >>> winner_checking(6,4)
    Computer wins!
    >>> winner_checking(4,1)
    Player wins!
    >>> winner_checking(5,4)
    Player wins!
    >>> winner_checking(0,6)
    Player wins!
    """ 
    if player_choice_num == computer_choice_num:
        print("Both ties!")
    elif((player_choice_num + 1) %7 ) == computer_choice_num or ((player_choice_num +3) %7) == computer_choice_num or ((player_choice_num +5) %7) == computer_choice_num:
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
    computer_choice_num = random.randint(0,6)
    computer_choice = convert_to_string(computer_choice_num)
    player_choice_num = convert_to_num(player_choice)
    print("Player chooses ", player_choice) 
    print("Computer chooses ", computer_choice)
    winner_checking(player_choice_num, computer_choice_num)  

if __name__ == '__main__':
    import doctest
    doctest.testmod()


