def check_valid_input(s):
    """
    *** DOCTESTS HERE ***
    >>> check_valid_input("rock")
    True
    >>> check_valid_input("paper")
    True
    >>> check_valid_input("scissors")
    True
    >>> check_valid_input("lizard")
    True
    >>> check_valid_input("spock")
    True
    >>> check_valid_input("god snape inwza 007")
    False
    """
    """*** CODE IS HERE ***"""
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
    """
    *** DOCTESTS HERE ***
    >>> convert_to_num("rock")
    0
    >>> convert_to_num("paper")
    1
    >>> convert_to_num("scissors")
    2
    >>> convert_to_num("spock")
    3
    >>> convert_to_num("lizard")
    4
    >>> convert_to_num("god snape inwza 007")
    Error: should not reach this if input is a valid one
    """
    """*** CODE IS HERE ***"""
    if s == "rock":
        return 0
    elif s == "lizard":
        return 4
    elif s == "spock":
        return 3
    elif s == "scissors":
        return 2
    elif s == "paper":
        return 1
    else:
        print("Error: should not reach this if input is a valid one")


def convert_to_string(n):
    """
    *** DOCTESTS HERE ***
    >>> convert_to_string(0)
    'rock'
    >>> convert_to_string(4)
    'lizard'
    >>> convert_to_string(3)
    'spock'
    >>> convert_to_string(2)
    'scissors'
    >>> convert_to_string(1)
    'paper'
    >>> convert_to_string(112)
    Error: should not reach this if input is a valid one
    """
    """*** CODE IS HERE ***"""
    if n == 0:
        return "rock"
    elif n == 4:
        return "lizard"
    elif n == 3:
        return "spock"
    elif n == 2:
        return "scissors"
    elif n == 1:
        return "paper"
    else:
        print("Error: should not reach this if input is a valid one")


def game_decision(player_choice_num, computer_choice_num):
    """
    *** DOCTESTS HERE ***
    let check it all!
    >>> game_decision(0,0)
    Both ties!
    >>> game_decision(0,1)
    Player wins!
    >>> game_decision(0,2)
    Computer wins!
    >>> game_decision(0,3)
    Player wins!
    >>> game_decision(0,4)
    Computer wins!

    >>> game_decision(1,0)
    Computer wins!
    >>> game_decision(1,1)
    Both ties!
    >>> game_decision(1,2)
    Player wins!
    >>> game_decision(1,3)
    Computer wins!
    >>> game_decision(1,4)
    Player wins!

    >>> game_decision(2,0)
    Player wins!
    >>> game_decision(2,1)
    Computer wins!
    >>> game_decision(2,2)
    Both ties!
    >>> game_decision(2,3)
    Player wins!
    >>> game_decision(2,4)
    Computer wins!

    >>> game_decision(3,0)
    Computer wins!
    >>> game_decision(3,1)
    Player wins!
    >>> game_decision(3,2)
    Computer wins!
    >>> game_decision(3,3)
    Both ties!
    >>> game_decision(3,4)
    Player wins!

    >>> game_decision(4,0)
    Player wins!
    >>> game_decision(4,1)
    Computer wins!
    >>> game_decision(4,2)
    Player wins!
    >>> game_decision(4,3)
    Computer wins!
    >>> game_decision(4,4)
    Both ties!
    """
    """*** CODE IS HERE ***"""
    if player_choice_num == computer_choice_num:
        print("Both ties!")
    elif ((player_choice_num + 1) % 5) != computer_choice_num and ((player_choice_num + 3) % 5) != computer_choice_num:
        print("Computer wins!")
    else:
        print("Player wins!")


# get an input from a player and validate



#######move from here to main for not runnnnnnnnnnn#####




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
...
"""
#######################  Remark for Understanding #############################
#####like when you draw multiply chart ex.3x.Their cycle is 3,6,9,2,5,8,1,4,7,0
#####Then sort it.
##### It's 5 charactors that mean 1 draw 2 loses and 2 wins ###################
#################                       player              ####################
#                                     /       \
#                                    /         \            2 clockwise = lose }  case of 5 charactor
#                                   /           \           2 counter =   win  }   case of 5 charactor
#################                 lose         win
#                                   \           /
#                                    \         /            3 clockwise = lose }  case of 7 charactor
#                                     \       /             3 counter   = win }  case of 7 charactor
#################                    win     lose           1 draw, number of lose= number of win





#####for now show in doctest terminal###############
def main() -> None:
    valid = False
    while valid == False:
        player_choice = input("Enter your choice: ")
        valid = check_valid_input(player_choice)
        if valid == False:
            print("Invalid choice. Enter again.")

    # random a response from a computer and print out player and computer choices
    import random

    computer_choice_num = random.randint(0, 4)
    computer_choice = convert_to_string(computer_choice_num)
    player_choice_num = convert_to_num(player_choice)
    print("Players chooses ", player_choice)
    print("Computer chooses ", computer_choice)

    # apply the rules of rock-lizard-spock-scissors-paper
    # rock-0 ; paper-1; scissors-2 ; spock-3 ; lizard-4 ;

    # do this
    game_decision(player_choice_num, computer_choice_num)
if __name__ == '__main__' :
    main()