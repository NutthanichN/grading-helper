

# 1
def ll_sum(new_list):
    """function that takes a list of lists of integers and adds up the elements from all of the
    nested lists.
    >>> ll_sum([[1, 2], [3], [4, 5, 6]])
    21
    >>> ll_sum([[1, 2], [6], [8, 10, 11]])
    38
    >>> ll_sum([[1, 4], [5], [7, 10]])
    27
    >>> ll_sum([[2, 3], [5], [7, 0]])
    17
    >>> ll_sum([[4, 6], [5], [7, 10]])
    32
    """
    num = 0
    for item in new_list:
        if type(item) == list:
            num = num + ll_sum(item)
        else:
            num = num + item
    return num


# 2
def cumulative_sum(num):
    """function that takes a list of numbers and returns the cumulative sum
    >>> cumulative_sum([1, 2, 3,4,5])
    [1, 3, 6, 10, 15]
    >>> cumulative_sum([1, 3, 5,7])
    [1, 4, 9, 16]
    >>> cumulative_sum([2, 4, 6,8])
    [2, 6, 12, 20]
    >>> cumulative_sum([2, 3, 8,9])
    [2, 5, 13, 22]
    >>> cumulative_sum([3, 7, 8,9])
    [3, 10, 18, 27]
    """
    start = 0
    result = []
    for number in num:
        start = start + number
        result.append(start)
    return result




# 3
def middle(old_list):
    """function that takes a list and returns a new list that contains all but the first and last
elements.
    >>> middle([1, 2, 3, 4])
    [2, 3]
    >>> middle([1, 2, 3, 4,5,6,7])
    [2, 3, 4, 5, 6]
    >>> middle([1, 3, 4, 5, 9])
    [3, 4, 5]
    >>> middle([2, 4, 6, 8, 10])
    [4, 6, 8]
    >>> middle([12, 13, 14, 15, 16])
    [13, 14, 15]
    """
    a_new_list = old_list[1:-1]
    return a_new_list


# 4
def chop(list):
    """function that takes a list, modifies it by removing the first and last elements, and returns None.
  >>> chop([0,1,2,3,4])

  >>> chop([1,2,3,4,7])

  >>> chop([2,4,5,6,8])

  >>> chop([10,11,12,13,14])

  >>> chop([20,21,22,23,24])

  """
    del list[0]
    del list[-1]




# 5
def is_sorted(old_list):
    """function  that takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise.
    >>> is_sorted([1,2,3])
    True
    >>> is_sorted(["b","a"])
    False
    >>> is_sorted([1,5,8,6])
    False
    >>> is_sorted([4,5,6,7,8])
    True
    >>> is_sorted(["p","f"])
    False
    """
    new_list = old_list[0:]
    new_list.sort()
    if (new_list == old_list):
        return True
    else:
        return False


# 6
def front_x(words):
    """function that returns a list with the strings in sorted order, except group all the strings that begin with 'x' first.
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    >>> front_x(['parn', 'xyz', 'apple'])
    ['xyz', 'apple', 'parn']
    >>> front_x(['iup', 'xnn', 'ske'])
    ['xnn', 'iup', 'ske']
    >>> front_x(['iuh.kp', 'xnlln', 'opk'])
    ['xnlln', 'iuh.kp', 'opk']
    >>> front_x(['uyfiu', 'xoihpo', 'ogk'])
    ['xoihpo', 'ogk', 'uyfiu']
    """
    xlist = []
    normallist = []

    for x_word in words:
        if x_word[0] == 'x':
            xlist.append(x_word)
        else:
            normallist.append(x_word)

    return sorted(xlist) + sorted(normallist)




# 7
def even_only(list):
    """function that will take a list of integers, and return a new list with only even numbers.
    >>> even_only([3,1,4,1,5,9,2,6,5])
    [4, 2, 6]
    >>> even_only([2,3,5,6,8,9])
    [2, 6, 8]
    >>> even_only([4,2,3,5,8,6])
    [4, 2, 8, 6]
    >>> even_only([1,2,3,4,5,10])
    [2, 4, 10]
    >>> even_only([11,12,13,14,15,10])
    [12, 14, 10]
    """
    even_list = [ ]
    for num in list:
      if num%2 == 0 :
        even_list.append(num)
    return even_list




# 8
def love(text):
    """  function that will change the second last word to “love”.
    >>> love("I really like Python")
    'I really love Python'
    >>> love("I like Python")
    'I love Python'
    >>> love("I hate you")
    'I love you'
    >>> love("pain is hate")
    'pain love hate'
    >>> love("i hate math.")
    'i love math.'
    """
    text_list= text.split(' ')
    text_list[-2] = 'love'
    new_text = ' '.join(text_list)
    return new_text


# 9
def is_anagram(string1, string2):
    """return True if strings are anagrams of each other
    >>> is_anagram('arrange', 'Rear Nag')
    True
    >>> is_anagram('analft', 'youu uu')
    False
    >>> is_anagram('analft','shjf')
    False
    >>> is_anagram('boy','girl')
    False
    >>> is_anagram('poui', 'oipu')
    True
    """
    list1 = list(string1.lower())
    list2 = list(string2.lower())
    if ' ' in list2 :
        list2.remove(' ')
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False




# 10
def has_duplicates(num):
    """function that takes a list and returns True if there is any element that
     appears more than once.

    >>> has_duplicates([1, 2, 3, 4, 5, 3])
    True
    >>> has_duplicates([1, 2, 3, 4, 5])
    False
    >>> has_duplicates([1, 2, 3, 2, 1, 3])
    True
    >>> has_duplicates([2,4,5,6,6,7])
    True
    >>> has_duplicates([11,12,13,14])
    False
    """
    a = sorted(num)
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            return True
    return False
# print(has_duplicates([1, 2, 3, 4, 5, 3]))


# 11
def average(nums):
    """ function that returns the mean average of a list of numbers.
    >>> average([1, 1, 5, 5, 10, 8, 7])
    5.285714285714286
    >>> average([3,4,5,7])
    4.75
    >>> average([5,6,9,7])
    6.75
    >>> average([15,16,19,17])
    16.75
    >>> average([12,14,16,17])
    14.75
    """
    a = sum(nums)
    b = len(nums)
    ave=a/b
    return ave

# 12
def centered_average(nums):
    """function that returns a "centered" average of a list of numbers,which is the mean average of the values
    that ignores the largest and smallest values in the list.
    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([2,3,4,5])
    3.5
    >>> centered_average([5,2,6,3])
    4.0
    >>> centered_average([15,12,16,13])
    14.0
    >>> centered_average([1,4,8,4,7])
    5.0
    """
    nums.sort()
    new_num = nums[1:-1]
    ave_num= sum(new_num)/(len(nums)-2)
    return  ave_num


# 13
def reverse_pair(str):
    """ function that returns the reverse pair of the input sentence.
    >>> reverse_pair("May the fourth be with you")
    'you with be fourth the May'
    >>> reverse_pair("i love you")
    'you love i'
    >>> reverse_pair("kill this love")
    'love this kill'
    >>> reverse_pair("you are mine")
    'mine are you'
    >>> reverse_pair("i love python")
    'python love i'
    """
    list=str.split(' ')
    new_list=list[::-1]
    new_str=" ".join(new_list)
    return  new_str


# 14
def match_ends(words):
    """ function returns the count of the number of strings where the string length is 2 or more and the first and last
    chars of the string are the same.
    >>> match_ends(["Gingering","hello","wow"])
    2
    >>> match_ends(["gingering","pig","kik"])
    2
    >>> match_ends(["pppppio","pip","kik"])
    2
    >>> match_ends(["panida","parn","juj"])
    1
    >>> match_ends(["panida","parn","ske"])
    0

    """
    chang_list_str =" ".join(words)
    new_word= chang_list_str.lower()
    new_list = new_word.split(" ")
    count = 0
    for i in new_list:
        if len(i) >= 2 :
          if i[0] == i[-1]:
            count = count + 1
        else:
            count = count+0
    return count


# 15
def remove_adjacent(nums):
    """ function that returns a list where all adjacent elements have been reduced to a single element.
    >>> remove_adjacent([1, 2,2,3])
    [1, 2, 3]
    >>> remove_adjacent([1, 2,4,4])
    [1, 2, 4]
    >>> remove_adjacent([1, 2, 3, 3, 6, 6])
    [1, 2, 3, 6]
    >>> remove_adjacent([1,1,3,4,5])
    [1, 3, 4, 5]
    >>> remove_adjacent([2,2,4,7,7])
    [2, 4, 7]
    """
    result = []
    for i in nums:
       if len(result) == 0 or i != result[-1]:
        result.append(i)
    return result


if __name__ == "__main__" :
    import doctest
    doctest.testmod(verbose=True)
