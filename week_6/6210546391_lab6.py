

# level 1
def ll_sum(x):
    '''
    This function takes a list of lists of integers and 
    adds up the elements from all of the nested lists.
    >>> ll_sum([[1, 2], [3], [4, 5, 6]])
    21
    >>> ll_sum([[6,1], 1,[3,2,1]])
    14
    >>> ll_sum([[0,0],0,1,[5,6]])
    12
    >>> ll_sum([0,0])
    0
    >>> ll_sum([1000,[277],13])
    1290
    '''
    result = 0
    for i in x:
        if type(i) == list:
            result += ll_sum(i)
        else:
            result += i
    return result

# level 2
def cumulative_sum(x):
    '''
    This function takes a list of numbers and returns the cumulative sum; that is, a
    new list where the ith element is the sum of the first i + 1 elements from the original list.
    >>> cumulative_sum([1, 2, 3])
    [1, 3, 6]
    >>> cumulative_sum([5, 4, 2])
    [5, 9, 11]
    >>> cumulative_sum([1, 1, 1])
    [1, 2, 3]
    >>> cumulative_sum([1, 3, 6])
    [1, 4, 10]
    >>> cumulative_sum([1, 4, 5])
    [1, 5, 10]
    '''
    sum = []
    total = 0
    for i in x:
        total += i
        sum.append(total)
    return sum

# level 3
def middle(x):
    '''
    This function that takes a list and returns a new list
    that contains all but the first and last elements.
    >>> middle([5,4,1,1])
    [4, 1]
    >>> middle([1,2,3,4])
    [2, 3]
    >>> middle([9,10,11,8])
    [10, 11]
    >>> middle([1,2,3])
    [2]
    >>> middle([8,7,6,5,4])
    [7, 6, 5]

    '''
    The_middle_one = len(x) - 1
    return x[1:The_middle_one]

# level 4
def chop(x):
    '''
    This function takes a list, modifies it by removing the first and last elements,
    and returns None.
    >>> t = [1, 2, 3, 4] #first doctest
    >>> print(chop(t))
    None
    >>> print(t)
    [2, 3]
    >>> t = [3, 2, 2, 1] #second doctest
    >>> print(chop(t))
    None
    >>> print(t)
    [2, 2]
    >>> t = [6, 5, 3, 1] #third doctest
    >>> print(chop(t))
    None
    >>> print(t)
    [5, 3]

    '''
    del x[0::(len(x)-1)]
    return None

# level 5
def is_sorted(x):
    '''
    This function takes a list as a parameter and returns True
    if the list is sorted in ascending order and False otherwise.
    >>> is_sorted([1,3,3])
    True
    >>> is_sorted(['a','b'])
    True
    >>> is_sorted(['D','I','O'])
    True
    >>> is_sorted([6,1,3])
    False
    >>> is_sorted([100,200,300])
    True
    '''
    if sorted(x) == x:
        return True
    else:
        return False

# level 6
def front_x(x):
    '''
    This function returns a list with the strings in sorted order, except
    group all the strings that begin with 'x' first.
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    >>> front_x(['dog','xenon','xegon','xblade','fish'])
    ['xblade', 'xegon', 'xenon', 'dog', 'fish']
    >>> front_x(['lulu','xenojiva','party','bird','cat'])
    ['xenojiva', 'bird', 'cat', 'lulu', 'party']
    >>> front_x(['omen','xsraxsra','oraora','mudamuda','duradura'])
    ['xsraxsra', 'duradura', 'mudamuda', 'omen', 'oraora']
    >>> front_x(['meme','sad','encourage','mom','hoho'])
    ['encourage', 'hoho', 'meme', 'mom', 'sad']
    '''
    xlist = []
    alist = []
    for word in x:
        if word.startswith('x'):
            xlist.append(word)
        else:
            alist.append(word)
    return sorted(xlist) + sorted(alist)

# level 7
def even_only(x):
    '''
    This function will take a list of integers, and return a new list with only even
    numbers.
    >>> even_only([3,1,4,1,5,9,2,6,5])
    [4, 2, 6]
    >>> even_only([1,2,3,4,5,6,7,8])
    [2, 4, 6, 8]
    >>> even_only([8,6,5,4,2,1,14,9,3])
    [8, 6, 4, 2, 14]
    >>> even_only([1,1,1,1,1,2,2,2,1,1,1,1])
    [2, 2, 2]
    >>> even_only([7,5,2,4,7,8,1,2,12])
    [2, 4, 8, 2, 12]
    '''
    num = []
    for y in x:
        if y % 2 == 0:
            num.append(y)
    return num


# level 9
def is_anagram(string1, string2):
    """
    return True if strings are anagrams of each other
    >>> print(is_anagram('arrange', 'arrange'))
    True
    >>> print(is_anagram('bat', 'cat'))
    False
    >>> print(is_anagram('arrange', 'rearnag'))
    True
    >>> print(is_anagram('beep', 'peeb'))
    True
    >>> print(is_anagram('ora', 'bora'))
    False
    """
    list1 = list(string1)
    list2 = list(string2)
    list1.sort()
    list2.sort()
    return list1 == list2
# level 10
def has_duplicates(my_list):
    '''
    This function  takes a list and returns True if there is any element that
    appears more than once. It should not modify the original list.
    >>> has_duplicates([1, 2, 3, 4, 5])
    False
    >>> has_duplicates([1, 5, 4, 1, 32, 2])
    True
    >>> has_duplicates([2, 2, 2, 2, 2, 2])
    True
    >>> has_duplicates([5, 1])
    False
    >>> has_duplicates([8, 9 ,10 ,11, 23, 8])
    True
    '''
    i = 0
    while i < len(my_list):
        if my_list.count(my_list[i]) > 1:
            return True
        elif i == (len(my_list) - 1):
            return False
        i += 1


# level 11
def average(x):
    '''
    This function returns the mean average of a list of numbers.
    >>> average([1, 1, 5, 5, 10, 8, 7])
    5.285714285714286
    >>> average([6,6,21,32,4,5,1])
    10.714285714285714
    >>> average([1,2,3,4,1,2,5123,2,34])
    574.6666666666666
    >>> average([10,10,10])
    10.0
    >>> average([2,3,4,1,2,3,45,6])
    8.25
    '''
    result = 0
    for i in x:
        result += i
        average_x = result / len(x)
    return average_x


# level 12
def centered_average(x):
    '''
    This function returns a "centered" average of a list of numbers,
    which is the mean average of the values that ignores the largest and smallest values in the list. If
    there are multiple copies of the smallest/largest value, pick just one copy. 
    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([11,11,11,11])
    11.0
    >>> centered_average([6,5,4,3,2,1])
    3.5
    >>> centered_average([9,6,1,3,2,1,4,5])
    3.5
    >>> centered_average([87,65,43,12])
    54.0
    '''
    index = sorted(x)[1:-1]
    return sum(index) / len(index)


# level 13
def reverse_pair(x):
    '''
    This function
    >>> reverse_pair("May the fourth be with you")
    'you with be fourth the May'
    >>> reverse_pair("Kono da dio da")
    'da dio da Kono'
    >>> reverse_pair("I want you")
    'you want I'
    >>> reverse_pair("dog is not a cat")
    'cat a not is dog'
    >>> reverse_pair("I am the god")
    'god the am I'
    '''
    return ' '.join(x.split(' ')[::-1])


# level 14
def match_ends(words):
    '''
    This function returns the count of the
    number of strings where the string length is 2 or more and the first and last
    chars of the string are the same.
    >>> match_ends(["gingering", "hello", "wow"])
    2
    >>> match_ends(["derodero", "momo", "sas"])
    1
    >>> match_ends(["ora", "meme", "gag"])
    1
    >>> match_ends(["hoho", "lo", "weep"])
    0
    >>> match_ends(["adsadsa", "for of", "if li"])
    3
    '''
    count = 0
    for i in words:
        if len(i) >= 2 and i[0] == i[-1]:
            count += 1
    return count

# level 15
def remove_adjacent(n):
    '''
    This function returns a list where all adjacent elements
    have been reduced to a single element.
    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([1, 1, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([6, 4, 2, 4])
    [6, 4, 2, 4]
    >>> remove_adjacent([1, 1, 1, 1])
    [1]
    >>> remove_adjacent([2, 2, 2, 2])
    [2]
    '''
    a = []
    for item in n:
        if len(a):
            if a[-1] != item:
                a.append(item)
        else:
            a.append(item)
    return a







