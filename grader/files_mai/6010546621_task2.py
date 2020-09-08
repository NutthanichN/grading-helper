import random
def choose():
    """
    >>> Player chooses : lizard
    Computer chooses scissors
    Computer win!

    >>> Player chooses : paper
    Computer chooses Spock
    Player win!
    """
    com = ("rock","scissors","paper","Spock","lizard")
    P = input("Player chooses : ")
    PC = random.choice(com)
    print(f"Computer chooses {PC}")
    if  (P == "rock" and PC == "scissors"):
        print("Player win!")
    elif(P == "rock" and PC == "lizard"):
        print("Player win!")
    elif(P == "scissors" and PC == "paper"):
        print("Player win!")
    elif(P == "scissors" and PC == "lizard"):
        print("Player win!")
    elif(P == "paper" and PC == "rock"):
        print("Player win!")
    elif(P == "paper" and PC == "Spock"):
        print("Player win!")
    elif(P == "lizard" and PC == "paper"):
        print("Player win!")
    elif(P == "lizard" and PC == "Spock"):
        print("Player win!")
    elif(P == "Spock" and PC == "scissors"):
        print("Player win!")
    elif(P == "Spock" and PC == "rock"):
        print("Player win!")
#----------------------------------------------
    elif(P == "scissors" and PC == "rock"):
        print("Computer win!")
    elif(P == "scissors" and PC == "Spock"):
        print("Computer win!")
    elif(P == "lizard" and PC == "scissors"):
        print("Computer win!")
    elif(P == "paper" and PC == "scissors"):
        print("Computer win!")
    elif(P == "paper" and PC == "lizard"):
        print("Computer win!")
    elif(P == "Spock" and PC == "paper"):
        print("Computer win!")
    elif(P == "Spock" and PC == "lizard"):
        print("Computer win!")
    elif(P == "rock" and PC == "paper"):
        print("Computer win!")
    elif(P == "rock" and PC == "Spock"):
        print("Computer win!")
    elif(P == "lizard" and PC == "rock"):
        print("Computer win!")
#----------------------------------------------
    elif(P == "rock" and PC == "rock"):
        print("Both tie!")
    elif(P == "scissors" and PC == "scissors"):
        print("Both tie!")
    elif(P == "paper" and PC == "paper"):
        print("Both tie!")
    elif(P == "lizard" and PC == "lizard"):
        print("Both tie!")
    elif(P == "Spock" and PC == "Spock"):
        print("Both tie!")

    else:
        print("Invaild")
choose()