

# 1
def ll_sum(t):
    ''' make the sum of all number in list
    >>> t = [[1,2],[3],[4,5,6]]
    >>> ll_sum(t)
    21
    >>> a = [[1,2],3,[4]]
    >>> ll_sum(a)
    10
    >>> b = [[5,6],[5,7]]
    >>> ll_sum(b)
    23
    >>> c = [1,2,3]
    >>> ll_sum(c)
    6
    >>> d = []
    >>> ll_sum(d)
    0
    '''
    b = []
    for i in t:
        if i in [1,2,3,4,5,6,7,8,9,0]:
            b.append(i)
        else:
            a = sum(i)
            b.append(a)
    return sum(b)

# 2
def cumulative_sum(t):
    ''' calculate the seqeunce of the number in list and show every value
    >>> t = [1, 2, 3]
    >>> cumulative_sum(t)
    [1, 3, 6]
    >>> a = [4, 5, 6]
    >>> cumulative_sum(a)
    [4, 9, 15]
    >>> b = [1, -3, 10]
    >>> cumulative_sum(b)
    [1, -2, 8]
    >>> c = [0, 0, 1]
    >>> cumulative_sum(c)
    [0, 0, 1]
    >>> d = [1, 1, 1, 1, 1]
    >>> cumulative_sum(d)
    [1, 2, 3, 4, 5]
    '''
    new_str = []
    series = 0
    for i in t:
        series += i
        new_str.append(series)
    return new_str

# 3
def middle(t):
    ''' cut the first and the last index of list, then return new string
    >>> t = [1,2,3,4]
    >>> middle(t)
    [2, 3]
    >>> a = ['cat','dog','fish','pig']
    >>> middle(a)
    ['dog', 'fish']
    >>> b = [2, 'cat', 4, 'dog']
    >>> middle(b)
    ['cat', 4]
    >>> c = [5,6,7,8]
    >>> middle(c)
    [6, 7]
    >>> d = [1, 2, 3]
    >>> middle(d)
    [2]
    '''
    t.remove(t[0])
    t.remove(t[-1])
    return t

# 4
def chop(t):
    ''' cut the first and the last index of list, then return None
    >>> t = [1,2,3,4]
    >>> chop(t)
    >>> t
    [2, 3]
    >>> a = ['cat','dog','fish','pig']
    >>> chop(a)
    >>> a
    ['dog', 'fish']
    >>> b = [2, 'cat', 4, 'dog']
    >>> chop(b)
    >>> b
    ['cat', 4]
    >>> c = [5,6,7,8]
    >>> chop(c)
    >>> c
    [6, 7]
    >>> d = [0, 1]
    >>> chop(d)
    >>> d
    []
    '''
    t.remove(t[0])
    t.remove(t[-1])
    return None

# 5
def is_sorted(t):
    ''' return True if list are sorted, otherwise return False
    >>> is_sorted([1,2,2])
    True
    >>> is_sorted(['b','a'])
    False
    >>> is_sorted(['a','c','b'])
    False
    >>> is_sorted([1, 2, 3, 4])
    True
    >>> is_sorted([6, 5])
    False
    '''
    for i in range(len(t)):
        if t[i-1] <= t[i]:
            value = True
        else:
            value = False
    return value

# 6
def front_x(t):
    ''' sort list by start with the first 'x' word and following the other  
    >>> l = ['xyz','apple','xdfs','bdfd']
    >>> front_x(l)
    ['xdfs', 'xyz', 'apple', 'bdfd']
    >>> a = []
    >>> front_x(a)
    []
    >>> b = ['apple','xasd']
    >>> front_x(b)
    ['xasd', 'apple']
    >>> c = ['xb','xa']
    >>> front_x(c)
    ['xa', 'xb']
    >>> d = ['a','c','b']
    >>> front_x(d)
    ['a', 'b', 'c']
    '''
    x_lst = []
    lst = []
    for i in t:
        if i[0] == 'x':
            x_lst.append(i)
        else:
            lst.append(i)
    x_lst.sort()
    lst.sort()
    return x_lst+lst

# 7
def even_only(lst):
    ''' return only even number
    >>> even_only([1, 2, 3, 4])
    [2, 4]
    >>> even_only([1, 3, 5])
    []
    >>> even_only([2, 1, 3, 6])
    [2, 6]
    >>> even_only([7, 9, 11])
    []
    >>> even_only([])
    []
    '''
    even = []
    for i in lst:
        if i%2 == 0:
            even.append(i)
        else:
            pass
    return even

# 8
def love(txt):
    ''' change the last second word to love
    >>> love('I like python')
    'I love python'
    >>> love('good morning teacher')
    'good love teacher'
    >>> love('I hate programing')
    'I love programing'
    >>> love('I hate elab')
    'I love elab'
    >>> love('I hate doctest')
    'I love doctest'
    '''
    new = txt.split(' ')
    new[-2] = 'love'
    return ' '.join(new)

# 9
def is_anagram(txt1,txt2):
    ''' if both of parameter are anagram for each other return True otherwise return False
    >>> is_anagram('hello','OLLEH')
    True
    >>> is_anagram(' i ','i')
    True
    >>> is_anagram(' ','')
    True
    >>> is_anagram('good','bad')
    False
    >>> is_anagram(',','')
    False
    '''
    tx1 = txt1.lower()
    tx2 = txt2.lower()
    new1 = []
    new2 = []
    for i in tx1:
        if i == ' ':
            pass
        else:
            new1.append(i)
    for i in tx2:
        if i == ' ':
            pass
        else:
            new2.append(i)
    new1.sort()
    new2.sort()
    if new1 == new2:
        return True
    else:
        return False

# 10
def has_duplicates(lst):
    ''' return if there are the same value in lst, otherwise return false
    >>> has_duplicates([1, 2, 3, 4, 5])
    False
    >>> has_duplicates([1, 2, 1])
    True
    >>> has_duplicates([])
    False
    >>> has_duplicates([1])
    False
    >>> has_duplicates([5, 6, 7])
    False
    '''
    n = []
    for i in lst:
        if i in n:
            return True
        else:
            n.append(i)
    return False

# 11
def average(lst):
    ''' return average of number in list
    >>> average([1, 2, 3])
    2.0
    >>> average([1, 1, 2, 3, 4])
    2.2
    >>> average([0])
    0.0
    >>> average([1, 1, 1])
    1.0
    >>> average([1, 2])
    1.5
    '''
    sums = sum(lst)
    n = []
    count = 0
    for i in lst:
        n.append(i)
        count += 1
    return float(sums/count)

# 12
def centered_average(lst):
    ''' return average of number in list
    >>> centered_average([1, 1, 2, 3, 4])
    2.0
    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([1, 2])
    0.0
    >>> centered_average([1, 5, 3])
    3.0
    >>> centered_average([3, 4])
    0.0
    '''
    n = []
    count = 0
    for i in lst:
        n.append(i)
        count += 1
    n.sort()
    n.remove(n[0])
    n.remove(n[-1])
    if count <= 2:
        n = [0]
    else:
        count -= 2
    return float(sum(n)/count)

# 13
def reverse_pair(txt):
    ''' reverse word form the last to the first
    >>> reverse_pair('I hate flower')
    'flower hate I'
    >>> reverse_pair('weathering with you')
    'you with weathering'
    >>> reverse_pair(' ')
    ' '
    >>> reverse_pair('I hate elab')
    'elab hate I'
    >>> reverse_pair('good morning')
    'morning good'
    '''
    new = txt.split(' ')
    new.reverse()
    lst = ' '.join(new)
    return lst

# 14
def match_ends(lst):
    ''' if the first and the last are same
    >>> math_ends(['google', 'facebook', 'twitter'])
    0
    >>> math_ends(['goog', 'wow', 'face'])
    2
    >>> math_ends(['txt', 'first'])
    1
    >>> math_ends(['lol', 'you'])
    1
    >>> math_ends(['hate', 'elab'])
    0
    '''
    count = 0
    for i in lst:
        if len(i) >= 2:
            if i[0].lower() == i[-1].lower():
                count += 1
            else:
                pass
        else:
            pass
    return count

# 15
def remove_adjacent(lst):
    ''' make the list have member like the set
    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([1, 1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([])
    []
    >>> remove_adjacent([1, 1, 1, 1, 1])
    [1]
    >>> remove_adjacent([0])
    [0]
    ''' 
    n = []
    for i in lst:
        if i in n:
            pass
        else:
            n.append(i)
    return n