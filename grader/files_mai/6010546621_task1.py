import random
def choose():
    """
    >>> Player chooses : paper
    Computer chooses scissors
    Computer win!

    >>> Player chooses : rock
    Computer chooses rock
    Both tie!

    """
    com = ("rock","scissors","paper")
    P = input("Player chooses : ")
    PC = random.choice(com)
    print(f"Computer chooses {PC}")
    if  (P == "rock" and PC == "scissors"):
        print("Player win!")
    elif(P == "scissors" and PC == "paper"):
        print("Player win!")
    elif(P == "paper" and PC == "rock"):
        print("Player win!")
#----------------------------------------------
    elif(P == "scissors" and PC == "rock"):
        print("Computer win!")
    elif(P == "paper" and PC == "scissors"):
        print("Computer win!")
    elif(P == "rock" and PC == "paper"):
        print("Computer win!")
#----------------------------------------------
    elif(P == "rock" and PC == "rock"):
        print("Both tie!")
    elif(P == "scissors" and PC == "scissors"):
        print("Both tie!")
    elif(P == "paper" and PC == "paper"):
        print("Both tie!")

    else:
        print("Invaild")
choose()
