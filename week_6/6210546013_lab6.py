

# 1.
def ll_sum(list):
    """ takes a list of lists of integers and adds up the elements from all of the nested lists.
    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> ll_sum(t)
    21
    >>> t = [[1,2,4], [3,4], [9,5,7]]
    >>> ll_sum(t)
    35
    >>> t = [[9,5], [9,4], [6,3]]
    >>> ll_sum(t)
    36
    >>> t = [[3,1,3,6,6], [9,1,7,8]]
    >>> ll_sum(t)
    44
    >>> t = [[0,9,6], [4,5,9], [0,5,4,6]]
    >>> ll_sum(t)
    48
    """
    x = []
    for i in range(len(list)):
        for j in range(len(list[i])):
            x.append(list[i][j])
    return sum(x)


# 2.
def cumulative_sum(list):
    """takes a list of numbers and returns the cumulative sum; that is, a new list where the ith element is the sum of the first i + 1 elements from the original list.
    >>> t = [1, 2, 3]
    >>> cumulative_sum(t)
    [1, 3, 6]
    >>> t = [4, 5, 6]
    >>> cumulative_sum(t)
    [4, 9, 15]
    >>> t = [7, 8, 9]
    >>> cumulative_sum(t)
    [7, 15, 24]
    >>> t = [3, 1, 3, 6, 6]
    >>> cumulative_sum(t)
    [3, 4, 7, 13, 19]
    >>> t = [9, 1, 7, 8]
    >>> cumulative_sum(t)
    [9, 10, 17, 25]
    """
    new_list = []
    result = 0
    for i in range(len(list)):
        result = result + list[i]
        new_list.append(result)
    return new_list


# 3.
def middle(List):
    """ that takes a list and returns a new list that contains all but the first and last elements.
    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    >>> t = [10, 9, 8, 7]
    >>> middle(t)
    [9, 8]
    >>> t = [3, 1, 3, 6, 6]
    >>> middle(t)
    [1, 3, 6]
    >>> t = [9, 1, 7, 8]
    >>> middle(t)
    [1, 7]
    >>> t = [2, 6, 1, 0]
    >>> middle(t)
    [6, 1]
    """
    new_list = []
    new_list = List.pop(-1)
    new_list = List.pop(0)
    return new_list


# 4.
def chop(List):
    """ That takes a list, modifies it by removing the first and last elements, and returns None.
    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    >>> t = [5, 6, 7, 8]
    >>> chop(t)
    >>> t
    [6, 7]
    >>> t = [3, 1, 3, 6, 6]
    >>> chop(t)
    >>> t
    [1, 3, 6]
    >>> t = [9, 1, 7, 8]
    >>> chop(t)
    >>> t
    [1, 7]
    >>> t = [2, 6, 1, 0]
    >>> chop(t)
    >>> t
    [6, 1]
    """
    List.pop(-1)
    List.pop(0)
    return


# 5.
def is_sorted(List):
    """ Takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise.
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    >>> is_sorted(['x', 'y'])
    True
    >>> is_sorted([9, 5, 4, 8])
    False
    >>> is_sorted([3, 1, 3, 6, 6,])
    False
    >>> is_sorted([1, 5, 7, 8])
    True
    """
    if sorted(List) == List:
        return True
    else:
        return False


# 6.
def front_x(List):
    """ Returns a list with the strings in sorted order, except group all the strings that begin with 'x' first.
    >>> l = ['mix', 'xyz', 'apple', 'xanadu', ‘aardvark']
    >>> front_x(l)
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    >>> l = ['xanada', 'maxim', 'xalute', 'xalact', 'pazaact']
    >>> front_x(l)
    ['xalact', 'xalute', 'xanada', 'maxim', 'pazaact']
    >>> l = ['xander', 'zero', 'one']
    >>> front_x(l)
    ['xander', 'one', 'zero']
    >>> l =['xerox', ' xaxxy', 'mine', 'craft']
    >>> front_X(l)
    ['xaxxy', 'xerox', 'craft', 'mine']
    >>> l = ['xine', 'aero' ,'space', 'xaxophone']
    >>> front_X
    ['xaxophone', 'xine', 'aero', 'space']
    """
    x_list = []
    not_x_list = []
    for i in range(len(List)):
        if List[i][0].lower() == 'x':
            x_list.append(List[i])
        if List[i][0].lower() != 'x':
            not_x_list.append(List[i])
    x_list.sort()
    not_x_list.sort()
    return x_list + not_x_list


# 7.
def even_only(list):
    """ take a list of integers, and return a new list with only even numbers.
    >>> even_only([3, 1, 4, 1, 5, 9, 2, 6, 5])
    [4, 2, 6]
    >>> even_only([3, 1, 3, 6, 6])
    [6, 6]
    >>> even_only([0, 9, 6, 4, 5, 9, 0, 5, 4, 6])
    [0, 6, 4, 0, 4, 6]
    >>> even_only([4, 5, 4, 2, 3, 1])
    [4, 4, 2]
    >>> even_only([0, 0, 0, 0, 0])
    [0, 0, 0, 0, 0]
    """
    even_list = []
    for i in range(len(list)):
        if list[i] % 2 == 0:
            even_list.append(list[i])
    return even_list


# 8.
def love(text):
    """ Return the second last word that change to “love”.
    >>> love("I like Python")
    "I love Python”
    >>> love("I really like Python”)
    "I really love Python"
    >>> love("I like ___")
    "I love ___"
    >>> love("I like programming")
    "I love programming"
    >>> love("I like your programming")
    "I your love programming"
    """
    text = text.split()
    for i in range(len(text)-1):
        if text[i] == 'like':
            text.pop(i)
    text.insert(-1, 'love')
    text = " ".join(text)
    return text


# 9.
def is_anagram(s1, s2):
    """ Takes two strings and returns True if they are anagrams.
    >>> is_anagram('arrange', 'Rear Nag’)
    True
    >>> is_anagram('ranger', 'ganrer')
    True
    >>> is_anagram('graph', 'gift')
    False
    >>> is_anagram('James', 'ja mes')
    True
    >>> is_anagram('It', 'TI')
    True
    """
    s1 = s1.split()
    s2 = s2.split()
    "".join(s1)
    "".join(s2)
    new_lists1 = []
    new_lists2 = [],
    for i in range(len(s1)):
        for j in range(len(s1[i])):
            new_lists1.append(s1[i][j].lower())
    for k in range(len(s2)):
        for l in range(len(s2[k])):
            new_lists2.append(s2[k][l].lower())
    if sorted(new_lists1) == sorted(new_lists2):
        return True
    else:
        return False


# 10.
def has_duplicates(List):
    """ Takes a list and returns True if there is any element that appears more than once. It should not modify the original list.
    >>> has_duplicates([1, 2, 3, 4, 5])
    False
    >>> has_duplicates([1, 2, 3, 4, 5, 2])
    True
    >>> has_duplicates([9,77,8,77,6,5])
    True
    >>> has_duplicates([1,2,3,4,5,6,7,8,9])
    False
    >>> has_duplicates([0, 9, 6, 4, 5, 9, 0, 5, 4, 6])
    True
    """
    List = sorted(List)
    for i in range(len(List)-1):
        if List[i] == List[i+1]:
            return True
    return False


# 11.
def average(nums):
    """ Returns the mean average of a list of numbers.
    >>> average([1, 1, 5, 5, 10, 8, 7])
    5.285714285714286
    >>> average([1,2,3,4,5,6,7,8,9])
    5.0
    >>> average([3,1,3,6,6])
    3.8
    >>> average([0,9,6,4,5,9,0,5,4,6])
    4.8
    >>> average([96, 459, 546])
    367.0
    """
    sum_nums = float(sum(nums))
    result = sum_nums/len(nums)
    return result


# 12.
def centered_average(nums):
    """ Returns a "centered" average of a list of numbers, 
    which is the mean average of the values that ignores the largest and smallest values in the list. 
    Ifthere are multiple copies of the smallest/largest value, pick just one copy.
    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([3,1,3,6,6])
    4.0
    >>> centered_average([0,9,6,4,5,9,0,5,4,6])
    4.875
    >>> centered_average([96, 459, 546])
    459.0
    >>> centered_average([0, 546, 613, 6954, 5400, 2543, 5464, 1955447])
    3586.6666666666665
    """
    nums = sorted(nums)
    nums.pop(0)
    nums.pop(-1)
    sum_nums = float(sum(nums))
    result = sum_nums/len(nums)
    return result


# 13.
def reverse_pair(string):
    """ Returns the reverse pair of the input sentence.
    >>> reverse_pair("May the fourth be with you")
    "you with be fourth the May"
    >>> reverse_pair("Love you")
    "you Love"
    >>> reverse_pair("I love You")
    "You love I"
    >>> reverse_pair("Ah ve et lo")
    "lo ve et Ah "
    >>> reverse_pair("Mine mice shock Craft")
    "Craft mice shock Mine"
    """
    string = string.split()
    string.reverse()
    return " ".join(string)


# 14.
def match_ends(List):
    """ returns the count of the number of strings where the string length is 2 or more and the first and last chars of the string are the same.
    >>> match_ends(["Gingering", “hello","wow"]
    2
    >>> match_ends(["Xerox", "Hidh", "Lovel"])
    3
    >>> match_ends(["Zabraz", "Gun", "Max"])
    1
    >>> match_ends(["Speaker", "Network", "Headphone"])
    0
    >>> match_ends(['1234561'])
    0
    """
    count = 0
    for i in range(len(List)-1):
        if len(List[i]) >= 2:
            if List[i][0].lower() == List[i][-1].lower():
                count += 1
    return count


# 15.
def remove_adjacent(List):
    """ Returns a list where all adjacent elements have been reduced to a single element.
    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([1,2,2,3,4,5,54,2,11])
    [1, 2, 3, 4, 5, 54, 2, 11]
    >>> remove_adjacent([3,1,3,6,6])
    [3, 1, 3, 6]
    >>> remove_adjacent([0, 9, 6, 4, 5, 9, 0, 5, 4, 6])
    [0, 9, 6, 4, 5, 9, 0, 5, 4, 6]
    """
    new_List = []
    for i in range(len(List)-1):
        if List[i] != List[i+1]:
            new_List.append(List[i])
    new_List.append(List[-1])
    return new_List
