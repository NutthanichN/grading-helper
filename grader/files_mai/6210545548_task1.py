# 01 / 09 / 2019
# NOTE: To tun doctest, Please Quickly type: [ 1 > 1 > 1 > q or Q ] then doctest will activate.

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  Functions. '''
#------------------------------------------------------------------------------------- Introduction and choices.
def rules():
    print('-'*40)
    print('Welcome to my application.\n\nPlease pick your choice:\n1. Rock\n2. Scissors\n3. Paper')
    print('-'*40)
#------------------------------------------------------------------------------------- Player's choice translate to integer.
def user_num(choice):
    if choice == 'Rock':
        return 0
    elif choice == 'Paper':
        return 1
    elif choice == 'Scissors':
        return 2
#------------------------------------------------------------------------------------- Computer's choice translate to string.
def jarvis_string(jarvis):
    if jarvis == 0:
        return 'Rock'
    elif jarvis == 1:
        return 'Paper'
    elif jarvis == 2:
        return 'Scissors'
    else:
        print('Error occurred.')
#------------------------------------------------------------------------------------- Check win / lose conditions.
def check(choice_num,jarvis_num):
    ''' checking results of possible outcomes. As my application keeps record of how many turn player wins or loses, there will be additional value below the test which varies
        on the results of each time the loop is executed [possible differences will mostlikely occurs.]
        Examples:
            >>> check(0,1)
            Computer wins!
            ----------------------------------------
            X [Note: this is not error of doctest but a return value of score records, It is different each time the program runs as it is based on chaining effects of the loop.]
            >>> check(1,2)
            Computer wins!
            ----------------------------------------
            X [Note: this is not error of doctest but a return value of score records, It is different each time the program runs as it is based on chaining effects of the loop.]
            >>> check(2,2)
            Both ties!
            ----------------------------------------
            X [Note: this is not error of doctest but a return value of score records, It is different each time the program runs as it is based on chaining effects of the loop.]
            >>> check(3,1)
            Computer wins!
            ----------------------------------------
            X [Note: this is not error of doctest but a return value of score records, It is different each time the program runs as it is based on chaining effects of the loop.]
            >>> check(4,4)
            Both ties!
            ----------------------------------------
            X [Note: this is not error of doctest but a return value of score records, It is different each time the program runs as it is based on chaining effects of the loop.]
    '''
    if choice_num == jarvis_num:
        print('Both ties!')
        print('-'*40)
        return score
    elif ((choice_num + 1) % 3) == jarvis_num:
        print("Computer wins!")
        print('-'*40)
        return (score - 1)
    else:
        print("Player wins!")
        print('-'*40)
        return (score + 1)
#------------------------------------------------------------------------------------- Displaying final result.
def score_check(score):
    if score == 0:
        print('NO WINNER.')
        print('-'*40)
    elif score > 0:
        print('YOU WIN.')
        print('-'*40)
    elif score < 0:
        print('YOU LOSE.')
        print('-'*40)
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  Operating Codes. '''
import random
# Application replay option added.
refresh = ''
while refresh.lower() != 'q':
    # declaring variables.
    count = 0
    score = 0
    # Instruction to what choices player has.
    rules()
    # Application begins. [Three rounds are given then final result will be display at the end.]
    while count < 3:
        choice = ''
        while choice.lower() != 'rock' or  choice.lower() != 'paper' or choice.lower() != 'scissors':
            try:
                choice = input('Pick your choice.\n[ 1 , 2 , 3 or Rock / Scissors / Paper ]:  ')
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
                else:
                    print('Invalid input, please try again.')
        choice_num = user_num(choice) # Translate player's choice to integer.
        jarvis_num = random.randint(0,2) # Generate random integer between 0 to 2.
        string = jarvis_string(jarvis_num) # Translate computer's choice to string.
        print(f'Your: {choice} VS {string} :Computer.') # Display outcome of both choices.
        score = check(choice_num,jarvis_num) # Scoring updated.
        count += 1 # while loop increment.
    score_check(score) # Player's Result.
    # Application replay choice.
    refresh = input('Type "Q" to quit the game | Type Anything to play again: ')
    # When refresh = 'q' or 'Q', program exit.
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  Doctest. '''
if __name__ == "__main__":
    import doctest
    doctest.testmod()
#------------------------------------------------------------------------------------- End.