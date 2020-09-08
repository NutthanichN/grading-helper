

def ll_sum(x):
    """1. Write a function called ll_sum that takes a list of lists of integers and adds up the elements from all of the
    nested lists. For example
    >>> i = [[1, 2], [3], [4, 5, 6]]
    21
    >>> i = [1,1,1, [1, 1, [1,1]]]
    7
    >>> i = [1,2,3,4,5,6]
    21
    >>> i = [1,2,3,4,5,6,[1,1,1,1]]
    25
    >>> i = [[1,2],3,4,5,6,[6,6]]
    33
    """
    result = 0 
    for i in x:
        if type(i) == list:
            result += ll_sum(i)
        else:
            result += i 
    return result

def cumulative_sum(l):
    """2. Write a function called cumulative_sum that takes a list of numbers and returns the cumulative sum; that is, a
    new list where the ith element is the sum of the first i + 1 elements from the original list. For example:
    >>> t = [1, 2, 3]
    [1, 3, 6]
    >>> list = [1, 2, 4, 8, 16]
    [1, 3, 7, 15, 31]
    >>> list = [1, 2, 4,]
    [1, 3, 7]
    >>> list = [1, 1, 1, 1, 1]
    [1, 2, 3, 4, 5]
    >>>list = [1, 2]
    [1, 3]
    """
    total = 0
    result = []
    for i in l:
        total += i
        result.append(total)
    return result

def middle(x):
    """3. Write a function called middle that takes a list and returns a new list that contains all but the first and last
    elements. For example:
    >>> t = [1, 2, 3, 4]
    [2, 3]
    >>>t = [1, 1, 1, 1]
    [1, 1]
    >>>t = [6, 3, 7, 8, 10, 500]
    [3, 7, 8, 10]
    >>>t = [100, 300, 700, 800, 100, 500]
    [300, 700, 800, 100]
    >>>t = [0, 0, 0, 0, 0]
    [0, 0, 0]
    """
    t = len(x) - 1
    return x[1:t]

t = [1, 2, 3, 4]
def chop(t):
    """4. Write a function called chop that takes a list, modifies it by removing the first and last elements, and returns
    None.
    >>> t = [1, 2, 3, 4]
    [2, 3]
    >>> chop(1,2,3,4,5)
    (2,3,4)
    >>> chop(2,3,4,5,6,7)
    (3,4,5,6)
    >>> chop(5,6,7,8)
    (6,7)
    >>> chop(1,2,3,5)
    (2,3)
    >>> chop(8,11,12,15)
    (11,12)
    """
    del t[0]
    del t[-1]
chop(t)


def is_sorted(stuff):
    """5. Write a function called is_sorted that takes a list as a parameter and returns True if the list is sorted in
    ascending order and False otherwise. For example:
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    >>> is_sorted([100, 5, 6580])
    False
    >>> is_sorted([100, 101, 102])
    True
    >>> is_sorted(['a', 'b', 'c' ])
    True
    >>>is_sorted(['a', 'l', 'f'])
    False
    """
    for i in range(1,len(stuff)):
        if stuff[i - 1] > stuff[i]:
           return False
    return True

def front_x(words):
    """6. Given a list of strings, write a function front_x that returns a list with the strings in sorted order, except
    group all the strings that begin with 'x' first. For example:
    >>> l = ['mix', 'xyz', 'apple', 'xanadu', ‘aardvark']
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    >>> l = ['yo', 'boe', 'noob']
    ['boe', 'noob', 'yo']
    >>> l = ['king', 'never', 'die']
    ['die', 'king', 'never']
    >>> l = ['puss', 'kuss', 'slay', 'yer']
    ['kuss', 'puss', 'slay', 'yer']
    >>> l = ['prayut', 'chanocha']
    ['chanocha', 'prayut']
    """
    xlist = []
    alist = []
    for word in words:
        if word.startswith('x'):
            xlist.append(word)
        else:
            alist.append(word)
    return sorted(xlist) + sorted(alist)

def even_only(list):
    """7. Create a function even_only(list) that will take a list of integers, and return a new list with only even
    numbers.
    >>> even_only([3,1,4,1,5,9,2,6,5])
    [4, 2, 6]
    >>> even_only([1,2,3,5,7,11])
    [2]
    >>> even_only([2,4,6,8,10])
    [2, 4, 6, 8, 10]
    >>> even_only([22,23,24,26,28])
    [22, 24, 26, 28]
    >>> even_only([2,22,32,42])
    [2, 22, 32, 42]
    """
    num = []
    for n in list:
        if n % 2 == 0:
            num.append(n)
    return num

def love(a):
    """8. Create a function love(text) that will change the second last word to “love”.
    >>> love("I like Python”)
    "I love Python”
    >>> love("I really like Python”)
    "I really love Python"
    >>> love("I like dog")
    'I love dog'
    >>> love("I like beautiful woman")
    'I love beautiful woman'
    >>> love("I really like jimmy")
    'I really love jimmy'
    >>> love("I like prayut")
    'I love prayut'
    """
    x = (a.split(' '))
    x[-2] = "love"
    return " ".join(x)

def is_anagram(x,y):
    """Two words are anagrams if you can rearrange the letters from one to spell the other. Write a function
    called is_anagram that takes two strings and returns True if they are anagrams.
    >>> is_anagram('boy', 'asfa')
    False
    >>> is_anagram("lover","lrove")
    True
    >>> is_anagram("ball","labl")
    True
    >>> is_anagram("ploys","ylops")
    True
    >>>is_anagram("sdfs","dsgsg")
    False
    """
    p = x.lower()
    q = y.lower()
    r = p.replace(" ","")
    s = q.replace(" ","")
    p1 = list(r)
    q = sorted(p1)
    r1 = list(s)
    s = sorted(r1)
    if q == s :
        return True
    else:
        return False


def has_duplicates(my_list):
    """Write a function called has_duplicates that takes a list and returns True if there is any element that
    appears more than once. It should not modify the original list.
    >>> has_duplicates([1, 2, 3, 4, 5])
    False
    >>> has_duplicates([1, 2, 3, 4, 5, 2])
    True
    >>> has_duplicates([1,1,1,1])
    False
    >> has_duplicates([52, 25, 36, 25]
    True
    >>> has_duplicates([100, 320, 459, 853]
    False
    >>> has_duplicates([0, 26, 45, 85]
    False
    """
    i = 0
    while i < len(my_list):
        if my_list.count(my_list[i]) > 1:
            return True
        elif i == (len(my_list) - 1):
            return False
        i += 1

def average(lst):
    # def Average(lst):
    """11. Create a function average(nums) that returns the mean average of a list of numbers.
    >>> Average([1, 1, 1, 1, 1])
    1.0
    >>> Average([1, 2, 3, 4, 5, 6])
    3.5
    >>> Average([1, 5, 6, 13, 25, 78])
    21.333333333333332
    >>> Average([10, 20, 30, 40, 50])
    30.0
    >>> Average([250, 365, 125, 365, 489])
    318.8
    """
    return sum(lst) / len(lst) 


def centered_average(nums):
    """12. Create a function centered_average(nums) that returns a "centered" average of a list of numbers,
    which is the mean average of the values that ignores the largest and smallest values in the list. If
    there are multiple copies of the smallest/largest value, pick just one copy.
    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([1, 1, 1 1, 1, 1, 1])
    1.0
    >>> centered_average([1, 2, 3, 4, 5, 6])
    3.5
    >>> centered_average([1, 3, 5, 10, 36]))
    6.0
    >>> centered_average([25, 36, 12, 350, 24, 289])
    93.5
    """
    min1=nums[0]
    max1=nums[0]
    for item in nums:
        if item > max1:
            max1 = item
        if item < min1:
            min1 = item
    sum1=(sum(nums)-(min1+max1))/(len(nums)-2)
    return sum1

def reverse_pair(x):
    """13. Two sentences are a “reverse pair” if each is the reverse of the other. Write a function reverse_pair that returns the reverse pair of the input sentence.
    >>> reverse_pair("May the fourth be with you")
    "you with be fourth the May"
    >>> reverse_pair("Prayut is the best")
    best the is Prayut
    >>> reverse_pair("i alway love her")
    her love alway i
    >>> reverse_pair("oof white")
    white oof
    >>> reverse_pair("just boring ass f")
    f ass boring just   
    """
    s = x.split(" ")
    a = s[::-1]
    "".join(a)
    return " ".join(a)


def match_ends(words):
    """14.Given a list of strings, write a function match_ends that returns the count of the
    number of strings where the string length is 2 or more and the first and last
    chars of the string are the same.
    >>> match_ends(["Gingering", “hello","wow"]
    2
    >>> match_ends(["hello","wow"]
    1
    >>> match_ends(["play", "wow"]
    1
    >>> match_ends(["playing", "wow", "wow"]
    2
    >>> match_ends(["sum", "pum", "sim"]
    0
    """
    count = 0
    for i in words:
        if len(i) >= 2 and i[-1] == i[0]:
            count = count + 1
    return count

def remove_adjacent(nums):
    """15.Given a list of numbers, write a function remove_adjacent that returns a list
    where all adjacent elements have been reduced to a single element.
    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([1, 1, 2, 2, 4, 5])
    [1, 2, 4, 5]
    >>> remove_adjacent([1, 1, 2, 2, 2])
    [1, 2]
    >>> remove_adjacent([180, 320, 180, 365, 365, 2, 1])
    [180, 320, 180, 365, 2, 1]
    >>> remove_adjacent([22,22,62,62,32,32,44,25])
    [22, 62, 32, 44, 25]
    """
    i = 1
    while i < len(nums):    
        if nums[i] == nums[i-1]:
            nums.pop(i)
            i -= 1  
        i += 1
    return nums


if __name__ == '__main__':
    import doctest
    doctest.testmod()