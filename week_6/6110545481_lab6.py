

def ll_sum(t):
    """
    Takes a list of lists of integers and adds up 
    the elements from all of the nested lists.
    >>> ll_sum([[5],[3,4],[2,3,4,5,6]])
    32
    >>> ll_sum([[6,7,8,9],[1,2,3,4,5],[4,7,6]])
    62
    >>> ll_sum([[4,8,9],[5,3,7,8],[1,5,8,4,7,8]])
    77
    >>> ll_sum([[3],[6],[5,3,7,5,7]])
    36
    >>> ll_sum([[3],[3],[5],[4,5,6,7,8]])
    41
    """
    count = 0 
    for i in t:
        count += sum(i)
    print(count)
# ll_sum([[1,2],[3],[4,5,6]])

def cumulative_sum(t):
    """
    Takes a list of numbers and returns the cumulative sum.
    >>> cumulative_sum([[5,10,15]])
    [5, 15, 30]
    >>> cumulative_sum([[4,5,6]])
    [4, 9, 15]
    >>> cumulative_sum([[1,3,9]])
    [1, 4, 13]
    >>> cumulative_sum([[2,4,6]])
    [2, 6, 12]
    >>> cumulative_sum([[3,6,9]])
    [3, 9, 18]
    """
    count = 0
    for i in t :
        count = [i[count],i[count]+i[count+1],i[count]+i[count+1]+i[count+2]]
    return count
#print(cumulative_sum([[1,2,3]]))

def middle(t):
    """
    Takes a  new list that contains the first and last elements.
    >>> middle([3,4,5,6])
    [4, 5]
    >>> middle([11,12,13,14])
    [12, 13]
    >>> middle([21,22,23,24])
    [22, 23]
    >>> middle([31,32,33,34,35])
    [32, 33, 34]
    >>> middle([])
    []
    """
    if t == []:
        return []
    else:
        new_list = t
        new_list.pop(0)
        new_list.pop(-1)
        return new_list
# print(middle([1,2,3,4]))

def chop(t):
    """
    Takes a list, modifies it by removing the first 
    and last elements, and returns None.
    >>> chop([4,6,2,6,2,5,2])
    [6, 2, 6, 2, 5]
    >>> chop([8,3,4,2,5,2])
    [3, 4, 2, 5]
    >>> chop([6,3,4,2,6,7])
    [3, 4, 2, 6]
    >>> chop([8,3,4,2,4,2,5])
    [3, 4, 2, 4, 2]
    >>> chop([9,6,3,5,2,1,5])
    [6, 3, 5, 2, 1]
    """
    t.pop(0)
    t.pop(-1)
    return t
# print(chop([1,2,3,4]))

def is_sorted(t):
    """
    Takes a list as a parameter and returns True 
    if the list is sorted in ascending order and False otherwise.
    >>> is_sorted([4,5,6,7,8])
    True
    >>> is_sorted(['a','b','c','d'])
    True
    >>> is_sorted([0,1,2,3,2,3])
    False
    >>> is_sorted([1,2,3,4,5,6,7])
    True
    >>> is_sorted([2,5,3,5,6,7])
    False
    """
    if t == sorted(t):
        return True
    else:
        return False

# print(is_sorted([1,2,3]))
# print(is_sorted(['b','a']))

def front_x(l):
    """
    Returns a list with the strings in sorted order, 
    except group all the strings that begin with 'x' first. 
    >>> front_x(["xqwerer","baananads","apadlsk","xadffda","xasdxca"])
    ['xadffda', 'xasdxca', 'xqwerer', 'apadlsk', 'baananads']
    >>> front_x(["mix","xyz","apple","xanadu","aardvark"])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    >>> front_x(["vfldksda","axaaw","xlsde","zwrsdlkf","xzld"])
    ['xlsde', 'xzld', 'axaaw', 'vfldksda', 'zwrsdlkf']
    >>> front_x(["safd","zadw","xldosdf","xadas","xaaadsa"])
    ['xaaadsa', 'xadas', 'xldosdf', 'safd', 'zadw']
    >>> front_x(["wer","wsdg","adyhf","xldoas","basdsd"])
    ['xldoas', 'adyhf', 'basdsd', 'wer', 'wsdg']
    """
    a = [i for i in l if i[0] == 'x' or i[0] == 'X']
    b = [i for i in l if i[0] != 'x' and i[0] != 'X']
    a.sort()
    b.sort()
    for i in b:
        a.append(i)
    return a
# print(front_x(["mix","xyz","apple","xanadu","aardvark"]))

def even_only(l):
    """
    Return a new list with only even numbers
    >>> even_only([6,3,1,5,3,2,7,9,8])
    [6, 2, 8]
    >>> even_only([1,2,3,4,5,6,7,8,9])
    [2, 4, 6, 8]
    >>> even_only([3,6,8,3,1,4,6,3,5])
    [6, 8, 4, 6]
    >>> even_only([0,5,3,5,3,5,3,5,7])
    [0]
    >>> even_only([2,5,7,6,3,6,8,3,5])
    [2, 6, 6, 8]
    """
    new_list = []
    for i in l:
        if i%2 == 0:
            new_list.append(i)
    return new_list
# print(even_only([3,1,4,1,5,9,2,6,5]))

def love(text):
    """
    Change the second last word to “love”.
    >>> love("I hate you")
    'I love you'
    >>> love("I really like you")
    'I really love you'
    >>> love("I really appreciate it")
    'I really love it'
    >>> love("I really hate you")
    'I really love you'
    >>> love("I adore you")
    'I love you'
    """
    text = text.split()
    text[-2] = "love"
    text = ' '.join(text)
    return text
# print(love("I like python"))
# print(love("I really like Python"))

def is_anagram(a,b):
    """
    Takes two strings and returns True if they are anagrams.
    >>> is_anagram("Python","Physics")
    True
    >>> is_anagram("Homework","Housework")
    True
    >>> is_anagram("Map","Earth")
    True
    >>> is_anagram("Apple","Zebra")
    True
    >>> is_anagram("sea","beach")
    True
    """
    x = list(a)
    y = list(b)
    z = x.sort() == y.sort()
    return z
print(is_anagram('arrange','Rear Nag'))

def has_duplicates(l):
    """
    Takes a list and returns True if there is 
    any element that appears more than once.
    >>> has_duplicates([4,6,3,5,3,6,7])
    True
    >>> has_duplicates([2,5,7,4,9,0])
    False
    >>> has_duplicates([1,2,5,2,4,6])
    True
    >>> has_duplicates([8,9,7,6,5,4,3])
    False
    >>> has_duplicates([3,9,0,5,3,5,7])
    True
    """
    count = 0
    while count < len(l):
        if count == (len(l) - 1):
            return False
        elif l.count(l[count]) > 1:
            return True
        count += 1
# print(has_duplicates([1,2,3,4,5]))
# print(has_duplicates([1,2,3,4,5,2]))

def average(nums):
    """
    Returns the mean average of a list of numbers.
    >>> average([2,3,5,2,5,2,4,1])
    3.0
    >>> average([4,5,2,5,6,3,6,7,8,3])
    4.9
    >>> average([2,4,6,3,7,9,0,6,8])
    5.0
    >>> average([24,63,53,67,34])
    48.2
    >>> average([23,53,68,53,78,32,42])
    49.857142857142854
    """
    count = 0
    for i in nums:
        count += i
    return count/len(nums)
# print(average([1,1,5,5,10,8,7]))

def centered_average(nums):
    """
    Returns the average of the values that ignores the largest and smallest values in the list. 
    >>> centered_average([1,1,1,1,1,1,1,1,3,5,6,7])
    2.1
    >>> centered_average([3,3,3,3,3,3,5,2,5,1,1,1])
    2.7
    >>> centered_average([4,6,3,5,3,5,2,1,1,1,1,1,5,6,7])
    3.3076923076923075
    >>> centered_average([5,4,6,3,12,45,2,14,6])
    7.142857142857143
    >>> centered_average([8,5,2,4,6,8,2,2,9,1])
    4.625
    """
    nums.remove(max(nums))
    nums.remove(min(nums))
    return average(nums)
# print(centered_average([1,1,5,5,10,8,7]))

def reverse_pair(s):
    """
    Returns the reverse pair of the input sentence.
    >>> reverse_pair("Python love I")
    'I love Python'
    >>> reverse_pair("easy is Python")
    'Python is easy'
    >>> reverse_pair("meal important most the is Breakfast")
    'Breakfast is the most important meal'
    >>> reverse_pair("Ain't nobody hurt you like I hurt you.")
    "you. hurt I like you hurt nobody Ain't"
    >>> reverse_pair("I still waiting for you")
    'you for waiting still I'
    """
    s = s.split()
    s = " ".join(reversed(s))
    return s
# print(reverse_pair("May the fourth be with you"))

def match_ends(word):
    """
   Returns the count of the number of strings where the string length is 2 
   or more and the first and last chars of the string are the same.
   >>> match_ends(['python','banana','Tot'])
   1
   >>> match_ends(['toy','ababababa','says','sos'])
   3
   >>> match_ends(['roar','Roes','Sos'])
   2
   >>> match_ends(['water','Drink'])
   0
   >>> match_ends(['Rice','Race'])
   0
    """
    count = 0
    for i in word:
        if i.lower()[0]==i.lower()[len(i)-1]:
            count = count + 1
    return count
# print(match_ends(["Gingering","hello","wow"]))

def remove_adjacent(t):
    """
    Returns a list where all adjacent elements have been reduced to a single element.
    >>> remove_adjacent([4,6,3,5,5,4])
    [4, 6, 3, 5, 4]
    >>> remove_adjacent([8,6,6,5,5,3])
    [8, 6, 5, 3]
    >>> remove_adjacent([5,6,6,3,3,2,4])
    [5, 6, 3, 2, 4]
    >>> remove_adjacent([2,4,4,6,6,7,7,8,3])
    [2, 4, 6, 7, 8, 3]
    >>> remove_adjacent([4,4,5,5,6,6,7,7,8,8])
    [4, 5, 6, 7, 8]
    """
    list = []
    for i in t:
        if len(list) == 0 or i != list[-1]:
            list.append(i)
    return list
# print(remove_adjacent([1, 2, 2, 3]))

if __name__ == "__main__":
    import doctest
    doctest.testmod