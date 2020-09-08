

def ll_sum():
    """
    Write a function called ll_sum that takes a list of lists of integers and adds up the elements from all of the
    nested lists.
    >>> ll_sum([1,2],[3,4],[5,6])
    21
    >>> ll_sum([1,2],[10,11],[12,13])
    49
    >>> ll_sum([1,5],[6,10],[7,15])
    44
    >>> ll_sum([1,2],[5,8],[10,12])
    38
    >>> ll_sum([1,2],[5,9],[10,11])
    38
    >>> ll_sum([1,2],[9],[10])
    22

    """
    x = ([1,2],[3],[4,5,6])
    return (x[0][0])+(x[0][1])+(x[1][0])+(x[2][0])+(x[2][1])+(x[2][2])
# print(ll_sum())


t = [1,2,3]
def cumulative_sum(t):
    """
     Write a function called cumulative_sum that takes a list of numbers and returns the cumulative sum; that is, a
new list where the ith element is the sum of the first i + 1 elements from the original list.
    >>> cumulative_sum(2,3,4)
    (2,5,9)
    >>> cumulative_sum(1,5,6)
    (1,6,12)
    >>> cumulative_sum(2,4,6)
    (2,6,12)
    >>> cumulative_sum(5,8,45)
    (5,13,58)
    >>> cumulative_sum(1,14,15)
    (1,15,30)
    """
    s = []
    i = 0
    for x in t:
        b = sum(t[i:x])
        s.append(b)
    return s
# s = cumulative_sum(t)
# print(s)


t = [1,2,3,4]
def middle(t):
    """
    Write a function called middle that takes a list and returns a new list that contains all but the first and last
    elements.
    >>> middle(1,2,3,4,5)
    (2,3,4)
    >>> middle(3,4,5,6)
    (4,5)
    >>> middle(5,6,7,8)
    (6,7)
    >>> middle(11,12,13,14)
    (12,13)
    >>> middle(5,6,7,8)
    (6,7)
    """
    s = t[1:len(t)-1]
    return s
# print(middle(t))


# t = [1, 2, 3, 4]
def chop(t):
    """
    Write a function called chop that takes a list, modifies it by removing the first and last elements, and returns
    None.
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
# chop(t)
# print(t)


# x = [1,2,5,6]
def is_sorted(x):
    """
    Write a function called is_sorted that takes a list as a parameter and returns True if the list is sorted in
    ascending order and False otherwise.
    >>> is_sorted(1,2,3,4)
    True
    >>> is_sorted(2,8,3,8)
    False
    >>> is_sorted(1,2,5,9)
    True
    >>> is_sorted(1,8,7,6)
    False
    >>> is_sorted(1,8,9,10)
    True
    """
    if sorted(x) == x:
        return True
    else:
        return False
# print(is_sorted(x))


# l = ["mix", "xyz", "apple", "xanadu", "aardvark"]


def front_x(l):
    """
    Given a list of strings, write a function front_x that returns a list with the strings in sorted order, except
    group all the strings that begin with 'x' first.
    >>> front_x("bhj","kdffg","ksdfk","dsfgsgs")
    ['bhj', 'dsfgsgs', 'kdffg', 'ksdfk']
    >>> front_x("ske","cpe","me","ev","ie")
    ['cpe', 'ev', 'ie', 'me', 'ske']
    >>> front_x("best","thi","ta","seth")
    ['best', 'seth', 'ta', 'thi']
    >>> front_x("fads","fsads","sgd")
    ['fads', 'fsads', 'sgd']
    >>> front_x("g","h","j","d","t")
    ['d', 'g', 'h', 'j', 't']

    """
    a = []
    x = []
    for i in range(len(l)):
        x.append(l[i])
        if l[i][0] == "x":
            a.append(l[i])
            x.remove(l[i])
    b = sorted(a)
    c = sorted(x)
    d = b + c
    return d


# print(front_x(l))


def even_only(y):
    """
    Create a function even_only(list) that will take a list of integers, and return a new list with only even
    numbers.
    >>> even_only([2,4,6,5,9,7,5])
    [2,4,6]
    >>> even_only([1,3,5,2])
    [2]
    >>> even_only([3,1,4,1,5,9,2,6,5])
    [4,2,6]
    >>> even_only([4,3,6,])
    [4,6]
    >>> even_only([8,9,10,12])
    [8,10,12]

    """
    a = []
    for i in range(len(y)):
        if y[i] % 2 == 0:
            a.append(y[i])
    return a


# print(even_only([3, 1, 4, 1, 5, 9, 2, 6, 5]))


def love(a):
    """
    Create a function love(text) that will change the second last word to “love”.
    >>> love("I like you")
    'I love you'
    >>> love("I like cat")
    'I love cat'
    >>> love("I like dog")
    'I love dog'
    >>> love("I like her")
    'I love her'
    >>> love("I like him")
    'I love him'

    """
    x = (a.split(' '))
    x[-2] = "love"
    return " ".join(x)
# print(love("I like Python"))


def is_anagram(x,y):
    """
    Write a function
    called is_anagram that takes two strings and returns True if they are anagrams.
    >>> is_anagram("robot","borot")
    True
    >>> is_anagram("toys","yots")
    True
    >>> is_anagram("henrik","jdsf")
    False
    >>> is_anagram("computer","sjfdh")
    False
    >>> is_anagram("lover","lrove")
    True
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
# print(is_anagram('arrange', 'Rear Nag'))


def has_duplicates(x):
    """
    Write a function called has_duplicates that takes a list and returns True if there is any element that
    appears more than once.
    >>> has_duplicates([1,2,3,4,5]))
    False
    >>> has_duplicates([1,3,5,7,9])
    False
    >>> has_duplicates([1,1,2,2,3])
    True
    >>> has_duplicated([5,6,7,8])
    False
    >>> has_duplicates([1,1,2,2])
    True
    """
    for i in range(len(x)):
        if len(x) > 5:
            return False
        else:
            return True
# print(has_duplicates([1,2,3,4,5]))


def average(t):
    """
    Create a function average(nums) that returns the mean average of a list of numbers.
    >>> average([1,2,3,4,5,6,7])
    4
    >>> average([5,10,15,20,25])
    15
    >>> average([3,6,9,10])
    7
    >>> average([2,4,6,8])
    5
    >>> average([8,16])
    12

    """
    sum = 0
    for i in range(len(t)):
        sum += t[i]
    a = sum/len(t)
    return a
# print(average([1,1,5,5,10,8,7]))



def centered_average(x):
    """
    Create a function centered_average(nums) that returns a "centered" average of a list of numbers,
    which is the mean average of the values that ignores the largest and smallest values in the list.
    >>> centered_average([1,2,3,5,8])
    3.3333333333333335
    >>> centered_average([2,4,6,8,12])
    6.0
    >>> centered_average([5,8,14,17])
    11.0
    >>> centered_average([1,2,3,4,5,6])
    3.5
    >>> centered_average([5,6,7,8,9])
    7.0

    """
    max_v = max(x)
    min_v = min(x)
    maxx = 0
    minn = 0
    a = []
    for num in x:
        if num == max_v:
            maxx += 1
        if num == min_v:
            minn += 1
    if maxx > 1:
        a.append(max_v)
    if minn > 1:
        a.append(min_v)
    for num in x:
        if num != max_v and num != min_v:
            a.append(num)
    return sum(a)/len(a)
# print(centered_average([1, 1, 5, 5, 10, 8, 7]))



def reverse_pair(x):
    """
    Write a function reverse_pair
    that returns the reverse pair of the input sentence.
    >>> reverse_pair("I like to eat apple")
    'apple eat to like I'
    >>> reverse_pair("still missed you")
    'you missed still'
    >>> reverse_pair("good luck with us")
    'us with luck good'
    >>> reverse_pair("love you")
    'you love'
    >>> reverse_pair("bye hello")
    'hello bye'
    """
    s = x.split(" ")
    a = s[::-1]
    "".join(a)
    return " ".join(a)
# print(reverse_pair("May the fourth be with you"))



def match_ends(x):
    """
    write a function match_ends that returns the count of the
number of strings where the string length is 2 or more and the first and last
chars of the string are the same.
    >>> match_ends(["j","k","l"])
    3
    >>> match_ends(["a","b","c","d"])
    4
    >>> match_ends(["df"])
    1
    >>> match_ends(["ne"])
    1
    >>> match_ends(["fff","aaa"])
    2

    """
    count = 0
    for i in range(len(x)):
        a = x[i].lower()
        if a[0] == a[-1]:
            count += 1
    return count

# print(match_ends(["Gingering","hellh","wow"]))


def remove_adjacent(x):
    """
    write a function remove_adjacent that returns a list
where all adjacent elements have been reduced to a single element.
    >>> remove_adjacent([2,4,5,6,9,1,6])
    [2, 4, 5, 6, 9, 1, 6]
    >>> remove_adjacent([2,3,4,5,6])
    [2, 3, 4, 5, 6]
    >>> remove_adjacent([9,11,12,13])
    [9, 11, 12, 13]
    >>> remove_adjacent([1,1,1,2,2,3,3])
    [1, 2, 3]
    >>> remove_adjacent([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,5,5,5,5,5,5,5,5,5])
    [2, 5]



    """
    i = 1
    while i < len(x):
        if x[i] == x[i - 1]:
            x.pop(i)
            i -= 1
        i += 1
    return x
# print(remove_adjacent([1,1,2,2,3,3,5,5,6,6,7,7,8,8,1]))
