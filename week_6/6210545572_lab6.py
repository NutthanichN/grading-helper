

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# 1
def ll_sum(n):
    """
    Function above will adds up the elements in list n below
    >>> n = [[3, 5], [2], [4, 6]]
    >>> ll_sum(n)
    20
    >>> n = [[1], [2], [7, 7, 7]]
    >>> ll_sum(n)
    24
    >>> n = [[4,5,6],[10]]
    >>> ll_sum(n)
    25
    >>> n = [[10,9],[6],[7],[8]]
    >>> ll_sum(n)
    40
    >>> n = [[1,9],[3],[4],[6],[7,8,9]]
    >>> ll_sum(n)
    47
    """
    result = 0
    for number in n:
        result += sum(number)
    return result


# 2
def cumulative_sum(n):
    """
    >>> n = [1, 2, 3]
    >>> cumulative_sum(n)
    [1, 3, 6]
    >>> n = [4, 6, 12]
    >>> cumulative_sum(n)
    [4, 10, 22]
    >>> n = [2, 3, 4]
    >>> cumulative_sum(n)
    [2, 5, 9]
    >>> n = [7, 8, 9]
    >>> cumulative_sum(n)
    [7, 15, 24]
    >>> n = [10, 20, 30]
    >>> cumulative_sum(n)
    [10, 30, 60]
    """
    cumsum = []
    total = 0
    for v in n:
        total += v
        cumsum.append(total)
    return cumsum


# 3
def middle(n):
    """
    Function above will slice the first and last elements in list n below
    >>> n = [1, 2, 3, 4]
    >>> middle(n)
    [2, 3]
    >>> n = [1, 2, 3, 4, 5]
    >>> middle(n)
    [2, 3, 4]
    >>> n = [11, 22, 33, 44]
    >>> middle(n)
    [22, 33]
    >>> n = [10, 9, 8, 7, 6, 5, 4, 3]
    >>> middle(n)
    [9, 8, 7, 6, 5, 4]
    >>> n = [9, 19, 29, 39, 49, 59]
    >>> middle(n)
    [19, 29, 39, 49]
    """
    result = n[1:-1]
    return result


# 4
def chop(n):
    """
    Function above will remove first and last elements in list n
    >>> n = [1, 2, 3, 4]
    >>> chop(n)
    >>> n
    [2, 3]
    >>> n = [1, 2, 3, 4, 5]
    >>> chop(n)
    >>> n
    [2, 3, 4]
    >>> n = [1, 2, 3, 4, 5, 6]
    >>> chop(n)
    >>> n
    [2, 3, 4, 5]
    >>> n = [1, 2, 3, 4, 5, 6, 7]
    >>> chop(n)
    >>> n
    [2, 3, 4, 5, 6]
    >>> n = [1, 2, 3, 4, 5, 6, 7, 8]
    >>> chop(n)
    >>> n
    [2, 3, 4, 5, 6, 7]
    """
    n.pop(0)
    n.pop(-1)


# 5
def is_sorted(n):
    """
    Function above will check list n if it's sorted it will return true if not the function will return false like below
    >>> is_sorted([1, 2, 3])
    True
    >>> is_sorted(['e', 'd'])
    False
    >>> is_sorted([3, 2, 4])
    False
    >>> is_sorted(['d', 'e'])
    True
    >>> is_sorted(['a', 'b'])
    True
    >>> is_sorted(['a', 'b', 'c'])
    True
    """
    result = sorted(n)
    if result == n:
        return True
    else:
        return False


# 6
def front_x(words):
    """
    This function will returns a list in sorted order but will group all the strings that begin with 'x' first.
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    >>> front_x(['banana', 'xyz', 'orange'])
    ['xyz', 'orange', 'banana']
    >>> front_x(['xxxtentacion', 'final', 'album'])
    ['xxxtentacion', 'final', 'album']
    >>> front_x(['fine', 'good', 'xbye'])
    ['xbye', 'fine', 'good']
    >>> front_x(['aaaa', 'bbbb', 'cccc', 'xddd', 'eeee'])
    ['xddd', 'eeee', 'aaaa', 'bbbb', 'cccc']
    """
    check = []
    for n in words:
        if n.begins_with("x"):
            check.append(n)
            words.remove(n)
    check.sort()
    words.sort()
    sort_x_list = check + words
    return sort_x_list




# 7
def even_only(nn):
    """
    >>> even_only([1, 2, 3, 4, 5, 6, 7, 8])
    [2, 4, 6, 8]
    >>> even_only([11, 22, 33, 44, 55, 66, 77, 88])
    [22, 44, 66, 88]
    >>> even_only([10, 20, 30, 40, 50, 60, 70, 80])
    [10, 20, 30, 40, 50, 60, 70, 80]
    >>> even_only([5, 10, 15, 20, 25])
    [10, 20]
    >>> even_only([9, 19, 29, 39, 49, 59, 60])
    [60]
    """
    c =[]
    for number in nn:
        if number %2==0:
            c.append(number)
    return c

# 8
def love(n):
    """
    This function will change the second last word to “love” whatever before is.
    >>> love_changed('I really like Python')
    'I really love Python'
    >>> love_changed('I like Python')
    'I love Python'
    >>> love_changed('I hate python')
    'I love python'
    >>> love_changed('I did not like python')
    'I did not love python'
    >>> love_changed('I did not hate math')
    'I did not love math'
    """
    words = n.split(" ")
    words[-2] = "love"
    new = " ".join(words)
    return new

# 9
def is_anagram(str1, str2):
    """
    if str1 and str2 are anagrams the function will return True
    >>> is_anagram('arrange', 'Rear Nag')
    True
    >>> is_anagram('love', 'you')
    False
    >>> is_anagram('hate','you')
    False
    >>> is_anagram('fine','neif')
    True
    >>> is_anagram('groove', 'vegroo')
    True
    """
    l1 = list(str1.lower())
    l2 = list(str2.lower())
    if " " in l2:
        l2.remove(" ")
    l1.sort()
    l2.sort()
    if l1 == l2:
        return True
    else:
        return False

# 10
def has_duplicates(n):
    """
    if elements in the list appear more than one times this function will return True
    >>> has_duplicates([1, 2, 3, 4, 5])
    False
    >>> has_duplicates([1, 2, 3, 4, 5, 1, 2, 3, 4])
    True
    >>> has_duplicates([1, 2, 1, 2, 3, 1, 2, 1, 2, 1])
    True
    >>> has_duplicates([1, 2, 3, 4, 4, 3, 2, 1])
    True
    >>> has_duplicates([3, 4, 5, 6])
    False
    """
    n.sort()
    for i in range(len(n) - 1):
        if n[i] == n[i + 1]:
            return True
        else:
            return False

# 11
def average(nums):
    """
    This function will returns average of a list
    >>> average([1, 2, 3, 4, 5])
    3.0
    >>> average([2, 3, 4, 5, 5, 4, 3, 2])
    3.5
    >>> average([10, 20, 30, 40])
    25.0
    >>> average([9, 19, 29, 39, 49])
    29.0
    >>> average([11, 22, 33, 44, 55])
    33.0
    """
    sumup = sum(nums)
    lenght = len(nums)
    average = sumup/lenght
    return average


# 12
def centered_average(nums):
    """
    This function will returns centered average, the mean average of the values
    >>> centered_average([1, 2, 3, 4, 5])
    3.0
    >>> centered_average([2, 3, 4, 5, 5, 4, 3, 2])
    3.5
    >>> centered_average([10, 20, 30, 40])
    25.0
    >>> centered_average([9, 19, 29, 39, 49])
    29.0
    >>> centered_average([11, 22, 33, 44, 55])
    33.0
    """
    nums.sort()
    cen_num = nums[1:-1]
    centered = sum(cen_num)/(len(nums)-2)
    return  centered


# 13
def reverse_pair(string):
    """
    This function will returns reverse of the input elements
    >>> reverse_pair("May the fourth be with you")
    'you with be fourth the May'
    >>> reverse_pair("I hate python")
    'python hate I'
    >>> reverse_pair("Lisa and Jenduck")
    'Jenduck and Lisa'
    >>> reverse_pair("Forget you")
    'you Forget'
    >>> reverse_pair("Hope not F")
    'F not Hope'
    """
    array = []
    re_list = string.split()
    re_list.reverse()
    array = " ".join(re_list)
    return array



# 14
def match_ends(words):
    """
    This function will returns the count of the number if the string length is 2 or more than that the first and last
    are the same then count
    >>> match_ends(["pop, top, job"])
    1
    >>> match_ends(["well, warm, white"])
    0
    >>> match_ends(["pineapple, soju, lalisal"])
    1
    >>> match_ends(["wow, mom, dad"])
    3
    >>> match_ends(["cartoon, jeejee, parn"])
    0

    """
    result = 0
    for lisa in words:
        if len(lisa) >= 2:
            if lisa.lower()[0] == lisa.lower()[-1]:
                result += 1
    return result


# 15
def remove_adjacent(n):
    """
    This function will returns a list where all adjacent elements decrease to a single one
    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([1, 2, 2, 3, 4, 4])
    [1, 2, 3, 4]
    >>> remove_adjacent([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
    [1, 2, 3, 4, 5]
    >>> remove_adjacent([1, 2, 1, 2, 3, 1, 2, 1, 2, 1])
    [1, 2, 3]
    >>> remove_adjacent([1, 3, 1, 4, 1, 5])
    [1, 3, 4, 5]
    """
    result = []
    for i in n:
       if len(result) == 0 or i != result[-1]:
        result.append(i)
        return result

