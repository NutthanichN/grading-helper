

#number 1
def ll_sum(t):
    """function that add up all the number in the lists and nested lists
    >>> ll_sum([[1,2],[3],[4,5,6]])
    21
    >>> ll_sum([[1,2,3,4,5]])
    15
    >>> ll_sum([[3,5,4,7,8]])
    27
    >>> ll_sum([[111,2],[4,3]])
    120
    >>> ll_sum([[2,3,4,5]])
    14
    """
    total = 0
    for i in t:
        total += sum(i)
    return total
    
    


#number 2
def cumulative_sum(t):
    """function that take the make a new list that add the sum from the next number and the previous number 
    >>> cumulative_sum([1,2,3])
    [1, 3, 6]
    >>> cumulative_sum([3,5,6])
    [3, 8, 14]
    >>> cumulative_sum([18,30,100])
    [18, 48, 148]
    >>> cumulative_sum([111,44,5])
    [111, 155, 160]
    >>> cumulative_sum([0,3,100])
    [0, 3, 103]
    """
    total=[]
    sum_total=0
    for i in t:
        sum_total +=i
        total.append(sum_total)
    return total


#number 3
def middle(t):
    """function that return a new list without the first and the last elements
    >>> middle([1,2,3,4])
    [2, 3]
    >>> middle([69,18,19,20,69])
    [18, 19, 20]
    >>> middle([18,69,69,69,18])
    [69, 69, 69]
    >>> middle([1,1,3,2001,0])
    [1, 3, 2001]
    >>> middle(["j","j","e","a","n","n"])
    ['j', 'e', 'a', 'n']


    """
    tnew = t[1:-1]
    return tnew


#number 4
def chop(t):
    """function that make a new list without the first and the last elements but return none 
    >>> t = ([1,2,3,4])
    >>> chop(t)
    >>> t
    [2, 3]
    >>> t = ([5,3,2,4,5])
    >>> chop(t)
    >>> t
    [3, 2, 4]
    >>> t = ([8,9,1,69,420,1])
    >>> chop(t)
    >>> t
    [9, 1, 69, 420]
    >>> t = ([555,444,333,222,111])
    >>> chop(t)
    >>> t
    [444, 333, 222]
    >>> t = ([69,111,420,2,3,5,69])
    >>> chop(t)
    >>> t
    [111, 420, 2, 3, 5]
    """
    t.pop(0)
    t.pop(-1)



#number 5
def is_sorted(t):
    """function that return True if the list is sorted or False if it's not
    >>> is_sorted([1, 2, 3])
    True
    >>> is_sorted([3, 4, 5])
    True
    >>> is_sorted(['b', 'a'])
    False
    >>> is_sorted(['j', 'e', 'a', 'n'])
    False
    >>> is_sorted([69, 69, 420, 360])
    False
    """
    newt = t[:]
    newt.sort()
    if newt == t:
        return True
    else:
        return False


#number 6
def front_x(t):
    """function that return a new sorted list that start with a group of string that begin with 'x' first
    >>> front_x(['mix','xyz','apple','xanadu','aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    >>> front_x(['xxx','abc','xax'])
    ['xax', 'xxx', 'abc']
    >>> front_x(['drax','axe','xeny'])
    ['xeny', 'axe', 'drax']
    >>> front_x(['jean', 'handsome', 'xay'])
    ['xay', 'handsome', 'jean']
    >>> front_x(['xxx','abc', 'xay','cde'])
    ['xay', 'xxx', 'abc', 'cde']
    """
    xlist = []
    for i in t:
        if i.startswith("x"):
            xlist.append(i)
            t.remove(i)
    xlist.sort()
    t.sort()
    newlist = xlist + t
    return newlist


#number 7 
def even_only(list):
    """function that return a new list of even numbers only
    >>> even_only([3,1,4,1,5,9,2,6,5])
    [4, 2, 6]
    >>> even_only([2,3,4,5,6,7,8])
    [2, 4, 6, 8]
    >>> even_only([1,3,5,7,8,9])
    [8]
    >>> even_only([69,420,360,18])
    [420, 360, 18]
    >>> even_only([6,2,1,5,4,5,5,8,1])
    [6, 2, 4, 8]
    """
    evenlist = []
    for i in list:
        if i%2 == 0:
            evenlist.append(i)
    return evenlist   


#number 8
def love(text):
    """function that replace the second last word with "love"
    >>> love('I like Python')
    'I love Python'
    >>> love('Everyone like Jean')
    'Everyone love Jean'
    >>> love('I really like you')
    'I really love you'
    >>> love('I really like PJeen')
    'I really love PJeen'
    >>> love('I hate physic')
    'I love physic'
    """
    splitt = text.split()
    word = splitt[-2]
    newt = text.replace(word,"love")
    return newt



#number 9
def is_anagram(x,y):
    """
    >>> is_anagram('arrange', 'Rear Nag')
    True
    >>> is_anagram('and','dan')
    True
    >>> is_anagram('thorn','rntho')
    True
    >>> is_anagram('jean','jeen')
    False
    >>> is_anagram('jeejee','jean')
    False
    >>> is_anagram('jean is cool','loconeajsi')
    True
    """
    newx = x.upper()
    newy = y.upper()
    newx2 = newx.split(" ")
    newy2 = newy.split(" ")
    newx3 = "".join(newx2)
    newy3 = "".join(newy2)
    newx4 = sorted(newx3)
    newy4 = sorted(newy3)
    if newx4 == newy4:
        return True
    else:
        return False


#number 10
def has_duplicates(t):
    """Function that return True if there is an element that have more than one or False if there is no duplicate
    >>> has_duplicate([1,2,3,4,5])
    False
    >>> has_duplicate([1,2,3,4,5,2,3,4])
    True
    >>> has_duplicate([69,69,69,69])
    True
    >>> has_duplicate([18,19,20])
    False
    >>> has_duplicate([1,3,2001,2001])
    True
    """
    dupe = set()
    for i in t:
        if i in dupe: return True
        dupe.add(i)
    return False


#number 11
def average(t):
    """
    >>> average([1,2,3,4,5])
    3.0
    >>> average([3,5,8,9,100])
    25.0
    >>> average([1,1,1,5,5,5,10,10])
    4.75
    >>> average([69,420,360])
    283.0
    >>> average([1,30,5,2,4,2,3,9,17])
    8.11111111111111

    """
    total = 0
    total = sum(t)
    total = total/len(t)
    return total


#number 12
def centered_average(t):
    """
    >>> centered_average([1,1,5,5,10,8,7])
    5.2
    >>> centered_average([10,5,7,3,4,2])
    4.75
    >>> centered_average([69,69,20,10,5,4,2,1,1])
    15.857142857142858
    >>> centered_average([1,1,1,1,1,10,10,10])
    4.0
    >>> centered_average([3,4,70,3,50,70])
    31.75
    """
    t.sort()
    newt = t[1:-1]
    total = 0
    total = sum(newt)
    total = total/len(newt)
    return total


#number 13
def reverse_pair(t):
    """
    >>> reverse_pair("May the fourth be with you")
    'you with be fourth the May'
    >>> reverse_pair("Jean is very handsome")
    'handsome very is Jean'
    >>> reverse_pair("Jean is name my")
    'my name is Jean'
    >>> reverse_pair("P Jeen very cute")
    'cute very Jeen P'
    >>> reverse_pair("homework much so is There")
    'There is so much homework'
    """
    newsentence = t.split()
    time = len(newsentence)
    reverse = []
    while time >= 1:
        reverse.append(newsentence[time-1])
        time = time-1
    reverse = " ".join(reverse)
    return reverse


#number 14
def match_ends(t):
    """
    >>> match_ends(["hello","wow","gingering"])
    2
    >>> match_ends(["jean","jeen","jeejeej"])
    1
    >>> match_ends(["thorn","sabai","eieie"])
    1
    >>> match_ends(["iii","jeenj","jeejeej"])
    3
    >>> match_ends(["physic","test","that"])
    2
    """
    num = 0
    for i in t:
        if len(i) >= 2:
            if i.startswith(i[0]) == i.endswith(i[0]):
                num += 1
    return num


#number 15
def remove_adjacent(t):
    """
    >>> remove_adjacent([1,2,2,3])
    [1, 2, 3]
    >>> remove_adjacent([1,2,3,3,4,4,5])
    [1, 2, 3, 4, 5]
    >>> remove_adjacent([1,1,1,1,1,1,1,2])
    [1, 2]
    >>> remove_adjacent([69,69,420,420,1,1,1,1])
    [69, 420, 1]
    >>> remove_adjacent([6,2,1,0,5,4,5,5,8,1])
    [6, 2, 1, 0, 5, 4, 5, 8, 1]
    """
    newt = []
    dupe = None
    for i in t:
        if i != dupe:
            newt.append(i)
        dupe = i
    return newt