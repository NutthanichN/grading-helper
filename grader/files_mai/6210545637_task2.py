import random
def rockpaperscissors(play,com):

    """The job of this function is to check who will  or tie(player or computer)
    play = what player choose from rock,paper,scissors,spock,lizard  -->string input
    com = what computer get from random in list b(rock,scissors,paper,lizard,spock)
    this function will compare what player choose and computer choose then show who will win or tie


    >>> rockpaperscissors('rock','rock')
    Both tie!
    >>> rockpaperscissors('paper','rock')
    Player wins!
    >>> rockpaperscissors("spock","lizard")
    Computer wins!
    >>> rockpaperscissors("rock","spock")
    Computer wins!
    """

    if play == com:
        print("Both tie!")
    elif (play=="rock" and (com == "scissors" or com == "lizard")) or (play=="scissors" and (com == "paper" or com == "lizard")) or (play=="paper" and (com == "rock" or com == "spock")) or (play == "spock" and (com == "rock" or com == "scissors")) or (play=="lizard" and (com=="paper" or com=="spock")):
        print("Player wins!")
    else:
        print("Computer wins!")
# play=input("Player chooses ")
# b=["rock","scissors","paper","lizard","spock"]
# com=random.choice(b)
# print(f"Computer chooses {com}")
# rockpaperscissors(play,com)