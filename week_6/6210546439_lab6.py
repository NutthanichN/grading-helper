

def ll_sum(t):
    """
    >>> t = [[5],[1,4],[8,2,7]]
    >>> ll_sum(t)
    27
    >>> t = [[],[1],[8,4,7]]
    >>> ll_sum(t)
    20
    >>> t = [[-2,-3],[6,7],[0]]
    >>> ll_sum(t)
    8
    >>> t = [[0,0],[0],[0,0,0]]
    >>> ll_sum(t)
    0
    >>> t = [[-8,-2],[-17,-2],[10]]
    >>> ll_sum(t)
    -19
    """
    sum = 0
    for ele in t:
        for i in ele:
            sum = sum+i
    return sum

def cumulative_sum(t):
    """
    >>> t = [1,2,3]
    >>> cumula,,tive_sum(t)
    [1, 3, 6]
    >>> t = [-1,-2,-3]
    >>> cumulative_sum(t)
    [-1, -3, -6]
    >>> t = [0,0,0,0,0]
    >>> cumulative_sum(t)
    [0, 0, 0, 0, 0]
    >>> t = [1,-2,3,-4]
    >>> cumulative_sum(t)
    [1, -1, 2, -2]
    >>> t = [5,6,7,8,9,-10]
    >>> cumulative_sum(t)
    [5, 11, 18, 26, 35, 25]
    """
    l = []
    sum = 0
    for ele in t:
        sum = ele+sum
        l.append(sum)
    return l

def middle(t):
    """
    >>> t = [1,2,3,4,5,6,7]
    >>> middle(t)
    [2, 3, 4, 5, 6]
    >>> t=[1,[1,2],[7,9],5]
    >>> middle(t)
    [[1, 2], [7, 9]]
    >>> t = [1,2,3]
    >>> middle(t)
    [3]
    >>> t =[2]
    >>> middle(t)
    []
    >>> t=[5,7,8,4,9,8,7,1515]
    >>> middle(t)
    [7, 8, 4, 9, 8, 7]
    """
    l = []
    for i in t[1:-1]:
        l.append(i)
    return l

def chop (t):
     """
    >>> t = [2,8,7,6,1]
    >>> chop(t)
    [8, 7, 6]
    >>> t=[878,[7,6],[3,4],515]
    >>> chop(t)
    [[7, 6], [3, 4]]
    >>> t = [111,112,113]
    >>> chop(t)
    [112]
    >>> t =[8]
    >>> chop(t)
    []
    >>> t=[5,5,5,5,5,6,6,6,6,6]
    >>> chop(t)
    [5, 5, 5, 5, 6, 6, 6, 6]
    """
     t = t [1:-1]
     return t

def is_sorted(t):
    """
    >>> t = [1,2,3]
    >>> is_sorted(t)
    True
    >>> t=['b','a']
    >>> is_sorted(t)
    False
    >>> t = ['a','b','c']
    >>> is_sorted(t)
    True
    >>> t=['bighit','jyp','sm']
    >>> is_sorted(t)
    True
    """
    if t == sorted(t):
        return True
    else:
        return False

def front_x(lists):
    """
    >>> lists = ['hoseok','yoonki','xiumin']
    >>> front_x(lists)
    ['xiumin', 'hoseok', 'yoonki']
    >>> lists = ['timtim','pream']
    >>> front_x(lists)
    ['pream', 'timtim']
    >>> lists = ['pim','ploy','pare']
    >>> front_x(lists)
    ['pare', 'pim', 'ploy']
    >>> lists  = ['nin','tar','tea','jaa']
    >>> front_x(lists)
    ['jaa', 'nin', 'tar', 'tea']
    >>> lists = ['the','sim','ple','things']
    >>> front_x(lists)
    ['ple', 'sim', 'the', 'things']
    """
    lists.sort()
    x = []
    y = []
    for i in lists :
        if i[0] == 'x':
            x.append(i)
        else:
            y.append(i)
    return x+y


def even_only(t):
    """
    >>> even_only([5,2,4,5,9,7,8])
    [2, 4, 8]
    >>> even_only([2,4,6,8,10])
    [2, 4, 6, 8, 10]
    >>> even_only([0,2,3,5,7])
    [0, 2]
    >>> even_only([1,3,5,7,9])
    []
    >>> even_only([77,78,79,80,0])
    [78, 80, 0]
    """
    l = []
    for ele in t :
        if ele %2 == 0:
            l.append(ele)
        else:
            pass
    return l

def love(text):
    """
    >>> love("I like bts")
    'I love bts'
    >>> love("I want to leave you")
    'I want to love you'
    >>> love('timtim do not like pream')
    'timtim do not love pream'
    >>> love('pim hate compro')
    'pim love compro'
    >>> love('we purple you')
    'we love you'
    """
    t = text.split(' ')
    t[-2] = 'love'
    return (' ' .join(t))

def is_anagram(string1,string2):
    """
    >>> is_anagram('sarocha', 'sittipon')
    False
    >>> is_anagram('love','hate')
    True
    >>> is_anagram('namjoon','seokjinnie')
    False
    >>> is_anagram('idol','save me')
    False
    >>> is_anagram('pimpimpurom','pompompurin')
    True
    """

    if sorted(string1) ==  sorted(string2):
        return True
    else :
        return False

def has_duplicates(l):
    """
    >>> has_duplicate([1,2,3])
    False
    >>> has_duplicate([1,1,2,2,3,3])
    True
    >>> has_duplicate([5,1,5,2,5,3])
    True
    >>> has_duplicate([8,88,888])
    False
    >>> has_duplicate([7,7,7])
    True
    """
    dul = []
    for i in l:
        if i not in dul:
            dul.append(i)
    if len(dul) < len(l) :
        return True
    else:
        return False

def average(l):
    """
    >>> average([5,7,8,4,5])
    5.8
    >>> average([1,2,1,2,3,1,2,1,2,1])
    1.6
    >>> average([5,-5)
    0.0
    >>> average([7,7,7,7,7,1])
    6.0
    >>> average([0,0,0])
    0.0
    """
    x= sum(l)/len(l)
    return x

def centered_average(l):
    """
    >>> centered_average([1,2,3,4,5,6])
    3.5
    >>> centered_average([5,4,3,2,5])
    3.0
    >>> centered_average([1,1,1,1,1,1])
    1.0
    >>> centered_average([5.5,4.1,7.5,7.66])
    5.8
    >>> centered_average([0,0,0])
    0.0
    """
    x = sum(l[1:-1])/(len(l[1:-1]))
    return x

def reverse_pair(s):
    """
    >>> reverse_pair("with you I feel rich")
    'rich feel I you with'
    >>> reverse_pair("I need your love before I fall")
    'fall I before love your need I'
    >>> reverse_pair('you can call me idol')
    'idol me call can you'
    >>> reverse_pair('I am so sick of this fake love')
    'love fake this of sick so am I'
    >>> reverse_pair('you are my light')
    'light my are you'
    """
    x = s.split(' ')
    z = x[::-1]
    return (' '.join(z))

def match_ends(l):
    """
    >>> match_ends(['lol','lul','lam'])
    2
    >>> match_ends(['poop','puuo'])
    1
    >>> match_ends(['look','like','love'])
    0
    """
    count =0
    for i in l :
        if len(i) >= 2 and (i[0] == i[-1]):
            count +=1
    return count

def remove_adjacent(l):
    """
    >>> remove_adjacent([1,2,3,4,4,5])
    [1, 2, 3, 4, 5]
    >>> remove_adjacent([2,3,4,5])
    [2, 3, 4, 5]
    >>> remove_adjacent([-1,-1,-2,-2,-3,-3])
    [-1, -2, -3]
    >>> remove_adjacent([0,0,0])
    [0]
    """
    x =1
    while x < len(l):
        if l[x] == l[x-1]:
            l.pop(x)
            x -= 1
        x += 1
    return l
