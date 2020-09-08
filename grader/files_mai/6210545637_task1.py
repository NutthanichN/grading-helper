import random
# play=input("Player chooses ")
# b=["rock","scissors","paper"]
# com=random.choice(b)
# print(f"Computer chooses {com}")
def check(play,com):


    """The job of this function is to check who will  or tie(player or computer)
    play = what player choose from rock,paper,scissors -->string input
    com= what computer get from random in list b(rock,scissors,paper)
    this function will compare what player choose and computer choose then show who will win or tie



    >>> check('rock','rock')
    Both tie!
    >>> check("rock","paper")
    Computer wins!
    >>> check("paper","rock")
    Player wins!
    >>> check("scissors","paper")
    Player wins!
    """

    if play == com:
        print("Both tie!")
    elif (play=="rock" and com == "scissors") or (play=="scissors" and com == "paper") or (play=="paper" and com == "rock"):
        print("Player wins!")
    else:
        print("Computer wins!")