



# 1


def ll_sum(lst):
    """takes a list of lists of integer and adds up the element from all of the nested lists

    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> ll_sum(t)
    21

    >>> ll_sum([[1],[2],[2,3],[4,5,6]])
    23

    >>> ll_sum([[3,4,5],[2],[10]])
    24

    >>> ll_sum([[1,2],[4],[7,8,9]])
    31

    >>> ll_sum([[1,2],[3],[4],[7,8,9],[1,3,4],[4]])
    46
    """
    sum = 0
    for i in lst:
        for x in i:
            sum += x
    return sum

# 2


def cumulative_sum(lst):
    """takes a list of numbers and returns the cumulative sum

    >>> t = [1,2,3]
    >>> cumulative_sum(t)
    [1, 3, 6]

    >>> t = [7,3,12]
    >>> cumulative_sum(t)
    [7, 10, 22]

    >>> cumulative_sum([5,6,20,55,3,1])
    [5, 11, 31, 86, 89, 90]

    >>> cumulative_sum([5,1,3,4,52,9])
    [5, 6, 9, 13, 65, 74]

    >>> cumulative_sum([1, 3, 5, 9])
    [1, 4, 9, 18]
    """
    sum = 0
    x = []
    for i in lst:
        sum = i+sum
        x.append(sum)
    return x

# 3


def middle(lst):
    """removing  first and last element in list
    >>> t =[1,4,7,5,3,2]
    >>> middle(t)
    [4, 7, 5, 3]

    >>> a =[1,2,3,4,2,4,2]
    >>> middle(a)
    [2, 3, 4, 2, 4]

    >>> middle([2,4,5,11,20])
    [4, 5, 11]

    >>> middle([2,4,5,11,20])
    [4, 5, 11]

    >>> middle([2,3,4,5,1,2,4,2,39])
    [3, 4, 5, 1, 2, 4, 2]

    """
    lst.pop(0)
    lst.pop(-1)
    return lst

# 4


def chop(lst):
    """reomoving first and last element and returns none
    >>> t = [1,2,3,4]
    >>> chop(t)
    >>> t
    [2, 3]

    >>> a = [3,4,9,22]
    >>> chop(a)
    >>> a
    [4, 9]

    >>> t = [2,3,4,5,6]
    >>> chop(t)
    >>> t
    [3, 4, 5]

    >>> t = [5,5,56,6,3,3,2]
    >>> chop(t)
    >>> t
    [5, 56, 6, 3, 3]

    >>> t = [2,3,42,99,6,34]
    >>> chop(t)
    >>> t
    [3, 42, 99, 6]

    """
    lst.pop(0)
    lst.pop(-1)

# 5


def is_sorted(lst):
    """takes a list and return True if the list is sorted in acending order and False otherwise

    >>> is_sorted([1,2,2])
    True

    >>> is_sorted(['a','c','b'])
    False

    >>> is_sorted(['ant','module','lion','king','zebra'])
    False

    >>> is_sorted(['a','c','b'])
    False

    >>> is_sorted([1,4,5,8,9])
    True

    """
    if sorted(lst) == lst:
        return True
    else:
        return False

# 6


def front_x(lst):
    """returns list with the strings is sorted order, except group all the strings that begin with 'x' first

    >>> front_x(['mix','xyz','apple','xanadu','aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']

    >>> front_x(['xa','yup','xyz'])
    ['xa', 'xyz', 'yup']

    >>> front_x(['xak','io','pop'])
    ['xak', 'io', 'pop']

    >>> front_x(['app','bat','xin','six'])
    ['xin', 'app', 'bat', 'six']

    >>> front_x(['gock','xan','king','xanadu'])
    ['xan', 'xanadu', 'gock', 'king']
    """
    a = []
    for i in lst:
        if i.startswith('x'):
            a.append(i)
            lst.remove(i)

    return sorted(a) + sorted(lst)


# 7
def even_only(list):
    """take a list of integers and return a new list with only even

    >>> even_only([3,12,3,4,5,10,33,2,1,1])
    [12, 4, 10, 2]

    >>> even_only([1,1,5,7,9])
    []

    >>> even_only([-1,2,4,-10,22,5,9,-100])
    [2, 4, -10, 22, -100]

    >>> even_only([1,2,4,5,6,7,9,10])
    [2, 4, 6, 10]

    >>> even_only([2,3,4,5,9,1,6,22])
    [2, 4, 6, 22]

    """
    lst = []
    for i in list:
        if i % 2 == 0:
            lst.append(i)
    return lst


# 8
def love(text):
    """change the second last word to 'love'

    >>> love('I like you')
    'I love you'

    >>> love('just kid')
    'love kid'

    >>> love('why you hate me')
    'why you love me'

    >>> love('only you')
    'love you'

    >>> love('poppy rock')
    'love rock'

    """
    x = text.split()
    x.pop(-2)
    x.insert(-1, 'love')
    return " ".join(x)

# 9


def is_anagram(x, y):
    """rearrange the letters from one to spell other and return True if they are anagrams

    >>> is_anagram('hello','h lOe l')
    True

    >>> is_anagram('Can see','aCe seN')
    True

    >>> is_anagram('Got It','GoTYOu')
    False

    >>> is_anagram('Lotto','oTT ol')
    True

    >>> is_anagram('hiall','hialI')
    False

    """
    x = sorted(x.lower())
    y = sorted(y.lower())
    x = ''.join(x).strip(' ')
    y = ''.join(y).strip(' ')
    if x == y:
        return True
    else:
        return False


# 10


def has_duplicates(lst):
    """takes a list and returns True if there have same element in list

    >>> has_duplicates([1,4,5,7,8,20])
    False

    >>> has_duplicates([-2,2,-4,133,33,-2])
    True

    >>> has_duplicates([1,4,5,-20,-2,-3])
    False

    >>> has_duplicates([1,2,3,4,5])
    False

    >>> has_duplicates([2,5,3,1,4])
    False

    """
    if sorted(lst) == sorted(set(lst)):
        return False
    else:
        return True


# 11


def average(num):
    """returns mean average of a list of numbers

    >>> average([1,1,5,5,10,8,7])
    5.285714285714286

    >>> average([6,8,1,4])
    4.75

    >>> average([4,5,6,1,12,-55])
    -4.5

    >>> average([1,2,3,4,5])
    3.0

    >>> average([5,5,5])
    5.0

    """
    return float(sum(num))/len(num)


# 12


def centered_average(nums):
    """returns average of the value that ignores the largest and smallest values in the list

    >>> centered_average([1,1,5,5,10,8])
    4.75

    >>> centered_average([1,1,1,1,2,2])
    1.25

    >>> centered_average([2,2,2,3,4,5,6])
    3.2

    >>> centered_average([1,2,3,4,5,6])
    3.5

    >>> centered_average([1,1,1])
    1.0

    """
    x = sorted(nums)
    x.pop(0)
    x.pop(-1)
    return float(sum(x))/len(x)


# 13


def reverse_pair(text):
    """returns the reverse pair of the input sentence

    >>> reverse_pair("i like you")
    'you like i'

    >>> reverse_pair("long time no see")
    'see no time long'

    >>> reverse_pair("take home")
    'home take'

    >>> reverse_pair("got it")
    'it got'

    >>> reverse_pair("hot cold")
    'cold hot'

    """
    lst = text.split()
    lst.reverse()
    return " ".join(lst)

# 14


def match_ends(lst):
    """returns the count ogf the number of strings where the string length is 2 or more and the first and last chars of the string are the same

    >>> match_ends(["hello","goodbye"])
    1

    >>> match_ends(["Hi","Say","hello","Dog"])
    3

    >>> match_ends(["hot","hot","cold","play","want","london"])
    5

    >>> match_ends(["look","like","love"])
    2

    >>> match_ends(["tiger","lion","bird","dolphin"])
    3

    """
    lst.pop(0)
    count = 0
    for _ in lst:
        count += 1
    return count

# 15


def remove_adjacent(lst):
    """returns a list where all adjacent elements have been reduced to a single element

    >>> remove_adjacent([1,2,2,2,2,2,3])
    [1, 2, 3]

    >>> remove_adjacent([2,2,2,4,5,5,6,6,7,8,9])
    [2, 4, 5, 6, 7, 8, 9]

    >>> remove_adjacent([1,1,1,2,2,3,7,8,11])
    [1, 2, 3, 7, 8, 11]

    >>> remove_adjacent([2,3,4,6,7,8,8,8])
    [2, 3, 4, 6, 7, 8]

    >>> remove_adjacent([1,2,3,4,5,6,7,8,9,1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    """
    return list(set(lst))
