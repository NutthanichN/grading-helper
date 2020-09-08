import random

print("Let's play Rock Paper Scissors Lizard Spock Gun and Zombie!")
player_name = str(input("Please enter your name! \n: "))

print("Rock = 0, Paper = 1, Scissors = 2, Lizard = 3, Spock = 4, Gun = 5, Zombie = 6")
player_choice = int(input("What do you choose? : "))
computer = random.randint(0,6)

def computer_choose(computer):
    """
    Print what computer choose
    >>> computer_choose(0)
    Computer choose : Rock
    >>> computer_choose(1)
    Computer choose : Paper
    >>> computer_choose(6)
    Computer choose : Zombie
    """
    if computer == 0:
        print("Computer choose : Rock")
    elif computer == 1:
        print("Computer choose : Paper")
    elif computer == 2:
        print("Computer choose : Scissor")
    elif computer == 3:
        print("Computer choose : Paper")
    elif computer == 4:
        print("Computer choose : Lizard")
    elif computer == 5:
        print("Computer choose : Spock")
    elif computer == 6:
        print("Computer choose : Zombie")

def compare(x, y):
    """
    Compare player's choice and computer
    >>> compare(0, 1)
    You Lose!
    >>> compare(1, 4)
    You Win!
    >>> compare(4, 0)
    You Win!
    >>> compare(5, 0)
    You Win!
    >>> compare(6, 1)
    You Win!
    """
    if x == y:
        print("Both Tie!")
    elif x == 0 and (y == 1 or y == 4 or y == 5):
        print("You Lose!")
    elif x == 0 and (y == 2 or y == 3 or y == 6):
        print("You Win!")
    elif x == 1 and (y ==  2 or y == 3 or y == 6):
        print("You Lose!")
    elif x == 1 and (y == 0 or y == 4 or y == 5):
        print("You Win!")
    elif x == 2 and (y ==  0 or y == 4 or y == 5):
        print("You Lose!")
    elif x == 2 and (y == 1 or y == 3 or y == 6):
        print("You Win!")
    elif x == 3 and (y == 0 or y == 2 or y == 6):
        print("You Lose!")
    elif x == 3 and (y == 1 or y == 4 or y == 5):
        print("You Win!")
    elif x == 4 and (y == 1 or y == 3 or y == 6):
        print("You Lose!")
    elif x == 4 and (y == 0 or y == 2 or y == 5):
        print("You Win!")
    elif x == 5 and (y == 1 or y == 3 or y == 4):
        print("You Lose!")
    elif x == 5 and (y == 0 or y == 2 or y == 6) :
        print("You Win!")
    elif x == 6 and (y == 0 or y == 2 or y == 5) :
        print("You Lose!")
    elif x == 6 and (y == 1 or y == 3 or y == 4) :
        print("You Win!")

def main():
    computer_choose(computer)
    a = compare(player_choice,computer)

if __name__ == '__main__':
    main()