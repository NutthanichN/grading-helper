# 09 / 09 / 2019
# NOTE: To tun doctest, Please Quickly type: [ 1 > 1 > 1 > n or N ] then doctest will activate.

'''----------------------------------------------------------------- FUNCTIONS -----------------------------------------------------------------'''
#------------------------------------------------------------------ Display application rules.
def intro():
    print('#'*40)
    print('Welcome to Application')
    print('-'*40)
    print("• Scissors cut paper\n• Paper covers rock\n• Rock crushes lizard\n• Lizard poisons Spock\n• Spock smashes (or melts) scissors\n• Scissors decapitate lizard\n• Lizard eats paper\n• Paper disproves Spock\n• Spock vaporizes rock\n• Rock breaks scissors")
    print('-'*40)
    print("Player's choice")
    print("1. Rock\n2. Paper\n3. Scissors\n4. Spock\n5. Lizard")
    print('-'*40)
#------------------------------------------------------------------ Player's choice converts to string.
def player_string(choice):
    if choice.lower() == 'rock' or choice.lower() == '1':
        return 'Rock' , 0
    elif choice.lower() == 'paper' or choice.lower() == '2':
        return 'Paper' , 1
    elif choice.lower() == 'scissors' or choice.lower() == '3':
        return 'Scissors' , 2
    elif choice.lower() == 'spock' or choice.lower() == '4':
        return 'Spock' , 3
    elif choice.lower() == 'lizard' or choice.lower() == '5':
        return 'Lizard' , 4
#------------------------------------------------------------------ Computer converts to string.
def jarvis_string(jarvis):
    if jarvis == 0:
        return 'Rock'
    elif jarvis == 1:
        return 'Paper'
    elif jarvis == 2:
        return 'Scissors'
    elif jarvis == 3:
        return 'Spock'
    elif jarvis == 4:
        return 'Lizard'
#------------------------------------------------------------------ Check winning conditions.
def check(player,jarvis):
    ''' checking results of possible outcomes. As my application keeps record of how many turn player wins or loses, there will be additional value below the test which varies
        on the results of each time the loop is executed [possible differences will mostlikely occurs.]
        Examples:
            >>> check(0,0)
            Both ties!
            ----------------------------------------
            X [Note: this is not error of doctest but a return value of score records, It is different each time the program runs as it is based on chaining effects of the loop.]
            >>> check(1,1)
            Both ties!
            ----------------------------------------
            X [Note: this is not error of doctest but a return value of score records, It is different each time the program runs as it is based on chaining effects of the loop.]
            >>> check(2,2)
            Both ties!
            ----------------------------------------
            X [Note: this is not error of doctest but a return value of score records, It is different each time the program runs as it is based on chaining effects of the loop.]
            >>> check(3,4)
            Computer wins!
            ----------------------------------------
            X [Note: this is not error of doctest but a return value of score records, It is different each time the program runs as it is based on chaining effects of the loop.]
            >>> check(2,4)
            Player wins!
            ----------------------------------------
            X [Note: this is not error of doctest but a return value of score records, It is different each time the program runs as it is based on chaining effects of the loop.]
            >>> check(0,5)
            Player wins!
            ----------------------------------------
            X [Note: this is not error of doctest but a return value of score records, It is different each time the program runs as it is based on chaining effects of the loop.]
            >>> check(1,4)
            Computer wins!
            ----------------------------------------
            X [Note: this is not error of doctest but a return value of score records, It is different each time the program runs as it is based on chaining effects of the loop.]
            >>> check(2,0)
            Computer wins!
            ----------------------------------------
            X [Note: this is not error of doctest but a return value of score records, It is different each time the program runs as it is based on chaining effects of the loop.]
    '''
    if player == jarvis:
        print('Both ties!')
        return score
    elif player == 0 and jarvis == 3:
        print('Computer wins!')
        return (score-1)
    elif player == 4 and jarvis == 0:
        print('Computer wins!')
        return (score-1)
    elif player == 1 and jarvis == 4:
        print('Computer wins!')
        return (score-1)
    elif ((player + 1) % 3) == jarvis:
        print('Computer wins!')
        return (score-1)
    else:
        print('Player wins!')
        return (score+1)
#------------------------------------------------------------------ Final score check.
def score_check(score):
    if score == 0:
        print('NO WINNER.')
    elif score > 0:
        print('PLAYER WINS.')
    elif score < 0:
        print('PLAYER LOSES.')
'''----------------------------------------------------------------- EXECUTION CODE -----------------------------------------------------------------'''
# Import random.
import random
# Aftermath replay setup.
replay = ''
while replay.lower() != 'n':
    intro()
    count = 0
    score = 0
    # Three rounds given then display final result.
    while count < 3:
        choice = ''
        while choice.lower() != 'rock' or  choice.lower() != 'paper' or choice.lower() != 'scissors' or choice.lower() != 'spock' or choice.lower() != 'lizard' or choice.lower() != '1' or choice.lower() != '2' or choice.lower() != '3' or choice.lower() != '4' or choice.lower() != '5':
            try:
                choice = input(f'Round {count+1}: Pick your Choice: ')
            except ValueError as e:
                print(e)
            else:
                if choice.lower() == 'rock' or choice.lower() == '1':
                    choice = 'Rock'
                    break
                elif choice.lower() == 'paper' or choice.lower() == '2':
                    choice = 'Paper'
                    break
                elif choice.lower() == 'scissors' or choice.lower() == '3':
                    choice = 'Scissors'
                    break
                elif choice.lower() == 'spock' or choice.lower() == '4':
                    choice = 'Spock'
                    break
                elif choice.lower() == 'lizard' or choice.lower() == '5':
                    choice = 'Lizard'
                    break
                else:
                    print('Invalid input, please try again.')
        # choice = player(f'Round {count+1}: Pick your Choice: ')
        player_pick , player_num = player_string(choice)
        jarvis = random.randint(0,4)
        jarvis_respond = jarvis_string(jarvis)
        print(f'Player: {player_pick} VS {jarvis_respond} :Computer.')
        score = check(player_num,jarvis)
        print('-'*40)
        count += 1
    # Score increment.
    score_check(score)
    print('-'*40)
    # Replay options.
    replay = input('Would you like to play again? [Y/N]: ')
# Finale
print('\nProgram exit.\n')
'''----------------------------------------------------------------- DOCTEST -----------------------------------------------------------------'''
if __name__ == '__main__':
    import doctest
    doctest.testmod()
else:
    print('This is not the original file.')