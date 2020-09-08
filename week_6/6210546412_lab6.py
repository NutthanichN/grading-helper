

#1=====================================
def ll_sum(listt):
    """ takes a list of lists of integers and adds up the elements from all of the nested lists.
    >>> ll_sum([[1, 2], [3], [4, 5, 6]])
    21
    >>> ll_sum([[1], [2,3], [6]])
    12
    >>> ll_sum([[2],[4,6,7],[3,4]])
    26
    >>> ll_sum([1,[5,4,5],3,[3,3]])
    24
    >>> ll_sum([1,2,3])
    6
    """
    sum = 0
    for i in range(len(listt)):
        if type(listt[i]) == list :
            for j in listt[i]:
                sum += j
        else: sum+= listt[i]
    return sum
#2======================================
def cumulative_sum(listt):
    """ takes a list of numbers and returns the cumulative sum; that is, a new list where the ith element is the sum of the first i + 1 elements from the original list.
    >>> cumulative_sum([1,2,3])
    [1, 3, 6]
    >>> cumulative_sum([2,1,3,4,5])
    [2, 3, 6, 10, 15]
    >>> cumulative_sum([1,3,5,7])
    [1, 4, 9, 16]
    >>> cumulative_sum([2,3,1,3])
    [2, 5, 6, 9]
    >>> cumulative_sum([1,1,1,1,1])
    [1, 2, 3, 4, 5]
    """
    for i in range(len(listt)):
        if i >=1:
            listt[i]+=listt[i-1]
    return listt
#3======================================
def middle(listt):
    """ takes a list and returns a new list that contains all but the first and last elements.
    >>> middle([1, 2, 3, 4])
    [2, 3]
    >>> middle(['a','b','c','d'])
    ['b', 'c']
    >>> middle(['a',1,'b',2])
    [1, 'b']
    >>> middle([1,2,'a',3])
    [2, 'a']
    >>> middle(['a','b',1,2,3])
    ['b', 1, 2]
    """
    new = listt[1:-1]
    return new
#4=====================================
def chop(listt):
    """ takes a list, modifies it by removing the first and last elements, and returns None.
    >>> a = [1,2,3]
    >>> chop(a)
    >>> a
    [2]
    >>> b = ['a','b','c']
    >>> chop(b)
    >>> b
    ['b']
    >>> c = [1,2,3,4]
    >>> chop(c)
    >>> c
    [2, 3]
    >>> d = [2,2,1,1,1,1]
    >>> chop(d)
    >>> d
    [2, 1, 1, 1]
    >>> e = ['a',1,'4',2,'5']
    >>> chop(e)
    >>> e
    [1, '4', 2]
    """
    listt.pop(0)
    listt.pop(-1)
#5=====================================
def is_sorted(listt):
    """ that takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise.
    >>> is_sorted([1,2,3,4])
    True
    >>> is_sorted([2,1,3,4])
    False
    >>> is_sorted([1,2,4,3])
    False
    >>> is_sorted(['a','b','c','d'])
    True
    >>> is_sorted(['b','a','c','s','a'])
    False
    """
    new = sorted(listt)
    if new == listt:
        return True
    else: return False
#6=====================================
def front_x(listt):
    """ returns a list with the strings in sorted order, except group all the strings that begin with 'x' first.
    >>> front_x(['aa','x','xy','ss'])
    ['x', 'xy', 'aa', 'ss']
    >>> front_x(['abc','xxx','xyz','bcs'])
    ['xxx', 'xyz', 'abc', 'bcs']
    >>> front_x(['a','b','c','d','e','x'])
    ['x', 'a', 'b', 'c', 'd', 'e']
    >>> front_x(['aa','xxx','xy','ssa'])
    ['xxx', 'xy', 'aa', 'ssa']
    >>> front_x(['abce','xad','xae','x'])
    ['x', 'xad', 'xae', 'abce']
    """
    x = []
    notx = []
    for i in listt:
        if i[0].lower() == "x":
            x.append(i)
        else: notx.append(i)
    x.sort()
    notx.sort()
    return x + notx
#7=====================================
def even_only(listt):
    """ take a list of integers, and return a new list with only even numbers.
    >>> even_only([3,1,4,1,5,9,2,6,5])
    [4, 2, 6]
    >>> even_only([1,2,3,4,5,6,6])
    [2, 4, 6, 6]
    >>> even_only([2,5,6,3,2,5,8,4])
    [2, 6, 2, 8, 4]
    >>> even_only([2,2,4,4,3,1,6,5,])
    [2, 2, 4, 4, 6]
    >>> even_only([1,1,4,3,2,2,1])
    [4, 2, 2]
    """
    new = []
    for i in listt:
        if i % 2 == 0:
            new.append(i)
    return new
#8=====================================
def love(text):
    """ change the second last word to “love”.
    >>> love("I like Python")
    'I love Python'
    >>> love("I really like Python")
    'I really love Python'
    >>> love("asas asdasda asf as")
    'asas asdasda love as'
    >>> love("I dont like Python")
    'I dont love Python'
    >>> love("I very very hate you")
    'I very very love you'
    """
    new = text.split(" ")
    new[-2] = "love"
    ans = " ".join(new)
    return ans
#9=====================================
def is_anagram(text1,text2):
    """ takes two strings and returns True if they are anagrams.
    >>> is_anagram("arrange", "Rear Nag")
    True
    >>> is_anagram("adfsfak", "aknMA asc")
    False
    >>> is_anagram("abccx", "abccxs")
    False
    >>> is_anagram("abcd", "Ab cD")
    True
    >>> is_anagram("abbbx", "aBBx")
    False
    """
    ntext1 = []
    ntext2 = []
    text1 = text1.lower()
    text2 = text2.lower()
    text1 = text1.replace(" ", "")
    text2 = text2.replace(" ", "")
    
    for i in text1:
        ntext1.append(i)
    for i in text2:
        ntext2.append(i)
    ntext1.sort()
    ntext2.sort()
    
    ntext1 = "".join(ntext1)
    ntext2 = "".join(ntext2)
    
    if ntext1 == ntext2:
        return True
    else: return False
#10=====================================
def has_duplicates(listt):
    """takes a list and returns True if there is any element that appears more than once.
    >>> has_duplicates([1, 2, 3, 4, 5])
    False
    >>> has_duplicates([1, 2, 3, 4, 5, 2])
    True
    >>> has_duplicates([1, 2, 4 , 5, 7, 8])
    False
    >>> has_duplicates([1, 1, 1, 1, 5, 2])
    True
    >>> has_duplicates([3, 2, 1])
    False
    """
    ans = False
    for i in range(len(listt)):
        for j in range(i-1):
            if listt[i] == listt[j]:
                ans = True
    return ans
#11====================================
import math
def average(nums):
    """ returns the mean average of a list of numbers.
    >>> average([1, 1, 5, 5, 10, 8, 7])
    5.285714285714286
    >>> average([2, 2, 4, 6])
    3.5
    >>> average([3, 4, 5, 6, 1])
    3.8
    >>> average([1, 3, 5, 1, 2])
    2.4
    >>> average([5, 5, 3, 2, 6])
    4.2
    """
    return (math.fsum(nums))/len(nums)
#12===================================
def centered_average(nums):
    """ returns a "centered" average of a list of numbers, which is the mean average of the values that ignores the largest and smallest values in the list. If there are multiple copies of the smallest/largest value, pick just one copy. 
    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([2,2,4,6,7,2])
    3.5
    >>> centered_average([1,3,6,7])
    4.5
    >>> centered_average([2,4,5,2])
    3.0
    >>> centered_average([1,2,4,2])
    2.0
    """
    nums.sort()
    nums.pop(0)
    nums.pop(-1)
    return math.fsum(nums)/len(nums)
#13==================================
def reverse_pair(text):
    """ returns the reverse pair of the input sentence.
    >>> reverse_pair("May the fourth be with you")
    'you with be fourth the May'
    >>> reverse_pair("asd asd as")
    'as asd asd'
    >>> reverse_pair("May the fourth be with me")
    'me with be fourth the May'
    >>> reverse_pair("kdkd kdkds aa")
    'aa kdkds kdkd'
    >>> reverse_pair("pakarat k")
    'k pakarat'
    """
    text = text.split(" ")
    ltext = []
    for i in text:
        ltext.append(i)
    ltext = " ".join(reversed(ltext))
    return ltext
#14==================================
def match_ends(listt):
    """ returns the count of the number of strings where the string length is 2 or more and the first and last chars of the string are the same.
    >>> match_ends(["Gingering", "hello","wow"])
    2
    >>> match_ends(['sss','asd','sqeS'])
    2
    >>> match_ends(['Pakarat','kk'])
    1
    >>> match_ends(['sss','s1ss1'])
    1
    >>> match_ends(['aasda','qwdq','efsddcrE'])
    3
    """
    sum = 0
    for i in listt:
        if i[0].lower() == i[-1].lower():
            sum += 1
    return sum
#15=================================
def remove_adjacent(listt):
    """ returns a list where all adjacent elements have been reduced to a single element.
    >>> remove_adjacent([1,2,3,3])
    [1, 2, 3]
    >>> remove_adjacent([2,1,3,4,4])
    [2, 1, 3, 4]
    >>> remove_adjacent([1,2,4,5,2,4,4])
    [1, 2, 4, 5, 2, 4]
    >>> remove_adjacent([2,2,2,1,1,1])
    [2, 1]
    >>> remove_adjacent([2,1,2,1])
    [2, 1, 2, 1]
    """
    prev = " "
    lis = []
    for i in listt:
        if i != prev:
            lis.append(i)
            prev = i
    return lis

import doctest
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
doctest.testmod()