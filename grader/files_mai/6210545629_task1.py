def check_valid_input(s):
    """
    *** DOCTESTS IS HERE ***
    >>> check_valid_input("rock")
    True
    >>> check_valid_input("paper")
    True
    >>> check_valid_input("scissors")
    True
    >>> check_valid_input("snape")
    False
    """
    """*** CODE IS HERE ***"""
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
    *** DOCTESTS IS HERE ***
    >>> convert_to_num("rock")
    0
    >>> convert_to_num("paper")
    1
    >>> convert_to_num("scissors")
    2
    >>> convert_to_num("snape")
    Error: should not reach this if input is a valid one
    """
    """*** CODE IS HERE ***"""
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
    *** DOCTESTS IS HERE ***
    >>> convert_to_string(0)
    'rock'
    >>> convert_to_string(1)
    'paper'
    >>> convert_to_string(2)
    'scissors'
    >>> convert_to_string(1150)
    Error: should not reach this if input is a valid one
    """
    """*** CODE IS HERE ***"""
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
    *** DOCTESTS IS HERE ***
    >>> game_decision(0,0)
    Both ties!
    >>> game_decision(0,1)
    Computer wins!
    >>> game_decision(0,2)
    Player wins!

    >>> game_decision(1,0)
    Player wins!
    >>> game_decision(1,1)
    Both ties!
    >>> game_decision(1,2)
    Computer wins!

    >>> game_decision(2,0)
    Computer wins!
    >>> game_decision(2,1)
    Player wins!
    >>> game_decision(2,2)
    Both ties!
    """
    """*** CODE IS HERE ***"""
    if player_choice_num == computer_choice_num:
        print("Both ties!")
    elif ((player_choice_num + 1) % 3) == computer_choice_num:
        print("Computer wins!")
    else:
        print("Player wins!")
    


# apply the rules of rock-paper-scissors
# rock-0 ; paper-1 ; scissors-2



# instead of this ugly if-elif-else nested block
"""
if player_choice_num == 0:
    if computer_choice_num == 0:
        print("Both ties!")
    elif computer_choice_num == 1:
        print("Computer wins!")
    else:
        print("Player wins!")
elif player_choice_num == 1:
    if computer_choice_num == 1:
        print("Both ties!")
    elif computer_choice_num == 2:
        print("Computer wins!")
    else:
        print("Player wins!")
else:
    if computer_choice_num == 2:
        print("Both ties!")
    elif computer_choice_num == 0:
        print("Computer wins!")
    else:
        print("Player wins!")
"""
def main() -> None:
    # get an input from a player and validate
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
    # do this
    game_decision(player_choice_num, computer_choice_num)
if __name__ == "__main__":
    main()