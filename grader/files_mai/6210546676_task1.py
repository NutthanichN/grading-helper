import random
def computer_check(n): 
    """
    >>> computer_check(0)
    Computer chooses: scissors
    >>> computer_check(1)
    Computer chooses: paper
    >>> computer_check(2)
    Computer chooses: rock
    """
    List = ["scissors", "paper", "rock"]
    for i in range(3):
        if n == i:
            print(f"Computer chooses: {List[i]}")

def player_check(n): 
    """
    >>> player_check("scissors")
    0
    >>> player_check("paper")
    1
    >>> player_check("rock")
    2
    """
    List = ["scissors", "paper", "rock"]
    for i in range(3):
        if n == List[i]:
            return i
    print("System Error!")
    SystemExit
        
def check_valid_input(v):
    if v == "scissors":
        return True
    elif v == "paper":
        return True
    elif v == "rock":
        return True
    else:
        return False
    
def convert_to_number(v):
    if v == "scissors":
        return 0
    elif v == "paper":
        return 1
    elif v == "rock":
        return 2
    else:
        print("Error: should not reach this if input is a valid one")
    
def convert_to_str(n):
    if n == 0:
        return "scissors"
    elif n == 1:
        return "paper"
    elif n == 2:
        return "rock"
    else:
        print("Error: should not reach this if input is a valid one")
       


def winner_check(player_choice, computer_choice): 
    """
    >>> winner_check(0,0)
    Both ties!
    >>> winner_check(1,1)
    Both ties!
    >>> winner_check(2,2)
    Both ties!
    """ 
    if player_choice == computer_choice:
        print("Both ties!")
    elif ((convert_to_number(player_choice) + 1) %3 ) == convert_to_number(computer_choice):
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
    computer_choice_number = random.randint(0,2)
    computer_choice = convert_to_str(computer_choice_number)
    print("Player chooses ", player_choice) 
    print("Computer chooses ", computer_choice)
    winner_check(player_choice, computer_choice)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
