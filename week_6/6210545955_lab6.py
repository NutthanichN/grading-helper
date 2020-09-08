

#1
def ll_sum(t):
    """ This function sum all the values inside the list (including list in list)
    >>> ll_sum([1,2,[3]])
    6
    >>> ll_sum([1,4,[3]])
    8
    >>> ll_sum([[1,6,7],2,[3]])
    19
    """
    result = 0
    for x in t:
        if type(x) == list:
            result += ll_sum(x)
        else:
            result += x
    return result

#2
def cumulative_sum(t):
    """" this function add the value to element by adding from the before elements.
    >>> cumulative_sum([1,3,5])
    [1, 4, 9]
    >>> cumulative_sum([1,7,10])
    [1, 8, 18]
    >>> cumulative_sum([1,3,5])
    [1, 4, 9]
    """
    total_sum = []
    initial = 0
    for i in t:
        initial = initial + i
        total_sum.append(initial)
    return total_sum

#3
def middle(t):
    """ This function remove the first and last elements in the list.
    >>> middle([1, 2, 3, 4])
    [2, 3]
    >>> middle(["ske", "is", "the", "best"])
    ['is', 'the']
    >>> middle(["Air", "plane"])
    []
    """
    del t[-1]
    del t[0]
    return t

#4
def chop(t):
    """ This function remove the first and last elements in the list.
    >>> chop([1, 2, 3, 4])
    [2, 3]
    >>> chop(["ske", "is", "the", "best"])
    ['is', 'the']
    >>> chop(["Air", "plane"])
    []
    """
    del t[-1]
    del t[0]
    return t

#5
def is_sorted(t):
    """ This function check if the given list is sorted.
    >>> is_sorted([1,2,3])
    True
    >>> is_sorted([5,1,3])
    False
    >>> is_sorted([1,6,10])
    True
    """
    a = t[:]
    a.sort()
    if a == t:
        return True
    else:
        return False

#6
def front_x(t):
    """ This function rearranges element inside the list except the word starts with "x"
    >>> front_x(["xxx","abc","ccc"])
    ['xxx', 'abc', 'ccc']
    >>> front_x(["xxx","abc","xxu","iop"])
    ['xxu', 'xxx', 'abc', 'iop']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']

    """
    initial = []
    for x in t:
        if x.startswith("x"):
            initial.append(x)
            t.remove(x)
    initial.sort()
    t.sort()
    new = initial + t
    return new

#7
def even_only(t):
    """ This function removes elements those are odd numbers from the list.
    >>> even_only([1,2,3,4,5,6])
    [2, 4, 6]
    >>> even_only([1,1,3,3,5,6])
    [6]
    >>> even_only([1,3,5,7,9,11,13])
    []
    """
    newlist = []
    for i in t:
        if i%2 == 0:
            newlist.append(i)
    return newlist

#8
def love(t):
    """ This function replaces second last word with "love"
    >>> love("I dislike him.")
    'I love him.'
    >>> love("I will never like you.")
    'I will never love you.'
    >>> love("I hate you.")
    'I love you.'
    """
    list_splitted = t.split()
    second_last = list_splitted[-2]
    changed = t.replace(second_last,"love")
    return changed

#9
def is_anagram(text1,text2):
    """" This function checks if those 2 word are anagram.
    >>> is_anagram("text","tetx")
    True
    >>> is_anagram("cheat","chat")
    False
    >>> is_anagram("swear","wears")
    True
    """
    t1 = list(text1)
    t2 = list(text2)
    t1.sort()
    t2.sort()
    if ''.join(t1) == ''.join(t2):
        return True
    else:
        return False
#10
def has_duplicates(t):
    """ This function checks if list's element are duplicated.
    >>> has_duplicates([1,1,2])
    True
    >>> has_duplicates([1,3,8])
    False
    >>> has_duplicates([1,1,1])
    True
    """
    start = t[:]
    start.sort()
    for i in range(len(start)-1):
        if start[i] == start[i+1]:
            return True
        else:
            return False

#11
def average(nums):
    """ This function evaluate average value of the list.
    >>> average([10,15,35])
    20.0
    >>> average([1, 1, 5, 5, 10, 8, 7])
    5.285714285714286
    >>> average([2,2,2])
    2.0
    """
    a = sum(nums)
    b = len(nums)
    avg = a/b
    return avg
#12
def centered_average(nums):
    """ This function calculates average of a list of numbers, which is the mean average of the values that ignores the largest and smallest values in the list.
    >>> centered_average([1,3,5,6])
    4.0
    >>> centered_average([1,7,6])
    6.0
    >>> centered_average([3,8,9,7])
    7.5
    """
    nums.sort()
    new_list = nums[1:-1]
    sum_list = sum(new_list)
    avg = sum_list/len(new_list)
    return avg

#13
def reverse_pair(t):
    """This function reverse the words.
    >>> reverse_pair("Hello world")
    'world Hello'
    >>> reverse_pair("Good to see you.")
    'you. see to Good'
    >>> reverse_pair("I love you")
    'you love I'
    """
    new = t.split()
    number = len(new)
    changed = []
    while number >=1:
        changed.append(new[number-1])
        number = number - 1
    changed = " ".join(changed)
    return changed

#14
def match_ends(t):
    """ This function tell the number of strings where the string length is 2 or more and the first and lastchars of the string are the same
    >>> match_ends(["great", "pump","lil"])
    2
    >>> match_ends(["greag", "pump","lil"])
    3
    >>> match_ends(["greet", "pop","lol"])
    2
    """
    num = 0
    for x in t:
        if len(x) >= 2:
            if x.startswith(x[0]) == x.endswith(x[0]):
                num += 1
    return num

#15
def remove_adjacent(t):
    """ This function removes duplicated element in the list
    >>> remove_adjacent([1,1,2,3,4,4])
    [1, 2, 3, 4]
    >>> remove_adjacent([1,3,5,7,9])
    [1, 3, 5, 7, 9]
    >>> remove_adjacent([100,100,100])
    [100]
    """
    removed = []
    for x in t:
        if (x in removed):
            continue
        else:
            removed.append(x)
    return removed