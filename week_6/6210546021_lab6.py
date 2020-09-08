

def ll_sum(list):
    """
    This function will calculate the sum of
    the list in the list
    >>> ll_sum([[1,2,3],[2,3]])
    11
    >>> ll_sum([[-1,-2,-3],[1,2,3],[4,5,6]])
    15
    >>> ll_sum([[1],[3],[]])
    4
    >>> ll_sum([[11,12,13,34],[-25,-30]])
    15
    >>> ll_sum([[1,1,1,1,1],[2,2,2],[3,4,5]])
    23

    """
    sum = 0
    for ch in list:
        for i in ch:
            sum += i
    return sum
def cumulative_sum(list):
    """
    This function will calculate the next
    int in the list with th eprevious int
    >>> cumulative_sum([1,2,3])
    [1, 3, 6]
    >>> cumulative_sum([4,5,6,7])
    [4, 9, 15, 22]
    >>> cumulative_sum([-1,-2,-3,1,2,3])
    [-1, -3, -6, -5, -3, 0]
    >>> cumulative_sum([10,11])
    [10, 21]
    >>> cumulative_sum([1,2,3,4,5,6,7,8,9,0])
    [1, 3, 6, 10, 15, 21, 28, 36, 45, 45]
    """
    sum = 0
    new = []
    for ch in list:
        sum += ch
        new.append(sum)
    return new
def middle(list):
    """
    This function will cut the first object in the list
    and cut the last object in the list and return the list
    >>> middle([1,2,3,4,5,6])
    [2, 3, 4, 5]
    >>> middle(['ing','is','not','happy','cream'])
    ['is', 'not', 'happy']
    >>> middle([5,4,3,2,1,0])
    [4, 3, 2, 1]
    >>> middle([-1,-1,-2,-3])
    [-1, -2]
    >>> middle([0,0,0,0,0,0,0])
    [0, 0, 0, 0, 0]
    """
    list.remove(list[0])
    list.remove(list[-1])
    return list
def chop(list):
    """
    This function will cut the first object in the list
    and cut the last object in the list and return None
    >>> chop([1,2,3,4,5,6])

    >>> chop(['ing','is','not','happy','cream'])

    >>> chop([5,4,3,2,1,0])

    >>> chop([-1,-1,-2,-3])

    >>> chop([0,0,0,0,0,0,0])

    """
    list.remove(list[0])
    list.remove(list[-1])
    return None
def is_sorted(list):
    """
    This function will check object in the
    if it got repeat object it will return True and
    if it not the repeat object it will return False
    >>> is_sorted([1,2,2,2,3,4,5])
    True
    >>> is_sorted([1,2,3,6,4,5])
    False
    >>> is_sorted([1,5,5,7,8,9,10])
    True
    >>> is_sorted([0,1,2,3,5,5])
    True
    >>> is_sorted([3,3,34,55,56])
    True
    """
    new = []
    for ch in list:
        new.append(ch)
    new.sort()
    if new == list:
        return True
    else:
        return False
def front_x(list):
    """
    This function will order the object in the list
    by x is the first order
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    >>> front_x(['abc','bcd','xera'])
    ['xera', 'abc', 'bcd']
    >>> front_x(['dog','egg','xxx','fish'])
    ['xxx', 'dog', 'egg', 'fish']
    >>> front_x(['shine','orange','xir','like','god'])
    ['xir', 'god', 'like', 'orange', 'shine']
    >>> front_x(['wow','lol','xox','king'])
    ['xox', 'king', 'lol', 'wow']
    """
    new = []
    new1 = []
    for ch in list:
        if ch[0] == "x":
            new.append(ch)
            new.sort()
        else:
            pass
    for ch in list:
        if ch[0] != "x":
            new1.append(ch)
            new1.sort()
        else:
            pass
    return new+new1
def even_only(list):
    """
    This function will pick only even number
    and return the list
    >>> even_only([1,2,3,4,5,6])
    [2, 4, 6]
    >>> even_only([22,24,26,28])
    [22, 24, 26, 28]
    >>> even_only([10,12,11,14,1,3,5,7,9,17])
    [10, 12, 14]
    >>> even_only([11,2,4,6,8,1,3,5,7])
    [2, 4, 6, 8]
    >>> even_only([11,22,33,44,55])
    [22, 44]
    """
    new =[]
    for ch in list:
        if ch%2 == 0:
            new.append(ch)
        else:
            pass
    return new
def love(msg):
    """
     This function will change before
     the last words to the love
     >>> love("I like Python")
     'I love Python'
     >>> love("You are very such a bad woman")
     'You are very such a love woman'
     >>> love("Why you don't like me")
     "Why you don't love me"
     >>> love("Every one hate you")
     'Every one love you'
     >>> love("You always hit me")
     'You always love me'
    """
    a = msg.split(" ")
    a.remove(a[-2])
    a.insert(-1,"love")
    sentence = (" ".join(a))
    return sentence
def is_anagram(string1,string2):
    """
    This function will check the string1 and string2
    if they have the same string it will return True
    >>> is_anagram('arrange','RearNag')
    True
    >>> is_anagram('actually','Riwuwd')
    False
    >>> is_anagram('yellow','WOLLEY')
    True
    >>> is_anagram('apple','PPlea')
    True
    >>> is_anagram('tiger','sheleaveme')
    False
    """
    new = list(string1.lower())
    if " " in new:
        new.remove(" ")
    new2 = list(string2.lower())
    if " " in new2:
        new2.remove(" ")
    new.sort()
    new2.sort()
    if new2 == new:
        return True
    else:
        return False
def has_duplicates(list):
    """
    This function will check the list if it got the same
    object in the list it will return True if it not it will return False
    >>> has_duplicate([1,2,2,3,4,4])
    True
    >>> has_duplicate([1,2,3,4])
    False
    >>> has_duplicate([1,1,2,3,4,5,6])
    True
    >>> has_duplicate([0,12,1,3,4,4])
    True
    >>> has_duplicate([3,4,5,6,7,8,8,9])
    True
    """
    b = []
    list.sort()
    index = 0
    for max in list:
        b.append(max)
        if index >= 1:
            a = list[index]
            if b[index-1] == a:
                return True
            else:
                pass
        index += 1
    return False

def average(list):
    """
    This function will calculate the average of the list
    >>> average([1,1,1,1,1,1,1,1])
    1.0
    >>> average([1,2,3,4,5,6,7,8,9,10])
    5.5
    >>> average([3,4,5,6])
    4.5
    >>> average([2,3,4,5,6,70])
    15.0
    >>> average([55,45,35,15])
    37.5
    """
    sum = 0
    for n in list:
        sum += n
    av = sum/(len(list))
    return av
def centered_average(list):
    """
      This function will calculate the average of the list
      but it will cut the first and the last object in the list
      before caculation
      >>> centered_average([1,1,1,1,1,1,1,1])
      1.0
      >>> centered_average([1,2,3,4,5,6,7,8,9,10])
      5.5
      >>> centered_average([3,4,5,6])
      4.5
      >>> centered_average([2,3,4,5,6,70])
      4.5
      >>> centered_average([55,45,35,15])
      40.0
      """
    list.sort()
    list.remove(list[-1])
    list.remove(list[0])
    sum = 0
    for n in list:
        sum += n
    av = sum/len(list)
    return av
def reverse_pair(msg):
    """
    This function will reverse the whole sentence
    >>> reverse_pair("I love you")
    'you love I'
    >>> reverse_pair("be my friend")
    'friend my be'
    >>> reverse_pair("what the goal!")
    'goal! the what'
    >>> reverse_pair("see you later bye!")
    'bye! later you see'
    >>> reverse_pair("POSSIBLE AM I")
    'I AM POSSIBLE'
    """
    a = msg.split(" ")
    a.reverse()
    b = ((" ").join(a))
    return b
def match_ends(list):
    """
    This function will check the objects in the list
    if the first string in the object is same as the last
    string in the same object it will count how many objects got
    property like this
    >>> match_ends(['Gingering','hello','wow'])
    2
    >>> match_ends(['lol','king','hello'])
    1
    >>> match_ends(['love','you','so','sos'])
    1
    >>> match_ends(['bye','nooooob','iot'])
    0
    >>> match_ends(['pop','popullar'])
    1
    """
    count = 0
    for ch in list:
        if len(ch) > 2:
            if ch[0].lower() == ch[-1].lower():
                count += 1
    return count
def remove_adjacent(list):
    """
    This function will check the objects in the list
    if the object has a same charecter more than one it will delete
    one of them
    >>> remove_adjacent([1,2,2,3,4,5])
    [1, 2, 3, 4, 5]
    >>> remove_adjacent([2,3,4,5,6,7,8,9])
    [2, 3, 4, 5, 6, 7, 8, 9]
    >>> remove_adjacent([1,2,3,3,4,5])
    [1, 2, 3, 4, 5]
    >>> remove_adjacent([9,9,8,7,6])
    [9, 8, 7, 6]
    >>> remove_adjacent([3,4,5,6,7,7,8])
    [3, 4, 5, 6, 7, 8]

    """
    a = []
    b = " "
    for i in list:
        if str(i) != b[-1]:
            b+= str(i)
    for i in b[1:]:
        a.append(int(i))
    return a


