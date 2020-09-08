

# 1. Write a function called ll_sum that takes a list of lists of integers and adds up the elements from all of the
# nested lists. For example:
# >>> t = [[1, 2], [3], [4, 5, 6]]
# >>> ll_sum(t)
# 21
def ll_sum(t):
    """

    :param t: a list of integers
    :return: an add up elements of integers list

    >>> s = [1,2,3,4,5]
    >>> ll_sum(s)
    15
    >>> c = [[1,2],2,[3,4]]
    >>> ll_sum(c)
    12
    >>> w = [2,3,4,[2,4]]
    >>> ll_sum(w)
    15
    >>> q = [1]
    >>> ll_sum(q)
    1
    >>> f = [2,3,4]
    >>> ll_sum(f)
    9

    """
    num = 0
    for number in t:
        if type(number) == list:
            num += ll_sum(number)
        else:
            num += number
    return num



# 2. Write a function called cumulative_sum that takes a list of numbers and returns the cumulative sum; that is, a
# new list where the ith element is the sum of the first i + 1 elements from the original list. For example:
# >>> t = [1, 2, 3]
# >>> cumulative_sum(t)
# [1, 3, 6]
def cumulative_sum(t):
    """

    :param t: list of integers
    :return: cumulative sum of integers inthe list

    >>> a = [1,3,6]
    >>> cumulative_sum(a)
    [1, 4, 10]
    >>> e = [2,3,[4]]
    >>> cumulative_sum(e)
    [2, 5, 9]
    >>> f = [2,66,7]
    >>> cumulative_sum(f)
    [2, 68, 75]
    >>> p = [2,[3],[5],6]
    >>> cumulative_sum(p)
    [2, 5, 10, 16]
    >>> x = [100,101,102,103]
    >>> cumulative_sum(x)
    [100, 201, 303, 406]

    """
    a = []
    num = 0
    for number in t:
        if type(number) == list:
            num += ll_sum(number)
            a.append(num)
        else:
            num += number
            a.append(num)
    return a



# 3. Write a function called middle that takes a list and returns a new list that contains all but the first and last
# elements. For example:
# >>> t = [1, 2, 3, 4]
# >>> middle(t)
# [2, 3]
def middle(t):
    """

    :param t: list of integers
    :return: the middle part of the list

    >>> t = [2,3,4,5]
    >>> middle(t)
    [3, 4]
    >>> d = [1,[2],[3,5],6]
    >>> middle(d)
    [[2], [3, 5]]
    >>> s = [1,2]
    >>> middle(s)
    []
    >>> x = [3,4,5]
    >>> middle(x)
    [4]
    >>> w = []
    >>> middle(w)
    []

    """
    return t[1:-1]



# 4. Write a function called chop that takes a list, modifies it by removing the first and last elements, and returns
# None. For example:
# >>> t = [1, 2, 3, 4]
# >>> chop(t)
# >>> t
# [2, 3]
def chop(t):
    """

    :param t: list of integers
    :return: none

    >>> f = [2,3,4]
    >>> chop(f)
    >>> f
    [3]
    >>> d = [2,[3,4],1]
    >>> chop(d)
    >>> d
    [[3, 4]]
    >>> w = [1,2]
    >>> chop(w)
    >>> w
    []
    >>> q =[1,2,3,4,5,6,7,8,9]
    >>> chop(q)
    >>> q
    [2, 3, 4, 5, 6, 7, 8]
    >>> n = [0,0,0,0,0]
    >>> chop(n)
    >>> n
    [0, 0, 0]

    """
    del t[0]
    del t[-1]



# 5. Write a function called is_sorted that takes a list as a parameter and returns True if the list is sorted in
# ascending order and False otherwise. For example:
# >>> is_sorted([1, 2, 2])
# True
# >>> is_sorted(['b', 'a'])
# False
def is_sorted(list):
    """

    :param list: input list
    :return: true or false depend on whether the list is sorted in ascending order or not

    >>> f = [1,2,3]
    >>> is_sorted(f)
    True
    >>> s = [3,3,3]
    >>> is_sorted(s)
    True
    >>> z = [3,2,8]
    >>> is_sorted(z)
    False
    >>> x = [0]
    >>> is_sorted(x)
    True
    >>> g = ['sort','is']
    >>> is_sorted(g)
    False

    """
    if list == sorted(list):
        return True
    else:
        return False



# 6. Given a list of strings, write a function front_x that returns a list with the strings in sorted order, except
# group all the strings that begin with 'x' first. For example:
# >>> l = ['mix', 'xyz', 'apple', 'xanadu', ‘aardvark']
# >>> front_x(l)
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
def front_x(list):
    """

    :param list: input list with string
    :return: sorted list with words start with x in front

    >>> x = ['xxxx','xann','wpspp','app']
    >>> front_x(x)
    ['xann', 'xxxx', 'app', 'wpspp']
    >>> a =['1','2','xana']
    >>> front_x(a)
    ['xana', '1', '2']
    >>> c = ['max','xolo','opqw']
    >>> front_x(c)
    ['xolo', 'max', 'opqw']
    >>> l = ['a','a','x']
    >>> front_x(l)
    ['x', 'a', 'a']
    >>> d = ['x','xa','xz']
    >>> front_x(d)
    ['x', 'xa', 'xz']

    """
    list1 = []
    for x in list[0:]:
        if x.startswith('x'):
            list1.append(x)
            list.remove(x)
    return sorted(list1)+sorted(list)



# 7. Create a function even_only(list) that will take a list of integers, and return a new list with only even
# numbers.
# >>> even_only([3,1,4,1,5,9,2,6,5])
# [4, 2, 6]
def even_only(list):
    """

    :param list: list of integers
    :return: even number only list

    >>> w = [1,2,3,4,5,6]
    >>> even_only(w)
    [2, 4, 6]
    >>> x = [2,2,2]
    >>> even_only(x)
    [2, 2, 2]
    >>> q = [1,3,5]
    >>> even_only(q)
    []
    >>> a = [7,6,3,4]
    >>> even_only(a)
    [6, 4]
    >>> h = [0]
    >>> even_only(h)
    [0]

    """
    list1 = []
    for x in list:
        if x % 2 == 0:
            list1.append(x)
    return list1



# 8. Create a function love(text) that will change the second last word to “love”.
#
# >>> love("I like Python”)
# "I love Python”
# >>> love("I really like Python”)
# "I really love Python"
def love(text):
    """

    :param text: input string
    :return: string but replace the second last word with 'love'

    >>> love('Flolida in USA')
    'Flolida love USA'
    >>> love('Orange grape pinapple soda')
    'Orange grape love soda'
    >>> love('cat cat')
    'love cat'
    >>> love('Python hate you')
    'Python love you'
    >>> love('seven eleven')
    'love eleven'

    """
    t = text.split(' ')
    t[-2] = ['love']
    a = (t[0:-2] + t[-2] + t[-1:])
    s = ' '.join(a)
    return s
# print(love('s ss'))



# 9. Two words are anagrams if you can rearrange the letters from one to spell the other. Write a function
# called is_anagram that takes two strings and returns True if they are anagrams.
# >>> is_anagram('arrange', 'Rear Nag’)
# >>> True
def is_anagram(x,y):
    """

    :param x: string 1
    :param y: string 2
    :return: true or false if the string is anagram or not

    >>> is_anagram('cat','rat')
    False
    >>> is_anagram('potato','topato')
    True
    >>> is_anagram('solo','yolo')
    False
    >>> is_anagram('Wally','wal ly')
    True
    >>> is_anagram('susan','usnaS')
    True

    """
    x = str.lower(x)
    y = str.lower(y)
    x = x.replace(' ','')
    y = y.replace(' ','')
    return sorted(x) == sorted(y)



# 10. Write a function called has_duplicates that takes a list and returns True if there is any element that
# appears more than once. It should not modify the original list.
# >>> has_duplicates([1, 2, 3, 4, 5])
# False
# >>> has_duplicates([1, 2, 3, 4, 5, 2])
# True
def has_duplicates(t):
    """

    :param t: list of integers
    :return: true or false whether or not it has duplicate

    >>> has_duplicates([1,2,3,4,5,6])
    False
    >>> has_duplicates([2,3,4,5,2])
    True
    >>> has_duplicates([2])

    >>> has_duplicates([2,2,2,2])
    True
    >>> has_duplicates([1,4,6,2,5,1,3])
    True

    """
    x = t[:]
    x.sort()
    for i in range(len(x)-1):
        if x[i] == x[i+1]:
            x.remove(x[0])
            return True
        else:
            return False



# 11. Create a function average(nums) that returns the mean average of a list of numbers.
#
# >>> average([1, 1, 5, 5, 10, 8, 7])
# 5.285714285714286
def average(nums):
    """

    :param nums: list of integers
    :return: average sum of list

    >>> average([1,1,1,1])
    1.0
    >>> average([2,2])
    2.0
    >>> average([12,3,5,2])
    5.5
    >>> average([1])
    1.0
    >>> average([3,4,6,2,0])
    3.0

    """
    return sum(nums)/len(nums)



# 12. Create a function centered_average(nums) that returns a "centered" average of a list of numbers,
# which is the mean average of the values that ignores the largest and smallest values in the list. If
# there are multiple copies of the smallest/largest value, pick just one copy.
#
# >>> centered_average([1, 1, 5, 5, 10, 8, 7])
# 5.2
def centered_average(nums):
    """

    :param nums: list of integers
    :return: centered average

    >>> centered_average([1,1,1,1])
    1.0
    >>> centered_average([2,4,6,7,4,2,3])
    3.8
    >>> centered_average([4])
    0
    >>> centered_average([2,7,4,1,4])
    3.3333333333333335
    >>> centered_average([4,1,6,2])
    3.0

    """
    sum = 0
    t = len(nums) - 2
    l = nums.index(max(nums))
    s = nums.index(min(nums))
    if l == s:
            for i in range(len(nums)):
                if nums[i] == nums[s]:
                    l = i
    for i in range(len(nums)):
            if i != l and i != s:
                sum = sum + nums[i]
    if t > 0:
            return sum / t
    else:
            return sum



# 13. Two sentences are a “reverse pair” if each is the reverse of the other. Write a function reverse_pair
# that returns the reverse pair of the input sentence.
# >>> reverse_pair("May the fourth be with you")
# "you with be fourth the May"
def reverse_pair(text):
    """

    :param text: input string
    :return: reversed pair of string text

    >>> reverse_pair('USA is in America')
    'America in is USA'
    >>> reverse_pair('chocolate flavour ice cream')
    'cream ice flavour chocolate'
    >>> reverse_pair('a rat running in a jar')
    'jar a in running rat a'
    >>> reverse_pair('cat say meow')
    'meow say cat'
    >>> reverse_pair('the big bang theory')
    'theory bang big the'

    """
    text = text.split(' ')
    text = reversed(text)
    text = ' '.join(text)
    return text



# 14.Given a list of strings, write a function match_ends that returns the count of the
# number of strings where the string length is 2 or more and the first and last
# chars of the string are the same.
# >>> match_ends(["Gingering", “hello","wow"]
# 2
def match_ends(string):
    """

    :param string: input string
    :return: number of string with same first and last character

    >>> match_ends(['running','jumping','lol'])
    1
    >>> match_ends(['aaaa','bbbb','cccc'])
    3
    >>> match_ends(['apple','orange','grape'])
    0
    >>> match_ends(['othello','chess'])
    1
    >>> match_ends(['dodod'])
    1

    """
    i = 0
    for x in string:
        if len(x) >= 2 and x[0].upper() == x[-1].upper():
            i += 1
    return i



# 15.Given a list of numbers, write a function remove_adjacent that returns a list
# where all adjacent elements have been reduced to a single element.
# >>> remove_adjacent([1, 2, 2, 3])
# [1, 2, 3]
def remove_adjacent(list):
    """

    :param list: list of integers
    :return: list that remove adjacent integers

    >>> remove_adjacent([1,2,2,2,3,4])
    [1, 2, 3, 4]
    >>> remove_adjacent([1,2,3,4])
    [1, 2, 3, 4]
    >>> remove_adjacent([3,3,4,4,5])
    [3, 4, 5]
    >>> remove_adjacent([1,1])
    [1]
    >>> remove_adjacent([2,2,3,5,1,1,])
    [2, 3, 5, 1]

    """
    x = []
    for num in list:
        if len(x) == 0 or num != x[-1]:
            x.append(num)
    return x