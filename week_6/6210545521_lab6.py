

#No1
def ll_sum(t):
    """Rhe function that plus all list
    >>> t = [[1],[2,3],[4,5,6]]
    >>> ll_sum(t)
    21
    >>> t = [[2],[2],[3,6,5]]
    >>> ll_sum(t)
    18
    >>> t = [[3],[],[4,5]]
    >>> ll_sum(t)
    12
    >>> t = [[0],[0]]
    >>> ll_sum(t)
    0
    >>> t = [[-12],[-6,-3],[-4]]
    >>> ll_sum(t)
    -25
    """
    sum = 0
    for element in t:
        for x in element:
            plus = plus+x
    return sum

#No.2
def cumulative_sum(t):
    """The function that plus like squence
    >>> t = [0,1,2,3]
    >>> cumulative_sum(t)
    [0, 1, 3, 6]
    >>> t = [2,4,6,8]
    >>> cumulative_sum(t)
    [2, 6, 12,20]
    >>> t = [0,0]
    >>> cumulative_sum(t)
    [0, 0]
    >>> t = [-2,-5,6,-7,9]
    >>> cumulative_sum(t)
    [-2, -7, 1, -6, 3]
    >>> t = [200,-50,-50,-100]
    >>> cumulative_sum(t)
    [200, 150, 100, 0]
    """
    blank = []
    plus = 0
    for element in t:
        plus = element + plus
        c.append(plus)
    return blank
#No.3
def middle(t):
    """The function that show  list  between first and last
    >>> t = [1,2,3]
    >>> middle(t)
    [2]
    >>> t=[10,[5],10,[15,25]]
    >>> middle(t)
    [[5], 10]
    >>> t = [1,2,3,[4],[5],6,7]
    >>> middle(t)
    [2, 3, [4], [5] ,6]
    >>> t =[0,0,0,0,0,0]
    >>> middle(t)
    [0, 0, 0, 0]
    >>> t = [5]
    >>> middle(t)
    []
    """
    blank = []
    for element in t[1:-1]:
        x.append(element)
    return blank

#No.4
def chop (t):
     """Function that cut the first and last list
    >>> t = [1,2,3]
    >>> chop(t)
    [2]
    >>> t=[10,[5],10,[15,25]]
    >>> chop(t)
    [[5], 10]
    >>> t = [1,2,3,[4],[5],6,7]
    >>> chop(t)
    [2, 3, [4], [5] ,6]
    >>> t =[0,0,0,0,0,0]
    >>> chop(t)
    [0, 0, 0, 0]
    >>> t = [5]
    >>> chop(t)
    []
    """
     p =t [1:-1]
     return p
#No.5
def is_sorted(t):
    """The funtion that arrange the list
    >>> is_sorted([1,2,3])
    True
    >>> is_sorted([10,2,5,0,8])
    False
    >>> is_sorted(['a','c','e'])
    False
    >>> is_sorted(['a','b','c')
    True
    >>> is_sorted(['abc','bcd','cdf'])
    True
    """
    if t == sorted(t):
        return True
    else:
        return False
#No.6
def front_x(lists):
    """The function that show the character that we set at first
    >>> lists = ['auu','sabai','pund']
    >>> front_x(lists)
    ['pund', 'auu', 'sabai']
    >>> lists = ['aaaa','bbbb','cccc','pppp']
    >>> front_x(lists)
    ['pppp','aaaa', 'bbbb','cccc']
    >>> lists = ['pund','pooh','pen','pencil]
    >>> front_x(lists)
    ['pencil', 'pen', 'pooh','pund']
    >>> lists = ['hello','apple','banana']
    >>> front_x(lists)
    ['apple', 'banana', 'hello']
    >>> lists = ['lazy','I','am']
    >>> front_x(lists)
    ['I','am','lazy']
    """
    lists.sort()
    a = []
    b = []
    for element in lists:
        if element[0] == 'p':
            a.append(element)
        else:
            b.append(element)
    return a+b

#No.7
def even_only(t):
    """function that show only even number
    >>> even_only([2,4,6,8,10,12])
    [2,4,6,8,10,12]
    >>> even_only([1,2,3,5,7,9)
    [2]
    >>> even_only([0,1,3,11])
    [0]
    >>> even_only([1,4,2,6,7,9,0])
    [4,2,6,0]
    >>> even_only([1,3,5,7,9])
    []
    """
    pund = []
    for element in t:
        if element % 2 == 0:
            l.append(element)
        else:
            pass
    return pund
#No.8
def love(sen):
    """function that add verb 'love' to a sentence
    >>> love("I hate you so much")
    'I love you so much'
    >>> love("I am so in lazy ")
    'I am so in love'
    >>> love('she hate you')
    'she love you'
    >>> love('I hate this menu so much')
    'I love this menu so much'
    >>> love('They still hate it ')
    'They still love it'
    """
    x = sen.split(' ')
    x[-2] = 'love'
    return (' ' .join(x))
#No.9
def is_anagram(string1,string2):
    """function that check the list that characters are the same or not
    >>> is_anagram('pund', 'dpnu')
    True
    >>> is_anagram('panitan','panitannn')
    False
    >>> is_anagram('pund','unpdd')
    False
    >>> is_anagram('handsome','somehand')
    True
    >>> is_anagram('I','so sleepy')
    False
    """

    if sorted(string1) == sorted(string2):
        return True
    else:
        return False
#No.10
def has_duplicates(t):
    """takes a list and returns True if there is any element that
    appears more than once.
    >>> has_duplicate([0,1,2,3])
    False
    >>> has_duplicate([0,0,1,1,2,3,4])
    True
    >>> has_duplicate([01,2,3,4,4,5])
    True
    >>> has_duplicate([2,3,3,2,3,2])
    True
    >>> has_duplicate([0,0,0])
    True
    >>> has_duplicate([10,20,30,40])
    False
    """
    duplicate = []
    for element in t:
        if element not in duplicate:
            duplicate.append(element)
    if len(duplicate) < len(t):
        return True
    else:
        return False
#No.11
def average(t):
    """ function that returns the mean average of a list of numbers.
    >>> average([1,2,3,4,5])
    3.0
    >>> average([10,20,30,30,50])
    28.0
    >>> average([0,0,0,0])
    0.0
    >>> average([2,4,6,8,10])
    6.0
    >>> average([1,3,5,7,9])
    5.0
    >>> average([1,2,2,2,2,5,7,4])
    2.7
    """
    p = sum(t)/len(t)
    return p
def centered_average(t):
    """that returns a "centered" average of a list of numbers,
    which is the mean average of the values that ignores the largest and smallest values in the list.
    >>> centered_average([1,2,3,4,5])
    3.0
    >>> centered_average([10,20,30,30,50])
    28.0
    >>> centered_average([0,0,0,0])
    0.0
    >>> centered_average([2,4,6,8,10])
    6.0
    >>> centered_average([1,2,2,2,2,5,7,4])
    2.7
    """
    p = sum(t[1:-1])/(len(t[1:-1]))
    return p
#No.13
def reverse_pair(t):
    """function that returns the reverse pair of the input sentence.
    >>> reverse_pair("I so sleepy")
    'sleepy I so'
    >>> reverse_pair("I love you so much")
    'so love I you much'
    >>> reverse_pair('love you I')
    'I love you'
    >>> reverse_pair('what the duck')
    'the what duck'
    >>> reverse_pair('I just try to make this sentence long')
    'try to make I sentence long just this'
    """
    a = t.split(' ')
    b = a[::-1]
    return (' '.join(b))
#No.14
def match_ends(t):
    """that returns the count of the
    number of strings where the string length is 2 or more and the first and last
    chars of the string are the same.
    >>> match_ends(["ppundp",'auuua',"pooh"])
    2
    >>> match_ends(["hello",'this','apple'])
    0
    >>> match_ends(['thesamet])
    1
    >>> match_ends(['panitanp','plengkhamp','sirapops'])
    3
    >>> match_ends(['hungry','so','much'])
    0
    """
    count = 0
    for element in t:
        if len(element) >= 2 and (element[0] == element[-1]):
            count += 1
    return count
#No.15
def remove_adjacent(t):
    """function that returns a list
    where all adjacent elements have been reduced to a single element.
    >>> remove_adjacent([1,2,3,4,5,1])
    [1, 2, 3, 4, 5, 1]
    >>> remove_adjacent([2,2,2,2,2,])
    [2]
    >>> remove_adjacent([-1,-2,-3,-4])
    [-1, -2, -3, -4]
    >>> remove_adjacent([0,2,4,6,8])
    [0, 2, 4, 6, 8]
    >>> remove_adjacent([1,1,2,2,3,3,4,4,5,5])
    [1, 2, 3, 4 ,5 ]
    """
    element = 1
    while element < len(t):
        if t[element] == t[element-1]:
            t.pop(element)
            element -= 1
        element += 1
    return t