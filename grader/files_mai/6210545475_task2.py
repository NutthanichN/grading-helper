import random
def check_input(n):
    """
        Determines if the text spelled incorrectly

        :param n: input text from player
        :type n: str
        :return: bool indicating if the text are spelled correctly

        >>>check_input("spock")
        True
        >>>check_input("abc")
        False
        >>>check_input("lizard")
        True
        >>>check_input("paper")
        True
        >>>check_input("spook")
        False
        """
    if n == "rock":
        return True
    elif n == "paper":
        return True
    elif n == "scissors":
        return True
    elif n == "lizard":
        return True
    elif n == "spock":
        return True
    else:
        return False
def rule(play, com):
    """
        Determine results of rock-paper-scissors game and return it in terms of bool

        :param play: player's choice
        :param com: computer's choice
        :return: bool indicating results of the game

        >>>rule("spock", "scissors")
        True
        >>>rule("lizard", "paper")
        True
        >>>rule("rock", "paper")
        False
        >>>rule("spock", "lizard")
        False
        >>>rule("spock", "spock")

        """
    if play == "rock":
        if com == "paper":
            return False
        elif com == "spock":
            return False
        elif com == "scissors":
            return True
        elif com == "lizard":
            return True
    elif play == "paper":
        if com == "scissors":
            return False
        elif com == "lizard":
            return False
        elif com == "rock":
            return True
        elif com == "spock":
            return True
    elif play == "scissors":
        if com == "rock":
            return False
        elif com == "spock":
            return False
        elif com == "paper":
            return True
        elif com == "lizard":
            return True
    elif play == "lizard":
        if com == "rock":
            return False
        elif com == "spock":
            return False
        elif com == "paper":
            return True
        elif com == "scissors":
            return True
    elif play == "spock":
        if com == "lizard":
            return False
        elif com == "paper":
            return False
        elif com == "rock":
            return True
        elif com == "scissors":
            return True

while True:
    my_list = ["rock", "paper", "scissors", "lizard", "spock"]
    com = random.choice(my_list)
    player = input("""Player chooses """)
    print(" ")
    valid = check_input(player)
    if valid == False:
        print("Invalid choice. Enter again.")
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
