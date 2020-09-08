

####################<LEVEL1>###################
def ll_sum (t):
    """
    function ll_sum(t) takes a list of lists of integers and adds up the elements from all of the
    nested lists.

    >>> t=[[1,2],[1],[3,4,5]]
    >>> ll_sum(t)
    16
    >>> t=[[1],[2,3],[2,3]]
    >>> ll_sum(t)
    11
    >>> t=[[1,2],[4],[7,8]]
    >>> ll_sum(t)
    22
    >>> t=[[1,2],[4],[7,8]]
    >>> ll_sum(t)
    22
    >>> t=[[3.5,4,2],[2],[7,8]]
    >>> ll_sum(t)
    26.5
    >>> t=[[1],[4],[-1]]
    >>> ll_sum(t)
    4


    """

    total=0
    a=0
    for inside in t:
        inside_sum=sum(inside)
        total+=inside_sum
        a+=1
    return total
####################<LEVEL2>###################
def cumulative_sum(t):
    """
    function cumulative_sum takes a list of numbers and returns the cumulative sum; that is, a
    new list where the ith element is the sum of the first i + 1 elements from the original list.

    >>> t=[1,2,3]
    >>> cumulative_sum(t)
    [1, 3, 6]

    >>> t=[3,5,7]
    >>> cumulative_sum(t)
    [3, 8, 15]

    >>> t=[1,2,3,9,10,11]
    >>> cumulative_sum(t)
    [1, 3, 6, 15, 25, 36]

    >>> t=[1,2]
    >>> cumulative_sum(t)
    [1, 3]

    >>> t=[0,1,4]
    >>> cumulative_sum(t)
    [0, 1, 5]

    """
    cu_sum = 0
    cu_list = []
    for i in t:
        cu_sum += i
        cu_list.append(cu_sum)
    return cu_list
####################<LEVEL3>###################
def middle(t):
    """
    function middle that a list and returns a new list that contains all but the first and last
    elements.
    >>> t=[1,2,3,4]
    >>> middle(t)
    [2, 3]

    >>> t=[1,2,3,4,5,6]
    >>> middle(t)
    [2, 3, 4, 5]

    >>> t=[1,2]
    >>> middle(t)
    []

    >>> t=[1,2,3,4,5]
    >>> middle(t)
    [2, 3, 4]

    >>> t=[1,4,6,10,23]
    >>> middle(t)
    [4, 6, 10]

    """

    list_after_remove=[]
    t.remove(t[0])
    t.remove(t[-1])
    for i in t:
        list_after_remove.append(i)

    return list_after_remove



####################<LEVEL4>###################
def chop(t):
    """
    function chop takes a list, modifies it by removing the first and last elements, and returns
    None.
    >>> t=[1,2,3,4]
    >>> chop(t)
    >>> t
    [2, 3]

    >>> t=[1,2,3,4,5,6]
    >>> chop(t)
    >>> t
    [2, 3, 4, 5]

    >>> t=[1,2]
    >>> chop(t)
    >>> t
    []

    >>> t=[1,2,3,4,5,6,8,9]
    >>> chop(t)
    >>> t
    [2, 3, 4, 5, 6, 8]

    >>> t=[1,2,2,2,2,9]
    >>> chop(t)
    >>> t
    [2, 2, 2, 2]
    """
    t.remove(t[0])
    t.remove(t[len(t) - 1])
####################<LEVEL5>###################
def is_sorted(t):
    """
    function is_sorted takes a list as a parameter and returns True if the list is sorted in
    ascending order and False otherwise.

    >>> is_sorted([1,2,2])
    True
    >>> is_sorted(['b','a'])
    False
    >>> is_sorted(['a','b','c'])
    True
    >>> is_sorted([1,2,4,3])
    False
    >>> is_sorted([1,2,2.2,2.3])
    True

    """


    base = sorted(t)
    if t == base:
        return True
    else:
        return False
####################<LEVEL6>###################
def front_x(t):
    """
    function front_x returns a list with the strings in sorted order, except
    group all the strings that begin with 'x'.

    >>> t = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
    >>> front_x(t)
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']

    >>> t=['1','2','3','x']
    >>> front_x(t)
    ['x', '1', '2', '3']

    >>> t=['a','b','c','x']
    >>> front_x(t)
    ['x', 'a', 'b', 'c']

    >>> t=['a','b','xa','x','xabc']
    >>> front_x(t)
    ['x', 'xa', 'xabc', 'a', 'b']

    >>> t=['xb','xc','xa','xd']
    >>> front_x(t)
    ['xa', 'xb', 'xc', 'xd']

    """


    original_list_with_no_x = []
    original_list_with_x = []
    for a in t:
        if a[0] == 'x':
            original_list_with_x.append(a)
        if a[0] != 'x':
            original_list_with_no_x.append(a)
    return sorted(original_list_with_x)+sorted(original_list_with_no_x)
####################<LEVEL7>###################
def even_only(list):
    """
    function even_only(list) will take a list of integers, and return a new list with only even
    numbers.
    >>> even_only([3,1,4,1,5,9,2,6,5])
    [4, 2, 6]
    >>> even_only([2,4,6,8,10])
    [2, 4, 6, 8, 10]
    >>> even_only([1,3,5,7,9])
    []
    >>> even_only([-1,-2,-3,-4])
    [-2, -4]
    >>> even_only([20,21,22,23,24,25])
    [20, 22, 24]
    """
    even_only_list_for_new=[]
    for i in list:
        if i%2==0:
            even_only_list_for_new.append(i)
    return even_only_list_for_new
####################<LEVEL8>###################
def love(text):
    """
    a function love that will change the second last word to “love”.
    >>> love("I like Python")
    'I love Python'
    >>> love('I dont like Python')
    'I dont love Python'
    >>> love('I super very hate Python')
    'I super very love Python'
    >>> love('I askjdhjasdhkhd Python')
    'I love Python'
    >>> love('abcd efgh ijkl mnop qrst Python')
    'abcd efgh ijkl mnop love Python'



    """
    word_list = text.split()
    word_list[-2]='love'
    space=' '
    return space.join(word_list)
####################<LEVEL9>###################
def is_anagram(original, arrange):
    """
    function 'is_anagram' takes two strings and returns True if they are anagrams.
    >>> is_anagram('arrange', 'Rear Nag')
    True
    >>> is_anagram("SAruj", "Juras")
    True
    >>> is_anagram('jom', 'jim')
    False
    >>> is_anagram('pineapple', 'Applepine')
    True
    >>> is_anagram('Kasetsart', 'testraka')
    False
    """

    original_list = []
    for i in original.lower():
        original_list.append(i)
        if i == " ":
            original_list.remove(i)

    arrange_list = []
    for a in arrange.lower():
        arrange_list.append(a)
        if a == " ":
            arrange_list.remove(a)
    if sorted(original_list) == sorted(arrange_list):
        return True
    else:
        return False
####################<LEVEL10>###################
def has_duplicates(t):
    """
    function has_duplicates takes a list and returns True if there is any element that
    appears more than once.
    >>> has_duplicates([1,2,3,4])
    False

    >>> has_duplicates([1,1,1,1])
    True

    >>> has_duplicates([1,1,2,2,3,3])
    True

    >>> has_duplicates(['jom','jom','jom'])
    True

    >>> has_duplicates(['jom','saruj','Sattayanurak'])
    False
    """
    num_list=[]
    for i in t:
        num_list.append(i)
    num=num_list.count(i)
    if num>1:
        return True
    elif num<=1:
        return False
####################<LEVEL11>###################
def average(nums):
    """
    function average(nums) returns the mean average of a list of numbers.

    >>> average([1, 1, 5, 5, 10, 8, 7])
    5.285714285714286
    >>> average([1,2,3,4,5])
    3.0
    >>> average([0.2,0.1,0.3,0.2,0.2])
    0.2
    >>> average([10,20,30,40])
    25.0

    >>> average([1,1,1,1,1,1,1])
    1.0


    """
    sum=0
    for i in nums:
        sum+=i
    avg_of_lit=sum/len(nums)
    return avg_of_lit
####################<LEVEL12>###################
def centered_average(nums):
    """
    a function centered_average(nums) returns a  average of a list of numbers,
    that ignores the largest and smallest values in the list.

    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([2,3,4,5])
    3.5
    >>> centered_average([10,10,10])
    10.0
    >>> centered_average([1,1,2,3])
    1.5
    >>> centered_average([-1,-1,-2,-2,-2,-2,-3])
    -1.8
    """
    sum=0
    maximum =max(nums)
    minimum=min(nums)
    nums.remove(maximum)
    nums.remove(minimum)
    for i in nums:
        sum+=i
    avg=sum/len(nums)
    return avg
####################<LEVEL13>###################
def reverse_pair(word):
    """
    function reverse_pair returns the reverse pair of the input sentence.
    >>> reverse_pair("May the fourth be with you")
    'you with be fourth the May'
    >>> reverse_pair("Jom Saruj Sattayanurak")
    'Sattayanurak Saruj Jom'
    >>> reverse_pair("ske 17")
    '17 ske'
    >>> reverse_pair("I love Python")
    'Python love I'
    >>> reverse_pair("i r o n m a n")
    'n a m n o r i'
    """
    word_list=word.split()
    word_list.reverse()
    space=' '
    return space.join(word_list)
####################<LEVEL14>###################
def match_ends(list_of_word):
    """
    function match_ends returns the count of the number of strings where the string that first and last chars of the string are the same.
    >>> match_ends(['Gingering', 'hello','wow'])
    2
    >>> match_ends(['Gig', 'mix','Koo'])
    1
    >>> match_ends(['JoksJ', 'Jjsbdj','wsjadW'])
    3
    >>> match_ends(['j', 'h','joj'])
    1
    >>> match_ends(['j', 'o','m'])
    0


    """
    count=0
    for i in list_of_word:
        if len(i) >= 2:
            if i[0].lower()==i[-1].lower():
                count+=1
    return count
####################<LEVEL15>###################
def remove_adjacent(num_list):
    """
    function remove_adjacent returns a list where all adjacent elements have been reduced to a single element.
    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([1,2,2,3,3])
    [1, 2, 3]
    >>> remove_adjacent([1,2,2,2,3])
    [1, 2, 3]
    >>> remove_adjacent([22,44,44,33])
    [22, 44, 33]
    >>> remove_adjacent([1, 2, 2, 1])
    [1, 2, 1]



    """
    index = 1
    while index <= len(num_list) - 1:
        if num_list[index] == num_list[index - 1]:
            num_list.remove(num_list[index])
            index-=1
        else:
            index+=1
            pass
    return num_list
######################-----READ_ME-------###############################
# ***NOTE*** : On this code there are one problem that I can not fix.
#if num_list = [2,2,2,2] (all same number in one list)
#The programs will show error with error massage:index out of range.
####################<THE_END>###################
# if __name__ == '__main__':
#         import doctest
# doctest.testmod(verbose=True)

