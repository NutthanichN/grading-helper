

def ll_sum(t):
    '''
    :param t:[int] list of numbers
    :return:[int] sum of numbers in the list

    >>> ll_sum([[1,2],[3],[5,6]])
    17
    >>> ll_sum([[2,7],[1,2,3]])
    15
    >>> ll_sum([[3,6,8],[1,2,3]])
    23
    >>> ll_sum([[1,3,4],[5],[8,2]])
    23
    >>> ll_sum([[2,8,4,3],[2,1]])
    20

    '''
    lst = []  #empty list
    for i in t:
        for j in range (len(i)):  # loop in list (that is also in the list)
            lst.append(i[j])    #add it to empty list
    return sum(lst)   #summation of the list

#=================== 1 ======================
def cumulative_sum(t):
    '''
    :param t:[int] list of numbers
    :return:[int] list of number that is the sum of the first 
    i + 1 elements from the original list
    
    >>> cumulative_sum([1,2,3])
    [1, 3, 6]
    >>> cumulative_sum([1,2,3,4,5])
    [1, 3, 6, 10, 15]
    >>> cumulative_sum([5,6,7,8])
    [5, 11, 18, 26]
    >>> cumulative_sum([10,2,5])
    [10, 12, 17]
    >>> cumulative_sum([2,2,2,2])
    [2, 4, 6, 8]

    '''
    lst1 = [t[0]]  # a list that have the first number of parameter in the list
    lst = t[0]   #assign lst has the value as a first number in the list 
    for i in range(len(t)-1):
        lst += t[i+1]  #lst plus and equal to the number that was called
        lst1.append(lst)  #add it to the list that have the first number already
    return lst1

#=================== 2 ======================
def middle(t):
    '''
    :param t: [int] list of numbers.
    :return:[int] the same list with the original one but cut 
    the first one and the last one out.

    >>> middle([1,3,4,5])
    [3, 4]
    >>> middle([2,2,2,3,4,5])
    [2, 2, 3, 4]
    >>> middle([4,5,6])
    [5]
    >>> middle([3,4,5,4,3])
    [4, 5, 4]
    >>> middle([6,7,6,7,6,7])
    [7, 6, 7, 6]

    '''
    return t[1:-1]    #cut the first one and the last one out

#==================== 3 =======================
def chop(t):
    '''
    :param t: [int] list of numbers
    :return: [int] the same list with the original one but cut 
    the first one and the last one out.

    >>> t = [1,3,4,5]
    >>> chop(t)
    >>> t
    [3, 4]
    >>> t = [2,2,2,3,4,5]
    >>> chop(t)
    >>> t
    [2, 2, 3, 4]
    >>> t = [4,5,6]
    >>> chop(t)
    >>> t
    [5]
    >>> t = [3,4,5,4,3]
    >>> chop(t)
    >>> t
    [4, 5, 4]
    >>> t = [7,6,5]
    >>> chop(t)
    >>> t
    [6]

    '''
    t.remove(t[0])   # cut the first one
    t.remove(t[-1])   # cut the last one

#===================== 4 =======================
def is_sorted(t):
    '''

    :param t:[str/int] list of number or str
    :return: [bool] check whether it arrange value from the least

    >>> is_sorted([1,2,3,4])
    True
    >>> is_sorted([4,3,5,2,7])
    False
    >>> is_sorted([2,2,1,3,4])
    False
    >>> is_sorted(['a','r','c','e'])
    False
    >>> is_sorted(['a','b','c','d'])
    True

    '''

    if t == sorted(t): #if list t equals to list t that is ordered respectively
        return True
    else:
        return False

#================== 5 ======================
def front_x(t):
    '''

    :param t: [str] list of words
    :return: [str] list of word but re-arrange by putting
    the word that start with 'X' first respectively

    >>> front_x(['xain','bird','any','xie'])
    ['xain', 'xie', 'any', 'bird']
    >>> front_x(['xon','won','tuang'])
    ['xon', 'tuang', 'won']
    >>> front_x(['xion','xauy','khing','jern'])
    ['xauy', 'xion', 'jern', 'khing']
    >>> front_x(['xander','xylan','bob','bambi'])
    ['xander', 'xylan', 'bambi', 'bob']
    >>> front_x(['xanlee','xanlae','acadia','sylvia'])
    ['xanlae', 'xanlee', 'acadia', 'sylvia']

    '''
    lst = []   #empty list
    lst1 = []    #empty list
    for i in t:
        if i[0] == 'x':   #if the first character of the word is x
            lst.append(i)   #add it to one list
        else:
            lst1.append(i)    # add it to another list
    return sorted(lst)+ sorted(lst1)   #re-arrange the list and put it together

#=================== 6 ====================
def even_only(t):
    '''

    :param t:[int] list of number
    :return: [int] list of even number that originated in parameter t

    >>> even_only([1,3,2,4,5,5])
    [2, 4]
    >>> even_only([3,7,9,8,6,4,2])
    [8, 6, 4, 2]
    >>> even_only([5,7,4,6,3])
    [4, 6]
    >>> even_only([9,9,7,8,6])
    [8, 6]
    >>> even_only([5,4,5,4])
    [4, 4]

    '''
    lst = []  #empty list
    for i in t:
        if i % 2 == 0:  # if i divisible by 2
            lst.append(i)  #add it to the list
    return lst

#================== 7 =====================
def love(text):
    '''
    :param text: [str] sentence
    :return:[str]change the second from the last word to 'love'

    >>> love('I hate you')
    'I love you'
    >>> love('I adore you')
    'I love you'
    >>> love('I sent it to you')
    'I sent it love you'
    >>> love('miss you')
    'love you'
    >>> love('all over you')
    'all love you'

    '''
    text = text.split(' ')  #split the text form every spaces so,it's gonna be a list
    text[-2] = 'love'   #the word before the last one replace it with the word 'love'
    text = ' '.join(text)  #turn list in to a normal text
    return text
#====================== 8 =========================
def is_anagram(a,b):
    '''
    :param a: [str] text
    :param b: [str] text you want to check if it's anagram with the word before
    :return:[bool] check if it's anagram

    >>> is_anagram('considerate','careisnoted')
    True
    >>> is_anagram('a gentleman','elegant man')
    True
    >>> is_anagram('boypablo','soypablo')
    False
    >>> is_anagram('signature','atruesige')
    False
    >>> is_anagram('school','slouch')
    False
    
    '''
    al = []   #list of parameter a
    bl = []    #list of parameter b
    for i in a:
        al.append(i)    #add it to list a
    for i in b:
        bl.append(i)    #dd it to list b
    if sorted(al) == sorted(bl):   #if list a that is sorted equal to list b that is sorted as well
        return True
    else:
        return False

#=================== 9 ===========================
def has_duplicates(t):
    '''
    :param lst: [int] list of numbers
    :return:[bool] check the list if there are any number that appear 
    more than once

    >>> has_duplicates([2,2,5,6,4])
    True
    >>> has_duplicates([2,5,6,4])
    False
    >>> has_duplicates([2,3,5,6,4,3])
    True
    >>> has_duplicates([3,3,6,6,4])
    True
    >>> has_duplicates([1,7,5,6,4])
    False

    '''
    lst = []  # empty list
    for i in t:
        if i not in lst:    #if i not in the list
            lst.append(i)    #add it to the list
    if lst == t:      #if that list equal to parameter t
        return False
    else:
        return True

#====================== 10 ======================
def average(nums):
    '''
    :param nums: [int] list of numbers
    :return: [float] an average of numbers in the list

    >>> average([1,2,3,4])
    2.5
    >>> average([2,2,2,2])
    2.0
    >>> average([1,2,2,5,6,4,4])
    3.4285714285714284
    >>> average([10,6,2,8])
    6.5
    >>> average([10,10,10,10,10,10])
    10.0

    '''
    for i in nums:
        sum(nums)  # summation of all numbers in the list
        return sum(nums)/len(nums)   #summation divided by amount of number
#=================== 11 =========================
def centered_average(nums):
    '''
    :param nums:[int] list of numbers
    :return:[float] average value that ignore 
    the largest and the smallest one

    >>> centered_average([1,2,3,4])
    2.5
    >>> centered_average([10,6,2,8])
    7.0
    >>> centered_average([10,10,10,10,10,10])
    10.0
    >>> centered_average([2,5,4,6,1])
    3.6666666666666665
    >>> centered_average([7,8,2,4,6,1])
    4.75
    
    '''
    a = sorted(nums)  # a as a list of parameter nums that is re-ordered
    nums = a[1:-1] #nums equal to list a but remove the firt one and the last one
    for i in nums:
        sum(nums)
        return sum(nums)/len(nums)
#===================== 12 =======================
def reverse_pair(t):
    '''
    :param t: [str] text you want to change
    :return: [str] same text with the parameter but order reversely

    >>> reverse_pair('I love you')
    'you love I'
    >>> reverse_pair('I hate you')
    'you hate I'
    >>> reverse_pair('How are you')
    'you are How'
    >>> reverse_pair('Good bye')
    'bye Good'
    >>> reverse_pair('miss you')
    'you miss'

    '''
    t = t.split(' ')   # split the text for every space(turns into a list)
    t = t[-1::-1]  #re-order it from the last one to the first one
    t = ' '.join(t)   #change it back to normal text
    return t
#==================== 13 ========================
def match_ends(t):
    '''
    :param t:[str] list of words
    :return: [int] number of the text that the first and last
    character are the same

    >>> match_ends(['yong','yay','hi','sas'])
    2
    >>> match_ends(['roar','ohho','limit','eliminate'])
    3
    >>> match_ends(['eri','pope','photo','sun'])
    0
    >>> match_ends(['yong','yay','hi','sas'])
    2
    >>> match_ends(['krak','ohio','nin','mum'])
    4

    '''
    count = 0
    for i in t:
        if i[0] == i[-1]:  #if the first character is the same as the last character
            count += 1  #count equal to 1 and add it up every time the condition is True
    return count
#======================= 14 =========================
def remove_adjacent(t):
    '''
    :param t: [int] list of number
    :return: [int] list of number but keep only one number of redundancy

    >>> remove_adjacent([2,2,6,5,6])
    [2, 6, 5, 6]
    >>> remove_adjacent([1,1,5,6])
    [1, 5, 6]
    >>> remove_adjacent([7,8,9,4])
    [7, 8, 9, 4]
    >>> remove_adjacent([7,7,7,7,6,5,5,4])
    [7, 6, 5, 4]
    >>> remove_adjacent([1,3,4,6,4,3,5,2,1,2])
    [1, 3, 4, 6, 4, 3, 5, 2, 1, 2]

    '''
    lst = []  #empty list
    for i in range(len(t)):
        if t[i] != t[i-1]:  #if that number is not the same value as the number before it
            lst.append(t[i])  #add it to the list
    return lst

#==================== 15 ====================


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)