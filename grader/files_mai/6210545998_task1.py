# import random
# list = ["rock","scissors","paper"]
# player = input("Play chooses: ")
# com = random.choice(list)
# print(f"Computer choose {com}")
def play(player, com):
    """
        >>> play('Scissors','Rock')
        Computer Wins!
        >>> play('Paper','Scissors')
        Computer Wins!
        >>> play('Paper','Paper')
        Both Tie!
        >>> play('Rock','Scissors')
        Player Wins!

    """
    if com == player:
        print("Both Tie!")
    if player == "Rock":
        if com == "Paper":
            print("Computer Wins!")
        if com == "Scissors":
            print("Player Wins!")
    if player == "Scissors":
        if com == "Rock":
            print("Computer Wins!")
        if com == "Paper":
            print("Player Wins!")
    if player == "Paper":
        if com == "Scissors":
            print("Computer Wins!")
        if com == "Rock":
            print("Player Wins!")
