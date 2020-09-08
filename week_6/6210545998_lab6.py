

import math
def ll_sum(t):
    '''
    This function will return sum of number in list .
    >>> t = [[1],[2,3,4],[2,6]]
    
    >>> ll_sum(t)
    18
    >>> t = [[1],[2,2],[3,3]]
    
    >>> ll_sum(t)
    11
    >>> t = [[1],[4,5,4],[1]]
    
    >>> ll_sum(t)
    15
    >>> t = [[7],[4,5],[0]]
    
    >>> ll_sum(t)
    16
    >>> t = [[2],[2],[1]]
    
    >>> ll_sum(t)
    5
    '''
    num = []
    for i in range (len(t)):
        for j in range (len(t[i])):
            num.append(t[i][j])
    return sum(num)
def cumulative_sum(t):
    '''
    This fuction will return list of number that sum with 
    number at the front where the ith element is the sum of the 
    first i + 1.
    >>> t = [1,2,3]
    >>> cumulative_sum(t)
    [1, 3, 6]
    >>> t = [1,2,3,4,5]
    >>> cumulative_sum(t)
    [1, 3, 6, 10, 15]
    >>> t = [4,3,3,5,6]
    >>> cumulative_sum(t)
    [4, 7, 10, 15, 21]
    >>> t = [2,2,2,2,2]
    >>> cumulative_sum(t)
    [2, 4, 6, 8, 10]
    >>> t = [1,1,1]
    >>> cumulative_sum(t)
    [1, 2, 3]
    '''
    num = [t[0]]*len(t)
    for i in range(1,len(t)):
       num[i]=num[i-1]+t[i] 
    return num
def middle(t):
    '''
    This function will remove a frist and last character 
    of list and return a new list.
    >>> t = [1,2,3]
    >>> middle(t)
    [2]
    >>> t = [1,2,3,4,5]
    >>> middle(t)
    [2, 3, 4]
    >>> t = [1,2,3,4]
    >>> middle(t)
    [2, 3]
    >>> t = ['duke','dddd','dukey','hhh']
    >>> middle(t)
    ['dddd', 'dukey']
    >>> t = [1,1,1,1]
    >>> middle(t)
    [1, 1]
    '''
    t = t[1:len(t)-1]
    return t
def chop(t):
    '''
    This function will remove a frist and last character 
    >>> a = [1,2,3,4]
    >>> chop(a)
    >>> a
    [2, 3]
    >>> b = [2,3,4,5]
    >>> chop(b)
    >>> b
    [3, 4]
    >>> c = [1,3,4,5]
    >>> chop(c)
    >>> c
    [3, 4]
    >>> d = [1,3,4,5,4,6,7,8]
    >>> chop(d)
    >>> d
    [3, 4, 5, 4, 6, 7]
    >>> e = ['d','u','k','e']
    >>> chop(e)
    >>> e
    ['u', 'k']
    '''    
    t.remove(t[0])
    t.remove(t[-1])
    return None

def is_sorted(t):
    '''
    >>> is_sorted([1,2,3,4,5,6,7,9,1])
    False
    >>> is_sorted([1,2,4,6])
    True
    >>> is_sorted(['a','c','d','h'])
    True
    >>> is_sorted(['a','c','d','h','f','a'])
    False
    >>> is_sorted(['d','u','k','e'])
    False
    '''    
    t1 = []
    for i in range(len(t)):
        t1.append(t[i])
    t1.sort()
    return t == t1
def front_x(l):
    '''
    This function will sort the word that 'x' in a frist 
    character on the front and sorted the word that have
    another character in a front on the second and return
    a new list.
    >>> l = ['xxxx','duke','thai','xaert']
    >>> front_x(l)
    ['xaert', 'xxxx', 'duke', 'thai']
    >>> l = ['qwer','asd','zxc','tyu']
    >>> front_x(l)
    ['asd', 'qwer', 'tyu', 'zxc']
    >>> l = ['xasdas','sdff','auk']
    >>> front_x(l)
    ['xasdas', 'auk', 'sdff']
    >>> l = ['x','xa','xe']
    >>> front_x(l)
    ['x', 'xa', 'xe']
    >>> l = ['x','eeeeeee','xiai']
    >>> front_x(l)
    ['x', 'xiai', 'eeeeeee']
    '''
    x = []
    l1 = []
    for i in range (len(l)):
        if l[i][0] == "x":
            x.append(l[i])
        else:
            l1.append(l[i])
    x.sort()
    l1.sort()
    return x + l1

def even_only(l):
    '''
    This function will return a new list that have a even
    number only.
    >>> even_only([2,3,4,5,6])
    [2, 4, 6]
    >>> even_only([1,2,3,4,5])
    [2, 4]
    >>> even_only([22,33,55,3,2])
    [22, 2]
    >>> even_only([22,44,66,2222,44444])
    [22, 44, 66, 2222, 44444]
    >>> even_only([2,1,1,1,2])
    [2, 2]
    
    '''
    even = []
    for i in range(len(l)):
        if l[i]%2 == 0:
            even.append(l[i])
    return even

def love(text):
    '''
    This fuction will replace second last word by 'love' 
    and return a new string.
    >>> love('I like programing 1')
    'I like love 1'
    >>> love('I l KU')
    'I love KU'
    >>> love('I love KU')
    'I love KU'
    >>> love('I like KUUUUU79')
    'I love KUUUUU79'
    >>> love('I love SKEEEEE17')
    'I love SKEEEEE17'
    '''
    l = text.split()
    new = text.replace(l[-2],'love')
    return new
# print(love('I like KU'))

def is_anagram(a,b):
    '''
    This function will return True if two word that inputed is anagram
    and return False if not.
    >>> is_anagram('qwer','ER qw')
    True
    >>> is_anagram('asdfg','ADF SG')
    True
    >>> is_anagram('duke','duk EE')
    False
    >>> is_anagram('eeeee','e e e e e')
    True
    >>> is_anagram('koifkw','Kwkoi   fff')
    False
    '''
    alpha = "abcdefghijklmnopqrstuvwxyz"
    a = a.lower()
    b = b.lower()
    a1 = []
    b1 = []
    for i in range(len(a)):
        if a[i] in alpha:
            a1.append(a[i])
    for i in range(len(b)):
        if b[i] in alpha:
            b1.append(b[i])
    return sorted(a1) == sorted(b1)

def has_duplicates(l):
    '''
    This fuction will check duplicates in list of number
    if it have fuction wil return True and False if not.
    >>> has_duplicates([1,2,3,3,3,4,5,6])
    True
    >>> has_duplicates([22,33,44,55,66])
    False
    >>> has_duplicates([1,2,3,7,7,9])
    True
    >>> has_duplicates([1,2,3,77,7,9,99])
    False
    >>> has_duplicates([1,1,1,1,11,111])
    True
    '''
    num = []
    num1 = []
    for i in range(len(l)):
            num.append(l[i])
    num.sort()
    for i in range(len(num)):
        if num[i] == num[i-1]:
            num1.append(num[i])
    if len(num1)>0:
        return True
    else:
        return False

def average(l):
    '''
    This function will calculate a average of number in list.
    >>> average([1,2,3,4])
    2.5
    >>> average([5,6,7,9])
    6.75
    >>> average([1,11,111])
    41.0
    >>> average([212,224,236])
    224.0
    >>> average([1,1,1])
    1.0
    '''
    return sum(l)/len(l)

def centered_average(l):
    '''
    This function will calculate a cntered average of number in list.
    >>> centered_average([1,2,3,4,5,6])
    3.5
    >>> centered_average([5,2,3,4,5,100])
    4.25
    >>> centered_average([1,3,5,7,9])
    5.0
    >>> centered_average([5,5,1,3,5,7,9])
    5.0
    >>> centered_average([1,1,5,7])
    3.0
    '''
    l.sort()
    num = l[1:len(l)-1]
    avg = sum(num)/len(num)
    return float(avg)

def reverse_pair(l):
    '''
    This fuction will reverse a string and return a
    new string.
    >>> reverse_pair('coding love I')
    'I love coding'
    >>> reverse_pair('KU University')
    'University KU'
    >>> reverse_pair('17 SKE')
    'SKE 17'
    >>> reverse_pair('79 KU')
    'KU 79'
    >>> reverse_pair('62 25')
    '25 62'
    '''
    new = l.split()
    new.reverse() 
    return (' '.join(new))

def match_ends(l):
    '''
    This function will check the word that have a same
    character on a frist and last and return a number of that.
    >>> match_ends(['zoo','oooo','dood','wow'])
    3
    >>> match_ends(['KU','KK','KKK'])
    2
    >>> match_ends(['abc','dfg','hij'])
    0
    >>> match_ends(['KUK','QWER','DDDDD','ERE'])
    3
    >>> match_ends(['quweq','quwep','duke'])
    1
    '''
    new = [l.lower() for l in l]
    new1 = []
    for i in range(len(l)):
        if new[i][0] == new[i][-1]:
            new1.append(l[i])
    return len(new1)

def remove_adjacent(l):
    '''
    This function will check adjacent element and reduced to
    sigle element.
    >>> remove_adjacent([1,2,2,3,3])
    [1, 2, 3]
    >>> remove_adjacent([3,2,2,1,1,3])
    [3, 2, 1, 3]
    >>> remove_adjacent([3,3,4,4,1,2,3,3])
    [3, 4, 1, 2, 3]
    >>> remove_adjacent([3,3,4,4,1,2,3,3,1,1,1])
    [3, 4, 1, 2, 3, 1]
    >>> remove_adjacent([3,3,4,4])
    [3, 4]
    
    '''
    num = [l[0]]
    for i in range(len(l)-1):
        if l[i] != l[i+1]:
            num.append(l[i+1]) 
    return num


    


    
        
            


    



            





    


        
    

            
            
        


