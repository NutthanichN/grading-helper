

#1
def ll_sum(t):
    """function that takes a list of integers and adds up the elements from all of the nested lists
    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> ll_sum(t)
    21
    >>> t = [[1],[4,6],[7]]
    >>> ll_sum(t)
    18
    >>> t = [[0,1],[3,5],[8,9]]
    >>> ll_sum(t)
    26
    >>> t = [[5,6],[4,8]]
    >>> ll_sum(t)
    23
    >>> t = [[0,5],[5,6],[8,7]]
    >>> ll_sum(t)
    31
    """
    total = 0
    for i in t:
        for sum in i:
            total += sum
    return total

#2
def cumulative_sum(t):
    """function that takes a list of numbers and returns the cumulative sum
    >>> a = [1,2,3]
    >>> cumulative_sum(a)
    [1, 3, 6]
    >>> b = [2,4,6]
    >>> cumulative_sum(b)
    [2, 6, 12]
    >>> c = [5,2,3]
    >>> cumulative_sum(c)
    [5, 7, 10]
    >>> d = [1,4,5]
    >>> cumulative_sum(d)
    [1, 5, 10]
    >>> e = [7,8,4]
    >>> cumulative_sum(e)
    [7, 15, 19]

    """
    sum = []
    total = 0
    for number in t:
        total += number
        sum.append(total)
    return sum

#3
def middle(t):
    """function that takes a list and returns a new list that contains all but the first and last elements
    >>> a = [1,2,3,4]
    >>> middle(a)
    [2, 3]
    >>> b = [2,6,8,7]
    >>> middle(b)
    [6, 8]
    >>> c = [2,4,6,8]
    >>> middle(c)
    [4, 6]
    >>> d = [4,8,3,7]
    >>> middle(d)
    [8, 3]
    >>> e = [1,6,6,9]
    >>> middle(e)
    [6, 6]
    """
    mid = t[:]
    del mid[0]
    del mid[len(mid)-1]
    return mid

#4
def chop(t):
    """function that takes a list, modifies it by removing the first and last elements, and returns None
    >>> a = [1,2,3,4]
    >>> chop(a)
    [2, 3]
    >>> b = [2,3,4,5]
    >>> chop(b)
    [3, 4]
    >>> c = [7,4,8,6]
    >>> chop(c)
    [4, 8]
    >>> d = [1,0,3,2]
    >>> chop(d)
    [0, 3]
    >>> e = [4,5,8,1]
    >>> chop(e)
    [5, 8]
    """
    del t[0]
    del t[len(t) - 1]
    return t

#5
def is_sorted(t):
    """function that takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise
    >>> is_sorted([1,2,2])
    True
    >>> is_sorted(['b','a'])
    False
    >>> is_sorted([2,4,6])
    True
    >>> is_sorted(['p','o','n','m'])
    False
    >>> is_sorted([1,8,9])
    True
    """
    for i in range(len(t)-1):
        
        if t[i+1] >= t[i]:
          return True  

    return False

#6
def front_x(l):
    """function that returns a list with the strings in sorted order, except group all the strings that begin with 'x' first
    >>> a = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
    >>> front_x(a)
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    >>> b = ['muay', 'coke', 'xenial', 'venom']
    >>> front_x(b)
    ['xenial', 'coke', 'muay', 'venom']
    >>> c = ['timmy', 'xessxa', 'macaba']
    >>> front_x(c)
    ['xessxa', 'macaba', 'timmy']
    >>> d = ['pukky', 'teemu', 'xhaka', 'granit']
    >>> front_x(d)
    ['xhaka', 'granit', 'pukky', 'teemu']
    >>> e = ['leg', 'xy']
    >>> front_x(e)
    ['xy', 'leg']
    """
    x_word = []
    any_word = []

    for word in l:
        if word[0] == 'x':
            x_word.append(word)
        else:
            any_word.append(word)
    return sorted(x_word) + sorted(any_word)

#7
def even_only(list):
    """function that will take a list of integers, and return a new list with only even numbers
    >>> a = [3,1,4,1,5,9,2,6,5]
    >>> even_only(a)
    [4, 2, 6]
    >>> b = [6,2,1,0,5]
    >>> even_only(b)
    [6, 2, 0]
    >>> c = [4,5,6,7,8]
    >>> even_only(c)
    [4, 6, 8]
    >>> d = [0,1,8,4,6,3,5,9]
    >>> even_only(d)
    [0, 8, 4, 6]
    >>> e = [0,1,7,6,5,3,9]
    >>> even_only(e)
    [0, 6]
    """
    even = []
    for number in list:
        if number %2 == 0:
            even.append(number)
    return even

#8
def love(text):
    """function that will change the second last word to “love”
    >>> love("I like Python")
    'I love Python'
    >>> love("I really like Python")
    'I really love Python'
    >>> love("I like you so much")
    'I love you so much'
    >>> love("But he also like her so much too")
    'But he also love her so much too'
    >>> love("I guess i have to stop like her")
    'I guess i have to stop love her'
    """
    if "like" in text:
        a = text.replace("like", "love")
        return a

#9
def is_anagram(string1,string2):
    """function that takes two strings and returns True if they are anagrams
    >>> is_anagram('arrange', 'rearnag')
    True
    >>> is_anagram('eric', 'cire')
    True
    >>> is_anagram('freak', 'kaerf')
    True
    >>> is_anagram('taco', 'capo')
    False
    >>> is_anagram('red', 'dem')
    False
    """
    string_1 = sorted(string1)
    string_2 = sorted(string2)
    if string_1 == string_2:
        return True
    else:
        return False

#10
def has_duplicates(t):
    """function that takes a list and returns True if there is any element that appears more than once
    >>> has_duplicates([1,2,3,4,5])
    False
    >>> has_duplicates([1,2,3,4,5,2])
    True
    >>> has_duplicates([1,4,6,8,7])
    False
    >>> has_duplicates([1,1,2])
    True
    >>> has_duplicates([8,7,6,5,4])
    False
    """
    a = 0
    for x in t:
        for y in t:
            if x == y:
                a = a+1
    if a > len(t):
        return True
    else:
        return False

#11
def average(nums):
    """function that returns the mean average of a list of numbers
    >>> average([1, 1, 5, 5, 10, 8, 7])
    5.285714285714286
    >>> average([3, 4, 5])
    4.0
    >>> average([1, 8, 7, 0])
    4.0
    >>> average([8, 4, 6, 2])
    5.0
    >>> average([6, 4, 7, 2, 3])
    4.4
    """
    average = sum(nums) / len(nums)
    return average

#12
def centered_average(nums):
    """function that returns a "centered" average of a list of numbers, that ignores the largest and smallest values in the list
    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([1, 5, 2, 8, 10])
    5.0
    >>> centered_average([2, 4, 8, 6, 9])
    6.0
    >>> centered_average([3, 4, 5, 6, 9, 8])
    5.75
    >>> centered_average([1, 8, 4, 7, 5, 9])
    6.0
    """
    max_value = nums[0]
    min_value = nums[0]
    sum = 0
    for n in nums:
        max_value = max(max_value, n)
        min_value = min(min_value, n)
        sum += n

    return (sum - max_value - min_value) / (len(nums) - 2)

#13
def reverse_pair(a):
    """function that returns the reverse pair of the input sentence
    >>> reverse_pair("May the fourth be with you")
    'you with be fourth the May'
    >>> reverse_pair("hell the What")
    'What the hell'
    >>> reverse_pair("Are you in or not")
    'not or in you Are'
    >>> reverse_pair("How are you doing")
    'doing you are How'
    >>> reverse_pair("Liverpool is the best")
    'best the is Liverpool'
    """
    input_word = a.split(' ')
    input_word1 = input_word[-1::-1]
    output_word = (' '.join(input_word1))
    return output_word

#14
def match_ends(word):
    """function that returns the count of the number of strings and the first and last chars of the string are the same
    >>> match_ends(["gingering","hello","wow"])
    2
    >>> match_ends(["aralle","flicker","tony"])
    0
    >>> match_ends(["nobeton","sucks","kak","ona"])
    3
    >>> match_ends(["noon","red","beer","wine"])
    1
    >>> match_ends(["oreo","oppo","ehere","elite"])
    4
    """
    n = 0
    for i in word:
        if len(i) >= 2 and (i[-1] == i[0]):
            n += 1
    return n

#15
def remove_adjacent(t):
    """function that returns a list where all adjacent elements have been reduced to a single element
    >>> a = [1,2,2,3]
    >>> remove_adjacent(a)
    [1, 2, 3]
    >>> b = [1,4,4,2]
    >>> remove_adjacent(b)
    [1, 4, 2]
    >>> c = [8,7,7,4]
    >>> remove_adjacent(c)
    [8, 7, 4]
    >>> d = [7,8,8,9]
    >>> remove_adjacent(d)
    [7, 8, 9]
    >>> e = [1,6,6,9]
    >>> remove_adjacent(e)
    [1, 6, 9]
    """
    result = []
    for num in t:
        if len(result) == 0 or num != result[-1]:
            result.append(num)
    return result














