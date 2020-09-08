import random

def convert_to_nums(s):
    ''' this function convert string to number respectively
    >>> convert_to_nums('paper')
    1
    >>> convert_to_nums('gun')
    4
    >>> convert_to_nums('lizard')
    3
    >>> convert_to_nums('scissors')
    0
    '''
    if s == 'scissors':
        return 0
    elif s == 'paper':
        return 1
    elif s == 'rock':
        return 2
    elif s == 'lizard':
        return 3
    elif s == 'gun':
        return 4
    elif s == 'zombie':
        return 5
    elif s == 'spock':
        return 6

def convert_to_string(n):
    ''' thsi function will convert the string to number respectively
    >>> convert_to_string(0)
    'scissors'
    >>> convert_to_string(4)
    'gun'
    >>> convert_to_string(1)
    'paper'
    >>> convert_to_string(2)
    'rock'
    '''
    if n == 0:
        return 'scissors'
    elif n == 1:
        return 'paper'
    elif n == 2:
        return 'rock'
    elif n == 3:
        return 'lizard'
    elif n == 4:
        return 'gun'
    elif n == 5:
        return 'zombie'
    elif n == 6:
        return 'spock'

def competition(nums,i):
        '''Return 't' if nums and i are equal. There are two condition that will return 'w'. First one is i-nums more than 0 and mod by 2
        is not equal 0. Second one is i-nums less than 0 ,but mod by 2 will equal 0. All other condition will return 't'
        >>> competition(0,1)
        'w'
        >>> competition(2,0)
        'w'
        >>> competition(1,1)
        't'
        >>> competition(1,0)
        'l'
        >>> competition(0,2)
        'l'
        '''
        if i == nums:
            return 't'
        elif i - nums > 0:
            if (i-nums)%2 != 0:
                return 'w'
            elif (i-nums)%2 == 0:
                return 'l'
        elif i - nums < 0:
            if (nums-i)%2 != 0:
                return 'l'
            elif (nums-i)%2 == 0:
                return 'w'

person = input('rock/paper/scissors/lizard/gun/zombie/spock: ')
com = random.randint(0,6)

print(f'Player chooses {person}')
print(f'Computer chooses {convert_to_string(com)}')

number = convert_to_nums(person)
condition = competition(number,com)

if  condition == 't':
    print('Both tie!')
elif condition == 'l':
    print('Computer win!')
elif condition == 'w':
    print('Player win!')