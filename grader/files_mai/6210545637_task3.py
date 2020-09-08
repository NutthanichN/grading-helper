import random
# play=input("Player chooses ")
# b=["rock","scissors","paper","lizard","spock","gun","zombie"]
# com=random.choice(b)
# print(f"Computer chooses {com}")
# check(play,com)
def strtonum(str):
    """The job of this function is to change player choice and computer choice to number for calculate
    str = player choice and computer choice -->string input



    >>> strtonum("paper")
    2
    >>> strtonum("rock")
    3
    """

    if str == "scissors":
        return int(1)
    elif str == "paper":
        return int(2)
    elif str == "rock":
        return int(3)
    elif str == "lizard":
        return int(4)
    elif str == "gun":
        return int(5)
    elif str == "zombie":
        return int(6)
    else:
        return int(7)
def morethan7(num):
    """
    the job of this function is checking if the number that gets in is more than 7 or not

    >>> morethan7(8)
    1
    >>> morethan7(7)
    7



    """
    if num>7:
        return num%7
    else:
        return num
def check(play,com):

    """The job of this function is to check who will win or tie(player or computer)
    play = what player choose from rock,paper,scissors,spock,lizard,gun,zombie  -->string input
    com = what computer get from random in list b(rock,scissors,paper,lizard,spock,gun,zombie)
    we found a method to check who will win or tie by plus computer choice and player choice but first, we need to change
    the choice to the number then if player choice +1 or +3 or +5 = computer choice then player wins for example we set scissors = 1
    ,set paper = 2,set lizard = 4 and set zombie = 6 you can see that 1+1=2 , 1+3=4 and 1+5=6 and scissors win paper,lizard and zombie
    if the number is more than 7 then we make a function to Modular number to return the number that is smaller than 7 and next to this is how we check tie
    if the number of player choice = number of computer choice so it ties and if it other than this so it computer win

    Note:
    morethan7() is funtion to modular number that more than 7
    strtonum() is function to turn player or computer choice to number






    >>> check('paper','paper')
    Both tie!
    >>> check('spock','spock')
    Both tie!

    >>> check('rock','paper')
    Computer wins!
    >>> check("paper","rock")
    Player wins!
    >>> check("gun","zombie")
    Player wins!
    >>> check("lizard","gun")
    Player wins!
    >>> check("spock","gun")
    Player wins!
    >>> check("paper","gun")
    Player wins!
    >>> check("zombie","rock")
    Computer wins!

    """
    player = strtonum(play)
    computer = strtonum(com)
    if morethan7(player+1) == computer or morethan7(player+3) == computer or morethan7(player+5) == computer:
        print("Player wins!")
    elif player == computer:
        print("Both tie!")
    else:
        print("Computer wins!")


