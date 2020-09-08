

# 1
def ll_sum(t):
    """ This function receive a list of number and return list sum
    >>> ll_sum([[1, 2], [3], [4, 5, 6]])
    21
    >>> ll_sum([[1,2],[3],[4]])
    10
    >>> ll_sum([[1,3,2],[3,2],[2,5]])
    18
    >>> ll_sum([[1,5],[6,3],[2]])
    17
    >>> ll_sum([[2,4,1],[3,4]])
    14
    """
    d = []
    for i in range(len(t)):
        for j in range(len(t[i])):
            d.append(t[i][j])
    return sum(d)

# 2
def cumulative_sum(t):
    """ This function receive a list of number then return their cumulative sum
    >>> cumulative_sum([1,2,3])
    [1, 3, 6]
    >>> cumulative_sum([1,5,7])
    [1, 6, 13]
    >>> cumulative_sum([2, 5, 0, 1])
    [2, 7, 7, 8]
    >>> cumulative_sum([5, 1, 6, 10])
    [5, 6, 12, 22]
    >>> cumulative_sum([3, 10, 2, 1])
    [3, 13, 15, 16]
    """
    d = []
    n = 0
    for i in range(len(t)):
        n = n + t[i]
        d.append(n)
    return d

# 3
def middle(list):
    """ This function receive a list then return the list except the first and last digit
    >>> middle([1,2,3,4])
    [2, 3]
    >>> middle([1, 2, 3, 4, 5, 6, 7, 8, 9])
    [2, 3, 4, 5, 6, 7, 8]
    >>> middle(['a', 'b', 'c', 'd'])
    ['b', 'c']
    >>> middle([3, 2, 5, 7])
    [2, 5]
    >>> middle([2, 1, 1, 1, 1, 2])
    [1, 1, 1, 1]
    """
    ans = list[1:-1]
    return ans

# 4
def chop(list):
    """ This function receive a list then modifies a list and retrun None
    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    >>> n = [2,5,2,4,6]
    >>> chop(n)
    >>> n
    [5, 2, 4]
    >>> m  = ['a','b','e','c']
    >>> chop(m)
    >>> m
    ['b', 'e']
    >>> c = ['abc','def','ghij','klm']
    >>> chop(c)
    >>> c
    ['def', 'ghij']
    >>> b = [1,3,5,7,9]
    >>> chop(b)
    >>> b
    [3, 5, 7]
    """
    list.pop()
    list.pop(0)
    return

# 5
def is_sorted(list):
    """ This function receive a list then check that the list have been sort or not
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    >>> is_sorted(['a','b','c','e'])
    True
    >>> is_sorted([4,2,6,9])
    False
    >>> is_sorted(['d','e','x','c'])
    False
    """
    n = []
    for i in range(len(list)):
        m = list[i]
        n.append(m)

    list.sort()
    if n == list:
        return True
    else:
        return False

# 6
def front_x(list):
    """ This function receive a list of letter then sort it except group that begin with x
    >>> l = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
    >>> front_x(l)
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    >>> m = ['max', 'ant', 'xyz']
    >>> front_x(m)
    ['xyz', 'ant', 'max']
    >>> b = ['kid', 'child', 'x-ray', 'xyz']
    >>> front_x(b)
    ['x-ray', 'xyz', 'child', 'kid']
    >>> c = ['abc', 'def', 'ghi', 'jkl']
    >>> front_x(c)
    ['abc', 'def', 'ghi', 'jkl']
    >>> n = ['xa', 'xb', 'xc']
    >>> front_x(n)
    ['xa', 'xb', 'xc']
    """
    x = []
    a = []
    total = []
    ans = []
    for i in list:
        if i[0] == 'x' or i[0] == 'X':
            x.append(i)
            x.sort()

        else:
            a.append(i)
            a.sort()

    total.append(x)
    total.append(a)
    for k in range(len(total)):
        for m in range(len(total[k])):
            ans.append(total[k][m])

    return ans

# 7
def even_only(list):
    """ This function receive a list of number and return an even number
    >>> even_only([3,1,4,1,5,9,2,6,5])
    [4, 2, 6]
    >>> even_only([3,5,8,7,10,22])
    [8, 10, 22]
    >>> even_only([2, 4, 6, 8])
    [2, 4, 6, 8]
    >>> even_only([1, 2, 3, 4, 5, 6, 7, 8, 9, ])
    [2, 4, 6, 8]
    >>> even_only([1, 3, 5, 7, 9])
    []
    """
    n = []
    for i in range(len(list)):
        if list[i] % 2 == 0:
            m = list[i]
            n.append(m)
    return n

# 8
def love(text):
    """ This function receive a text then change the second last word to love
    then return a modified text
    >>> love("I like Python")
    'I love Python'
    >>> love("I really like Python")
    'I really love Python'
    >>> love("I really like apple")
    'I really love apple'
    >>> love("She doesn't like banana")
    "She doesn't love banana"
    >>> love("I really like series")
    'I really love series'
    """
    text.split()
    a = text.split()[-2]
    n = text.replace(a,"love")
    return n

# 9
def is_anagram(str1,str2):
    """ This function receive two list of letter and check is it is an anagram or not
    >>> is_anagram('arrange', 'Rear Nag')
    True
    >>> is_anagram('Euro', 'orue')
    True
    >>> is_anagram('bottle', 'bot')
    False
    >>> is_anagram('calendar', 'Choco')
    False
    >>> is_anagram('water', 'Tawer')
    True
    """
    w = []
    c = []

    str1 = str1.lower()
    str2 = str2.lower()

    for i in str1:
        w.append(i)
    for j in str2:
        c.append(j)

    w.sort()
    c.sort()

    new_s1 = "".join(w)
    new_s2 = "".join(c)
    real_s1 = new_s1.lower()
    real_s2 = new_s2.lower()
    real_s1 = real_s1.strip()
    real_s2 = real_s2.strip()

    if real_s1 == real_s2:
        return True
    else:
        return False

# 10
def has_duplicates(list):
    """ This function receive a list of number and check that is any element appear
    more than one time
    >>> has_duplicates([1, 2, 3, 4, 5])
    False
    >>> has_duplicates([1, 2, 3, 4, 5, 2])
    True
    >>> has_duplicates([1, 3, 5, 7, 9])
    False
    >>> has_duplicates([2, 4, 6, 8, 2, 4])
    True
    >>> has_duplicates([2, 2, 3, 1, 3])
    True
    """
    list.sort()
    for i in list:
        if list[i] == list[i+1]:
            return True
        else:
            return False

# 11
def average(nums):
    """ This function receive a list of number then calculate average mean of the list
    >>> average([1, 1, 5, 5, 10, 8, 7])
    5.285714285714286
    >>> average([1, 2, 3, 4, 5])
    3.0
    >>> average([2, 4, 6, 8, 10])
    6.0
    >>> average([1, 3, 5, 7, 9])
    5.0
    >>> average([1, 1, 2, 2, 3, 3, 4, 4])
    2.5
    """
    s = sum(nums)
    d = len(nums)
    ans = s/d
    return ans

# 12
def centered_average(nums):
    """ This function receive a list of number then calculate the center average
    of a list of number
    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([1, 2, 3, 4, 5, 6])
    3.5
    >>> centered_average([2, 4, 6, 8, 10])
    6.0
    >>> centered_average([5, 10, 15, 20, 25])
    15.0
    >>> centered_average([1, 3, 5, 7, 9])
    5.0
    """
    nums.sort()
    nums.pop(0)
    nums.pop()
    s = sum(nums)
    d = len(nums)
    ans = s/d
    return ans

# 13
def reverse_pair(text):
    """ This function receive a text then return it as a reverse
    >>> reverse_pair("May the fourth be with you")
    'you with be fourth the May'
    >>> reverse_pair("Happy birth day to you")
    'you to day birth Happy'
    >>> reverse_pair("Mini hand care set")
    'set care hand Mini'
    >>> reverse_pair("let take a break")
    'break a take let'
    >>> reverse_pair("work hard play hard")
    'hard play hard work'
    """
    split_text = text.split()
    split_text.reverse()
    ans = " ".join(split_text)
    return ans

# 14
def match_ends(list):
    """ This function receive a list of strings and return the count of the number
    of stru=ing that the first and last chars of string are th same
    >>> match_ends(["Gingering", "hello","wow"])
    2
    >>> match_ends(['Gang', 'Group', 'wow', 'lol'])
    3
    >>> match_ends(['wow', 'lol', 'bob', 'nope'])
    3
    >>> match_ends(['Dad', 'mom', 'child'])
    2
    >>> match_ends(['pop', 'ioi', 'wow'])
    3
    """
    count = 0
    list = " ".join(list)
    n = list.lower()
    m = n.split()
    for i in range(len(m)):
        if m[i][0] == m[i][-1]:
            count += 1
    return count

# 15
def remove_adjacent(list):
    """ This function receive a list of number and modify a list by reduce an
    adjacent then return a modified list
    >>> remove_adjacent([1, 1, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([1, 2, 3, 3, 4])
    [1, 2, 3, 4]
    >>> remove_adjacent([2, 4, 6, 6, 8])
    [2, 4, 6, 8]
    >>> remove_adjacent([1, 2, 3, 4, 5, 5])
    [1, 2, 3, 4, 5]
    """
    for i in range(len(list)):
        if list[i] == list[i+1]:
            list.remove(list[i+1])
            return list
