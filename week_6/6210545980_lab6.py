

def ll_sum(x):
    """
    >>> t = [[1,2],[3],[4,5,6]]
    >>> ll_sum(t)
    21
    >>> a = [[2],[4],[6]]
    >>> ll_sum(a)
    12
    >>> b = [[8,2],[6,4],[1,9],[5,5]]
    >>> ll_sum(b)
    40
    >>> c = [[1],[2],[3],[4]]
    >>> ll_sum(c)
    10
    >>> d = [[5,10,15,20],[1]]
    >>> ll_sum(d)
    51
    """
    sum = 0
    for i in x:
        for j in i:
            sum = sum + j
    return sum

def cumulative_sum(x):
    """
    >>> t = [1, 2, 3]
    >>> cumulative_sum(t)
    [1, 3, 6]
    >>> a = [2, 4, 6]
    >>> cumulative_sum(a)
    [2, 6, 12]
    >>> b = [6,8,10]
    >>> cumulative_sum(b)
    [6, 14, 24]
    >>> c = [1,1,1]
    >>> cumulative_sum(c)
    [1, 2, 3]
    >>> d = [7,8,9]
    >>> cumulative_sum(d)
    [7, 15, 24]
    """
    sum = 0
    new_list = []
    for i in x:
        sum = sum + i
        new_list.append(sum)
    return new_list

def middle(x):
    """
    >>> t = [1,2,3,4]
    >>> middle(t)
    [2, 3]
    >>> a = [25,4,3]
    >>> middle(a)
    [4]
    >>> b = [9,8,7,6,5,4]
    >>> middle(b)
    [8, 7, 6, 5]
    >>> c = [1,3,6,1]
    >>> middle(c)
    [3, 6]
    >>> d = [1,2,1]
    >>> middle(d)
    [2]
    """
    new_list = x.copy()
    del new_list[0]
    del new_list[-1]
    return new_list

def chop(x):
    """
    >>> t = [1,2,3,4]
    >>> chop(t)
    >>> t
    [2, 3]
    >>> a = [25,4,3]
    >>> chop(a)
    >>> a
    [4]
    >>> b = [9,8,7,6,5,4]
    >>> chop(b)
    >>> b
    [8, 7, 6, 5]
    >>> c = [1,3,6,1]
    >>> chop(c)
    >>> c
    [3, 6]
    >>> d = [1,2,1]
    >>> chop(d)
    >>> d
    [2]
    """
    del x[0]
    del x[-1]

def is_sorted(x:list):
    """
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted([2, 3, 7])
    True
    >>> is_sorted([8, 7, 9, 2])
    False
    >>> is_sorted([7, 14, 2, 4])
    False
    >>> is_sorted([1, 1, 1, 2])
    True
    """
    return x == sorted(x)

def front_x(x):
    """
    >>> i = ['mix','xyz','apple','xanadu','aardvark']
    >>> front_x(i)
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    >>> a = ['youtube','facebook','xintax']
    >>> front_x(a)
    ['xintax', 'facebook', 'youtube']
    >>> b = ['sirapop','pittayut','xzy']
    >>> front_x(b)
    ['xzy', 'pittayut', 'sirapop']
    >>> c = ['pymsen','xxiee']
    >>> front_x(c)
    ['xxiee', 'pymsen']
    >>> d = ['xyz','xab','korn']
    >>> front_x(d)
    ['xab', 'xyz', 'korn']
    """
    x.sort()
    x_list = []
    normal_list = []
    for i in x:
        if i.startswith("x") == True:
            x_list.append(i)
        else :
            normal_list.append(i)
    return x_list + normal_list

def even_only(x:list):
    """
    >>> even_only([3,1,4,1,5,9,2,6,5])
    [4, 2, 6]
    >>> even_only([1,2,3,4,5,6,7])
    [2, 4, 6]
    >>> even_only([15,2,14,7,9,45,23,4])
    [2, 14, 4]
    >>> even_only([9,8,11,2,4,5,6,8])
    [8, 2, 4, 6, 8]
    >>> even_only([])
    []
    """
    new_list = []
    for i in x:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

def love(text:str):
    """
    >>> love('I like Python')
    'I love Python'
    >>> love('I very hate Python')
    'I very love Python'
    >>> love('Because I hate you.')
    'Because I love you.'
    >>> love('Why you hate me.')
    'Why you love me.'
    >>> love('Please leave me.')
    'Please love me.'
    """
    a = text.split(" ")
    a[-2] = "love"
    return " ".join(a)

def is_anagram(x:str,y:str):
    """
    >>> is_anagram("arrange", "Rear Nag")
    True
    >>> is_anagram("Paruj", "jupar")
    True
    >>> is_anagram("Korn", "ok Nr")
    True
    >>> is_anagram("Sabai","Jean")
    False
    >>> is_anagram("Love","Hate")
    False
    """
    x = x.lower()
    y = y.lower()
    x = x.replace(' ','')
    y = y.replace(' ','')
    return sorted(x) == sorted(y)

def has_duplicates(x:list):
    """
    >>> has_duplicates([1, 2, 3, 4, 5])
    False
    >>> has_duplicates([1, 1, 1, 1])
    True
    >>> has_duplicates([99, 98, 97, 99])
    True
    >>> has_duplicates([2, 4, 6, 8, 10])
    False
    >>> has_duplicates([1101, 1101])
    True
    """
    for i in x:
        if i in x[x.index(i)+1:]:
            return True
        else:
            return False

def average(nums:list):
    """
    >>> average([1, 1, 5, 5, 10, 8, 7])
    5.285714285714286
    >>> average([5, 5, 5, 5, 5])
    5.0
    >>> average([9, 8, 7, 6, 5, 4])
    6.5
    >>> average([2, 4, 6, 8])
    5.0
    >>> average([0])
    0.0
    """
    sum = 0
    for i in nums:
        sum += i
    return sum / len(nums) 

def centered_average(nums:list):
    """
    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([1, 5, 5, 5, 5, 5, 7])
    5.0
    >>> centered_average([9, 9, 8, 7, 6, 5, 4, 4])
    6.5
    >>> centered_average([0, 2, 4, 6, 8, 10])
    5.0
    >>> centered_average([7, 0, 2])
    2.0
    """
    sum = 0
    nums = sorted(nums)
    del nums[0]
    del nums[-1]
    for i in nums:
        sum += i
    return sum / len(nums)

def reverse_pair(text:str):
    """
    >>> reverse_pair("May the fourth be with you")
    'you with be fourth the May'
    >>> reverse_pair("I love you with all my heart")
    'heart my all with you love I'
    >>> reverse_pair("Best teacher's Paruj")
    "Paruj teacher's Best"
    >>> reverse_pair("You and I")
    'I and You'
    >>> reverse_pair("Black and White")
    'White and Black'
    """
    new_list_text = []
    list_text = text.split(" ")
    for i in list_text:
        new_list_text.insert(0,i)
    return " ".join(new_list_text)

def match_ends(text:list):
    """
    >>> match_ends(["Gingering", "hello", "wow"])
    2
    >>> match_ends(["Ant", "Cat", "Bird"])
    0
    >>> match_ends(["Bad", "Dad", "LOL", "Dude"])
    2
    >>> match_ends(["Luck", "Greg", "POP", "Luck"])
    2
    >>> match_ends(["nun", "Dungeon"])
    1
    """
    counter = 0
    for i in text:
        if i[0].lower() == i[-1].lower() and len(i) >= 2:
            counter += 1
    return counter

def remove_adjacent(num:list):
    """
    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([4,7,6,6,4])
    [4, 7, 6]
    >>> remove_adjacent([1, 2, 3, 4, 5, 6])
    [1, 2, 3, 4, 5, 6]
    >>> remove_adjacent([1, 1, 0, 1])
    [1, 0]
    >>> remove_adjacent([3,5,9,2,1,5,1])
    [3, 5, 9, 2, 1]
    """
    new_num = []
    for i in num:
        if i not in new_num:
            new_num.append(i)
    return new_num
