import random, sys
num = 0

def computer(num):
    """Chaning int into str and return it
    >>> computer(1)
    'Computer choose rock'
    >>> computer(2)
    'Computer choose paper'
    >>> computer(3)
    'Computer choose scissors'
    """
    if num == 1:
        com = "Computer choose rock"
        return com
    elif num == 2:
        com = "Computer choose paper"
        return com
    elif num == 3:
        com = "Computer choose scissors"
        return com

def main() -> None:
    while True:
        choose = input("Player chooses ")
        com = random.randint(1,3)
        computer_try = computer(com)


        if choose == "rock" and computer_try == "Computer choose rock":
            print(computer_try)
            print("Both tie!")
        elif choose == "paper" and computer_try == "Computer choose paper":
            print(computer_try)
            print("Both tie!")
        elif choose == "scissors" and computer_try == "Computer choose scissors":
            print(computer_try)
            print("Both tie!")

        elif choose == "rock" and computer_try == "Computer choose scissors":
            print(computer_try)
            print("Player win!")
        elif choose == "paper" and computer_try == "Computer choose rock":
            print(computer_try)
            print("Player win!")
        elif choose == "scissors" and computer_try == "Computer choose paper":
            print(computer_try)
            print("Player win!")

        elif choose == "rock" and computer_try == "Computer choose paper":
            print(computer_try)
            print("Computer win!")
        elif choose == "paper" and computer_try == "Computer choose scissors":
            print(computer_try)
            print("Computer win!")
        elif choose == "scissors" and computer_try == "Computer choose rock":
            print(computer_try)
            print("Computer win!")

        else:
            print("Invalid choice")
            sys.exit()



if __name__ == '__main__':
    main()





