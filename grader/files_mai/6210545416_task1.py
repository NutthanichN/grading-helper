import random
def computer_checking(n): #Getting a number that was random by the random function.
    """
    DOCTEST
    >>> computer_checking(0)
    Computer chooses: scissors
    >>> computer_checking(1)
    Computer chooses: paper
    >>> computer_checking(2)
    Computer chooses: rock
    """
    List = ["scissors", "paper", "rock"]
    for i in range(3):
        if n == i:
            print(f"Computer chooses: {List[i]}")

def player_checking(n): #Getting the result from the user and return the associate number.
    """
    DOCTEST
    >>> player_checking("scissors")
    0
    >>> player_checking("paper")
    1
    >>> player_checking("rock")
    2
    """
    List = ["scissors", "paper", "rock"]
    for i in range(3):
        if n == List[i]:
            return i
    print("System Error!")
    SystemExit
        
def check_valid_input(t):
    if t == "scissors":
        return True
    elif t == "paper":
        return True
    elif t == "rock":
        return True
    else:
        return False
    
def convert_to_num(t):
    if t == "scissors":
        return 0
    elif t == "paper":
        return 1
    elif t == "rock":
        return 2
    else:
        print("Error: should not reach this if input is a valid one")
    
def convert_to_string(n):
    if n == 0:
        return "scissors"
    elif n == 1:
        return "paper"
    elif n == 2:
        return "rock"
    else:
        print("Error: should not reach this if input is a valid one")

def winner_checking(player_choice, computer_choice): #Getting the result from the user and check if the computer or the user won.
    """
    DOCTEST
    >>> winner_checking(0,0)
    Both ties!
    >>> winner_checking(1,1)
    Both ties!
    >>> winner_checking(2,2)
    Both ties!
    """ 
    if player_choice == computer_choice:
        print("Both ties!")
    elif ((convert_to_num(player_choice_num) + 1) %3 ) == convert_to_num(computer_choice_num):
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
    computer_choice_num = random.randint(0,2)
    computer_choice = convert_to_string(computer_choice_num)
    print("Player chooses ", player_choice) 
    print("Computer chooses ", computer_choice)
    winner_checking(player_choice, computer_choice)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
