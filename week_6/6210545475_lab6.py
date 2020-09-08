

# exercise 1
def ll_sum(t):
    """
    takes a list of lists of integers and adds up the elements from all of the nested lists.

    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> ll_sum(t)
    21

    >>> t = [[1], [2], [3]]
    >>> ll_sum(t)
    6

    >>> t = [[0], [1], [2, 3, 4]]
    >>> ll_sum(t)
    10

    >>> t = [[-1, -7], [-9], [-5, -6]]
    >>> ll_sum(t)
    -28

    >>> t = [[5], [5], [5]]
    >>> ll_sum(t)
    15
    """
    number = []
    for i in t:
        number += i
    return sum(number)

# exercise 2
def cumulative_sum(t):
    """
    takes a list of numbers and returns the cumulative sum; that is, a new list where the ith element is the sum of
    the first i + 1 elements from the original list.

    >>> t = [1, 2, 3]
    >>> cumulative_sum(t)
    [1, 3, 6]

    >>> t = [4, 5, 6]
    >>> cumulative_sum(t)
    [4, 9, 15]

    >>> t = [1000000, 999999.9999, 3636353]
    >>> cumulative_sum(t)
    [1000000, 1999999.9999000002, 5636352.9999]

    >>> t = [-1, -2, -3]
    >>> cumulative_sum(t)
    [-1, -3, -6]

    >>> t = [a, b, c]
    >>> cumulative_sum(t)
    Traceback (most recent call last):
    ...
    NameError: name 'a' is not defined
    """
    summary = []
    num = []
    for i in t:
        num.append(i)
        summary.append(sum(num))
    return summary

# exercise 3
def middle(t):
    """
    function called middle that takes a list and returns a new list that contains all but the first and last elements.

    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]

    >>> t = [1, 2, 3, 4, 5, 6]
    >>> middle(t)
    [2, 3, 4, 5]

    >>> t = [0]
    >>> middle(t)
    []

    >>> t = []
    >>> middle(t)
    []

    >>> t = [[1, 2],[3],[4, 5, 6],[7]]
    >>> middle(t)
    [[3], [4, 5, 6]]
    """
    new_list = []
    removed_string = []
    count = 0
    for i in t:
        if count == 0 or count == (len(t) - 1):
            removed_string.append(i)
            count += 1
        else:
            new_list.append(i)
            count += 1
    print(f"{new_list}")

# exercise 4
def chop(t):
    """
        takes a list, modifies it by removing the first and last elements, and returns None.

        >>> t = [1, 2, 3, 4]
        >>> chop(t)
        >>> t
        [2, 3]

        >>> t = [1, 2, 3, 4, 5, 6]
        >>> chop(t)
        >>> t
        [2, 3, 4, 5]

        >>> t = [0]
        >>> chop(t)
        >>> t
        []

        >>> t = []
        >>> chop(t)
        >>> t
        []

        >>> t = [[1, 2],[3],[4, 5, 6],[7]]
        >>> chop(t)
        >>> t
        [[3], [4, 5, 6]]
    """
    count = 0
    for i in t:
        if count == 0 or count == (len(t) - 1):
            t.remove(i)
            count += 1
        else:
            count += 1

# exercise 5
def is_sorted(list):
    """
        takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise.

        >>> is_sorted([1, 2, 2])
        True

        >>> is_sorted([1, 2, 3, 4, 0])
        False

        >>> is_sorted(["a","b","c"])
        True

        >>> is_sorted(["b","a"])
        False

        >>> is_sorted([b,a])
        Traceback (most recent call last):
        ...
        NameError: name 'b' is not defined
    """
    if list == sorted(list):
        return True
    else:
        return False

# exercise 6
def front_x(l):
    """
    Returns a list with the strings in sorted order, except group all the strings that begin with 'x' first.

        >>> l = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
        >>> front_x(l)
        ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']

        >>> l = ['b', 'd', 'e', 'a', 'x', 'c']
        >>> front_x(l)
        ['x', 'a', 'b', 'c', 'd', 'e']

        >>> l = ['xxx', 'xxxxx', 'x', 'xx', 'xxxx']
        >>> front_x(l)
        ['x', 'xx', 'xxx', 'xxxx', 'xxxxx']

        >>> l = ['xz', 'x3', 'x1', 'xa']
        >>> front_x(l)
        ['x1', 'x3', 'xa', 'xz']

        >>> l = ['x%', 'x*', 'x!', 'x&', 'x#']
        >>> front_x(l)
        ['x!', 'x#', 'x%', 'x&', 'x*']
    """
    x_string = []
    list_string = []
    for i in l:
        if i[0] == "x":
            x_string.append(i)
        else:
            list_string.append(i)
    return sorted(x_string) + sorted(list_string)

# exercise 7
def even_only(list):
    """
    Take a list of integers, and return a new list with only even numbers.

        >>> even_only([3,1,4,1,5,9,2,6,5])
        [4, 2, 6]

        >>> even_only([3,1,1,5,9,5])
        []

        >>> even_only([7,8,0,1,9,4,3])
        [8, 0, 4]

        >>> even_only(1+1,2+2,3+6,4+9,5+7)
        Traceback (most recent call last):
        ...
        TypeError: even_only() takes 1 positional argument but 5 were given

        >>> even_only([[2],2,3,4])
        Traceback (most recent call last):
        ...
        TypeError: unsupported operand type(s) for %: 'list' and 'int'
    """
    even_num = []
    for i in list:
        if i % 2 == 0:
            even_num.append(i)
        else:
            pass
    return even_num

# exercise 8
def love(text):
    """
    Change the second last word of the text to “love”.

        >>> love("I like Python")
        "I love Python"

        >>> love("I really like XiaoZhan")
        "I really love XiaoZhan"

        >>> love("I hate Physics")
        "I love Physics"

        >>> love(I like Python)
        File "C:/Gift/6210545475_lab6.py", line 267
        ...
        SyntaxError: invalid syntax

        >>> love("IlikePython")
        Traceback (most recent call last):
        IndexError: pop index out of range
    """
    text_list = text.split()
    text_list.pop(-2)
    text_list.insert(-1, "love")
    return " ".join(text_list)

# exercise 9
def is_anagram(text1, text2):
    """
    Takes two strings and returns True if they are anagrams.

        >>> is_anagram('arrange', 'Rear Nag')
        >>> True

        >>> is_anagram('arrange', 'Rear Nig')
        >>> False

        >>> is_anagram('Undertale', 'deltarune')
        >>> True

        >>> is_anagram('ah Nazi ox', 'Xiao Zhan')
        >>> True

        >>> is_anagram('13', '31')
        >>> True
    """
    list_1 = []
    list_2 = []
    for i in text1:
        if i == " ":
            pass
        else:
            list_1.append(i.lower())
    for i in text2:
        if i == " ":
            pass
        else:
            list_2.append(i.lower())
    return sorted(list_1) == sorted(list_2)

# exercise 10
def has_duplicates(list):
    """
    Takes a list and returns True if there is any element that appears more than once.
    It should not modify the original list.

        >>> has_duplicates([1, 2, 3, 4, 5])
        False

        >>> has_duplicates([1, 2, 3, 4, 5, 2])
        True

        >>> has_duplicates(["a", "b", "d", "e"])
        False

        >>> has_duplicates(["a", "b", "d", "e", "b"])
        True

        >>> has_duplicates([a,b,c,a])
        Traceback (most recent call last):
        ...
        NameError: name 'a' is not defined
    """
    new_list = []
    for i in list:
        if i in new_list:
            return True
        else:
            new_list.append(i)
    return False

# exercise 11
def average(nums):
    """
    Returns the mean average of a list of numbers.

        >>> average([1, 1, 5, 5, 10, 8, 7])
        5.285714285714286

        >>> average([1,2,3,4,5,6])
        3.5

        >>> average([[1], 1, 5, 5, 10, 8, 7])
        Traceback (most recent call last):
        ...
        TypeError: unsupported operand type(s) for +: 'int' and 'list'

        >>> average([a, 1, 5, 5, 10, 8, 7])
        Traceback (most recent call last):
        ...
        NameError: name 'a' is not defined

        >>> average([5,5,5,5])
        5.0
    """
    return (sum(nums))/(len(nums))

# exercise 12
def centered_average(nums):
    """
    returns a "centered" average of a list of numbers, which is the mean average of the values that ignores the
    largest and smallest values in the list. If there are multiple copies of the smallest/largest value,
    pick just one copy.

        >>> centered_average([1, 1, 5, 5, 10, 8, 7])
        5.2

        >>> centered_average([1,2,3,4,5,6])
        3.5

        >>> centered_average([1,1,1,1])
        1.0

        >>> centered_average([1,10])
        Traceback (most recent call last):
        ZeroDivisionError: division by zero

        >>> centered_average([])
        Traceback (most recent call last):
        ValueError: min() arg is an empty sequence
    """
    nums.remove(min(nums))
    nums.remove(max(nums))
    return (sum(nums))/(len(nums))

# exercise 13
def reverse_pair(text):
    """
    Two sentences are a “reverse pair” if each is the reverse of the other. Write a function reverse_pair that returns
    the reverse pair of the input sentence.

        >>> reverse_pair("May the fourth be with you")
        "you with be fourth the May"

        >>> reverse_pair("LanWangji and WeiWuxian friends forever")
        "forever friends WeiWuxian and LanWangji"

        >>> reverse_pair("Love you")
        "you Love"

        >>> reverse_pair(123)
        Traceback (most recent call last):
        ...
        AttributeError: 'int' object has no attribute 'split'

        >>> reverse_pair("Mo,dao,zu,shi")
        "Mo,dao,zu,shi"
    """
    split_text = text.split()
    return " ".join(split_text[::-1])

# exercise 14
def match_ends(list):
    """
    returns the count of the number of strings where the string length is 2 or more and the first and last chars of
    the string are the same.

        >>> match_ends(["Gingering", "hello","wow"])
        2

        >>> match_ends(["loL", "papapa","Uwu", "blaB"])
        3

        >>> match_ends(["in", "on","at"])
        0

        >>> match_ends(["Aa", "Bb","Cc"])
        3

        >>> match_ends(["A", "a","b"])
        0
    """
    match = 0
    for i in list:
        if len(i) >= 2:
            if i[0].lower() == i[-1].lower():
                match += 1
    return match

# exercise 15
def remove_adjacent(list):
    """
    Returns a list where all adjacent elements have been reduced to a single element.

        >>> remove_adjacent([1, 2, 2, 3])
        [1, 2, 3]

        >>> remove_adjacent([1, 2, 3, 1, 4])
        [1, 2, 3, 4]

        >>> remove_adjacent(["a", "b", "c", "a", "c", "d"])
        ['a', 'b', 'c', 'd']

        >>> remove_adjacent([1])
        [1]

        >>> remove_adjacent([1+0,1,0+1])
        [1]
    """
    new_list = []
    for i in list:
        if i in new_list:
            pass
        else:
            new_list.append(i)
    return new_list
