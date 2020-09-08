import random
def game_operation(player_choice_num,computer_choice_num):
    # main program
    '''
    This function will gonna show us how it this program work so first of all this function will gonna
    recieve the values from the convert_choice_to_num function and it will calculate in this function by
    substracted player and computer choice in number and if the values is even that mean the player wins
    but in the other hand if the values is odd computer gonna wins. The outcome can be change when the values
    is negative it gonna change the outcome to be in contrast such as the even gonna mean computer wins and the odd 
    mean player wins.

    (0=scissor, 1=paper, 2=rock, 3=lizard, 4=gun, 5=zombie, 6=spock)

        >>> game_operation(0,1)
        Player wins.
        >>> game_operation(5,0)
        Computer wins.
        >>> game_operation(4,2)
        Player wins.
        >>> game_operation(6,1)
        Computer wins.
        >>> game_operation(5,6)
        Player wins.

    '''
    
    if player_choice_num == computer_choice_num:
        print('Both tie')
    elif (player_choice_num - computer_choice_num)%2 == 0 and (player_choice_num - computer_choice_num)>0:
        print('Player wins.')
    elif (player_choice_num - computer_choice_num)%2 !=0 and (player_choice_num - computer_choice_num)>0:
        print('Computer wins.')
    elif (player_choice_num - computer_choice_num)%2 ==0 and (player_choice_num - computer_choice_num)<0:
        print('Computer wins.')
    elif (player_choice_num - computer_choice_num)%2 !=0 and (player_choice_num - computer_choice_num)<0:
        print('Player wins.')
    
def convert_choice_to_num(choice):
    # convert input to integer
    if choice == 'scissor':
        return 0
    elif choice == 'paper':
        return 1
    elif choice == 'rock':
        return 2
    elif choice == 'lizard':
        return 3
    elif choice == 'gun':
        return 4
    elif choice == 'zombie':
        return 5
    elif choice == 'spock':
        return 6
    else:
        print("Error: should not reach this if input is a valid one")

def convert_num_to_string(num):
    # convert integer to string
    if num == 0:
        return 'scissor'
    elif num == 1:
        return 'paper'
    elif num == 2:
        return 'rock'
    elif num == 3:
        return 'lizard'
    elif num == 4:
        return 'gun'
    elif num == 5:
        return 'zombie'
    elif num == 6:
        return 'spock'
    else:
        print("Error: should not reach this if input is a valid one")
    
    
# please don't hesitate to uncomment this execution to try input the values to check this code run correctly or not.

# execution code    
'''choice = input('Enter your choice: ')
while choice != 'rock' and choice != 'scissor' and choice != 'paper' and choice != 'spock' and choice != 'lizard' and choice != 'gun' and choice != 'zombie' :
    print('"Invalid choice. Enter again."')
    choice = input('Enter your choice: ')
computer_choice_num = random.randint(0, 6)
computer_choice = convert_num_to_string(computer_choice_num)
player_num = convert_choice_to_num(choice)
print(f'Player choose {choice}')
print(f'Computer choose {computer_choice}')
game_operation(player_num,computer_choice_num)'''
