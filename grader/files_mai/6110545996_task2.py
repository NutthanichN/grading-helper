import random
def computer_display(n):
    """
    DOCTEST
    >>> computer_display(0)
    Computer chooses: rock
    >>> computer_display(1)
    Computer chooses: paper
    >>> computer_display(2)
    Computer chooses: scissors
    >>> computer_display(3)
    Computer chooses: spock
    >>> computer_display(4)
    Computer chooses: lizard
    """
    a = ["rock","paper","scissors","lizard","spock"]
    for i in range(5):
        if n==i:
            print(f"Computer chooses: {a[i]}")

def player_display(n):
    """
    >>> player_display("rock")
    0
    >>> player_display("scissors")
    2
    >>> player_display("paper")
    1
    >>> player_display("lizard")
    4
    >>> player_display("spock")
    3

    """
    l = ["rock","paper","scissors","lizard","spock"]
    for i in range(5):
        if n==l[i]:
            return i
    print(f"system error!")
    SystemExit
    
    
def check_valid_input(s):
    if s == "rock":
        return True
    elif s == "paper":
        return True
    elif s == "scissors":
        return True
    elif s == "spock":
        return True
    elif s == "lizard":
        return True
    else:
        return False

def convert_to_num(s):
    if s == "rock":
        return 0
    elif s == "paper":
        return 1
    elif s == "scissors":
        return 2
    elif s == "spock":
        return 3
    elif s == "lizard":
        return 4
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
        return "lizard"
    else:
        print("Error: should not reach this if input is a valid one")

def game_decision(player_choice_num, computer_choice_num):
    if player_choice_num == computer_choice_num:
        print("Both ties!")
    elif ((player_choice_num + 1) % 5) == computer_choice_num or ((player_choice_num+3)%5)==computer_choice_num:
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
    computer_choice_num = random.randint(0,4)
    computer_choice = convert_to_string(computer_choice_num)
    player_choice_num = convert_to_num(player_choice)
    print("Player chooses ", player_choice) 
    print("Computer chooses ", computer_choice)
    winner_checking(player_choice_num, computer_choice_num)

 
if __name__ == '__main__':
    import doctest
    doctest.testmod()





