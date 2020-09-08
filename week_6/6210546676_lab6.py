

# 1
def ll_sum(t):
    """
    Create a function that takes a list of lists of integers and adds up the elements from all of the nested lists.
    >>> t = [[1,2],[3],[4,5,7]]    
    >>> ll_sum(t) 
    22

    >>> t = [[3,3],[4,2,7],[1,7,5,3]]
    >>> ll_sum(t)
    35

    >>> t = [[4,3],[1,6,7],[3,7,2,9]]
    >>> ll_sum(t)
    42

    >>> t = [[3,3,4],[4,2,7,1],[7,5,3]]
    >>> ll_sum(t)
    39

    >>> t = [[3,9],[4,5,7],[1,2,1,3]]
    >>> ll_sum(t)
    35
    
    """
    
    result = 0
    for num in t:
        result += sum(num)
    return result

# 2
def cumulative_sum(t):
    """
    Create a function that use to takes a list of numbers and returns the cumulative sum that is a new list where the element is the sum of the first i + 1 elements from the original list.
    >>> t = [1,2,4]
    >>> cumulative_sum(t)
    [1, 3, 7]
    
    >>> t = [1,3,3]
    >>> cumulative_sum(t)
    [1, 4, 7]

    >>> t = [1,4,5]
    >>> cumulative_sum(t)
    [1, 5, 10]
     
    >>> t = [1,7,6]
    >>> cumulative_sum(t)
    [1, 8, 14]
    
    >>> t = [1,9,9]
    >>> cumulative_sum(t)
    [1, 10, 19]

    """
    result = []
    a = 0
    for num in t:
        a += num
        result.append(a)
    return result

# 3
def middle(t):
    """
    Create a function that use to takes a list and returns a new list that contains all but the first and last elements.
    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]

    >>> t = [1, 5, 7, 4]
    >>> middle(t)
    [5, 7]

    >>> t = [1, 3, 4, 4]
    >>> middle(t)
    [3, 4]

    >>> t = [1, 9, 8, 4]
    >>> middle(t)
    [9, 8]

    >>> t = [1, 6, 1, 4]
    >>> middle(t)
    [6, 1]
    """
    new_list = t[1:-1]
    return new_list

# 4 
def chop(t):
    """
    Create a function that use to modifies it by removing the first and last elements and return none
    >>> t = [1, 2, 35, 4]
    >>> chop(t)
    >>> t
    [2, 35]
    
    >>> t = [1, 24, 35, 4]
    >>> chop(t)
    >>> t
    [24, 35]
    
    >>> t = [1, 7, 40, 4]
    >>> chop(t)
    >>> t
    [7, 40]

    >>> t = [1, 9, 0, 4]
    >>> chop(t)
    >>> t
    [9, 0]

    >>> t = [1, 66, 77, 4]
    >>> chop(t)
    >>> t
    [66, 77]

    """
    t.pop(0)
    t.pop(-1)
    a = t[1:-1]
    

    

# 5 
def is_sorted(t):
    """
    Create a function that use to takes a list as a parameter and returns True is the list is sorted ub ascending order and False otherwise
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False

    >>> is_sorted([1, 2, 3])
    True
    >>> is_sorted(['c', 'a'])
    False

    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    """
    if t == sorted(t):
        return True
    else:
        return False

# 6
def front_x(l):
    """
    Create a function that use to returns a list with the strings in sorted order, except group all the strings that begin with x first
    >>> l = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
    >>> front_x(l)
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    
    >>> l = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark','xxxxxx']
    >>> front_x(l)
    ['xanadu', 'xxxxxx', 'xyz', 'aardvark', 'apple', 'mix']
    
    >>> l = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark','xbxxxx']
    >>> front_x(l)
    ['xanadu', 'xbxxxx', 'xyz', 'aardvark', 'apple', 'mix']
    
    >>> l = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark','xcdefg']
    >>> front_x(l)
    ['xanadu', 'xcdefg', 'xyz', 'aardvark', 'apple', 'mix']
    
    >>> l = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark','xxxxxx', 'lover']
    >>> front_x(l)
    ['xanadu', 'xxxxxx', 'xyz', 'aardvark', 'apple', 'lover', 'mix']
    
    """
    a = []
    for b in l:        
        if b.startswith('x'):
            a.append(b)
            l.remove(b)
    a.sort()
    l.sort()
    return a + l

# 7
def even_only(list):
    """
    Create a function that will take a list of integers and return a new list with only even numbers.
    >>> even_only([3,1,4,1,5,9,2,6,5,15,14,22,24])
    [4, 2, 6, 14, 22, 24]

    >>> even_only([3,1,4,1,5,9,2,6,5,8])
    [4, 2, 6, 8]

    >>> even_only([3,1,4,1,5,9,2,6,5,7,10,12])
    [4, 2, 6, 10, 12]

    >>> even_only([3,1,4,1,5,9,2,6,5,12,14,16])
    [4, 2, 6, 12, 14, 16]

    >>> even_only([3,1,4,1,5,9,2,6,5,20,22,24])
    [4, 2, 6, 20, 22, 24]
    """
    a =  []
    for b in list:
        if b %2!= 1:
            a.append(b)
    return a

# 8
def love(text):
    """
    Create a funtion that will change the second last word to love
    >>> love("I . Python")
    'I love Python'

    >>> love("I really a Python")
    'I really love Python'

    >>> love('I hate python')
    'I love python'

    >>> love('I like you')
    'I love you'

    >>> love('Beam like you')
    'Beam love you'

    """
    l = text.split()
    l.pop(-2)
    l.insert(-1,'love')
    o = (' '.join(l))
    return o

# 9
def is_anagram(a,b):
    """
    Create a function that use to rearrange the letters from one to spell the other
    >>> is_anagram('arrange','Rear Nga')
    True
    
    >>> is_anagram('abc','acv')
    False
    
    >>> is_anagram('acz','zca')
    True
    
    >>> is_anagram('asdfg','ags fd')
    True
    
    >>> is_anagram('zxcvb','bxzcva')
    False

    """
    a = a.upper()
    b = b.upper()
    a = a.split()
    b = b.split()
    a = ''.join(a)
    b = ''.join(b)
    a = sorted(a)
    b = sorted(b)

    if a == b:
        return True  
    else:
        return False

# 10
def has_duplicates(a):
    """
    Create a funtion that takes a list and returns True if there is any element that appers more than once
    >>> has_duplicates([1, 2, 3, 4])
    False

    >>> has_duplicates([1, 2, 3, 4, 5, 5])
    True

    >>> has_duplicates([1, 2, 1, 4, 5, 5])
    True

    >>> has_duplicates([1, 2, 3, 7, 8, 6])
    False

    >>> has_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9])
    False

    """
    b = []
    for c in a:
        if c not in b:
            b.append(c)
    if b == a:
        return False
    else:
        return True
        
# 11
def average(nums):
    """
    Create a funtion that use to returns the mean average of a list number
    >>> average([1, 1, 5, 5, 10, 8, 8])
    5.428571428571429
    
    >>> average([1, 2, 5, 5, 10, 8, 8])
    5.571428571428571

    >>> average([1, 1, 3, 5, 10, 8, 8])
    5.142857142857143
    
    >>> average([1, 9, 5, 5, 10, 8, 8])
    6.571428571428571

    >>> average([8, 3, 2, 5, 10, 8, 8])
    6.285714285714286

    """
    a = sum(nums)
    return a/len(nums)

# 12
def centered_average(nums):
    """
    Create a funtion that use to returns centered average of a list of numbers.
    >>> centered_average([1, 1, 5, 7, 10, 8, 7])
    5.6

    >>> centered_average([1, 3, 5, 7, 10, 8, 7])
    6.0

    >>> centered_average([1, 3, 5, 7, 10, 8, 7, 7, 8])
    6.428571428571429

    >>> centered_average([1, 3, 5, 7, 10, 8, 7, 8, 9, 10])
    7.125

    >>> centered_average([1, 3, 5, 7])
    4.0

    """
    a = sorted(nums)[1:-1]
    return sum(a) / len(a)

# 13
def reverse_pair(a):
    """
    Create a function that reverse of the other
    >>> reverse_pair("May the fourth be with youu")
    'youu with be fourth the May'
    
    >>> reverse_pair("May the fourthh be with youu")
    'youu with be fourthh the May'

    >>> reverse_pair("May thee fourth be with youu")
    'youu with be fourth thee May'

    >>> reverse_pair("you the fourth be with may")
    'may with be fourth the you'

    >>> reverse_pair("May the force be with youu")
    'youu with be force the May'


    """


    c = a.split(' ')
    d = ' '.join(reversed(c))
    return d

# 14
def match_ends(a):
    """
    Create a function that returns the count of the number of strings where the string length is 2 or more and the first and last chars of the string are the same
    >>> match_ends(["bqb","hello","abba"])
    2

    >>> match_ends(["bqd","hellh","cbbc","abfdgdfa"])
    3

    >>> match_ends(["abca","aella"])
    2

    >>> match_ends(["bqb","hello","abba", "asdfghja","qqwertyuiq"])
    4

    >>> match_ends(["bqwewdgfvfh","eelle","casfc"])
    2
    """

    b = 0
    for c in a:
        if len(c) >= 2 and c[0] == c[-1]:
            b += 1
    return b

# 15
def remove_adjacent(a):
    """
    Create a funtion that use to remove adjacent
    >>> remove_adjacent([1,2,3,3])
    [1, 2, 3]
    
    >>> remove_adjacent([1,2,2,3,3,4,5])
    [1, 2, 3, 4, 5]

    >>> remove_adjacent([1,2,3,4,5,6,7,7])
    [1, 2, 3, 4, 5, 6, 7]
    
    >>> remove_adjacent([1,2,3,4,5,6,7,8,9,9,8])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    >>> remove_adjacent([8,5,7,3,6,7,2,8])
    [8, 5, 7, 3, 6, 2]
    
    """
    b = []
    for c in a:
        if c not in b:
            b.append(c)
    return b 
    






    




        













