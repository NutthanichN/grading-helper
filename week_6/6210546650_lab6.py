

# Chanathip Thumkanon
# 6210546650

def ll_sum(lists_int):
    """
    This function takes a list of lists of integers
    and adds up the elements in all of the
    nested lists.
    :param lists_int: List of lists of integers.
    :return: The sum of all integers in all nested lists.
    >>> ll_sum([[2],[3],[4,5]])
    14
    >>> ll_sum([[5,6],[11,20],[2],[1]])
    45
    >>> ll_sum([[9,-14,3],[-7,-19]])
    -28
    >>> ll_sum([])
    0
    >>> ll_sum([[],[3,17],[-12]])
    8
    """
    a = 0
    for L in lists_int:
        for i in L:
            a += i
    return a


def cumulative_sum(num_list):
    """
    This function takes a list of numbers and returns the cumulative sum;
    that is, a new list where the ith element is the sum
    of the first i + 1 elements from the original list.
    :param num_list: List of integers.
    :return: List of cumulative sum of integer from <num_list>.
    >>> cumulative_sum([1,3,5,7,9])
    [1, 4, 9, 16, 25]
    >>> cumulative_sum([4,12,-5,8,0])
    [4, 16, 11, 19, 19]
    >>> cumulative_sum([9,80,500,2000,10000])
    [9, 89, 589, 2589, 12589]
    >>> cumulative_sum([])
    []
    >>> cumulative_sum([4302,-5000,-2000,100,197])
    [4302, -698, -2698, -2598, -2401]
    """
    b = 0
    new_list = []
    for i in range(len(num_list)):
        b += num_list[i]
        new_list.append(b)
    return new_list


def middle(list):
    """
    This function takes a list and returns a new list
    that contains all but the first and last elements.
    :param list: List of any type of element.
    :return: A new list that has all the elements from the input
             except the first and the last ones.
    >>> middle([12,4,15,8])
    [4, 15]
    >>> middle(['log','wood','lumber'])
    ['wood']
    >>> middle([5,4])
    []
    >>> middle([])
    []
    >>> middle(['none'])
    []
    """
    new_list = list[1:-1]
    return new_list


def chop(list):
    """
    This function takes a list, modifies it by removing the
    first and last elements, and returns None.
    :param list: List of any type of element.
    :return: None
    >>> chop(['1','11','9','7']) # this case returns None

    >>> t = ['First','Middle','Last']; chop(t); print(t)
    ['Middle']
    >>> s = [999,99,9,99,999]; chop(s); print(s)
    [99, 9, 99]
    >>> r = []; chop(r); print(r)
    []
    >>> u = ['-72',72,'dog',50.2,'Pokemon','noob']; chop(u); print(u)
    [72, 'dog', 50.2, 'Pokemon']
    """
    if len(list) >= 2:
        list.pop(0)
        list.pop(-1)
    return None


def is_sorted(list):
    """
    This function takes a list as a parameter and returns True
    if the list is sorted in ascending order and False otherwise.
    :param list: List of elements of the same type.
    :return: True or False
    >>> is_sorted([1,2,3,4,5,10])
    True
    >>> is_sorted([1,2,3,4,5,1,2,3,4,5])
    False
    >>> is_sorted(['bac','on','plate','zebra'])
    True
    >>> is_sorted(['indigo'])
    True
    >>> is_sorted([])
    True
    """
    for i in range(1,len(list)):
        if list[i-1] > list[i]:
            return False
    return True


def front_x(list):
    """
    This function takes a list of strings and returns a list
    with the strings in sorted order, except group all the
    strings that begin with 'x' first.
    :param list: List of <string>
    :return: List of sorted <string> where any <string> that begins
    with 'x' has the higher priority.
    >>> front_x(['40','20'])
    ['20', '40']
    >>> front_x(['avocado','Avogadro','Bantu','bag'])
    ['Avogadro', 'Bantu', 'avocado', 'bag']
    >>> front_x(['Eirin', 'Xunatic', 'xade', 'Yagokoro', 'elixir'])
    ['Xunatic', 'xade', 'Eirin', 'Yagokoro', 'elixir']
    >>> front_x(['Fuji','First','Xin Zhao','Last'])
    ['Xin Zhao', 'First', 'Fuji', 'Last']
    >>> front_x([])
    []
    """
    xlist = []
    olist = []
    for s in list:
        if s[0] == 'x' or s[0] == 'X':
            xlist.append(s)
        else:
            olist.append(s)
    xlist.sort()
    olist.sort()
    return xlist + olist


def even_only(list):
    """
    This function take a list of integers,
    and return a new list with only even numbers.
    :param list: List of integers.
    :return: List of even integers.
    >>> even_only([908,14,35,17])
    [908, 14]
    >>> even_only([21,17,11,9])
    []
    >>> even_only([1,2,3,4,5,6,7,8,9,10,0,11,10])
    [2, 4, 6, 8, 10, 0, 10]
    >>> even_only([2,10000,4005,2343])
    [2, 10000]
    >>> even_only([])
    []
    """
    new_list = []
    for i in list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list


def love(text):
    """
    This function changes the second last word to “love”
    :param text: A sequence of words separated by spaces.
    :return: A modified text where the second last word is 'love'.
    >>> love("I won't stop you")
    "I won't love you"
    >>> love("I both like and dislike Pokemon")
    'I both like and love Pokemon'
    >>> love("I hate myself")
    'I love myself'
    >>> love("Have you attend the programming class?")
    'Have you attend the love class?'
    >>> love("A")
    'A'
    """
    list = text.split()
    if len(list) >= 2:
        list[-2] = 'love'
        return ' '.join(list)
    return text


def is_anagram(str1,str2):
    """
    This function compares two input <string> and
    returns whether they are anagrams.
    :param str1: First string to compare.
    :param str2: Second string to compare.
    :return: True or False
    >>> is_anagram('Pokemon','Komopen')
    True
    >>> is_anagram('Fienn TIcaMg', 'magnificent')
    True
    >>> is_anagram('Dog', 'good')
    False
    >>> is_anagram('1354','3541')
    True
    >>> is_anagram(' ',' ')
    True
    """
    l1 = []
    l2 = []
    s1 = str1.lower()
    s2 = str2.lower()
    for c in s1:
        if c != ' ':
            l1.append(c)
    for c in s2:
        if c != ' ':
            l2.append(c)
    l1.sort()
    l2.sort()
    return l1 == l2


def has_duplicates(list):
    """
    This function takes a list and returns True if there is any element
    that appears more than once. It does not modify the original list.
    :param list: List of elements of the same type.
    :return: True or False; whether there is any duplicate elements.
    >>> has_duplicates([1,2,3,4,5,6,0,7,11])
    False
    >>> has_duplicates([3,5,7,33,4,5])
    True
    >>> has_duplicates(['iup','ske','cpe','Iup'])
    False
    >>> has_duplicates([])
    False
    >>> has_duplicates(['',''])
    True
    """
    new_list = list
    new_list.sort()
    for i in range(1,len(new_list)):
        if new_list[i-1] == new_list[i]:
            return True
    return False


def average(nums):
    """
    This function takes a list of numbers and returns their average.
    :param nums: A list of numbers.
    :return: An average.
    >>> average([1,3,5])
    3.0
    >>> average([58.98,1.7,49.85,111.1])
    55.4075
    >>> average([7,4,2,-8,10,-9])
    1.0
    >>> average([99.9,-133.4,-54,-72,100])
    -11.9
    >>> average([])
    0
    """
    sum = 0
    if len(nums) != 0:
        for n in nums:
            sum += n
        return sum/len(nums)
    return 0


def centered_average(nums):
    """
    This function returns a "centered" average of a list of numbers,
    which is the mean average of the values that ignores the largest
    and smallest values in the list. If there are multiple copies of
    the smallest/largest value, it takes just one copy of each.
    :param nums: A list of numbers.
    :return: An average without the largest and smallest number
    >>> centered_average([25,1,9,7])
    8.0
    >>> centered_average([4.22,1,9.4,12,5.2,1,12])
    6.364
    >>> centered_average([-3,-94,8,5,7,4,-11])
    0.4
    >>> centered_average([24,12])
    18.0
    >>> centered_average([])
    0
    """
    if len(nums) != 0:
        sm = nums[0]
        lg = nums[0]
        sum = 0
        for n in nums:
            sum += n
            if sm > n:
                sm = n
            if lg < n:
                lg = n
        if len(nums) >= 3:
            return (sum-sm-lg)/(len(nums)-2)
        return sum/len(nums)
    return 0


def reverse_pair(sentence):
    """
    This function returns the reverse pair of the input sentence.
    :param sentence: A sequence of words.
    :return: A reversed order of the sentence.
    >>> reverse_pair("The cat is a dog")
    'dog a is cat The'
    >>> reverse_pair("13 + 5 = 18")
    '18 = 5 + 13'
    >>> reverse_pair("Pokemon gotta catch'em all.")
    "all. catch'em gotta Pokemon"
    >>> reverse_pair("Reversedorderofthesentence")
    'Reversedorderofthesentence'
    >>> reverse_pair("")
    ''
    """
    list = sentence.split()
    l = []
    for s in list:
        l = [s] + l
    return ' '.join(l)


def match_ends(list):
    """
    This function takes a list of strings and returns the
    count of strings which their length are 2 or more and their
    first and last chars are the same.
    :param list: A list of strings.
    :return: The number of strings that have matching ends
    >>> match_ends(['youth','stamp','magnet'])
    0
    >>> match_ends(['refer','solids','rag'])
    2
    >>> match_ends(['1001','5425', '2904', '4034'])
    3
    >>> match_ends([])
    0
    """
    count = 0
    for s in list:
        s = s.lower()
        if len(s) >= 2:
            if s[0] == s[-1]:
                count += 1
    return count


def remove_adjacent(list):
    """
    This function takes a list of any elements with the same type and
    returns a list where all adjacent elements have been reduced
    to a single element.
    :param list: List of elements with the same type.
    :return: A new list with all duplicate adjacent removed.
    >>> remove_adjacent([2,4,5,2])
    [2, 4, 5, 2]
    >>> remove_adjacent([47,2,5,2,7,7,3,3])
    [47, 2, 5, 2, 7, 3]
    >>> remove_adjacent(['very','good','good','so','so','great'])
    ['very', 'good', 'so', 'great']
    >>> remove_adjacent(['',' ','',''])
    ['', ' ', '']
    >>> remove_adjacent([])
    []
    """
    new_list = list[:1]
    for i in range(1,len(list)):
        if list[i] != list[i-1]:
            new_list.append(list[i])
    return new_list
