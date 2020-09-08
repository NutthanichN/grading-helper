

#1

def ll_sum(t):
    """
    get a list of number from user and sum all of them then return the result of th summation.
    >>> ll_sum([[1,2],[3],[4,5,6]])
    21
    >>> ll_sum([[5,6,7],[0,1,2,3]])
    24
    >>> ll_sum([[9],[8],[7,3],[1,2]])
    30
    >>> ll_sum([[100,200],[1,1,1,1,1]])
    305
    >>> ll_sum([[500],[500],[205,601]])
    1806
    >>> ll_sum([[111],[105],[0,5,4,3]])
    228
    """
    result = []
    for num in t:
        result = result + num
    return sum(result)


# t = [[1,2],[3],[4,5,6]]
# print(ll_sum(t))


#2

def cumulative_sum(l):
    '''
    receiving a list of numbers from user and return a new list that the elements in the list is the
    cumulative sum of the preceding numbers. For example, [1,2,3] will be [1,(1+2), (1+2+3)].
    >>> cumulative_sum([1,2,3])
    [1, 3, 6]
    >>> cumulative_sum([9,9,9,9,9])
    [9, 18, 27, 36, 45]
    >>> cumulative_sum([5,7,9,10,15])
    [5, 12, 21, 31, 46]
    >>> cumulative_sum([10,10,10,10,10])
    [10, 20, 30, 40, 50]
    >>> cumulative_sum([1,1,1,1,1,1,1,1,1,1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    '''
    result = 0
    new_list = []
    for i in l :
        result = result + i
        new_list.append(result)
    return new_list

# t = [1, 2, 3]
# print(cumulative_sum(t))



#3

def middle(t):
    '''
    get a list from a user and return the new list without the first and last element of the original list.
    >>> middle([1,2,3])
    [2]
    >>> middle(['a','c','b','s','y'])
    ['c', 'b', 's']
    >>> middle(['apple', 'banana', 'cherry', 'cheese', 'cake'])
    ['banana', 'cherry', 'cheese']
    >>> middle(['rain', 'forest', 'water', 'fire'])
    ['forest', 'water']
    >>> middle(['school', 'building', 'tower'])
    ['building']
    >>> middle(['panda', 'monkey', 'frog', 'cow', 'chicken'])
    ['monkey', 'frog', 'cow']
    '''
    new_list = []
    for i in t[1:-1]:
        new_list.append(i)
    return new_list


# t = [1, 2, 3, 4]
# print(middle(t))



#4

def chop(t):
    '''
    receiving a list, removing the first and last elements of the list, then return none. There is no new list
    created in this function, but the original one is changed.
    >>> chop(['q','w','e','r','t'])

    >>> chop([1, 2, 3, 4])

    >>> chop(['a','b'])

    >>> chop(['spaghetti','steak','salad','fried rice'])

    >>> chop(['hello','goodbye','whiskey','rum','wine'])

    '''
    del t[0]
    del t[-1]
    return

# t = [1, 2, 3, 4]
# print(chop(t)) #None



#5

def is_sorted(l):
    '''
    get a list from user check whether the list is sorted if it is, return True. If it is not, return False.
    >>> is_sorted([1,2,3])
    True
    >>> is_sorted(['spaghetti', 'Ham', 'Pork'])
    False
    >>> is_sorted([5,3,1])
    False
    >>> is_sorted(['i','want','to','sleep'])
    False
    >>> is_sorted(['apple', 'banana', 'cherry'])
    True
    >>> is_sorted(['zebra','yoyo','x'])
    False
    '''
    a = []
    for i in l:
        a.append(i)
    l.sort()
    if a == l:
        return True
    else:
        return False

# print(is_sorted([1,2,3]))
# print(is_sorted(['b', 'a']))



#6

def front_x(l):
    '''
    get a list of strings from user and return the sorted original list, but if the list has a string that begins
    with 'x' those strings beginning with 'x' will come first and followed by the other words that are sorted.
    >>> front_x(['xxxx','fff','cccc'])
    ['xxxx', 'cccc', 'fff']
    >>> front_x(['z','x','c','v','v','b'])
    ['x', 'b', 'c', 'v', 'v', 'z']
    >>> front_x(['pig','cow','mouse','rat'])
    ['cow', 'mouse', 'pig', 'rat']
    >>> front_x(['xerox','apple','xapple','banana'])
    ['xapple', 'xerox', 'apple', 'banana']
    >>> front_x(['table','chair','xtime','xsnow'])
    ['xsnow', 'xtime', 'chair', 'table']
    '''
    list_x = []
    new_list = []
    for i in range(len(l)):
        if l[i][0] == 'x':
            list_x.append(l[i])
            list_x.sort()
        else:
            new_list.append(l[i])
            new_list.sort()

    return list_x + new_list

# l = ['mix', 'axyz', 'apple', 'axanadu', 'aardvark']
# b = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
# print(front_x(l))
# print(front_x(b))



#7

def even_only(list):
    '''
    get a list of integers from user and return a new list that contains only even numbers. For example,
    [1,2,3,4,5] ---> [2,4]
    >>> even_only([1,2,3,4,5])
    [2, 4]
    >>> even_only([3,1,4,1,5,9,2,6,5])
    [4, 2, 6]
    >>> even_only([10,20,5,7])
    [10, 20]
    >>> even_only([3,9,2,4])
    [2, 4]
    >>> even_only([25,7,99,800,55,60])
    [800, 60]
    >>> even_only([0,1000,546,32,77,17,71])
    [0, 1000, 546, 32]
    '''
    new_list = []
    for i in list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list


#print(even_only([3,1,4,1,5,9,2,6,5]))



#8

def love(text):
    '''
    get a sentence and change the second last word in sentence to the word LOVE and return the alternation
    >>> love("I like Python")
    'I love Python'
    >>> love("I really like Python")
    'I really love Python'
    >>> love('I hate ice-cream')
    'I love ice-cream'
    >>> love('I hate cockroach')
    'I love cockroach'
    >>> love('I like sleeping')
    'I love sleeping'
    '''
    new_text = text.split()
    new_text[-2] = 'love'
    new_text = ' '.join(new_text)
    return new_text


# print(love("I like Python"))
# print(love("I really like Python"))


#9

def is_anagram(origin, change):
    '''
    get two strings from user and compare them whether they are anagram or not. If it is return True, if it is
    not return False. Method to check = check the characters of each word. if the word uses the same characters,
    it is anagram.
    >>> is_anagram('arrange', 'Rear Nag')
    True
    >>> is_anagram('listen', 'silent')
    True
    >>> is_anagram('abcde', 'hijkl')
    False
    >>> is_anagram('game', 'mega')
    True
    >>> is_anagram('hello', 'world')
    False
    '''
    origin = origin.upper()
    origin = origin.split()
    origin = ''.join(origin)
    change = change.upper()
    change = change.split()
    change = ''.join(change)
    origin_s = []
    change_s = []
    for i in origin:
        origin_s.append(i)
    for i in change:
        change_s.append(i)
    origin_s.sort()
    change_s.sort()
    if origin_s == change_s:
        return True
    else:
        return False


# print(is_anagram('arrange', 'Rear Nag'))
# print(is_anagram('listen', 'silent'))


#10

def has_duplicates(l):
    '''
    get a list from user and check if there is the same element in the list. return False if none of the elements
    are the same, on the contradict, return True (the function does not change the original text.)
    >>> has_duplicates([1, 2, 3, 4, 5, 2])
    True
    >>> has_duplicates([1, 2, 3, 4, 5])
    False
    >>> has_duplicates(['abc','a','b','c','g','h','t'])
    False
    >>> has_duplicates(['monday','tuesday', 'friday'])
    False
    >>> has_duplicates([123,567,123,89,9,6])
    True
    >>> has_duplicates(['food', 'pizza', 'pork-chop','food','drink'])
    True
    '''
    check = []
    for i in l:
        if i in check:
            return True
        check.append(i)

    return False


# print(has_duplicates([1, 2, 3, 4, 5, 2]))
# print(has_duplicates([1, 2, 3, 4, 5]))
# print(has_duplicates(['abc','a','b','c','g','h','t']))




#11

def average(nums):
    '''
    get a list of numbers and return the average of that list by sum up the list and divide by the number
    of the elements in the list.
    >>> average([1, 1, 5, 5, 10, 8, 7])
    5.285714285714286
    >>> average([10,10,10,10])
    10.0
    >>> average([5,6,7,8,1,2,3,4,9,0])
    4.5
    >>> average([13,20,90,100,67])
    58.0
    >>> average([5000,100,45,93,45,24,17])
    760.5714285714286
    >>> average([43,56,78,15,405,707,77])
    197.28571428571428
    '''
    total = sum(nums)
    result = total / len(nums)
    return result

#print(average([1, 1, 5, 5, 10, 8, 7]))


#12

def centered_average(l):
    '''
    get a list of numbers and calculate the average of the numbers in the middle (the first and last number,
    which are the largest and the smallest number, are excluding.)
    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([1,2,3,4,5,6,7,8,9,10])
    5.5
    >>> centered_average([19,18,17,22,34,36,78,23])
    25.333333333333332
    >>> centered_average([100,104,333,566,723,999])
    431.5
    >>> centered_average([99,56,111,478,901,100,111,100])
    166.5
    >>> centered_average([1,1,1,77,88,99,100,100])
    61.0
    '''
    l.sort()
    a = []
    for i in l[1:-1]:
        a.append(i)
    total = sum(a)
    result = total / len(a)
    return result


#13

def reverse_pair(s):
    '''
    get a string and return the reverse version of that string. The reverse string will start with the last word
    and end with the first word. For example, 'May the fourth be with you' will be 'you with be fourth the May'
    >>> reverse_pair('May the fourth be with you')
    'you with be fourth the May'
    >>> reverse_pair('I want to sleep')
    'sleep to want I'
    >>> reverse_pair('please give money')
    'money give please'
    >>> reverse_pair('I want to go travelling')
    'travelling go to want I'
    >>> reverse_pair('eating is the best')
    'best the is eating'
    '''
    q = []
    string = s.split()
    for i in range(len(string)):
        q.append(string[-(i+1)])
    final = ' '.join(q)
    return final

#print(reverse_pair("May the fourth be with you"))



#14

def match_ends(l):
    '''
    get a list of a string and check if each of the string start and end with the same character. Return the number
    of the word that the beginning character and the ending character are the same. For example,

    >>> match_ends(["Gingering", "hello","wow"])
    2
    >>> match_ends(['pizza','seafood','pudding','mama'])
    0
    >>> match_ends(['lay','fanta','coke','pepsi'])
    0
    >>> match_ends(['aaa','bed','pajama','zzz','slipper'])
    2
    >>> match_ends(['shift','ice-cream','pep','tie','test','tttt'])
    3
    '''
    c = 0
    for i in l:
        i = i.lower()
        if len(i) >= 2:
            if i[-1] == i[0]:
                c += 1
            else:
                c += 0
        else:
            c += 0
    return c


#15
def remove_adjacent(l):
    '''
    get a list of number and check if there is adjacent elements if it has, the function will reduce to one.
    For example, [1,1,2,3,4,4,5] will be change to [1,2,3,4,5]
    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([1,1,2,3,4,4,5])
    [1, 2, 3, 4, 5]
    >>> remove_adjacent([11,100,105,4,104,32,1])
    [11, 100, 105, 4, 104, 32, 1]
    >>> remove_adjacent([34,34,5,2,8,7,50,51])
    [34, 5, 2, 8, 7, 50, 51]
    >>> remove_adjacent([1,45,66,82,66,66,88,1])
    [1, 45, 66, 82, 66, 88, 1]
    '''
    check = []
    for i in range(len(l)):
        if i == 0:
            check.append(l[i])
        elif l[i-1] != l[i]:
            check.append(l[i])
    return check











