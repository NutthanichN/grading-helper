def check_valid_input(s):
    """
    this function is used to check whether the input is valid or not

    >>> check_valid_input("rock")
    True
    >>> check_valid_input("paper")
    True
    >>> check_valid_input("potato")
    False
    
    """
    if s == "rock":
        return True
    elif s == "paper":
        return True
    elif s == "scissors":
        return True
    else:
        return False

def convert_to_num(s):
    """
    This function is used to convert the string input to number

    >>> convert_to_num("rock")
    0
    >>> convert_to_num("paper")
    1
    >>> convert_to_num("potato")
    Error: should not reach this if input is a valid one

    """

    if s == "rock":
        return 0
    elif s == "paper":
        return 1
    elif s == "scissors":
        return 2
    else:
        print("Error: should not reach this if input is a valid one")

def convert_to_string(n):
    """
    this function is used to convert the number input into a string

    >>> convert_to_string(0)
    'rock'
    >>> convert_to_string(1)
    'paper'
    >>> convert_to_string(4)
    Error: should not reach this if input is a valid one

    """

    if n == 0:
        return "rock"
    elif n == 1:
        return "paper"
    elif n == 2:
        return "scissors"
    else:
        print("Error: should not reach this if input is a valid one")

def game_decision(player_choice_num, computer_choice_num):
    """
    this function tells the rock-paper-scissors rule and decide who wins

    >>> game_decision(0,1)
    Computer wins!
    >>> game_decision(1,0)
    Player wins!
    >>> game_decision(0,0)
    Both ties!

    """
    if player_choice_num == computer_choice_num:
        print("Both ties!")
    elif ((player_choice_num + 1) % 3) == computer_choice_num:
        print("Computer wins!")
    else:
        print("Player wins!")
    
# get an input from a player and validate
def main():
    valid = False
    while valid == False:
        player_choice = input("Enter your choice: ")
        valid = check_valid_input(player_choice)
        if valid == False:
            print("Invalid choice. Enter again.")

# random a response from a computer and print out player and computer choices
    import random
    computer_choice_num = random.randint(0, 2)
    computer_choice = convert_to_string(computer_choice_num)
    player_choice_num = convert_to_num(player_choice)
    print("Players chooses ", player_choice)
    print("Computer chooses ", computer_choice)

# apply the rules of rock-paper-scissors
# rock-0 ; paper-1 ; scissors-2

# do this
    game_decision(player_choice_num, computer_choice_num)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

