

# 1
def ll_sum(main_list: list):
    """This func is to takes a list of lists of integers 
    and adds up the elements from all of the nested lists.

    Examples:
        >>> ll_sum([[1, 2], [3], [4, 5, 6]])
        21
        >>> ll_sum([[6, 66, [66]], 666, [6666, 66666]])
        74136
        >>> ll_sum([[[13], [32], [43]], 54, [[56], 76]])
        274
        >>> ll_sum([3, [25, [33]], [456], [8858, 67]])
        9442
        >>> ll_sum([[3, 4, 9], [4, [8], [[16]]]])
        44
    """
    sum = 0
    for element in main_list:
        if type(element) == list:
            sum += ll_sum(element)
        else:
            sum += element
    return sum

# 2
def cumulative_sum(listx: list):
    """This func is to takes a list of numbers and 
    returns a new list where the ith element is the sum of the first i + 1 elements from the original list.

    Examples:
        >>> cumulative_sum([1, 2, 3])
        [1, 3, 6]
        >>> cumulative_sum([4, 66, 77, 88, 99])
        [4, 70, 147, 235, 334]
        >>> cumulative_sum([67, 342, 32])
        [67, 409, 441]
        >>> cumulative_sum([77, 0, 9 ,81])
        [77, 77, 86, 167]
        >>> cumulative_sum([1, 3, 5, 7, 9])
        [1, 4, 9, 16, 25]
    """
    sum = 0
    intex = 0
    for element in listx:
        sum += element
        listx[intex] = sum
        intex += 1
    return listx

# 3
def middle(listy: list):
    """This func is to takes a list and returns a new list that contains all but the first and last elements.

    Examples:
        >>> middle([1, 2, 3, 4])
        [2, 3]
        >>> middle([54, 78, 656, 90, 77])
        [78, 656, 90]
        >>> middle([1111, 900, 7367, 366, 9999])
        [900, 7367, 366]
        >>> middle([77, 787, 878, 88])
        [787, 878]
        >>> middle([565, 766, 787, 9009, 212, 3232])
        [766, 787, 9009, 212]
    """
    del listy[0]
    del listy[-1]
    return listy

# 4
def chop(listz: list):
    """This func is to takes a list, modifies it by removing the first and last elements, and returns None.

    Examples:
        >>> t = [1, 2, 3, 4]
        >>> chop(t)
        >>> t
        [2, 3]

        >>> me = [54, 78, 656, 90, 77]
        >>> chop(me)
        >>> me
        [78, 656, 90]

        >>> you = [1111, 900, 7367, 366, 9999]
        >>> chop(you)
        >>> you
        [900, 7367, 366]

        >>> john = [77, 787, 878, 88]
        >>> chop(john)
        >>> john
        [787, 878]

        >>> son_of_john = [565, 766, 787, 9009, 212, 3232]
        >>> chop(son_of_john)
        >>> son_of_john
        [766, 787, 9009, 212]
    """
    del listz[0]
    del listz[-1]
    return

# 5
def is_sorted(unknow_list: list):
    """This func is to takes a list as a parameter and 
    returns True if the list is sorted in ascending order and False otherwise.

    Examples:
        >>> is_sorted([1, 2, 2])
        True
        >>> is_sorted(['b', 'a'])
        False
        >>> is_sorted([])
        True
        >>> is_sorted([-4.7, -3, 1.008, 43.88])
        True
        >>> is_sorted([766, 987, 544, 65, 1])
        False
    """
    return unknow_list == sorted(unknow_list)

# 6
def front_x(xxxlist: list):
    """This func is to returns a list with the strings in sorted order, 
    except group all the strings that begin with 'x' first.

    Examples:
        >>> l = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
        >>> front_x(l)
        ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']

        >>> gg = ['all', 'text', 'between', 'actions', 'is', 'copied']
        >>> front_x(gg)
        ['actions', 'all', 'between', 'copied', 'is', 'text']

        >>> tt = ['xu', 'xis', 'xyst', 'xylan', 'xtster', 'xerosis', 'xanthine', 'xerophile', 'xenotropic', 'xanthophyll', 'xylograph']
        >>> front_x(tt)
        ['xanthine', 'xanthophyll', 'xenotropic', 'xerophile', 'xerosis', 'xis', 'xtster', 'xu', 'xylan', 'xylograph', 'xyst']

        >>> ss = ['Below', 'is', 'Alist', 'Of', 'Xletter']
        >>> front_x(ss)
        ['Xletter', 'Alist', 'Below', 'Of', 'is']

        >>> kk = ['xbox', 'live', 'except', 'XLNT_Excellent', 'XGF_exgirlfriend']
        >>> front_x(kk)
        ['XGF_exgirlfriend', 'XLNT_Excellent', 'xbox', 'except', 'live']

    """
    list_have_x = []
    list_have_no_x = []
    for word in xxxlist:
        if word[0] == "x" or word[0] == "X":
            list_have_x.append(word)
        else:
            list_have_no_x.append(word)
    return sorted(list_have_x)+sorted(list_have_no_x)

# 7
def even_only(num_list: list):
    """This func is to take a list of integers, and return a new list with only even numbers.

    Examples:
        >>> even_only([3, 1, 4, 1, 5, 9, 2, 6, 5])
        [4, 2, 6]
        >>> even_only([4, 5, 463, 3, 35, 55, 4566, 6])
        [4, 4566, 6]
        >>> even_only([43, 54, 54, 656, 34, 324, 232323, 3])
        [54, 54, 656, 34, 324]
        >>> even_only([88, 898, 797, 77, 109])
        [88, 898]
        >>> even_only([6, 4, 3, 433, 6786])
        [6, 4, 6786]
    """
    even_list = []
    for num in num_list:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

# 8
def love(no_love_sentence: str):
    """This func is to change the second last word to “love”.

    Examples:
        >>> love("I like Python")
        'I love Python'
        >>> love("I really like Python")
        'I really love Python'
        >>> love("Do u like me")
        'Do u love me'
        >>> love("What do u like Java")
        'What do u love Java'
        >>> love("how u like it!!!")
        'how u love it!!!'
    """
    love_list = no_love_sentence.split()
    love_list[-2] = 'love'
    return " ".join(love_list)

# 9
def is_anagram(str1: str, str2: str):
    """This func is to takes two strings and returns True if they are anagrams.

    Examples:
        >>> is_anagram('arrange', 'Rear Nag')
        True
        >>> is_anagram('Dusty', 'Study')
        True
        >>> is_anagram('Denver', 'Nrve')
        False
        >>> is_anagram('Stressed', 'Desserts')
        True
        >>> is_anagram('Astronomer', 'Mon tarer')
        False
    """
    str1 = [x for x in str1.lower() if x != " "]
    str2 = [y for y in str2.lower() if y != " "]
    check_list = []
    for ch in str1:
        if ch in str2:
            str2.remove(ch)
        else:
            check_list.append(ch)
    return check_list == [] and str2 == []

# 10
def has_duplicates(original_list: list):
    """This func is to takes a list and returns True if there is any element that appears more than once.

    Examples:
        >>> has_duplicates([1, 2, 3, 4, 5])
        False
        >>> has_duplicates([1, 2, 3, 4, 5, 2])
        True
        >>> has_duplicates([1, 2, 4, 6, 1, 2])
        True
        >>> has_duplicates([3, 45, 57, 99, 50, 8])
        False
        >>> has_duplicates([5, 55, 555, 5, 5555])
        True
    """
    copy_list = original_list.copy()
    for element in original_list:
        copy_list.remove(element)
        if element in copy_list:
            return True
    return False

# 11
def average(nums: list):
    """This func is to returns the mean average of a list of numbers.

    Examples:
        >>> average([1, 1, 5, 5, 10, 8, 7])
        5.285714285714286
        >>> average([2, 43, 536, 65, 65])
        142.2
        >>> average([53, 54, 66, 676, 6])
        171.0
        >>> average([435, 5465, 656, 56567, 5, 34])
        10527.0
        >>> average([6, 76, 7, 5, 4, 2432, 43, 4, 43, 4, 34])
        241.63636363636363
    """
    return sum(nums)/len(nums)

# 12
def centered_average(nums: list):
    """This func is to returns a "centered" average of a list of numbers,
    ignores the largest and smallest values in the list.

    Examples:
        >>> centered_average([1, 1, 5, 5, 10, 8, 7])
        5.2
        >>> centered_average([2, 4, 3, 54, 65, 7, 54])
        24.4
        >>> centered_average([434, 54, 656, 7, 8, 8764, 654, 65, 32])
        271.85714285714283
        >>> centered_average([7, 7, 3, 3, 3, 6])
        4.75
        >>> centered_average([6, 9, 8, 7, 3, 42, 34])
        12.8
    """
    nums = sorted(nums)
    del nums[0], nums[-1]
    return sum(nums)/len(nums)

# 13
def reverse_pair(sentence: str):
    """This func is to returns the reverse pair of the input sentence.

    Examples:
        >>> reverse_pair("May the fourth be with you")
        'you with be fourth the May'

        >>> reverse_pair("First get the reader's attention")
        "attention reader's the get First"

        >>> reverse_pair("what you are going to discuss")
        'discuss to going are you what'

        >>> reverse_pair("You could state the causes and effects to be discussed")
        'discussed be to effects and causes the state could You'

        >>> reverse_pair("the main points that will develop your argument")
        'argument your develop will that points main the'
    """
    sentence_list = sentence.split()
    return ' '.join(list(reversed(sentence_list)))

# 14
def match_ends(a_list: list):
    """This func is to returns the count of the number of strings 
    where the string length is 2 or more and the first and last chars of the string are the same.

    Examples:
        >>> match_ends(["Gingering", "hello", "wow"])
        2
        >>> match_ends(["non-interactive", "Text", "labels", "GUI"])
        1
        >>> match_ends(["command", "as", "follows", "throughout", "section"])
        1
        >>> match_ends(["test", "t", "face-off", "lumbersexual", "me", "friend"])
        3
        >>> match_ends(["Quick", "play", "pray", "place"])
        0
    """
    n = 0
    for word in a_list:
        if len(word) >= 2 and word[0].lower() == word[-1].lower():
            n += 1
    return n

# 15                                                  
def remove_adjacent(ajt_list: list):
    """This func is to returns a list where 
    all adjacent elements have been reduced to a single element.

    Examples:
        >>> remove_adjacent([1, 2, 2, 3])
        [1, 2, 3]
        >>> remove_adjacent([2, 3, 2, 4, 4, 5, 4, 5, 3, 3])
        [2, 3, 2, 4, 5, 4, 5, 3]
        >>> remove_adjacent([3, 4, 2, 2, 1, 11, 1, 3])
        [3, 4, 2, 1, 11, 1, 3]
        >>> remove_adjacent([4, 7, 67, 67, 4, 99, 99, 8, 9900, 99])
        [4, 7, 67, 4, 99, 8, 9900, 99]
        >>> remove_adjacent([23, 34, 12, 32])
        [23, 34, 12, 32]
    """
    index = 0
    new_ajt_list = []
    for thing in ajt_list:
        if thing == ajt_list[index-1] and index != 0:
            pass
        else:
            new_ajt_list.append(thing)
        index += 1
    return new_ajt_list


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
