

# No.1
def ll_sum(t):
    """
    >>> t = [1,2],[3],[4,5,6]
    >>> ll_sum(t)
    21
    >>> t = [3,1,2],[6,7,8]
    >>> ll_sum(t)
    27
    >>> t = [23,10],[15,2],[5,4],[1,8],[9]
    >>> ll_sum(t)
    77
    >>> t = [1,2,3,4],[6,5,4,3],[10,20]
    >>> ll_sum(t)
    58
    >>> t = [20,30],[10,40],[25,35]
    >>> ll_sum(t)
    160
    """
    return sum(sum(x) for x in t)

# No.2
def cumulative_sum(t):
    """
    >>> t = [1,2,3]
    >>> cumulative_sum(t)
    [1, 3, 6]
    >>> t = [4,5,6]
    >>> cumulative_sum(t)
    [4, 9, 15]
    >>> t = [7,8,9]
    >>> cumulative_sum(t)
    [7, 15, 24]
    >>> t = [1,5,6]
    >>> cumulative_sum(t)
    [1, 6, 12]
    >>> t = [10,12,14]
    >>> cumulative_sum(t)
    [10, 22, 36]
    """
    set = []
    zero = 0
    for i in t:
        zero += i
        set.append(zero)
    return set 

# No.3
def middle(t):
    """
    >>> t = [1,2,3,4]
    >>> middle(t)
    [2, 3]
    >>> t = [6,7,8,9]
    >>> middle(t)
    [7, 8]
    >>> t = [10,11,12,14]
    >>> middle(t)
    [11, 12]
    >>> t = [1,2,3,4,5,6,7,8,9]
    >>> middle(t)
    [2, 3, 4, 5, 6, 7, 8]
    >>> t = [11,12,13,14,15,16,17]
    >>> middle(t)
    [12, 13, 14, 15, 16]
    """
    t.pop(0)
    t.pop(-1)
    return t

# No.4
def chop(t):
    """
    >>> t = [1,2,3,4]
    >>> chop(t)
    >>> t
    [2, 3]
    >>> t = [2,3,4,5]
    >>> chop(t)
    >>> t
    [3, 4]
    >>> t = [6,7,8,9]
    >>> chop(t)
    >>> t
    [7, 8]
    >>> t = [1,7,9,10]
    >>> chop(t)
    >>> t 
    [7, 9]
    >>> t = [12,13,14,15]
    >>> chop(t)
    >>> t
    [13, 14]
    """
    t.pop(0)
    t.pop(-1)

# No.5
def is_sorted(t):
    """
    >>> is_sorted([1,2,2])
    True
    >>> is_sorted(['b','a'])
    False
    >>> is_sorted([1,2,3,4,5])
    True
    >>> is_sorted([3,4,7,6,1,8,9])
    False
    >>> is_sorted(['m','n','o','p'])
    True
    """
    set = []
    for i in t:
        set.append(i)
    
    set.sort()
    if t == set:
        return True
    else:
        return False

#No.6 
def front_x(t):
    """
    >>> t = ['mix','xyz','apple','xanadu','aardvark']
    >>> front_x(t)
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    >>> t = ['xray', 'foofoorock', 'xqc', 'saiparn', 'korn']
    >>> front_x(t)
    ['xqc', 'xray', 'foofoorock', 'korn', 'saiparn']
    >>> t = ['zombie', 'xenomorph', 'Ice', 'pund']
    >>> front_x(t)
    ['xenomorph', 'Ice', 'pund', 'zombie']
    >>> t = ['rat', 'queen', 'free', 'queue', 'xoxo']
    >>> front_x(t)
    ['xoxo', 'free', 'queen', 'queue', 'rat']
    >>> t = ['why', 'so', 'many', 'doctest', 'case', 'lmao', 'stupidaf', 'xexexe']
    >>> front_x(t)
    ['xexexe', 'case', 'doctest', 'lmao', 'many', 'so', 'stupidaf', 'why']
    """
    set = []
    set2 = []
    for i in t:
        if i[0] == 'x':
            set.append(i)
        else:
            set2.append(i)

    set.sort()
    set2.sort()
    return set+set2

# No.7
def even_only(list):
    """
    >>> even_only([3,1,4,1,5,9,2,6,5])
    [4, 2, 6]
    >>> even_only([1,4,3,5,7,8,9,5,3])
    [4, 8]
    >>> even_only([1,2,3,4,5,6,7,8,9])
    [2, 4, 6, 8]
    >>> even_only([10,11,12,13,14,15,16])
    [10, 12, 14, 16]
    >>> even_only([2,4,6,8,10,12])
    [2, 4, 6, 8, 10, 12]
    """
    set = []
    for i in list:
        if i % 2 == 0:
            set.append(i)
    return set

# No.8
def love(text):
    """
    >>> love("I like Python")
    I love Python
    >>> love("I really like Python")
    I really love Python
    >>> love("I like pussy")
    I love pussy
    >>> love("Foo dislike dick")
    Foo love dick
    >>> love("Saiparn dislike dick")
    Saiparn love dick
    """
    original_text = text.split(" ")
    original_text[-2] = "love"
    veryshinytext = " ".join(original_text)
    # print(veryshinytext) <-- old
    return veryshinytext

# No.9
def is_anagram(string1, string2):
    """
    >>> is_anagram('arrange', 'Rear Nag')
    True
    >>> is_anagram('holyshit', 'shoity')
    False
    >>> is_anagram('sword', 'drows')
    True
    >>> is_anagram('rock', 'cork')
    True
    >>> is_anagram('sidewalk', 'dewide')
    False
    """
    text1 = list(string1.upper())
    text2 = list(string2.upper())
    if " " in text2 :
        text2.remove(' ')
    text1.sort()
    text2.sort()
    if text1 == text2:
        return True
    else:
        return False
    
# No.10
def has_duplicates(t):
    """
    >>> has_duplicates([1,2,3,4,5])
    False
    >>> has_duplicates([1,2,3,4,5,2])
    True
    >>> has_duplicates([1,5,2,3,4,6,7,5,4,2])
    True
    >>> has_duplicates([2,3,4,5,4,8,7,8,1,2])
    True
    >>> has_duplicates([1,5,6,9,8,7,4,1,2,3])
    True
    """
    t.sort()
    set = []
    for i in t:
        if i not in set:
            set.append(i)
    if set == t:
        return False
    else:
        return True

# No.11
def average(nums):
    """
    >>> average([1,1,5,5,10,8,7])
    5.285714285714286
    >>> average([1,2,3,4,5,6,7,8])
    4.5
    >>> average([2,1,4,6,7,4,5])
    4.142857142857143
    >>> average([9,6,2,1,5,6,4])
    4.714285714285714
    >>> average([10,2,5,7,4,2,7])
    5.285714285714286
    """
    return sum(nums)/len(nums)

# No.12
def centered_average(nums):
    """
    >>> centered_average([1,1,5,5,10,8,7])
    5.2
    >>> centered_average([2,2,3,3,4,4,5,5])
    3.5
    >>> centered_average([1,1,1,2,2,2,3,3,3])
    2.0
    >>> centered_average([5,2,1,3,4,5,6])
    3.8
    >>> centered_average([2,3,4,5,1,6,7,8])
    4.5
    """
    nums.sort()
    nums.pop(0)
    nums.pop(-1)
    twopoint = sum(nums)/len(nums)
    return twopoint

# No.13
def reverse_pair(text):
    """
    >>> reverse_pair("May the fourth be with you")
    'you with be fourth the May'
    >>> reverse_pair("no things too long to reach")
    'reach to long too things no'
    >>> reverse_pair("Just do it make your dream come true")
    'true come dream your make it do Just'
    >>> reverse_pair("No one really know what's best for you")
    "you for best what's know really one No"
    >>> reverse_pair("no sacrifice too great")
    'great too sacrifice no'
    """
    a = []
    a = text.split()
    a.reverse()
    return ' '.join(a)

# No.14
def match_ends(char):
    """
    >>> match_ends(["Gingering", "hello", "wow"])
    2
    >>> match_ends(["Pirate", "Assassin", "discord"])
    1
    >>> match_ends(["rock", "paper", "scissors"])
    1
    >>> match_ends(["shoot", "exercise", "Medium"])
    2
    >>> match_ends(["loot", "use", "move"])
    0
    """
    count = 0
    for i in char:
        if i.upper()[0] == i.upper()[-1]:
            count += 1
    return count

# No.15
def remove_adjacent(t):
    """
    >>> remove_adjacent([1,2,2,3])
    [1, 2, 3]
    >>> remove_adjacent([2,2,3,3,4])
    [2, 3, 4]
    >>> remove_adjacent([3,4,4,5,6,7])
    [3, 4, 5, 6, 7]
    >>> remove_adjacent([7,7,7,8,8,9,9,9,10,10,11])
    [7, 8, 9, 10, 11]
    >>> remove_adjacent([2,2,3,4,5,5,6,7,8])
    [2, 3, 4, 5, 6, 7, 8]
    """
    set = []
    for i in t:
        if i not in set:
            set.append(i)
        else:
            pass
    return set