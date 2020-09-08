

def ll_sum(Y):
    """ This function returns the sum of the lists in a list.

    >>> YO = [[1,2], [3], [4,5,6]]
    >>> ll_sum(YO)
    21
    >>> t = [[1,2,3,4,5,6,7,8,9,10], [2,3,4], [5,5,5,5,5]]
    >>> ll_sum(t)
    89
    >>> MyNameIs = [[1,1,1,1,1], [2,2,2,2,2], [3,3,3,3,3], [4,4,4,4,4], [5,5,5,5,5]]
    >>> ll_sum(MyNameIs)
    75
    >>> Nut = [[2,4,6,8,10], [1,3,5,7,9]]
    >>> ll_sum(Nut)
    55
    >>> ThisDoctestIsTooHardToCopy = [[1,2,3], [2,3,4], [3,4,5], [4,5,6], [5,6,7]]
    >>> ll_sum(ThisDoctestIsTooHardToCopy)
    60

    """
    a = []
    for i in range(len(Y)):
        for j in range(len(Y[i])):
            a.append(Y[i][j])
    YEAH = sum(a)
    return YEAH



def cumulative_sum(SoSleepy):
    """ This function returns the sum of the first i + 1 element.

    >>> s = [1,2,3]
    >>> cumulative(s)
    [1, 3, 6]
    >>> s = [2,4,6,8,10]
    >>> cumulative(s)
    [2, 6, 12, 20, 30]
    >>> s = [1,5,9]
    >>> cumulative(s)
    [1, 6, 15]
    >>> s = [10,20,30,40,50,60,70,80,90,100]
    >>> cumulative(s)
    [10, 30, 60, 100, 150, 210, 280, 360, 450, 550]
    >>> s = [5,5,5,5,5]
    >>> cumulative(s)
    [5, 10, 15, 20, 25]
    """
    a = []
    re = 0
    for i in SoSleepy:
        re = re + i
        a.append(re)
    return a


def middle(l):
    """ This function returns a new list that contain all elements except the first and the last elements.

    >>> s = [1,2,3,4]
    >>> middle(s)
    [2, 3]
    >>> s = [2,4,6,8,10]
    >>> middle(s)
    [4, 6, 8]
    >>> s = [1,3,5,7,9]
    >>> middle(s)
    [3, 5, 7]
    >>> s = [123,456,789]
    >>> middle(s)
    [456]
    >>> s = [11,22,33,44,55]
    >>> middle(s)
    [22, 33, 44]
    """
    return l[1:-1]


def chop(s):
    """ This function take a list and removing it first and last elements and return None

    >>> t = [1,2,3,4]
    >>> chop(t)
    >>> t
    [2, 3]
    >>> t = [1,2,3,4,5,6,7,8,9,10]
    >>> chop(t)
    >>> t
    [2, 3, 4, 5, 6, 7, 8, 9]
    >>> mae5 = [5,10,15,20,25,30]
    >>> chop(mae5)
    >>> mae5
    [10, 15, 20, 25]
    >>> mae7 = [7,14,21,28,35,42]
    >>> chop(mae7)
    >>> mae7
    [14, 21, 28, 35]
    >>> mae10 = [10,20,30,40,50,60]
    >>> chop(mae10)
    >>> mae10
    [20, 30, 40, 50]
    """
    del s[0]
    del s[-1]


def is_sorted(n):
    """ This function returns the boolean according to the order of the parameter

    >>> n = ['a', 'b', 'c', 'd', 'e']
    >>> is_sorted(n)
    True
    >>> n = [1,5,8,0]
    >>> is_sorted(n)
    False
    >>> n = [1,2,2]
    >>> is_sorted(n)
    True
    >>> n = ['b', 'a']
    >>> is_sorted(n)
    False
    >>> n = [1,22,333]
    >>> is_sorted(n)
    True
    """
    if sorted(n) == n:
        return True
    else:
        return False


def front_x(l):
    """ This function returns the sorted order among all string but the string that start with x will become the first order

    >>> YO = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
    >>> front_x(YO)
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    >>> Copying = ['jacky', 'nut', 'may', 'ploy', 'peem', 'jame', 'keyboard', 'boom']
    >>> front_x(Copying)
    ['boom', 'jacky', 'jame', 'keyboard', 'may', 'nut', 'peem', 'ploy']
    >>> IS = ['aa', 'dd', 'xx', 'gg', 'cc']
    >>> front_x(IS)
    ['aa', 'cc', 'dd', 'gg']
    >>> really = ['xobad', 'salamander', 'deteremined', 'gopro', 'xbac']
    >>> front_x(really)
    ['xbac', 'xobad', 'deteremined', 'gopro', 'salamander']
    >>> BAD = ['xerath', 'veromos', 'valkyrie', 'okeanos', 'bastet']
    >>> front_x(BAD)
    ['bastet', 'okeanos', 'valkyrie', 'veromos']
    """
    a = []

    for i in l:
        if i[0] == 'x':
            a.append(i)
            l.remove(i)
            A = sorted(a)
            L = sorted(l)
            real = A + L
        else:
            L = sorted(l)
            real = L

    return real




def even_only(l):
    """ This function returns the new list that take the even integers from old list

    >>> O = [3,1,4,1,5,9,2,6,5]
    >>> even_only(O)
    [4, 2, 6]
    >>> NO = [8,2,1,4,5,8,4,9,6,0]
    >>> even_only(NO)
    [8, 2, 4, 8, 4, 6, 0]
    >>> randN = [102,698, 9435, 345, 2354]
    >>> even_only(randN)
    [102, 698, 2354]
    >>> Mae3 = [0,3,6,9,12,15,18,21,24,27,30,33,36]
    >>> even_only(Mae3)
    [0, 6, 12, 18, 24, 30, 36]
    >>> Mae9 = [0,9,18,27,36,45,54,63,72,81,90,99,108]
    >>> even_only(Mae9)
    [0, 18, 36, 54, 72, 90, 108]
    """
    a = []
    for i in l:
        if i % 2 == 0:
            a.append(i)
        elif i % 2 != 0:
            pass
    return a


def love(text):
    """ This function returns the replacement between the second last words of string into "love"

    >>> Can = "I like Python"
    >>> love(Can)
    'I love Python'
    >>> Not = "I really like Python"
    >>> love(Not)
    'I really love Python'
    >>> Think = "Do you like me?"
    >>> love(Think)
    'Do you love me?'
    >>> More = "From my heart, you are my sunshine and I really like you"
    >>> love(More)
    'From my heart, you are my sunshine and I really love you'
    >>> Doctest = "My grammar is so suck"
    >>> love(Doctest)
    'My grammar is love suck'
    """
    a = list(text.split(" "))
    a[-2] = "love"
    yo = (" ".join(a))
    return yo


def is_anagram(a, b):
    """ This function check that the two parameter are anagram or not and return the boolean

    >>> is_anagram('arrange', 'Rear  Nag')
    True
    >>> is_anagram('Teeranut', 'TrETnUeA')
    True
    >>> is_anagram('Nut', 'T      n     U')
    True
    >>> is_anagram('soHungry', 'hungrys')
    False
    >>> is_anagram('doctest', 'docstring')
    False
    """
    one = a.lower()
    two = b.lower()


    real_a = one.replace(" ", "")
    real_b = two.replace(" ", "")


    real_one = sorted(real_a)
    real_two = sorted(real_b)


    if real_one == real_two:
        return True
    else:
        return False



def has_duplicates(n):
    """ This function returns the boolean according to the adjacent value of a number in list

    >>> has_duplicate([1,2,3,4,5])
    False
    >>> has_duplicate([1,2,3,4,5,2])
    True
    >>> has_duplicate([1,1,2,3,3,4,5,5,5,5,5,5,5,5,5])
    True
    >>> has_duplicate([33245654758,8576453213,4563222,5657645,6534,67456353])
    False
    >>> has_duplicate([0,9,7,2,0,7,9,0,6,0])
    True
    """
    for i in range(len(n)):
        if n.count(i) >= 2:
            return True
    return False




def average(n):
    """ This function returns the mean average of a list of number

    >>> average([1,1,5,5,10,8,7])
    5.285714285714286
    >>> average([1,2,3,4,5,6,7,8,9,10])
    5.5
    >>> average([3,5,3,5,7,4,5])
    4.571428571428571
    >>> average([1,3,5,4,8,3,6,4,3,5,7,7,4,6,8,4,9])
    5.117647058823529
    >>> average([12,23,34,45,56,67,78,89,90])
    54.888888888888886
    """
    sorted(n)
    all = sum(n)
    return all/len(n)



def centered_average(nums):
    """ This function returns the average of a list except the min and max value and if they are multiple of copied of min and max, choose one

    >>> nums = [1,1,5,5,10,7,8]
    >>> centered_average(nums)
    5.2
    >>> nums = [1,10,5,3,10,7,9]
    >>> centered_average(nums)
    6.8
    >>> nums = [234,436,41,436,53,25,3]
    >>> centered_average(nums)
    157.8
    >>> nums = [4,52,54,54,657,534]
    >>> centered_average(nums)
    173.5
    >>> nums = [1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,1]
    >>> centered_average(nums)
    4.764705882352941
    """
    max = nums[0]
    min = nums[0]
    for i in nums:
        if i > max:
            max = i
        if i < min:
            min = i
        all = max + min
    return (sum(nums) - all) / (len(nums) - 2)

def reverse_pair(text):
    """ This function returns reversed sentence

    >>> reverse_pair("May the force be with you")
    'you with be force the May'
    >>> reverse_pair("To be continued")
    'continued be To'
    >>> reverse_pair("Copying is really bad")
    'bad really is Copying'
    >>> reverse_pair("SKE are the best")
    'best the are SKE'
    >>> reverse_pair("We are the warriors that build this town")
    'town this build that warriors the are We'
    """
    res = list(text.split(" "))
    real_res = res[::-1]
    yo = (" ".join(real_res))
    return yo



def match_ends(text):
    """ This function returns the amount of string that the first char and the last char are the same

    >>> match_ends(["Gingering", "hello", "wow"])
    2
    >>> match_ends(["enforce", "Shotgun", "gunner", "pop", "illuminati"])
    3
    >>> match_ends(["health", "refer", "to", "modern"])
    2
    >>> match_ends(["supercalafragalisticexpialidocious", "supervision", "nationalism"])
    1
    >>> match_ends(["Why", "Im", "So", "Sleepy"])
    0
    """
    count = 0
    for i in text:
        if i[0].lower() == i[-1].lower():
            count = count + 1
    return count



def remove_adjacent(element):
    """ This function returns a list where all similar value are deleted

    >>> remove_adjacent([1,2,2,3,3,4,4,5])
    [1, 2, 3, 4, 5]
    >>> remove_adjacent([1,1,1,1,1,1,1,1,1,2,3])
    [1, 2, 3]
    >>> remove_adjacent([2,2,4,3,3,9,4,4,16])
    [2, 4, 3, 9, 4, 16]
    >>> remove_adjacent([5,5,25,6,6,36,7,7,49])
    [5, 25, 6, 36, 7, 49]
    >>> remove_adjacent([8,8,64,9,9,81,10,10,100])
    [8, 64, 9, 81, 10, 100]
    >>> remove_adjacent([1,2,2,3,2,2,1])
    [1, 2, 3, 2, 1]
    """
    i = 1
    while i < len(element):
        if element[i] == element[i - 1]:
            del element[i]
            i = i - 1
        i = i + 1
    return element


