import random
def check_input(n):
    """
    Determines if the text spelled incorrectly

    :param n: input text from player
    :type n: str
    :return: bool indicating if the text are spelled correctly

    >>>check_input("rock")
    True
    >>>check_input("555")
    False
    >>>check_input("paper")
    True
    >>>check_input("scissors")
    True
    >>>check_input("Rock")
    False
    """
    if n == "rock":
        return True
    elif n == "paper":
        return True
    elif n == "scissors":
        return True
    else:
        return False
def rule(play, com):
    """
    Determine results of rock-paper-scissors game and return it in terms of bool

    :param play: player's choice
    :param com: computer's choice
    :return: bool indicating results of the game

    >>>rule("rock", "scissors")
    True
    >>>rule("scissors", "paper")
    True
    >>>rule("rock", "paper")
    False
    >>>rule("scissors", "scissors")

    >>>rule("rock", "rock")

    """
    if play == "rock":
        if com == "paper":
            return False
        elif com == "scissors":
            return True
    elif play == "paper":
        if com == "rock":
            return True
        elif com == "scissors":
            return False
    elif play == "scissors":
        if com == "paper":
            return True
        elif com == "rock":
            return False

while True:
    my_list = ["rock", "paper", "scissors"]
    com = random.choice(my_list)
    player = input("""Player chooses """)
    print(" ")
    valid = check_input(player)
    if valid == False:
        print("Invalid choice. Enter again.")
        print(" ")
    else:
        print(f"Computer chooses {com}")
        print(" ")
        if rule(player, com) == True:
            print("Player wins!")
            print(" ")
        elif rule(player, com) == False:
            print("Computer wins!")
            print(" ")
        else:
            print("Both tie!")
            print(" ")


