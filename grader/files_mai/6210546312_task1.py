def check_valid_input(s):
    """ function which check that input have only rock , paper and scissors """
    if s == "rock" or s == "paper" or s == "scissors":
        return True
    else:
        return False

def convert_to_num(s):
    """ function that convert string to number
    >>> convert_to_num("scissors")
    2
    >>> convert_to_num("paper")
    1
    >>> convert_to_num("rock")
    0
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
    """ function that convert number to string
    >>> convert_to_string(0)
    'rock'
    >>> convert_to_string(1)
    'paper'
    >>> convert_to_string(2)
    'scissors'
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
    """ function that check which one is the winner
    >>> game_decision(1,1)
    Both ties!
    >>> game_decision(1,2)
    Player wins!
    >>> game_decision(2,1)
    Computer wins!
    """
    if player_choice_num == computer_choice_num:
        print('Both ties!')
    elif ((player_choice_num + 1) % 3) == computer_choice_num:
        print('Player wins!')
    else:
        print('Computer wins!')
    
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
if __name__ == '__main__':
    import doctest
    doctest.testmod()

# apply the rules of rock-paper-scissors
# rock-0 ; paper-1 ; scissors-2

# do this



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