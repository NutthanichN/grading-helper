from typing import Union, Iterable, Optional

DOCTEST_PREPEND = '>>> '


def write_doctest(func_name: str, output: str, *args,
                  sep=', ', kwargs: Optional[str] = None) -> None:
    """Write a doctest test case.

    :param func_name:
    :param output:
    :param sep:
    :param args: arguments of the function to be called
    :param kwargs: keyqord arguments of the function toi be called
    :return:
    """
    print(DOCTEST_PREPEND + func_name + '(' + sep.join(args) + ((', ' + kwargs) if kwargs else '') + ')')
    print(output)
    print(' ...')
    pass


# correct
P1_WIN = "Player wins!"
P2_WIN = "Computer wins!"
DRAW = "Both ties!"

# P1_WIN = "Player wins!"
# P2_WIN = "Com wins!"
# DRAW = "Both ties!"

# P1_WIN = "PLAYER WIN !"
# P2_WIN = "COMPUTER WIN !"
# DRAW = "BOTH TIE !"

# P1_WIN = "Yeah!, I found John Conner."
# P2_WIN = "Oh no!, This is Skynet?!!"
# DRAW = "Both Ties!!!"

# P1_WIN = "True"
# P2_WIN = "False"
# DRAW = ""

# P1_WIN = "PLAYER WIN !"
# P2_WIN = "COMPUTER WIN !"
# DRAW = "BOTH TIE !"

# P1_WIN = "'Player wins!'"
# P2_WIN = "'Computer wins!'"
# DRAW = "'Both ties!'"

# P1_WIN = "'w'"
# P2_WIN = "'l'"
# DRAW = "'t'"

# SCISSORS = "'Scissors'"
# PAPER = "'Paper'"
# ROCK = "'Rock'"
# LIZARD = "'Lizard'"
# GUN = "'Gun'"
# ZOMBIE = "'Zombie'"
# SPOCK = "'Spock'"

# SCISSORS = "'scissors'"
# PAPER = "'paper'"
# ROCK = "'rock'"
# LIZARD = "'lizard'"
# GUN = "'gun'"
# ZOMBIE = "'zombie'"
# SPOCK = "'Spock'"

SCISSORS = 2
PAPER = 1
ROCK = 0
LIZARD = 6
GUN = 5
ZOMBIE = 4
SPOCK = 3

FUNC_NAME = 'game_decision'

FUNC_NAME = 'check'
# 'play', 'rule', 'winner_checking', 'check', 'result', 'competition', 'game_operation', 'game_result

TASK = 3
SWAP = False

SCISSORS = str(SCISSORS)
PAPER = str(PAPER)
ROCK = str(ROCK)
LIZARD = str(LIZARD)
GUN = str(GUN)
ZOMBIE = str(ZOMBIE)
SPOCK = str(SPOCK)


def write_doctest_lab4_task3(swap=False):
    """Print doctest for lab4 task3"""
    if swap:
        p1_win, p2_win = P2_WIN, P1_WIN
    else:
        p1_win, p2_win = P1_WIN, P2_WIN
    write_doctest(FUNC_NAME, p1_win, SCISSORS, PAPER)
    write_doctest(FUNC_NAME, p2_win, SCISSORS, ROCK)
    write_doctest(FUNC_NAME, p1_win, SCISSORS, LIZARD)
    write_doctest(FUNC_NAME, p2_win, SCISSORS, GUN)
    write_doctest(FUNC_NAME, p1_win, SCISSORS, ZOMBIE)
    write_doctest(FUNC_NAME, p2_win, SCISSORS, SPOCK)
    write_doctest(FUNC_NAME, p1_win, PAPER, ROCK)
    write_doctest(FUNC_NAME, p2_win, PAPER, LIZARD)
    write_doctest(FUNC_NAME, p1_win, PAPER, GUN)
    write_doctest(FUNC_NAME, p2_win, PAPER, ZOMBIE)
    write_doctest(FUNC_NAME, p1_win, PAPER, SPOCK)
    write_doctest(FUNC_NAME, p1_win, ROCK, LIZARD)
    write_doctest(FUNC_NAME, p2_win, ROCK, GUN)
    write_doctest(FUNC_NAME, p1_win, ROCK, ZOMBIE)
    write_doctest(FUNC_NAME, p2_win, ROCK, SPOCK)
    write_doctest(FUNC_NAME, p1_win, LIZARD, GUN)
    write_doctest(FUNC_NAME, p2_win, LIZARD, ZOMBIE)
    write_doctest(FUNC_NAME, p1_win, LIZARD, SPOCK)
    write_doctest(FUNC_NAME, p1_win, GUN, ZOMBIE)
    write_doctest(FUNC_NAME, p2_win, GUN, SPOCK)
    write_doctest(FUNC_NAME, p1_win, ZOMBIE, SPOCK)

    write_doctest(FUNC_NAME, p2_win, PAPER, SCISSORS)
    write_doctest(FUNC_NAME, p1_win, ROCK, SCISSORS)
    write_doctest(FUNC_NAME, p2_win, LIZARD, SCISSORS)
    write_doctest(FUNC_NAME, p1_win, GUN, SCISSORS)
    write_doctest(FUNC_NAME, p2_win, ZOMBIE, SCISSORS)
    write_doctest(FUNC_NAME, p1_win, SPOCK, SCISSORS)
    write_doctest(FUNC_NAME, p2_win, ROCK, PAPER)
    write_doctest(FUNC_NAME, p1_win, LIZARD, PAPER)
    write_doctest(FUNC_NAME, p2_win, GUN, PAPER)
    write_doctest(FUNC_NAME, p1_win, ZOMBIE, PAPER)
    write_doctest(FUNC_NAME, p2_win, SPOCK, PAPER)
    write_doctest(FUNC_NAME, p2_win, LIZARD, ROCK)
    write_doctest(FUNC_NAME, p1_win, GUN, ROCK)
    write_doctest(FUNC_NAME, p2_win, ZOMBIE, ROCK)
    write_doctest(FUNC_NAME, p1_win, SPOCK, ROCK)
    write_doctest(FUNC_NAME, p2_win, GUN, LIZARD)
    write_doctest(FUNC_NAME, p1_win, ZOMBIE, LIZARD)
    write_doctest(FUNC_NAME, p2_win, SPOCK, LIZARD)
    write_doctest(FUNC_NAME, p2_win, ZOMBIE, GUN)
    write_doctest(FUNC_NAME, p1_win, SPOCK, GUN)
    write_doctest(FUNC_NAME, p2_win, SPOCK, ZOMBIE)

    write_doctest(FUNC_NAME, DRAW, ROCK, ROCK)
    write_doctest(FUNC_NAME, DRAW, SCISSORS, SCISSORS)
    write_doctest(FUNC_NAME, DRAW, PAPER, PAPER)
    write_doctest(FUNC_NAME, DRAW, LIZARD, LIZARD)
    write_doctest(FUNC_NAME, DRAW, GUN, GUN)
    write_doctest(FUNC_NAME, DRAW, ZOMBIE, ZOMBIE)
    write_doctest(FUNC_NAME, DRAW, SPOCK, SPOCK)


def write_doctest_lab4_task2(swap=False):
    """Print doctest for lab4 task2"""
    if swap:
        p1_win, p2_win = P2_WIN, P1_WIN
    else:
        p1_win, p2_win = P1_WIN, P2_WIN
    write_doctest(FUNC_NAME, p1_win, SCISSORS, PAPER)
    write_doctest(FUNC_NAME, p2_win, SCISSORS, ROCK)
    write_doctest(FUNC_NAME, p1_win, SCISSORS, LIZARD)
    write_doctest(FUNC_NAME, p2_win, SCISSORS, SPOCK)
    write_doctest(FUNC_NAME, p1_win, PAPER, ROCK)
    write_doctest(FUNC_NAME, p2_win, PAPER, LIZARD)
    write_doctest(FUNC_NAME, p1_win, PAPER, SPOCK)
    write_doctest(FUNC_NAME, p1_win, ROCK, LIZARD)
    write_doctest(FUNC_NAME, p2_win, ROCK, SPOCK)
    write_doctest(FUNC_NAME, p1_win, LIZARD, SPOCK)

    write_doctest(FUNC_NAME, p2_win, PAPER, SCISSORS)
    write_doctest(FUNC_NAME, p1_win, ROCK, SCISSORS)
    write_doctest(FUNC_NAME, p2_win, LIZARD, SCISSORS)
    write_doctest(FUNC_NAME, p1_win, SPOCK, SCISSORS)
    write_doctest(FUNC_NAME, p2_win, ROCK, PAPER)
    write_doctest(FUNC_NAME, p1_win, LIZARD, PAPER)
    write_doctest(FUNC_NAME, p2_win, SPOCK, PAPER)
    write_doctest(FUNC_NAME, p2_win, LIZARD, ROCK)
    write_doctest(FUNC_NAME, p1_win, SPOCK, ROCK)
    write_doctest(FUNC_NAME, p2_win, SPOCK, LIZARD)

    write_doctest(FUNC_NAME, DRAW, ROCK, ROCK)
    write_doctest(FUNC_NAME, DRAW, SCISSORS, SCISSORS)
    write_doctest(FUNC_NAME, DRAW, PAPER, PAPER)
    write_doctest(FUNC_NAME, DRAW, LIZARD, LIZARD)
    write_doctest(FUNC_NAME, DRAW, SPOCK, SPOCK)


def write_doctest_lab4_task1(swap=False):
    """Print doctest for lab4 task1"""
    if swap:
        p1_win, p2_win = P2_WIN, P1_WIN
    else:
        p1_win, p2_win = P1_WIN, P2_WIN
    write_doctest(FUNC_NAME, p1_win, SCISSORS, PAPER)
    write_doctest(FUNC_NAME, p2_win, SCISSORS, ROCK)
    write_doctest(FUNC_NAME, p1_win, PAPER, ROCK)

    write_doctest(FUNC_NAME, p2_win, PAPER, SCISSORS)
    write_doctest(FUNC_NAME, p1_win, ROCK, SCISSORS)
    write_doctest(FUNC_NAME, p2_win, ROCK, PAPER)

    write_doctest(FUNC_NAME, DRAW, ROCK, ROCK)
    write_doctest(FUNC_NAME, DRAW, SCISSORS, SCISSORS)
    write_doctest(FUNC_NAME, DRAW, PAPER, PAPER)


{1: write_doctest_lab4_task1,
 2: write_doctest_lab4_task2,
 3: write_doctest_lab4_task3}[TASK](swap=SWAP)
