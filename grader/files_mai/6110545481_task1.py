import random

print("Let's play Rock Paper and Scissors!")
player_name = str(input("Please enter your name! \n: "))

print("Rock = 0, Paper = 1, Scissors = 2")
player_choice = int(input("What do you choose? : "))
computer =  random.randint(0,2)


def computer_choose(computer):
    """
    Print what computer choose
    >>> computer_choose(0)
    Computer choose : Rock
    >>> computer_choose(1)
    Computer choose : Paper
    >>> computer_choose(2)
    Computer choose : Scissor
    """
    if computer == 0:
        print("Computer choose : Rock")
    elif computer == 1:
        print("Computer choose : Paper")
    elif computer == 2:
        print("Computer choose : Scissor")



def compare(x, y):
    """
    Compare player's choice and computer
    >>>compare(2,1)
    You win!
    >>>compare(0,0)
    Both Tie!
    >>>compare(2,0)
    You lose!
    """
    if x == y:
        print("Both Tie!")
    elif (x+1)%3 == y:
        print("You Lose!")
    else:
        print("You Win!")

def main():
    computer_choose(computer)
    a = compare(player_choice,computer)

if __name__ == '__main__':
    main()