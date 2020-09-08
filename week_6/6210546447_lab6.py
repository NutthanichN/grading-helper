

#1
def ll_sum(t):
    """
    >>> t = [[5],[8,3],[6,7,8]]
    >>> ll_sum(t)
    37
    >>> t = [[-5],[0],[8,7,6]]
    >>> ll_sum(t)
    16
    >>> t = [[-8,-5],[],[7,3]]
    >>> ll_sum(t)
    -3
    >>> t = [[-93,-9],[97,9],[-98]]
    >>> ll_sum(t)
    -94
    >>> t = [[0,0],[0],[0,0,0]]
    >>> ll_sum(t)
    0
    """

    result = 0
    for num in t:
        result += sum(num)
    return result


#2
def cumulative_sum(t):
    """
    >>> t = [1,5,5,9]
    >>> cumulative_sum(t)
    [1, 6, 11, 20]
    >>> t = [-5,6]
    >>> cumulative_sum(t)
    [-5, 1]
    >>> t = [4,-6,5,-9,7]
    >>> cumulative_sum(t)
    [4, -2, 3, -6, 1]
    >>> t = [3,4,56,7,-100]
    >>> cumulative_sum(t)
    [3, 7, 63, 70, -30]
    >>> t = [0,0,0]
    >>> cumulative_sum(t)
    [0, 0, 0]
    """

    sumsum = []
    result = 0
    for i in t:
        result += i
        sumsum.append(result)
    return sumsum


#3
def middle(t):
    """
    >>> t = [1,3,7,9,11,13,7]
    >>> middle(t)
    [3, 7, 9, 11, 13]
    >>> t = [2,[3],[4,5],6]
    >>> middle(t)
    [[3], [4, 5]]
    >>> t = [3,6,9]
    >>> middle(t)
    [6]
    >>> t =[3.14]
    >>> middle(t)
    []
    >>> t = [9,10,11,12,13,14]
    >>> middle(t)
    [10, 11, 12, 13]
    """

    result = t[1:-1]
    return result


#4
def chop (t):
     """
    >>> t = [1,3,7,9,11,13,7]
    >>> chop(t)
    >>> t
    [3, 7, 9, 11, 13]
    >>> t = [2,[3],[4,5],6]
    >>> chop(t)
    >>> t
    [[3], [4, 5]]
    >>> t = [3,6,9]
    >>> chop(t)
    >>> t
    [6]
    >>> t =[3, 5, 7, 9]
    >>> chop(t)
    >>> t 
    [5, 7]
    >>> t = [9,10,11,12,13,14]
    >>> chop(t)
    >>> t
    [10, 11, 12, 13]
    """
     
     t.pop(0)
     t.pop(-1)


#5
def is_sorted(t):
    """
    >>> is_sorted([2,3,5])
    True
    >>> is_sorted(['c','b'])
    False
    >>> is_sorted(['c','d','e'])
    True
    >>> is_sorted([10,11,12])
    True
    >>> is_sorted(['lmn','opq','rst'])
    True
    """

    if t == sorted(t):
        return True
    else:
        return False


#6
def front_x(lists):
    """
    >>> lists = ['wryyyy','dio','the','world','xabix']
    >>> front_x(lists)
    ['xabix', 'dio', 'the', 'world', 'wryyyy']
    >>> lists = ['shining','apple']
    >>> front_x(lists)
    ['apple', 'shining']
    >>> lists = ['xaxx', 'b', 'c']
    >>> front_x(lists)
    ['xaxx', 'b', 'c']
    >>> lists = ['jo', 'jay', 'jeb', 'xin']
    >>> front_x(lists)
    ['xin', 'jay', 'jeb', 'jo']
    >>> lists = ['ab','six','i','x']
    >>> front_x(lists)
    ['x', 'ab', 'i', 'six']
    """

    check = []
    for num in lists:
        if num.startswith("x"):
            check.append(num)
            lists.remove(num)
    check.sort()
    lists.sort()
    sortlist = check + lists
    return sortlist


#7
def even_only(t):
    """
    >>> even_only([10,11,17,19,27,39,40])
    [10, 40]
    >>> even_only([10,12,14,16,18])
    [10, 12, 14, 16, 18]
    >>> even_only([5,6,7,2])
    [6, 2]
    >>> even_only([5,7,9,11,13])
    []
    >>> even_only([7,9,10,12,0])
    [10, 12, 0]
    """

    result = []
    for even in t :
        if even % 2 == 0:
            result.append(even)
        else:
            pass
    return result


#8
def love(text):
    """
    >>> love("I like her")
    'I love her'
    >>> love("I really like her")
    'I really love her'
    >>> love('Actually I hate her')
    'Actually I love her'
    >>> love('I do not like him')
    'I do not love him'
    >>> love("I'm kind of like her")
    "I'm kind of love her"
    """

    x = text.split(' ')
    x.pop(-2)
    x.insert(-1,'love')
    return (' ' .join(x))


#9
def is_anagram(string1,string2):
    """
    >>> is_anagram('arrange', 'rearnag')
    True
    >>> is_anagram('dio','doi')
    True
    >>> is_anagram('the world','thwer eld')
    False
    >>> is_anagram('hoha','ohho')
    False
    >>> is_anagram('Pooh','Opoh')
    True
    """

    listj = list(string1.lower())
    listj.sort()
    listk = list(string2.lower())
    listk.sort()
    if listj == listk:
        return True
    else:
        return False
    

#10
def has_duplicates(lists):
    """
    >>> has_duplicates([6,7,8,9,10])
    False
    >>> has_duplicates([3,3,3,4,3])
    True
    >>> has_duplicates([3,4,1,2,1])
    True
    >>> has_duplicates([7,6,7,3,7])
    True
    >>> has_duplicates([7,7,7,7,7,7,7])
    True
    """

    dupli = []
    for i in lists:
        if i not in dupli:
            dupli.append(i)
    if len(dupli) < len(lists) :
        return True
    else:
        return False


#11
def average(lists):
    """
    >>> average([5,6,7,8,9])
    7.0
    >>> average([3,4,5,4,5])
    4.2
    >>> average([1,1,1,1,6])
    2.0
    >>> average([6,8,5,5,5])
    5.8
    >>> average([1,1,1,1,1,1,1])
    1.0
    """

    x = sum(lists)/len(lists)
    return x


#12
def centered_average(lists):
    """
    >>> centered_average([1,2,3,4,5])
    3.0
    >>> centered_average([1,2,3,7,3])
    4.0
    >>> centered_average([1,1,0,5,4])
    2.0
    >>> centered_average([3,4,5,6,7])
    5.0
    >>> centered_average([0,0,0,0,0,0,0])
    0.0
    """

    x = sum(lists[1:-1])/(len(lists[1:-1]))
    return x


#13
def reverse_pair(rev):
    """
    >>> reverse_pair("I like her")
    'her like I'
    >>> reverse_pair("I really like her")
    'her like really I'
    >>> reverse_pair('I hate him')
    'him hate I'
    >>> reverse_pair('I do not like him')
    'him like not do I'
    >>> reverse_pair("I'm kind of like her")
    "her like of kind I'm"
    """

    a = rev.split(' ')
    b = a[::-1]
    return (' '.join(b))


#14
def match_ends(lists):
    """
    >>> match_ends(['poop','python','dio'])
    1
    >>> match_ends(['hello','my','name'])
    0
    >>> match_ends(['wryw','diod','pooh'])
    2
    >>> match_ends(['poip','qqql'])
    1
    >>> match_ends(['the','world','idoiti'])
    1
    """

    result = 0
    for a in lists :
        if len(a) >= 2 and (a[0] == a[-1]):
            result += 1
    return result


#15
def remove_adjacent(lists):
    """
    >>> remove_adjacent([2,4,5,6,7,9])
    [1, 3, 4, 5, 6, 1]
    >>> remove_adjacent([1,3,3,3,6,7])
    [1, 3, 5, 6]
    >>> remove_adjacent([3,-5,-7,-9,0])
    [3, -5, -7, -9, 0]
    >>> remove_adjacent([1,1,1,1,1])
    [1]
    >>> remove_adjacent([2,2,3,4,4,6,7])
    [2, 3, 4, 6, 7]
    """

    a = 1
    while a < len(lists):
        if lists[a] == lists[a-1]:
            lists.pop(a)
            a -= 1 
        a += 1
    return lists