

def ll_sum(l):
    """a function that takes a list of lists of integers and sums up the elements from all of the nested lists

    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> ll_sum(t)
    21
    >>> ll_sum([[1,2],[3,4],[5,6,7,8,9,10]])
    55
    >>> ll_sum([[9,2,5,8],[5,8,5,3,4,2,6],[6,8,5]])
    76
    >>> ll_sum([[3,5,7,4,8,8,5,4,7,4,1,2,5,5],[3,6,8,8,5,4,5,5],[9,8,5,45,7,5,1,2,3]])
    197
    >>> ll_sum([[5,4,7,8,1,2,5,5,2,3,58,58,2],[5],[8],[9,5,54,74,12,2]])
    329
    >>> ll_sum([[0]])
    0
    >>> ll_sum([[8,5,7,4,1,2],[5,9,25,41]])
    107
    """
    a = []
    for i in range(len(l)):
        for j in range(len(l[i])):
            a.append(l[i][j])
    return sum(a)
def cumulative_sum(l):
    """a function that takes a list of numbers and returns the cumulative sum; that is, a new list that show the step of the sum

    >>> t = [1, 2, 3]
    >>> cumulative_sum(t)
    [1, 3, 6]
    >>> cumulative_sum([1,2,3,4])
    [1, 3, 6, 10]
    >>> cumulative_sum([1,2,3,4,5])
    [1, 3, 6, 10, 15]
    >>> cumulative_sum([0,0,0,0,0])
    [0, 0, 0, 0, 0]
    >>> cumulative_sum([-5,-4,-3,-2,-1,0])
    [-5, -9, -12, -14, -15, -15]
    >>> cumulative_sum([-3,-2,-1,0,1,2,3])
    [-3, -5, -6, -6, -5, -3, 0]
    >>> cumulative_sum([6,2,1,0,5,4,5,9,7,1])
    [6, 8, 9, 9, 14, 18, 23, 32, 39, 40]
    """
    a = []
    b = 0
    for i in range(len(l)):
        b = b + l[i]
        a.append(b)
    return a
def middle(l):
    """ a function that takes a list and returns a new list that contains all but the first and last elements

    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    >>> middle([1,3,2,1,5])
    [3, 2, 1]
    >>> middle([1,2])
    []
    >>> middle(['yare','yare','daze'])
    ['yare']
    >>> middle([0,1,2,3,4,5,6,7,8,9,0])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> middle(['ora','ora','ora'])
    ['ora']
    >>> middle(['b',6,2,1,0,5,4,5,9,7,1])
    [6, 2, 1, 0, 5, 4, 5, 9, 7]
    >>> middle(['m','i','d','d','l','e'])
    ['i', 'd', 'd', 'l']
    """
    l.pop();l.pop(0)
    return l
def chop(l):
    """a function that takes a list, modifies it by removing the first and last elements, and returns None.

    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    >>> t = chop([1,2,3,4,5,6])
    >>> t
    >>> chop([1,2,3,4,5,6,7,8])
    >>> l = ['a','b','c','d']
    >>> chop(l)
    >>> l
    ['b', 'c']
    >>> chop(l)
    >>> l
    []
    >>> num = [1,2,3,4,5]
    >>> chop(num)
    >>> num
    [2, 3, 4]
    >>> chop(num)
    >>> num
    [3]
    >>> str = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
    >>> chop(str)
    >>> str
    ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    >>> chop(str)
    >>> str
    ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    >>> chop(str)
    >>> str
    ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    """
    l.pop()
    l.pop(0)
    return
def is_sorted(l):
    """a function that takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise

    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    >>> is_sorted([1,2,3,4])
    True
    >>> is_sorted(['a','b','c'])
    True
    >>> is_sorted(['a','A'])
    False
    >>> is_sorted([0])
    True
    >>> is_sorted([0,1,2,3,4,5,7,6])
    False
    >>> is_sorted([6,2,1,0,5,4,5,9,7,1])
    False
    >>> is_sorted(['A','B','a','b'])
    True
    """
    ln = l.copy();ln.sort()
    if ln == l:
        return True
    else:
        return False
def front_x(l):
    """a function that returns a list with the strings in sorted order, except group all the strings that begin with 'x' first.

    >>> l = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
    >>> front_x(l)
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    >>> front_x(['a','b','d','c','xz','xx','xy','xa','x'])
    ['x', 'xa', 'xx', 'xy', 'xz', 'a', 'b', 'c', 'd']
    >>> front_x(['e','a','f','c','b'])
    ['a', 'b', 'c', 'e', 'f']
    >>> front_x(['a','b','g','d''xxt','xar','x','erf'])
    ['x', 'xar', 'a', 'b', 'dxxt', 'erf', 'g']
    >>> front_x(['z','a','xa','we','abe'])
    ['xa', 'a', 'abe', 'we', 'z']
    >>> front_x(['fr','xa','wer','sad','not','notive'])
    ['xa', 'fr', 'not', 'notive', 'sad', 'wer']
    >>> front_x(['sunday','monday','tuseday','xmas'])
    ['xmas', 'monday', 'sunday', 'tuseday']
    """
    lf = []
    ls = []
    for i in range(len(l)):
        if l[i].find('x') == 0:
            lf.append(l[i])
        else:
            ls.append(l[i])
    lf.sort();
    ls.sort()
    return lf+ls
def even_only(list):
    """a function that will take a list of integers, and return a new list with only even numbers.

    >>> even_only([3,1,4,1,5,9,2,6,5])
    [4, 2, 6]
    >>> even_only([6,2,1,0,5,4,5,9,7,1])
    [6, 2, 0, 4]
    >>> even_only([5,5,7,7,1,2,5,1,2,3,4,5,9,5,5,8])
    [2, 2, 4, 8]
    >>> even_only([8,5,6,8,5,51,1,2,5,3,5,2,10,2,5,354,245,000,54564,34856])
    [8, 6, 8, 2, 2, 10, 2, 354, 0, 54564, 34856]
    >>> even_only([5,4,7,8,14,2,45,1,5614,861,651,56,426,165,165,1896,165,1965,165,156])
    [4, 8, 14, 2, 5614, 56, 426, 1896, 156]
    >>> even_only([489,7456,64,324,21,65477,8927756,434,234,485,362,3,5.2,3,948,165])
    [7456, 64, 324, 8927756, 434, 234, 362, 948]
    >>> even_only([1,3,5,7,9,11,13,17,19,23,29,31,37,41,43,47,53,59,61,71,79,83,89,97])
    []
    """
    lr = []
    for i in range(len(list)):
        if list[i] % 2 == 0:
            lr.append(list[i])
    return lr
def love(text):
    """a function that will change the second last word to “love”.

    >>> love("I like Python")
    'I love Python'
    >>> love("I really like Python")
    'I really love Python'
    >>> love("Do you know dawae")
    'Do you love dawae'
    >>> love("For this code i hate this")
    'For this code i love this'
    >>> love("This is sparta!")
    'This love sparta!'
    >>> love("Whom art thou?")
    'Whom love thou?'
    >>> love("I really like to play osu!")
    'I really like to love osu!'
    """
    l = text.split(" ")
    l[-2] = "love"
    l = " ".join(l)
    return l
def is_anagram(word_1,word_2):
    """a function that takes two strings and returns True if they are anagrams.

    >>> is_anagram('arrange', 'Rear Nag')
    True
    >>> is_anagram('Resting','Stinger')
    True
    >>> is_anagram('singer','renigs')
    True
    >>> is_anagram('renigs','resign')
    True
    >>> is_anagram('sering','signer')
    True
    >>> is_anagram('star platinum','The world')
    False
    >>> is_anagram('Magician Red','Hermit Purple')
    False
    """
    list_1 = []
    for i in range(len(word_1)):
        list_1.append(word_1[i].lower())
    for i in range(word_1.count(' ')):
        list_1.remove(' ')
    list_1.sort()
    list_2 = []
    for i in range(len(word_2)):
        list_2.append(word_2[i].lower())
    for i in range(word_2.count(' ')):
        list_2.remove(' ')
    list_2.sort()
    if list_1 == list_2:
        return True
    else:
        return False
def has_duplicates(list):
    """a function that takes a list and returns True if there is any element that appears more than once.

    >>> has_duplicates([1, 2, 3, 4, 5])
    False
    >>> has_duplicates([1, 2, 3, 4, 5, 2])
    True
    >>> has_duplicates([6,2,1,0,5,4,5,9,7,1])
    True
    >>> has_duplicates(['a','a'])
    True
    >>> has_duplicates(['b''c''a'])
    False
    >>> has_duplicates([6,5,8,4,7,8,4,2,1,3,5])
    True
    >>> has_duplicates([1,2,3,4,5,6,7,8,9,10])
    False
    """
    for i in range(len(list)):
        if list.count(list[i]) > 1:
            return True
    return False
def average(nums):
    """ a function that returns the mean average of a list of numbers.

    >>> average([1, 1, 5, 5, 10, 8, 7])
    5.285714285714286
    >>> average([5,1,5,2,6,48,5,56,456,894,9])
    135.1818181818182
    >>> average([5,456,4685,189,19,5156,1,324,654,534,65498])
    7047.363636363636
    >>> average([1,2,3,4,5,6,7,8,9,10])
    5.5
    >>> average([6,2,1,0,5,4,5,9,7,1])
    4.0
    >>> average([45,54,2,123,18,156,156,1623,12,123,45,1])
    196.5
    >>> average([5,4,12,31,321,564,61,654,6516])
    907.5555555555555
    """
    return sum(nums)/len(nums)
def centered_average(nums):
    """a function that returns a "centered" average of a list of numbers, which is the mean average of the values that ignores the largest and smallest values in the list.

    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([6,2,1,0,5,4,5,9,7,1])
    3.875
    >>> centered_average([45,56,15,489,465,123,132,743,432])
    248.85714285714286
    >>> centered_average([456,456,456,489,45,465,1,456])
    389.0
    >>> centered_average([4,561,56,4894,465,153,456,7432,7,4,65159])
    1558.6666666666667
    >>> centered_average([1,2,3,4,5,6,7,8,9,10])
    5.5
    >>> centered_average([-5,-4,-3,-2,-1,0])
    -2.5
    """
    nums.sort();nums.pop();nums.pop(0)
    return sum(nums)/len(nums)
def reverse_pair(text):
    """a function that returns the reverse pair of the input sentence.

    >>> reverse_pair("May the fourth be with you")
    'you with be fourth the May'
    >>> reverse_pair("You are already dead")
    'dead already are You'
    >>> reverse_pair("this is not a joke")
    'joke a not is this'
    >>> reverse_pair('Omae wa mou shinde iru')
    'iru shinde mou wa Omae'
    >>> reverse_pair('sincere true')
    'true sincere'
    >>> reverse_pair('link start')
    'start link'
    >>> reverse_pair('BanG Dream!')
    'Dream! BanG'
    >>> reverse_pair('Reach Out To The Truth')
    'Truth The To Out Reach'
    """
    list = text.split()
    list.reverse()
    list = ' '.join(list)
    return list
def match_ends(list):
    """a function that returns the count of the number of strings where the string length is 2 or more and the ﬁrst and last chars of the string are the same.

    >>> match_ends(["Gingering","hello","wow"])
    2
    >>> match_ends(['star platinum','the world','bub','ora'])
    1
    >>> match_ends(['nothing','close','suffer'])
    0
    >>> match_ends(['That','restart','control'])
    1
    >>> match_ends(['list','strings','nums'])
    1
    >>> match_ends(['crazy diamond','made in heaven'])
    0
    >>> match_ends(['file','edit','view','navigate','code','refactor','run','tools','vcs','window','help'])
    2
    """
    match = 0
    for i in range(len(list)):

        if list[i][0].lower() == list[i][-1].lower() and len(list[i]) >= 2:
            match += 1
    return match
def remove_adjacent(nums):
    """a function that returns a list where all adjacent elements have been reduced to a single element.

    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([1,2,2,3,2,2,1])
    [1, 2, 3, 2, 1]
    >>> remove_adjacent([1,1,2,2,3,3,2,2])
    [1, 2, 3, 2]
    >>> remove_adjacent([1,2,3,4,4,5,5,3,6,5,6,4,8,8,9,9])
    [1, 2, 3, 4, 5, 3, 6, 5, 6, 4, 8, 9]
    >>> remove_adjacent([9,8,5,5,5,3,3,3,5,6,4,8])
    [9, 8, 5, 3, 5, 6, 4, 8]
    >>> remove_adjacent([1,1,2,2,3,5,6,5,5,3])
    [1, 2, 3, 5, 6, 5, 3]
    >>> remove_adjacent([1,1,2,2,3,4,4,5,6,3,3,2,1,0])
    [1, 2, 3, 4, 5, 6, 3, 2, 1, 0]
    >>> remove_adjacent([9,9,8,8,7,7,6,5,4,3,2,1,5,2,2])
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 5, 2]
    """
    new = nums.copy()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            new.pop(i)
            new.insert(i, ' ')
    for i in range(new.count(' ')):
        new.remove(' ')
    return new