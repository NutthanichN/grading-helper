

def ll_sum(nested_list):#This function will calculate a number in the list
    """"
    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> ll_sum(t)
    21
    >>> a = [[5,2],[34,7],[1,2,3,4]]
    >>> ll_sum(a)
    58
    >>> b = [[85,20],[3,7,54],[10,42,63,4],[4,3,2,1]]
    >>> ll_sum(b)
    298
    >>> c = [[37,75],[5,8,4,3]]
    >>> ll_sum(c)
    132
    >>> d = [[21,53],[3847,5],[87,875,54,543]]
    >>> ll_sum(d)
    5485
    >>> e = [[45,45],[84,75],[14,42,83,64]]
    >>> ll_sum(e)
    452
    """
    result = 0
    for item in nested_list:
        if type(item) == list:
            result += ll_sum(item)
        else:
            result += item
    return result

def cumulative_sum(numbers):#This function will calculate a cumulative sum of a number in the list.
    """
    >>> t = [1, 2, 3]
    >>> cumulative_sum(t)
    [1, 3, 6]
    >>> a = [3,8,7]
    >>> cumulative_sum(a)
    [3, 11, 18]
    >>> b = [5,4,3,8,7,5]
    >>> cumulative_sum(b)
    [5, 9, 12, 20, 27, 32]
    >>> c =[57,43,36,83,37,55]
    >>> cumulative_sum(c)
    [57, 100, 136, 219, 256, 311]
    >>> d = [545,564,843,328,127,255]
    >>> cumulative_sum(d)
    [545, 1109, 1952, 2280, 2407, 2662]
    >>> e = [52,45,84,24,84,54,84,21]
    >>> cumulative_sum(e)
    [52, 97, 181, 205, 289, 343, 427, 448]
    """
    sums = []
    total = 0
    for i in numbers:
        total += i
        sums.append(total)
    return sums

def middle(list):#This function will return a middle number in the list.
    """
    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    >>> a = [654, 45654, 654]
    >>> middle(a)
    [45654]
    >>> b = [12,321,321,123,5642]
    >>> middle(b)
    [321, 321, 123]
    >>> c = [456,654,456,21,215,6354,2151]
    >>> middle(c)
    [654, 456, 21, 215, 6354]
    >>> d = [1,2,3,4,5,6,7,8,9,0]
    >>> middle(d)
    [2, 3, 4, 5, 6, 7, 8, 9]
    >>> e = [10,11,12,13,14,15,16,17,18,19,20]
    >>> middle(e)
    [11, 12, 13, 14, 15, 16, 17, 18, 19]
    """
    new_list = list[1:]
    del new_list[-1]
    return new_list

def chop(list):#This function will removing the first and last elements.
    """
    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    >>> a = [1,2,3,4,5,6,7,8,9,10]
    >>> chop(a)
    >>> a
    [2, 3, 4, 5, 6, 7, 8, 9]
    >>> b = [11,12,13]
    >>> chop(b)
    >>> b
    [12]
    >>> c = [321,654534,745234,7488,65454,654687,5484]
    >>> chop(c)
    >>> c
    [654534, 745234, 7488, 65454, 654687]
    >>> d = [354534534,857468,53484,84,354835,4354,3545,424]
    >>> chop(d)
    >>> d
    [857468, 53484, 84, 354835, 4354, 3545]
    >>> e = [3354,35453,4534,534,84,5,151]
    >>> chop(e)
    >>> e
    [35453, 4534, 534, 84, 5]
    """
    del list[0::(len(list) - 1)]
    return None
    return chop(list)

def is_sorted(list):#This function will checking if the list is sorted it will return True and return False otherwise.
    """
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    >>> is_sorted([2132,567454,88488])
    False
    >>> is_sorted(["a", "z"])
    True
    >>> is_sorted(["Z", "A"])
    False
    >>> is_sorted([123,321])
    True
    >>> is_sorted([6545646,456456,321321])
    False
    """
    if sorted(list) == list:
        return True
    else:
        return False

def front_x(list):#This function will append a words but the start letter is x instead a.
    """
    >>> l = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
    >>> front_x(l)
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    >>> a = ['xxx', 'asd', 'yyy', 'zzz', 'aaa']
    >>> front_x(a)
    ['xxx', 'aaa', 'asd', 'yyy', 'zzz']
    >>> b = ['asd', 'dsa', 'xsw', 'xdsa', 'xdsa', 'axax']
    >>> front_x(b)
    ['xdsa', 'xdsa', 'xsw', 'asd', 'axax', 'dsa']
    >>> c = ['x', 'a', 'xa']
    >>> front_x(c)
    ['x', 'xa', 'a']
    >>> d = ['xa' ,'ax', 'xax', 'axa']
    >>> front_x(d)
    ['xa', 'xax', 'ax', 'axa']
    >>> e = ['zxc', 'xzc', 'zca', 'xcxz', 'asx']
    >>> front_x(e)
    ['xcxz', 'xzc', 'asx', 'zca', 'zxc']
    """
    asd = []
    dsa = []

    for word in list:
        if word.startswith('x'):
            asd.append(word)
        else:
            dsa.append(word)

    return sorted(asd) + sorted(dsa)

def even_only(list):#Return a list of only the even numbers in the input list.
    """
    >>> even_only([3,1,4,1,5,9,2,6,5])
    [4, 2, 6]
    >>> even_only([1,3,5,7,9])
    []
    >>> even_only([0,2,4,6,8,10,12,14])
    [0, 2, 4, 6, 8, 10, 12, 14]
    >>> even_only([1,2,3,4,5,6,7,8,9,0])
    [2, 4, 6, 8, 0]
    >>> even_only([10,11,12,13,14,15])
    [10, 12, 14]
    >>> even_only([10,20,30,40,50])
    [10, 20, 30, 40, 50]
    """
    evens=[x for x in list if x%2 == 0]
    return evens

def love(text):#This function will change the second last word to "love"
    """
    >>> love("I like Python")
    'I love Python'
    >>> love("I really like Python")
    'I really love Python'
    >>> love("Sabai very like food")
    'Sabai very love food'
    >>> love("Sabai very like sleep")
    'Sabai very love sleep'
    >>> love("I like icecream")
    'I love icecream'
    >>> love("Do you like me?")
    'Do you love me?'
    >>> love("I like eat")
    'I love eat'
    """
    sabai=text.split(' ')
    sabai[-2]='love'
    handsome=' '.join(sabai)
    return  handsome

def is_anagram(stringone, stringtwo):#This function will takes two strings and returns True if they are anagrams.
    """
    >>> is_anagram('arrange', 'Rear Nag')
    True
    >>> is_anagram('fish', 'dog')
    False
    >>> is_anagram('sabai', 'handsome')
    False
    >>> is_anagram('bird', 'sky')
    False
    >>> is_anagram('mouse', 'rat')
    False
    >>> is_anagram('cat', 'dog')
    False
    """
    one=list(stringone.lower())
    two=list(stringtwo.lower())
    if' 'in two :
        two.remove(' ')
    one.sort()
    two.sort()
    if one != two:
        return False
    else:
        return True



def has_duplicates(my_list):#This function will check a list,If there is any element that appears more than once it will return True.
    """
    >>> has_duplicates([1, 2, 3, 4, 5])
    False
    >>> has_duplicates([1, 2, 3, 4, 5, 2])
    True
    >>> has_duplicates([1,1,2,3,4,5,6,7,8,9,10])
    True
    >>> has_duplicates([0,1,2,3,4,5,6,7,8,9,10])
    False
    >>> has_duplicates([5,5,5,5,5,5,5,5,5,5,5])
    True
    >>> has_duplicates([123,123,321,321,123,21,321,321,21,31,23,213,21,2])
    True
    >>> has_duplicates([0,124,7,5,8,1,5454,4684534,543864653])
    False
    """
    i = 0
    while i < len(my_list):
        if my_list.count(my_list[i]) > 1:
            return True
        elif i == (len(my_list) - 1):
            return False
        i += 1


def average(nums):#This function will calculate an average of the list of numbers.
    """
    >>> average([1, 1, 5, 5, 10, 8, 7])
    5.285714285714286
    >>> average([5,5,7,98,1,3,74,5,1,1])
    20.0
    >>> average([684,687465,4684,6874,684,645])
    116839.33333333333
    >>> average([654,54,654,654,54,654])
    454.0
    >>> average([54,684,654,864,65465,4564])
    12047.5
    >>> average([654,654,654,654,867,41,54,5644])
    1152.75
    """
    return sum(nums) / len(nums)


def centered_average(nums):#This function returns a "centered" average of a list of numbers, which is the mean average of the values that ignores the largest and smallest values in the list.
    """
    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([542,6548,65421,23121])
    14834.5
    >>> centered_average([5454,354534,3215,1])
    4334.5
    >>> centered_average([24,84,510,654,8654,5,1050])
    464.4
    >>> centered_average([321,38,456,4156,4,18,7451561,54])
    840.5
    >>> centered_average([564,2315,48,75,21,97,84])
    173.6
    """
    asd = sorted(nums)[1:-1]
    return sum(asd) / len(asd)

def reverse_pair(asd):#This function returns the reverse pair of the input sentence.
    """
    >>> reverse_pair("May the fourth be with you")
    'you with be fourth the May'
    >>> reverse_pair("You and I")
    'I and You'
    >>> reverse_pair("Sabai is very handsome")
    'handsome very is Sabai'
    >>> reverse_pair("I am the Flash")
    'Flash the am I'
    >>> reverse_pair("My name is Sabai")
    'Sabai is name My'
    >>> reverse_pair("Happy birthday to you")
    'you to birthday Happy'
    """
    sabai=asd.split(' ')
    newlist=sabai[::-1]
    newstring=" ".join(newlist)
    return  newstring

def match_ends(asd):#This function will returns the count of the number of strings where the string length is 2 or more and the first and last chars of the string are the same.
    """
    >>> match_ends(["Gingering","hello","wow"])
    2
    >>> match_ends(["asdasd","dsasd","dsasdsad"])
    2
    >>> match_ends(["olo","razer","wowowowowowow","asdasd"])
    3
    >>> match_ends(["lazer","render","asasasa","sabai"])
    2
    >>> match_ends(["hen","chic","reacher"])
    2
    >>> match_ends(["asdasda","cvcvc","vcvcv","hohoh","ohohohoh"])
    4
    """
    beer=" ".join(asd)
    sabai=beer.lower()
    xxx=sabai.split(" ")
    numnum=0
    for x in xxx:
        if len(x)>=2:
            if x[0]==x[-1]:
                numnum += 1
        else:
            numnum = numnum + 0
    return numnum

def remove_adjacent(nums):#This function will returns a list where all adjacent elements have been reduced to a single element.
    """
    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([1,1,1,1,1,2])
    [1, 2]
    >>> remove_adjacent([1,2,3,4,5,6,7,8,9,0,0,0,0,0,0,0])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    >>> remove_adjacent([5,55,4,5])
    [5, 55, 4, 5]
    >>> remove_adjacent([123,321,123,322])
    [123, 321, 123, 322]
    >>> remove_adjacent([64,65,66,66,676,68,69])
    [64, 65, 66, 676, 68, 69]
    """
    result = []
    for num in nums:
        if len(result) == 0 or num != result[-1]:
            result.append(num)
    return result