

#1
def ll_sum(t):
    """
    >>> t = [[1,2],[3],[4,5,6]]
    >>> ll_sum(t)
    21
    >>> t = [[2,3],[4],[5,6,7]]
    >>> ll_sum(t)
    27
    >>> t = [[5,6],[7],[8,9,10]]
    >>> ll_sum(t)
    45
    >>> t = [[4,4],[5],[6,7,8]]
    >>> ll_sum(t)
    34
    >>> t = [[1,2],[3],[4,4,5]]
    >>> ll_sum(t)
    19
    """
    x = list(sum(t, []))
    return sum(x)

#2
def cumulative_sum(t):
    """
    >>> t = [1,2,3]
    >>> cumulative_sum(t)
    [1,3,6]
    >>> t = [2,3,4]
    >>> cumulative_sum(t)
    [2,5,9]
    >>> t = [4,5,6]
    >>> cumulative_sum(t)
    [4,9,15]
    >>> t = [7,8,9]
    >>> cumulative_sum(t)
    [7,15,24]
    >>> t = [1,1,2]
    >>> cumulative_sum(t)
    [1,2,4]
    """
    for i in range(1, len(t)):
        x = t[i]
        y = t[i-1]
        t[i] = x + y
        return t

# 3
def middle(t):
    """
    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2,3]
    >>> t = [5, 6, 7, 8]
    >>> middle(t)
    [6,7]
    >>> t = [1, 1, 2, 2]
    >>> middle(t)
    [1,2]
    >>> t = [5, 6, 8, 9]
    >>> middle(t)
    [6,8]
    >>> t = [3, 4, 5, 6]
    >>> middle(t)
    [4,5]
    """
    del(t[0])
    del(t[-1])
    x = t
    return x

# 4
def chop(t):
    """
    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2,3]
    >>> t = [2, 2, 3, 5]
    >>> chop(t)
    >>> t
    [2,3]
    >>> t = [3, 6, 7, 9]
    >>> chop(t)
    >>> t
    [6,7]
    >>> t = [5, 5, 6, 7]
    >>> chop(t)
    >>> t
    [5,6]
    >>> t = [11, 12, 13, 14]
    >>> chop(t)
    >>> t
    [12,13]
    """
    del(t[0], t[-1])
    return None

# 5
def is_sorted(t):
    """
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    >>> is_sorted([3, 4, 5])
    True
    >>> is_sorted([4, 1, 3])
    False
    >>> is_sorted(['a', 'b', 'c'])
    True
    """
    if(min(t) == t[0] and max(t) == t[-1]):
        return True
    else:
        return False

# 6
def front_x(l):
    """
    >>> l = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
    >>> front_x(l)
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    >>> l = ['ant', 'xo', 'bee', 'xxx', 'one']
    >>> front_x(l)
    ['xo', 'xxx', 'ant', 'bee', 'one']
    >>> l = ['ace', 'abc', 'zoo', 'tot', 'xpp']
    >>> front_x(l)
    ['xpp', 'abc', 'ace', 'tot', 'zoo']
    >>> l = ['uuu', 'eye', 'iphone', 'xcv', 'yell']
    >>> front_x(l)
    ['xcv', 'eye', 'iphone', 'uuu', 'yell']
    >>> l = ['so', 'sad', 'auu', 'xox', 'tear']
    >>> front_x(l)
    ['xox', 'auu', 'tear', 'sad', 'so']
    """
    first = [x for x in l if x[0]=="x"]
    last  = [y for y in l if y[0]!="x"]
    return sorted(first) + sorted(last)

# 7
def even_only(list):
    """
    >>> even_only([3,1,4,1,5,9,2,6,5])
    [4,2,6]
    >>> even_only([3,3,6,2,5,10,1,3,3])
    [6,2,10]
    >>> even_only([2,1,4,8,8,1,2,7,5])
    [2,4,8]
    >>> even_only([4,2,1,1,9,1,8,11,7])
    [4,2,8]
    >>> even_only([12,1,4,13,9,9,2,6,4])
    [12,4,2,6]

    """
    e = [i for i in list if i%2==0]
    return e

# 8
def love(text):
    """
    >>> love("I like Python”)
    "I love Python”
    >>> love("I really like Python”)
    "I really love Python"
    >>> love("I like iphone”)
    "I love iphone"
    >>> love("I very like s1000”)
    "I very love s1000 "
    >>> love("I like you”)
    "I love you"

    """
    t = text.split()
    t[-2] = "love"
    return " ".join(t)

# 9
def is_anagram(x,y):
    """
    >>> is_anagram('arrange', 'Rear Nag’)
    True
    >>> is_anagram('tree', 'reai')
    False
    >>> is_anagram('your', 'uyor’)
    True
    >>> is_anagram('murder', 'De Murr’)
    True
    >>> is_anagram('Hello', 'hiyeh')
    False
    """
    L = list(x.lower())
    L.sort()
    y1 = y.split()
    a = "".join(y1)
    L2 = list(a.lower())
    L2.sort()
    return L == L2

# 10
def has_duplicates(list):
# def has_duplicate(list):
    """
    >>> has_duplicates([1, 2, 3, 4, 5])
    False
    >>> has_duplicates([1, 2, 3, 4, 5, 2])
    True
    >>> has_duplicates([1, 2, 3, 4, 5, 3])
    True
    >>> has_duplicates([1, 2, 3, 4, 5, 6])
    False
    >>> has_duplicates([1, 2, 3, 4, 5, 5])
    True
    """
    x = 0
    cout = 0
    while x < len(list):
        if(list.count(list[x]) > 1):
            return True
        else:
            cout += 1
        x += 1
    if cout > 0 :
        return False

# 11
def average(nums):
    """
    >>> average([1, 1, 5, 5, 10, 8, 7])
    5.285714285714286
    >>> average([2, 1, 3, 4, 12])
    4.4
    >>> average([15, 3, 5, 1])
    6
    >>> average([1, 7, 8, 15, 1, 8, 8])
    6.857142857
    >>> average([9, 6, 6, 5, 3, 2, 7])
    5.428571429

    """
    all = 0
    for i in nums:
        all += i
    return all/len(nums)

# 12
def centered_average(nums):
    """
    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([2, 3, 6, 5, 6, 12, 7])
    5.4
    >>> centered_average([4, 4, 7, 6, 3, 13, 5])
    5.2
    >>> centered_average([1, 1, 2, 3, 9, 8, 2])
    3.2
    >>> centered_average([5, 2, 3, 5, 12, 3, 3])
    3.8
    """
    all = 0
    for i in nums:
        all += i
    return (all - max(nums) - min(nums)) / (len(nums)- 2)

# 13
def reverse_pair(word):
    """
    >>> reverse_pair("May the fourth be with you")
    "you with be fourth the May"
    >>> reverse_pair("you are god in the world")
    "world the in god are you"
    >>> reverse_pair("I have iphone")
    "iphone have I"
    >>> reverse_pair("s1000 is the best")
    "best the is s1000"
    >>> reverse_pair("Trust me if you can")
    "can you if me Trust"
    """
    x = list(word.split())
    y = x[::-1]
    return " ".join(y)

# 14
def match_ends(list):
    """
    >>> match_ends(["Gingering", "hello","wow"]
    2
    >>> match_ends(["venv", "apply","raper"]
    2
    >>> match_ends(["love", "yellow","gambling"]
    1
    >>> match_ends(["betting", "naruto","yes"]
    0
    >>> match_ends(["sacculus", "sadness","macadam"]
    3

    """
    a = " ".join(list)
    b = a.lower()
    c = b.split()
    count = 0
    for i in range(0, len(list)):
        if c[i][0] == c[i][-1]:
            count += 1
    return count

# 15
def remove_adjacent(L):
    """
    >>> remove_adjacent([1, 2, 2, 3])
    [1,2,3]
    >>> remove_adjacent([1, 2, 3, 3])
    [1,2,3]
    >>> remove_adjacent([1, 4, 4, 5])
    [1,4,5]
    >>> remove_adjacent([2, 5, 5, 6])
    [2,5,6]
    >>> remove_adjacent([1, 1, 2, 3])
    [1,2,3]

    """
    x = list(set(L))
    return x


