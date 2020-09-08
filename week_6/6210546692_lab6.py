

#1
def ll_sum(t):
    """
    This function called ll_sum that takes a list of lists of integers and adds up the elements from all of the
    nested lists.

    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> ll_sum(t)
    21

    >>> a = [[1, 3], [5,6], [4, 5, 7]]
    >>> ll_sum(a)
    31

    >>> b = [[1,2,3], [5,6,7], [4, 5, 9]]
    >>> ll_sum(b)
    42

    >>> c = [[1,2,15], [15,16,17], [24, 35, 49]]
    >>> ll_sum(c)
    174

    >>> d = [[23,24,15], [14,1,77], [2, 5, 9]]
    >>> ll_sum(d)
    170
    """
    total = 0
    for ch in range(len(t)):
        if type(t[ch]) == list:
            for u in range(len(t[ch])):
                total += t[ch][u]
        else:
            total += t[ch]
    return total


"""
python3 -m doctest 6210546692_lab6.py
"""

#2
def cumulative_sum(t):
    """

    """
    new_list = []
    for ch in range(len(t)):
        if ch == 0:
            new_list.append(t[ch])
        elif ch != 0 and ch < len(t):
            b = new_list[ch-1] + t[ch]
            new_list.append(b)
        else:
            c = sum(t)
            new_list.append(c)
    return new_list

#3
def middle(t):
    """
    This function that takes a list and returns a new list
    that contains all but the first and last elements.
    >>> middle([1, 2, 3, 4])
    [2, 3]
    >>> middle([4, 3, 2, 1])
    [3, 2]
    >>> middle([2, 4, 6, 8])
    [4, 6]
    >>> middle([1, 3, 5])
    [3]
    >>> middle([5, 8, 1, 3, 0])
    [8, 1, 3]

    """
    mid = len(t) - 1
    return t[1:mid]

#4
def chop(t):
    """
    This function called chop that takes a list, modifies it by removing the first and last elements, and returns
    None.

    >>> t = [1, 2, 3, 4]
    >>> print(chop(t))
    None
    >>> print(t)
    [2, 3]

    >>> t = [1, 2, 3, 4, 5]
    >>> print(chop(t))
    None
    >>> print(t)
    [2, 3, 4]

    >>> t = [4, 3, 2, 1]
    >>> print(chop(t))
    None
    >>> print(t)
    [3, 2]

    >>> t = [1, 5, 8, 1]
    >>> print(chop(t))
    None
    >>> print(t)
    [5, 8]

    >>> t =[4, 4, 4, 4]
    >>> print(chop(t))
    None
    >>> print(t)
    [4, 4]
    """
    t.remove(t[0])
    t.remove(t[-1])
    return None

#5
def is_sorted(t):
    """
    This function called is_sorted that takes a list as a parameter and returns True if the list is sorted in
    ascending order and False otherwise.

    >>> is_sorted([1,2,4])
    True
    >>> is_sorted([4,3,1])
    False
    >>> is_sorted(['a','b','c'])
    True
    >>> is_sorted(['b','a'])
    False
    >>> is_sorted(['cat','elephants'])
    True

    """
    if sorted(t) == t:
        return True
    else:
        return False

#6
def front_x(l):
    """
    This returns a list with the strings in sorted order, except
    group all the strings that begin with 'x' first.

    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    >>> front_x(['xad','fax','qwex','xsw'])
    ['xad', 'xsw', 'fax', 'qwex']
    >>> front_x(['cat','dog','xat'])
    ['xat', 'cat', 'dog']
    >>> front_x(['xxxtentacion','lil peep','travis scott','xander'])
    ['xander', 'xxxtentacion', 'lil peep', 'travis scott']
    >>> front_x(['xaxbxc','xax','xbxc','xdxexfxg'])
    ['xax', 'xaxbxc', 'xbxc', 'xdxexfxg']

    """
    new_list = []
    new_list_2 = []
    for i in range(len(l)):
        if l[i].startswith('x'):
            new_list.append(l[i])
            new_list.sort()
        else:
            new_list_2.append(l[i])
            new_list_2.sort()
    return new_list + new_list_2

#7
def even_only(l):
    """
    This function will take a list of integers, and return a new list with only even
    numbers.

    >>> even_only([1, 2, 3, 4])
    [2, 4]
    >>> even_only([4, 0, 9, 5])
    [4, 0]
    >>> even_only([1, 3, 5, 7, 9])
    []
    >>> even_only([-2, 2, 5, 8])
    [2, 8]
    >>> even_only([-2,-4,-6, 0])
    [0]
    """
    even = []
    for i in range(len(l)):
        if l[i] % 2 == 0 and l[i] >= 0:
            even.append(l[i])
    return even

#8
def love(t):
    """
    This function will change the second last word to “love”.

    >>> love('I really like python')
    'I really love python'
    >>> love('I like python')
    'I love python'
    >>> love('I like anime')
    'I love anime'
    >>> love("I doesn't like dog")
    "I doesn't love dog"
    >>> love("I don't coding")
    'I love coding'

    """
    parts = t.split()
    parts[-2] = 'love'
    return " ".join(parts)

#9
def is_anagram(a, b):
    """
    This function called is_anagram that takes two strings and returns True if they are anagrams.

    >>> is_anagram('arrange','Rear Nag')
    True
    >>> is_anagram('elephants','pele')
    False
    >>> is_anagram('rhino','ho no')
    False
    >>> is_anagram('jotaro','jatoo r')
    True
    >>> is_anagram('phumrapee','peerapmhu')
    True

    """
    s = list(a.lower())
    if " " in s:
        s.remove(" ")
    w = list(b.lower())
    if " " in w:
        w.remove(" ")
    s.sort()
    w.sort()
    if s == w:
        return True
    else:
        return False

#10
def has_duplicates(l):
    """
    takes a list and returns True if there is any element that
    appears more than once. It should not modify the original list.

    >>> has_duplicates([1,2,3,4])
    False
    >>> has_duplicates([1,2,2,3,4])
    True
    >>> has_duplicates([4,3,6,8,10])
    False
    >>> has_duplicates([5,5,5,5])
    True
    >>> has_duplicates([-2,-1,-4,-2])
    True

    """
    if sorted(l) != list(set(l)):
        return True
    else:
        return False

#11
def average(nums):
    """
    This function returns the mean average of a list of numbers.

    >>> average([1,1,5,5,10,8,7])
    5.285714285714286
    >>> average([1,10,4,9,45])
    13.8
    >>> average([2,4,6,8,10,7])
    6.166666666666667
    >>> average([1,3,5,7,9,13])
    6.333333333333333
    >>> average([8,8,9,13,15,12])
    10.833333333333334
    """
    total = sum(nums)
    av = total/len(nums)
    return av

#12
def centered_average(nums):
    """

    returns a "centered" average of a list of numbers, which is the mean average of the values that ignores the largest and smallest values in the list. If
    there are multiple copies of the smallest/largest value, pick just one copy.

    >>> centered_average([1,5,7,8,14])
    6.666666666666667
    >>> centered_average([4,3,2,1,9,10])
    4.5
    >>> centered_average([1,1,1,1,1])
    1.0
    >>> centered_average([-2,17,12,20,-11])
    9.0
    >>> centered_average([33,45,11,-44,-32,100,120])
    31.4

    """
    a = sorted(nums)
    a.pop(0)
    a.pop(-1)

    return sum(a) / len(a)

#13
def reverse_pair(t):
    """
    This function returns the reverse pair of the input sentence.

    >>> reverse_pair("I love python very much")
    'hcum yrev nohtyp evol I'
    >>> reverse_pair("Kasetsart University")
    'ytisrevinU trastesaK'
    >>> reverse_pair("I'm SKE17th!!")
    "!!ht71EKS m'I"
    >>> reverse_pair("I want to be a Data scientist")
    'tsitneics ataD a eb ot tnaw I'
    >>> reverse_pair("teacher assistants Na Rak <3")
    '3< kaR aN stnatsissa rehcaet'

    """
    return ''.join(reversed(t))

#14
def match_ends(t):
    """
    returns the count of the number of strings where the string length is 2 or more and the first and last
    chars of the string are the same.
    >>> match_ends(["Gingering", "hello", "wow"])
    2
    >>> match_ends(["racecar","swims","ring"])
    2
    >>> match_ends(["fighting","swimming","running","showering"])
    0
    >>> match_ends(["Pump","Travis Scott","James","Earn","Lil peep"])
    2
    >>> match_ends(["P'mai","P'mo","P'ai","P'wine","P'maxx","everyone are cute"])
    1
    """
    count = 0
    for i in range(len(t)):
        if t[i][0].lower() == t[i][-1].lower():
            count += 1
    return count

#15
def remove_adjacent(t):
    """
    This function returns a list
    where all adjacent elements have been reduced to a single element.

    >>> remove_adjacent([1, 2, 2, 4])
    [1, 2, 4]
    >>> remove_adjacent([1, 2, 2, 4, 5, 2])
    [1, 2, 4, 5, 2]
    >>> remove_adjacent([1, 2, 2, 3, 3, 4])
    [1, 2, 3, 4]
    >>> remove_adjacent([1, 2, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([10, 10, 11, 11, 12, 11, 13])
    [10, 11, 12, 11, 13]

    """
    new_list = []
    for i in range(len(t)):
        if t[i] != t[i - 1]:
            new_list.append(t[i])
    return new_list






