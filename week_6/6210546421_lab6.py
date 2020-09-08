

#1
def ll_sum(num):
    """this function takes a list of lists of integers and adds up the elements from all of the
    nested lists.

    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> ll_sum(t)
    21
    >>> u = [[1, 3], [3], [4, 5, 6]]
    >>> ll_sum(u)
    22
    >>> v = [[1, 2], [5], [4, 5, 6]]
    >>> ll_sum(v)
    23
    >>> w = [[2, 2], [4], [5, 5, 6]]
    >>> ll_sum(w)
    24
    >>> x = [[1], [3], [4, 6, 6, 9]]
    >>> ll_sum(x)
    29
    >>> y = [[1,2,3,4,5,6,7,8,9,10]]
    >>> ll_sum(y)
    55

    """
    result = 0
    for item in num:
        if type(item) == list:
            result += ll_sum(item)
        else:
            result += item
    return result

#2
def cumulative_sum(eiei):
    """this function takes a list of numbers and returns the cumulative sum; that is, a
    new list where the ith element is the sum of the first i + 1 elements from the original list.

    >>> t = [1, 2, 3]
    >>> cumulative_sum(t)
    [1, 3, 6]

    >>> t = [1, 5, 18]
    >>> cumulative_sum(t)
    [1, 6, 24]

    >>> t = [1, 3, 5]
    >>> cumulative_sum(t)
    [1, 4, 9]

    >>> t = [2, 3, 4, 5, 6]
    >>> cumulative_sum(t)
    [2, 5, 9, 14, 20]

    >>> t = [1, 2]
    >>> cumulative_sum(t)
    [1, 3]

    >>> t = [4, 6, 8]
    >>> cumulative_sum(t)
    [4, 10, 18]

    """
    result = []
    jeejee = 0
    for number in eiei:
        jeejee = jeejee + number
        result.append(jeejee)
    return result

#3
def middle(a):
    """this function takes a list and returns a new list that contains all but the first and last
    elements.

    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    >>> t = [1, 1, 8, 4]
    >>> middle(t)
    [1, 8]
    >>> t = [1, 2, 3, 4, 5, 6, 7, 8]
    >>> middle(t)
    [2, 3, 4, 5, 6, 7]
    >>> t = [1, 3, 3, 3, 1]
    >>> middle(t)
    [3, 3, 3]
    >>> t = [21, 22, 23, 24, 25]
    >>> middle(t)
    [22, 23, 24]
    >>> t = [99, 98, 97]
    >>> middle(t)
    [98]

    """
    b = len(a) - 1
    return a[1:b]

#4
def chop(x):
    """this function takes a list, modifies it by removing the first and last elements, and returns
    None.

    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    >>> t = [2, 2, 3, 6]
    >>> chop(t)
    >>> t
    [2, 3]
    >>> t = [1, 3, 5, 7, 9]
    >>> chop(t)
    >>> t
    [3, 5, 7]
    >>> t = [15, 18, 19, 27, 11, 9, 10]
    >>> chop(t)
    >>> t
    [18, 19, 27, 11, 9]
    >>> t = [11, 12, 13, 14, 15]
    >>> chop(t)
    >>> t
    [12, 13, 14]
    >>> t = [3, 4, 5, 6, 7]
    >>> chop(t)
    >>> t
    [4, 5, 6]

    """
    del x[0::(len(x)-1)]
    return None

#5
def is_sorted(j):
    """this function takes a list as a parameter and returns True if the list is sorted in
    ascending order and False otherwise.

    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    >>> is_sorted([1, 3, 2])
    False
    >>> is_sorted(['a', 'b'])
    True
    >>> is_sorted([1, 2, 3, 4])
    True
    >>> is_sorted(['w', 'b'])
    False
    >>> is_sorted([18, 9, 27])
    False
    >>> is_sorted(['t', 'z'])
    True
    >>> is_sorted([1, 2, 2, 3, 4, 5])
    True
    >>> is_sorted(['d', 'r'])
    True
    >>> is_sorted([100, 300, 1000])
    True
    >>> is_sorted(['q', 'a', 'z'])
    False

    """
    if sorted(j) == j:
        return True
    else:
        return False

#6
def front_x (l) :
    """this function returns a list with the strings in sorted order, except
    group all the strings that begin with 'x' first.

    >>> l = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
    >>> front_x(l)
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    >>> l = ['six', 'abz', 'paruj', 'pwine']
    >>> front_x(l)
    ['abz', 'paruj', 'pwine', 'six']
    >>> l = ['pitchapa', 'qwz', 'xcoco']
    >>> front_x(l)
    ['xcoco', 'pitchapa', 'qwz']
    >>> l = ['beef', 'xav', 'jeejee']
    >>> front_x(l)
    ['xav', 'beef', 'jeejee']
    >>> l = ['xct', 'www', 'pet', 'ox']
    >>> front_x(l)
    ['xct', 'ox', 'pet', 'www']
    >>> l = ['xcry', 'or']
    >>> front_x(l)
    ['xcry', 'or']

    """
    x = []
    for i in l:
        if i.startswith("x"):
            x.append(i)
            l.remove(i)
    x.sort()
    l.sort()
    return x + l
#7
def even_only(list):
    """this function will take a list of integers, and return a new list with only even
    numbers.

    >>> even_only([3,1,4,1,5,9,2,6,5])
    [4, 2, 6]
    >>> even_only([9,10,11])
    [10]
    >>> even_only([2,3,4,5,6])
    [2, 4, 6]
    >>> even_only([3,6,9])
    [6]
    >>> even_only([8,9,7,5,6,18])
    [8, 6, 18]
    >>> even_only([6,9,10,11])
    [6, 10]

    """
    even = []
    for num in list:
      if num%2 == 0 :
        even.append(num)
    return even

#8
def love(text):
    """this function will change the second last word to “love”.

    >>> love("I like Python")
    'I love Python'
    >>> love("I really like Python")
    'I really love Python'
    >>> love("I hate you")
    'I love you'
    >>> love("I dont like you")
    'I dont love you'
    >>> love("You hate me")
    'You love me'
    >>> love("I really like TParuj")
    'I really love TParuj'
    >>> love("I like Pwine")
    'I love Pwine'

    """
    textlist = text.split(' ')
    textlist[-2] = 'love'
    newt = ' '.join(textlist)
    return newt

#9
def is_anagram(str1,str2) :
    """this function takes two strings and returns True if they are anagrams.

    >>> is_anagram('arrange','Rear Nag')
    True
    >>> is_anagram('pitch','stupid')
    False
    >>> is_anagram('saelim','limsae')
    True
    >>> is_anagram('apple','mylove')
    False
    >>> is_anagram('dog','god')
    True

    """
    a = list(str1.lower())
    b = list(str2.lower())
    if ' ' in b :
        b.remove(' ')
    a.sort()
    b.sort()
    if a == b:
        return True
    else:
        return False

#10
def has_duplicates(list):
    """this  that takes a list and returns True if there is any element that
    appears more than once. It should not modify the original list.

    >>> has_duplicates([1, 2, 3, 4, 5])
    False
    >>> has_duplicates([1, 2, 3, 4, 5, 2])
    True
    >>> has_duplicates([6, 9, 18])
    False
    >>> has_duplicates([1, 1, 1, 1])
    True
    >>> has_duplicates([8, 9, 11, 12])
    False
    >>> has_duplicates([4, 6, 8, 4])
    True
    >>> has_duplicates([5, 6, 7, 5, 8, 9])
    True

    """
    i = 0
    while i < len(list):
        if list.count(list[i])>1:
            return True
        elif i == (len(list)-1):
            return False
        i = i+1

#11
def average(nums) :
    """this function returns the mean average of a list of numbers.

    >>> average([1, 1, 5, 5, 10, 8, 7])
    5.285714285714286
    >>> average([1, 2, 3])
    2.0
    >>> average([18, 9, 3])
    10.0
    >>> average([2, 4])
    3.0
    >>> average([99, 1])
    50.0
    >>> average([69, 7, 4, 3, 1])
    16.8

    """
    a = sum(nums)
    b = len(nums)
    aver = a/b
    return aver

#12
def centered_average(nums) :
    """this function returns a "centered" average of a list of numbers,
    which is the mean average of the values that ignores the largest and smallest values in the list. If
    there are multiple copies of the smallest/largest value, pick just one copy.

    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([1, 3, 5, 7])
    4.0
    >>> centered_average([18, 9, 3, 2, 1, 5])
    4.75
    >>> centered_average([3, 6, 7, 8, 1, 2])
    4.5
    >>> centered_average([2, 4, 6, 8])
    5.0
    >>> centered_average([1, 2, 4, 6, 9, 5])
    4.25

    """
    nums.sort()
    newnum = nums[1:-1]
    aver_num= sum(newnum)/(len(nums)-2)
    return  aver_num

#13
def reverse_pair(text):
    """this function returns the reverse pair of the input sentence.

    >>> reverse_pair("May the fourth be with you")
    'you with be fourth the May'
    >>> reverse_pair("My name is Jeejee")
    'Jeejee is name My'
    >>> reverse_pair("eiei is haha")
    'haha is eiei'
    >>> reverse_pair("Im so tried")
    'tried so Im'
    >>> reverse_pair("soy bad")
    'bad soy'
    >>> reverse_pair("Kasetsart unvst")
    'unvst Kasetsart'
    """
    list = text.split(' ')
    newlist = list[::-1]
    newtext = " ".join(newlist)
    return  newtext

#14
def match_ends(text):
    """this function returns the count of the number of strings where the string length is 2 or more and the first and last
    chars of the string are the same.

    >>> match_ends(["Gingering", "hello", "wow"])
    2
    >>> match_ends(["pitch", "hi", "sos"])
    1
    >>> match_ends(["jeejeej", "saeeas", "tot"])
    3
    >>> match_ends(["muracami", "xox", "xoxo"])
    1
    >>> match_ends(["bored", "ngo", "ggbbg"])
    1
    >>> match_ends(["sad", "dad", "mom"])
    2

    """
    newstr = " ".join(text)
    newtext = newstr.upper()
    newlst = newtext.split(" ")
    start = 0
    for i in newlst :
        if len(i) >= 2 :
          if i[0] == i[-1]:
            start = start + 1
        else:
            start = start + 0
    return start

#15
def remove_adjacent(num):
    """this function returns a list where all adjacent elements have been reduced to a single element.

    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([2, 4, 5, 6, 6, 7])
    [2, 4, 5, 6, 7]
    >>> remove_adjacent([18, 19, 19, 20, 21, 22])
    [18, 19, 20, 21, 22]
    >>> remove_adjacent([1, 1, 3, 5, 7])
    [1, 3, 5, 7]
    >>> remove_adjacent([2, 4, 6, 6, 8])
    [2, 4, 6, 8]
    >>> remove_adjacent([69, 70, 71, 71, 72])
    [69, 70, 71, 72]

    """
    result = []
    for i in num:
        if len(result) == 0 or i != result[-1]:
            result.append(i)
    return result
