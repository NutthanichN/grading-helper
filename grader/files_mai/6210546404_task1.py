# def check_valid_input(s):
#     if s == "rock":
#         return True
#     elif s == "paper":
#         return True
#     elif s == "scissors":
#         return True
#     else:
#         return False

# def convert_to_num(s):
#     if s == "rock":
#         return 0
#     elif s == "paper":
#         return 1
#     elif s == "scissors":
#         return 2
#     else:
#         print("Error: should not reach this if input is a valid one")

# def convert_to_string(n):
#     if n == 0:
#         return "rock"
#     elif n == 1:
#         return "paper"
#     elif n == 2:
#         return "scissors"
#     else:
#         print("Error: should not reach this if input is a valid one")

# def game_decision(player_choice_num, computer_choice_num):
#     if player_choice_num == computer_choice_num:
#         print("Both ties!")
#     elif ((player_choice_num + 1) % 3) == computer_choice_num:
#         print("Computer wins!")
#     else:
#         print("Player wins!")
    
# # get an input from a player and validate
# valid = False
# while valid == False:
#     player_choice = input("Enter your choice: ")
#     valid = check_valid_input(player_choice)
#     if valid == False:
#         print("Invalid choice. Enter again.")

# # random a response from a computer and print out player and computer choices
# import random
# computer_choice_num = random.randint(0, 2)
# computer_choice = convert_to_string(computer_choice_num)
# player_choice_num = convert_to_num(player_choice)
# print("Players chooses ", player_choice)
# print("Computer chooses ", computer_choice)

# # apply the rules of rock-paper-scissors
# # rock-0 ; paper-1 ; scissors-2

# # do this
# game_decision(player_choice_num, computer_choice_num)

# # instead of this ugly if-elif-else nested block
# """
# if player_choice_num == 0:
#     if computer_choice_num == 0:
#         print("Both ties!")
#     elif computer_choice_num == 1:
#         print("Computer wins!")
#     else:
#         print("Player wins!")
# elif player_choice_num == 1:
#     if computer_choice_num == 1:
#         print("Both ties!")
#     elif computer_choice_num == 2:
#         print("Computer wins!")
#     else:
#         print("Player wins!")
# else:
#     if computer_choice_num == 2:
#         print("Both ties!")
#     elif computer_choice_num == 0:
#         print("Computer wins!")
#     else:
#         print("Player wins!")
# """

def check_valid_input(s):
    if s == "rock":
        return True
    elif s == "paper":
        return True
    elif s == "scissors":
        return True
    elif s == "lizard":
        return True
    elif s == "Spock":
        return True
    else:
        return False

def convert_to_num(s):
    """
    change input to num
    >>> convert_to_num("rock")
    0
    >>> convert_to_num("spock")
    1
    >>> convert_to_num("paper")
    2
    >>> convert_to_num("lizard")
    3
    >>> convert_to_num("scissors")
    4
    >>> convert_to_num("amorn")
    Error: should not reach this if input is a valid one
    """
    if s == "rock":
        return 0
    elif s == "spock":
        return 1
    elif s == "paper":
        return 2
    elif s == "lizard":
        return 3
    elif s == "scissors":
        return 4
    else:
        print("Error: should not reach this if input is a valid one")

def convert_to_string(n):
    """ 
    change num to string
    >>> convert_to_string(0)
    rock
    >>> convert_to_string(1)
    spock
    >>> convert_to_string(2)
    paper
    >>> convert_to_string(3)
    lizard
    >>> convert_to_string(4)
    scissors
    >>> convert_to_string(5)
    Error: should not reach this if input is a valid one
    """
    if n == 0:
        return "rock"
    elif n == 1:
        return "spock"
    elif n == 2:
        return "paper"
    elif n == 3:
        return "lizard"
    elif n == 4:
        return "scissors"
    else:
        print("Error: should not reach this if input is a valid one")

def game_decision(player_choice_num, computer_choice_num):
    """
    calculate the result
    >>> game_decision(0,1)
    Computer wins!
    >>> game_decision(2,1)
    Player wins!
    >>> game_decision(3,3)
    Both ties!
    """
    g = player_choice_num - computer_choice_num
    g = g % 5   
    if g == 0:
        print("Both ties!")
    elif g == 1 or g == 2:
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

    import random
    computer_choice_num = random.randint(0, 4)
    computer_choice = convert_to_string(computer_choice_num)
    player_choice_num = convert_to_num(player_choice)
    print("Players chooses ", player_choice)
    print("Computer chooses ", computer_choice)
    game_decision(player_choice_num, computer_choice_num)

# def check_valid_input(s):
#     if s == "rock":
#         return True
#     elif s == "paper":
#         return True
#     elif s == "scissors":
#         return True
#     elif s == "lizard":
#         return True
#     elif s == "Spock":
#         return True
#     elif s == "zombie":
#         return True
#     elif s == "gun":
#         return True
#     else:
#         return False

# def convert_to_num(s):
#     if s == "rock":
#         return 0
#     elif s == "gun":
#         return 1
#     elif s == "spock":
#         return 2
#     elif s == "paper":
#         return 3
#     elif s == "lizard":
#         return 4
#     elif s == "zombie":
#         return 5
#     elif s == "scissors":
#         return 6
#     else:
#         print("Error: should not reach this if input is a valid one")

# def convert_to_string(n):
#     if n == 0:
#         return "rock"
#     elif n == 1:
#         return "gun"
#     elif n == 2:
#         return "spock"
#     elif n == 3:
#         return "paper"
#     elif n == 4:
#         return "lizard"
#     elif n == 5:
#         return "zombie"
#     elif n == 6:
#         return "scissors"
#     else:
#         print("Error: should not reach this if input is a valid one")

# def game_decision(player_choice_num, computer_choice_num):
#     g = player_choice_num - computer_choice_num
#     g = g % 7   
#     if g == 0:
#         print("Both ties!")
#     elif g == 1 or g == 2 or g == 3:
#         print("Player wins!")
#     else:
#         print("Computer wins!")

# def main():
#     valid = False
#     while valid == False:
#         player_choice = input("Enter your choice: ")
#         valid = check_valid_input(player_choice)
#         if valid == False:
#             print("Invalid choice. Enter again.")

#     import random
#     computer_choice_num = random.randint(0, 6)
#     computer_choice = convert_to_string(computer_choice_num)
#     player_choice_num = convert_to_num(player_choice)
#     print("Players chooses ", player_choice)
#     print("Computer chooses ", computer_choice)
#     game_decision(player_choice_num, computer_choice_num)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# def check_valid_input(s):
#     """Check valid
#     >>> check_valid_input("rock")
#     True
#     >>> check_valid_input("paper")
#     True
#     >>> check_valid_input("scissors")
#     True
#     >>> check_valid_input("lizard")
#     True
#     >>> check_valid_input("spock")
#     True
#     >>> check_valid_input("dog")
#     False
#     """
#     if s == "rock":
#         return True
#     elif s == "paper":
#         return True
#     elif s == "scissors":
#         return True
#     elif s == "lizard":
#         return True
#     elif s == "Spock":
#         return True
#     else:
#         return False

# def convert_to_num(s):
#     """
#     change input to num
#     >>> convert_to_num("rock")
#     0
#     >>> convert_to_num("spock")
#     1
#     >>> convert_to_num("paper")
#     2
#     >>> convert_to_num("lizard")
#     3
#     >>> convert_to_num("scissors")
#     4
#     >>> convert_to_num("amorn")
#     Error: should not reach this if input is a valid one
#     """
#     if s == "rock":
#         return 0
#     elif s == "spock":
#         return 1
#     elif s == "paper":
#         return 2
#     elif s == "lizard":
#         return 3
#     elif s == "scissors":
#         return 4
#     else:
#         print("Error: should not reach this if input is a valid one")

# def convert_to_string(n):
#     """ 
#     change num to string
#     >>> convert_to_string(0)
#     rock
#     >>> convert_to_string(1)
#     spock
#     >>> convert_to_string(2)
#     paper
#     >>> convert_to_string(3)
#     lizard
#     >>> convert_to_string(4)
#     scissors
#     >>> convert_to_string(5)
#     Error: should not reach this if input is a valid one
#     """
#     if n == 0:
#         return "rock"
#     elif n == 1:
#         return "spock"
#     elif n == 2:
#         return "paper"
#     elif n == 3:
#         return "lizard"
#     elif n == 4:
#         return "scissors"
#     else:
#         print("Error: should not reach this if input is a valid one")

# def game_decision(player_choice_num, computer_choice_num):
#     """
#     calculate the result
#     >>> game_decision(0,1)
#     Computer wins!
#     >>> game_decision(2,1)
#     Player wins!
#     >>> game_decision(3,3)
#     Both ties!
#     """
#     g = player_choice_num - computer_choice_num
#     g = g % 5
#     if g == 0:
#         print("Both ties!")
#     elif g == 1 or g == 2:
#         print("Player wins!")
#     else:
#         print("Computer wins!")

# valid = False
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




