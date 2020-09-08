

#1
def ll_sum(s):
    """ function that sum the list.
    >>> ll_sum([[1,2],[3],[4,5,6]])
    21
    >>> ll_sum([[-5,-2],[11],[10,9,7]])
    30
    >>> ll_sum([[4,5,6],[8],[1],2])
    26
    >>> ll_sum([[-1,-2],[-3,-4],[-5,-6]])
    -21
    >>> ll_sum([[0],1])
    1
    """
    result = 0
    for item in s:
        if type(item) == list:
            result += ll_sum(item)
        else:
            result += item 
    return result
    
#2
def cumulative_sum(s):
    """ function that cumulative sum from list.
    >>> cumulative_sum([1,2,3])
    [1, 3, 6]
    >>> cumulative_sum([-1,-2,-3])
    [-1, -3, -6]
    >>> cumulative_sum([1,2,3,4,5])
    [1, 3, 6, 10, 15]
    >>> cumulative_sum([5,4,3,2,1])
    [5, 9, 12, 14, 15]
    >>> cumulative_sum([0,0,0])
    [0, 0, 0]

    """
    cumu = []
    cumu_sum = 0
    for a in s:
        cumu_sum += a
        cumu.append(cumu_sum)
    return cumu
t = [1,2,3]
# print(cumulative_sum(t))

#3
def middle(s):
    """ function that return new list that contain all but the first and last elements.
    >>> middle([1,2,3,4])
    [2, 3]
    >>> middle([1,2,3,4,5,6])
    [2, 3, 4, 5]
    >>> middle([0,0,0,0,0,0,0])
    [0, 0, 0, 0, 0]
    >>> middle([-4,-5,8,5,7,-5])
    [-5, 8, 5, 7]
    >>> middle([9,8,7,6,5,4,3,2,1])
    [8, 7, 6, 5, 4, 3, 2]
    """
    return s[1:2] + s[2:-1]

#4
def chop(s):
    """ function that change the list s to the new list that contain all but the first and last elements but didn't return.
    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    >>> t = [1, 2, 3, 4,5,6]
    >>> chop(t)
    >>> t
    [2, 3, 4, 5]
    >>> t = [0,0,0,0,0,0,0]
    >>> chop(t)
    >>> t
    [0, 0, 0, 0, 0]
    >>> t = [-4,-5,8,5,7,-5]
    >>> chop(t)
    >>> t
    [-5, 8, 5, 7]
    >>> t = [9,8,7,6,5,4,3,2,1]
    >>> chop(t)
    >>> t
    [8, 7, 6, 5, 4, 3, 2]
    """
    s.pop(0)
    s.pop(-1)
        



#5
def is_sorted(s):
    """ function that check is the list sorted or not if it sorted return True if not return False.
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    >>> is_sorted(['a','d','e','i','l','p'])
    True
    >>> is_sorted(['z','x','y'])
    False
    >>> is_sorted([9,8,7,5,6,5,4,3,2,1])
    False
    """
    a = []
    for num in s:
        a.append(num)
    s.sort()
    if a == s:
        return True
    else:
        return False


#6
def front_x(s):
    """ function that sort the taken list of string but the string start with x will go first.
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    >>> front_x(['xxx' , 'eiei' , 'oreo' , 'aroi'])
    ['xxx', 'aroi', 'eiei', 'oreo']
    >>> front_x(['xaaaaa', 'xbbbbb', 'xccccc', 'xyyyyy' , 'xzzzzz'])
    ['xaaaaa', 'xccccc', 'xzzzzz', 'xbbbbb', 'xyyyyy']
    >>> front_x(['m', 'is', 'very', 'x', 'leay', 'kub'])
    ['x', 'is', 'kub', 'leay', 'm', 'very']
    >>> front_x(['z', 'y', 'x'])
    ['x', 'y', 'z']

    """
    new = []
    for a in s:
        if a.startswith("x"):
            new.append(a)
            s.remove(a)
    new.sort()
    s.sort()
    return new + s
# print (front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))

#7
def even_only(s):
    """ function that take the list of any number and return only the list of even number.
    >>> even_only([3,1,4,1,5,9,2,6,5])
    [4, 2, 6]
    >>> even_only([1,2,3,4,5,6,7,8,9])
    [2, 4, 6, 8]
    >>> even_only([2,11,12,16,85,246])
    [2, 12, 16, 246]
    >>> even_only([56,89,75,12,3,5,4,56])
    [56, 12, 4, 56]
    >>> even_only([56,54,2,54,245,54,54,542])
    [56, 54, 2, 54, 54, 54, 542]
    """
    even =[]
    for a in s:
        if a%2 ==0:
            even.append(a)
    return even

#8
def love(text):
    """ function that change the second last of the string to 'love'.
    >>> love("I like Python")
    'I love Python'
    >>> love("I really like Python")
    'I really love Python'
    >>> love("I am very very very fcking hate python")
    'I am very very very fcking love python'
    >>> love("I need some xee kub")
    'I need some love kub'
    >>> love("I very really super very amazing very hate boob")
    'I very really super very amazing very love boob'
    """
    a = text.split()
    a.pop(-2)
    a.insert(-1,"love")
    z = (" ".join(a))
    return z

#9
def is_anagram(s1,s2):
    """ function that return True if it anagram and Flase if it not.
    >>> is_anagram('arrange', 'Rear Nag')
    True
    >>> is_anagram('ab c  d f g', 'AFcdb g')
    True
    >>> is_anagram('omaewa', 'a w om ae')
    True
    >>> is_anagram('pussy', 'dick')
    False
    >>> is_anagram('kuy', 'H E e')
    False
    """
    a1 = s1.lower()
    a2 = s2.lower()
    t1 = a1.split(" ")
    t2 = a2.split(" ")
    z1 = ''.join(t1)
    z2 = ''.join(t2)
    x1 = sorted(z1)
    x2 = sorted(z2)
    if x1 == x2:
        return True
    else:
        return False
        
#10
def has_duplicates(s):
    """ function that return True if the list is duplicate and False if it not.
    >>> has_duplicates([1, 2, 3, 4, 5])
    False
    >>> has_duplicates([1, 2, 3, 4, 5, 2])
    True
    >>> has_duplicates([1, 2, 3, 4, 5,6,56,23,57,654])
    False
    >>> has_duplicates([1, 2, 3, 4, 5,5,5,5,5,5,5,4,4,4,3,3,3,2,2,2])
    True
    >>> has_duplicates([1, 2, 3, 4, 5,545,4879,874654,57,246,65468,46])
    False
    
    """
    a = 0
    while a < len(s):
        if s.count(s[a]) > 1:
            return True
        elif a == (len(s) - 1):
            return False
        a += 1

#11
def average(nums):
    """ function that calculate the average in list .
    >>> average([1, 1, 5, 5, 10, 8, 7])
    5.285714285714286
    >>> average([1,2,3,4,5])
    3.0
    >>> average([5,4,7,8,9,21,1])
    7.857142857142857
    >>> average([6,5,23,21,2,4,55,4])
    15.0
    >>> average([8,6,5,4,2,3,5,7,4])
    4.888888888888889
    """
    return sum(nums)/len(nums)

#12
def centered_average(s):
    """ function that remove the first and last number in list and calculate the average in list. 
    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([1,2,3,4,5])
    3.0
    >>> centered_average([5,4,7,8,9,21,1])
    6.6
    >>> centered_average([6,5,23,21,2,4,55,4])
    10.5
    >>> centered_average([8,6,5,4,2,3,5,7,4])
    4.857142857142857
    """
    s.sort()
    s.pop(0)
    s.pop(-1)
    return sum(s)/len(s)

#13
def reverse_pair(s):
    """ function that reverse the taken string.
    >>> reverse_pair("May the fourth be with you")
    'you with be fourth the May'
    >>> reverse_pair("M mang kod loh kod mang m")
    'm mang kod loh kod mang M'
    >>> reverse_pair("sa wad dee kub")
    'kub dee wad sa'
    >>> reverse_pair("yak dai line tong tam ngai")
    'ngai tam tong line dai yak'
    >>> reverse_pair("you suay mak kub koh jeeb dai mai")
    'mai dai jeeb koh kub mak suay you'
    """
    s = s.split()
    s.reverse()
    a = " ".join(s)
    return a

#14
def match_ends(s):
    """ function that count string in list that have the same first and last word.
    >>> match_ends(["Gingering", "hello","wow"])
    2
    >>> match_ends(["EE", "suay","mak"])
    1
    >>> match_ends(["mia", "tee","dee"])
    0
    >>> match_ends(["koh", "line","ngai","dee"])
    0
    >>> match_ends(["seng", "sus","sus"])
    2
    """
    count = 0
    s = " ".join(s)
    s = s.lower()
    z = s.split()
    for a in z:
        if a[0] == a[-1]:
            count += 1
        else:
            count += 0
    return count


#15
def remove_adjacent(s):
    """ function that remove all adjacent elements to single element.
    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([1, 2, 2, 3,3])
    [1, 2, 3]
    >>> remove_adjacent([1,2,2,2,2,2,2,2,2])
    [1, 2]
    >>> remove_adjacent([9,9,9,9,9,9,9,9,9,9,9,9])
    [9]
    >>> remove_adjacent([9,8,7,6,5,4,3,2,1])
    [9, 8, 7, 6, 5, 4, 3, 2, 1]
    """
    new_list = []
    for nums in s:
        if nums in new_list :
            continue
        else:
            new_list.append(nums)
    return new_list







    




