

#1
def ll_sum(t):
    """
    sum all the list.
    >>> t = [[1],[2,3],[4,5,6]]
    >>> ll_sum(t)
    21
    >>> t = [[-5],[],[1,8,2]]
    >>> ll_sum(t)
    6
    >>> t = [[-1,-3],[2],[1,3]]
    >>> ll_sum(t)
    2
    >>> t = [[0,0],[0],[0,0,0]]
    >>> ll_sum(t)
    0
    >>> t = [[-20,-3],[10,4],[-5]]
    >>> ll_sum(t)
    -14
    """
    x = 0
    for i in t:
        x += sum(i)
    return x

#2
def cumulative_sum(t):
    """
    cumulative sum in list.
    >>> t = [1,2,3,4]
    >>> cumulative_sum(t)
    [1, 3, 6, 10]
    >>> t = [0,0,0]
    >>> cumulative_sum(t)
    [0, 0, 0]
    >>> t = [-1,-2]
    >>> cumulative_sum(t)
    [-1, -3]
    >>> t = [2,6,4,-2,5]
    >>> cumulative_sum(t)
    [2, 8, 12, 10, 15]
    >>> t = [5,4,3,10,-15]
    >>> cumulative_sum(t)
    [5, 9, 12, 22, 7]
    """
    a = []
    sum = 0
    for ele in t:
        sum = ele + sum
        a.append(sum)
    return a

#3
def middle(t):
    """
    perform the middle list to new list.
    >>> t = [6,5,10,5,-5,6,1]
    >>> middle(t)
    [5, 10, 5, -5, 6]
    >>> t = [5,[10],[7,5],12]
    >>> middle(t)
    [[10], [7, 5]]
    >>> t = [1,5,6]
    >>> middle(t)
    [5]
    >>> t = [4.6]
    >>> middle(t)
    []
    >>> t = [1,4,2,6,2,1]
    >>> middle(t)
    [4, 2, 6, 2]
    """
    x = []
    for i in t[1:-1]:
        x.append(i)
    return x

#4
def chop (t):
     """
     cut the first and last item in list when call the function.
    >>> t = [2,5,12,5,23,4,3]
    >>> chop(t)
    [5, 12, 5, 23, 4]
    >>> t=[4,[5],[4,1],9]
    >>> chop(t)
    [[5], [4, 1]]
    >>> t = [1,5,4]
    >>> chop(t)
    [5]
    >>> t =[1.5]
    >>> chop(t)
    []
    >>> t = [4,1,8,4,6,5]
    >>> chop(t)
    [1, 8, 4, 6]
    """
     t = t[1:-1]
     return t

#5
def is_sorted(t):
    """
    if the list sorted,it will return True or if item in list aren't sorted or they are string,it will return False.
    >>> is_sorted([2,4,6])
    True
    >>> is_sorted(['o','g'])
    False
    >>> is_sorted(['a','b','c'])
    True
    >>> is_sorted([1,5,7])
    True
    >>> is_sorted(['abc','ghi','jkl'])
    True
    """
    if t == sorted(t):
        return True
    else:
        return False
#6
def front_x(lists):
    """
    if first character in first item is "x",they will be the first position and rearrange the list.
    >>> lists = ['ibe','ekca','xx','tjv,']
    >>> front_x(lists)
    ['xx', 'ekca', 'ibe', 'tjv,']
    >>> lists = ['pep','ass']
    >>> front_x(lists)
    ['ass', 'pep']
    >>> lists = ['xdom','xeqw','xop']
    >>> front_x(lists)
    ['xdom', 'xeqw', 'xop']
    >>> lists = ['loe','lol','asd','xe']
    >>> front_x(lists)
    ['xe', 'asd', 'loe', 'lol']
    >>> lists = ['das','mgr','kreqwe','mgfd']
    >>> front_x(lists)
    ['das', 'kreqwe', 'mgfd', 'mgr']
    """
    lists.sort()
    a = []
    b = []
    for i in lists:
        if i[0] == 'x':
            a.append(i)
        else:
            b.append(i)  
    return a+b

#7
def even_only(t):
    """
    return the even number in the list.
    >>> even_only([1,56,5,48,61])
    [56, 48]
    >>> even_only([5,8,4,1,52,4])
    [8, 4, 52, 4]
    >>> even_only([15,618,84,45])
    [618, 84]
    >>> even_only([3,5,7,11,9])
    []
    >>> even_only([0,5,1,79,52,8])
    [0, 52, 8]
    """
    l = []
    for ele in t:
        if ele % 2 == 0:
            l.append(ele)
        else:
            pass
    return l

#8
def love(text):
    """
    change the word "like" to "love".
    >>> love("I like you")
    'I love you'
    >>> love("I really like you")
    'I really love you'
    >>> love('I hate lobster')
    'I love lobster'
    >>> love('I do not like god')
    'I do not love god'
    >>> love('She would like to go up')
    'She would like to love up'
    """
    x = text.split(' ')
    x[-2] = 'love'
    return (' ' .join(x))

#9
def is_anagram(string1,string2):
    """
    check if the word are anagram.
    >>> is_anagram('losad', 'dasol')
    True
    >>> is_anagram('goup','opuog')
    False
    >>> is_anagram('bdad','ddsb')
    False
    >>> is_anagram('play hard','drah yasa')
    False
    >>> is_anagram('hate','etah')
    True
    """
    if sorted(string1) == sorted(string2):
        return True
    else:
        return False

#10
def has_duplicates(l):
    """
    check if the number in list are duplicated.
    >>> has_duplicates([5,2,3,4,5])
    True
    >>> has_duplicates([4,5,6,7,7])
    True
    >>> has_duplicates([5,6,7,3,4])
    False
    >>> has_duplicates([4,4,5,5,5])
    True
    >>> has_duplicates([0,0,0,0,0,0,0])
    True
    """
    du = []
    for i in l:
        if i not in du:
            du.append(i)
    if len(du) < len(l):
        return True
    else:
        return False

#11
def average(l):
    """
    find the average of number in the list.
    >>> average([5,15,48,51,2])
    24.2
    >>> average([5,15,51,1])
    18.0
    >>> average([1,5,154,51,2])
    42.6
    >>> average([8,15,15,63,21])
    24.4
    >>> average([0,0,0,0,0,0,0])
    0.0
    """
    x = sum(l)/len(l)
    return x

#12
def centered_average(l):
    """
    find the average of the centered number in list.
    >>> centered_average([5,15,48,51,2])
    38.0
    >>> centered_average([5,15,51,1])
    33.0
    >>> centered_average([1,5,154,51,2])
    70.0
    >>> centered_average([8,15,15,63,21])
    31.0
    >>> centered_average([0,0,0,0,0,0,0])
    0.0
    """
    x = sum(l[1:-1])/(len(l[1:-1]))
    return x

#13
def reverse_pair(s):
    """
    reverse the word.
    >>> reverse_pair("I really like you")
    'you like really I'
    >>> reverse_pair("He is liar")
    'liar is He'
    >>> reverse_pair('You trick me')
    'me trick You'
    >>> reverse_pair('I hate you')
    'you hate I'
    >>> reverse_pair('Go to die')
    'die to Go'
    """
    x = s.split(' ')
    w = x[::-1]
    return (' '.join(w))

#14
def match_ends(l):
    """
    check the word if first char and last char are the same,count for 1.
    >>> match_ends(["lol",'duck',"hih"])
    2
    >>> match_ends(["lul",'qeeq','lozxc'])
    2
    >>> match_ends(['fdksa','asdf','ewaty'])
    0
    >>> match_ends(['lxcoisl','vaat'])
    1
    >>> match_ends(['kxzcs','mom','o'])
    1
    """
    count = 0
    for i in l:
        if len(i) >= 2 and (i[0] == i[-1]):
            count += 1
    return count

#15
def remove_adjacent(l):
    """
    remove the duplicated number in the  list.
    >>> remove_adjacent([15,561,23,51,123])
    [15, 561, 23, 51, 123]
    >>> remove_adjacent([25,544,25,548,6])
    [25, 544, 25, 548, 6]
    >>> remove_adjacent([51,-6,-5,151])
    [51, -6, -5, 151]
    >>> remove_adjacent([0,0,0,0,0])
    [0]
    >>> remove_adjacent([2,2,254,84,15])
    [2, 254, 84, 15]
    """
    i = 1
    while i < len(l):
        if l[i] == l[i-1]:
            l.pop(i)
            i -= 1 
        i += 1
    return l


if __name__ == '__main__':
    import doctest
    doctest.testmod()
