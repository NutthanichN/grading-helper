

# 1
def ll_sum(t):
    """
    This function will sum all number in list t.
    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> ll_sum(t)
    21
    >>> t = [[5], [7], [6, 6, 6]]
    >>> ll_sum(t)
    30
    >>> t = [[8,9,10],[6]]
    >>> ll_sum(t)
    33
    >>> t = [[5,6],[2],[4],[3]]
    >>> ll_sum(t)
    20
    >>> t = [[1,6],[2],[8],[6],[5,6,7]]
    >>> ll_sum(t)
    41
    """
    result = 0
    for num in t:
        result += sum(num)
    return result

# 2
def cumulative_sum(t):
    """
    This function will cumulative sum number in list t.
    >>> t = [1, 2, 3]
    >>> cumulative_sum([1, 2, 3])
    [1, 3, 6]
    """
    cumsum = []
    total = 0
    for vv in t:
        total += vv
        cumsum.append(total)
    return cumsum

# 3 
def middle(t):
    """
    This function will show the slicing the first and last elements in list t.
    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    >>> t = [8, 5, 7, 4, 6]
    >>> middle(t)
    [5, 7, 4]
    >>> t = [14, 23, 17, 66]
    >>> middle(t)
    [23, 17]
    >>> t = [8, 5, 7, 4, 6, 5, 9 ,25]
    >>> middle(t)
    [5, 7, 4, 6, 5, 9]
    >>> t = [7, 8, 9, 12, 16, 4]
    >>> middle(t)
    [8, 9, 12, 16]
    """ 
    a = t[1:-1]
    return a

# 4
def chop(t):
    """
    This function will remove first and last elements in list t.
    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    >>> t = [8, 5, 7, 4, 6]
    >>> chop(t)
    >>> t
    [5, 7, 4]
    >>> t = [14, 23, 17, 66]
    >>> chop(t)
    >>> t
    [23, 17]
    >>> t = [8, 5, 7, 4, 6, 5, 9 ,25]
    >>> chop(t)
    >>> t
    [5, 7, 4, 6, 5, 9]
    >>> t = [7, 8, 9, 12, 16, 4]
    >>> chop(t)
    >>> t
    [8, 9, 12, 16]
    """
    t.pop(0)
    t.pop(-1)

# 5
def is_sorted(t):
    """
    This function will check list t if it's sorted will return true else will return false.
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    >>> is_sorted([3, 2, 2])
    False
    >>> is_sorted(['a', 'b'])
    True
    >>> is_sorted(['x', 'y'])
    True
    >>> is_sorted(['y', 'x'])
    False
    """
    a = sorted(t)
    if a == t:
        return True
    else:
        return False

# 6
def front_x(l):
    """
    This function will returns a list with the strings in sorted order, except
    group all the strings that begin with 'x' first.
    >>> l = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """
    check_x = []
    for num in l:
        if num.startswith("x"):
            check_x.append(num)
            l.remove(num)
    check_x.sort()
    l.sort()
    sortxlist = check_x + l
    return sortxlist

# 7
def even_only(tt):
    """
    This fucntion will return only even numbers.
    >>> even_only([3,1,4,1,5,9,2,6,5])
    [4, 2, 6]
    >>> even_only([1,2,1,2,1,2,1,2])
    [2, 2, 2, 2]
    >>> even_only([5,4,6,1,5,6,4])
    [4, 6, 6, 4]
    >>> even_only([1,2,3,1,3,4])
    [2, 4]
    >>> even_only([8,7,8,4,2,1])
    [8, 8, 4, 2]
    """
    a =[]
    for num in tt:
        if num %2==0:
            a.append(num) 
    return a  

# 8
def love(text):
    """
    This fucntion will change the second last word to "love".
    >>> love("I like Python")
    'I love Python'
    >>> love("I really like Python")
    'I really love Python'
    >>> love("I hate gap")
    'I love gap'
    >>> love("I like yunglean")
    'I love yunglean'
    >>> love("I hate jjt")
    'I love jjt'
    """
    check = text.split()
    change = check[-2]
    to_love = text.replace(change,"love")
    return to_love
# 9
def is_anagram(j,k):
    """
    This function will check the anagram if in these 2 list are anagram will return True else will return False.
    >>> is_anagram('arrange', 'Rear Nag')
    True
    >>> is_anagram('arrange', 'Rear Nao')
    False
    >>> is_anagram('cEEB', 'c e B e')
    True
    >>> is_anagram('dawgbran', 'dogbrain')
    False
    >>> is_anagram('dog', 'G O D')
    True
    """
    checkj = j.lower()
    checkk = k.lower()
    removespace_j = checkj.split(" ")
    removespace_k = checkk.split(" ")
    joinj = "".join(removespace_j)
    joink = "".join(removespace_k)
    sortj = sorted(joinj)
    sortk = sorted(joink)
    if sortj == sortk:
        return True
    else:
        return False

#10
def has_duplicates(aaa):
    """
    This function will check duplicate numbers in list if it's has duplicate number will return True else will return False.
    >>> has_duplicates([1, 2, 3, 4, 5])
    False
    >>> has_duplicates([1, 2, 3, 4, 5, 2])
    True
    >>> has_duplicates([5,4,2,2,6,4,8,7])
    True
    >>> has_duplicates([7,8,9,7,5,6,4])
    True
    >>> has_duplicates([7,8,4,3,5,6,1,10])
    False
    """
    check = {}
    for num in aaa:
        if num in check:
            return True
        check[num] = num
    else: return False

#11
def average(nums):
    """
    This function will sum all number in list and compute average.
    >>> average([1, 1, 5, 5, 10, 8, 7])
    5.285714285714286
    >>> average([7,8,9,4,2])
    6.0
    >>> average([4,5,6,7])
    5.5
    >>> average([8,6,7,5,7,8,9,4])
    6.75
    >>> average([2,4,7,8,3,4,56,87])
    21.375
    """
    result = 0
    result = sum(nums)/len(nums)
    return result

#12
def centered_average(nums):
    """
    This function will remove highest and lowest number then sum all the numbers that left and compute average.
    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([7,8,9,4,2])
    6.333333333333333
    >>> centered_average([8,6,7,5,7,8,9,4])
    6.833333333333333
    >>> centered_average([2,4,7,8,3,4,56,87])
    13.666666666666666
    >>> centered_average([4,5,6,7])
    5.5
    """
    result = 0
    numsort = sorted(nums)
    numsort.pop(0)
    numsort.pop(-1)
    result = sum(numsort)/len(numsort)
    return result

#13 
def reverse_pair(j):
    """
    This function will reverse strings in list.
    >>> reverse_pair("May the fourth be with you")
    'you with be fourth the May'
    >>> reverse_pair("Steal your girlfriend")
    'girlfriend your Steal'
    >>> reverse_pair("Slow da gee")
    'gee da Slow'
    >>> reverse_pair("Plz no fu fu")
    'fu fu no Plz'
    >>> reverse_pair("trap like a trapstar")
    'trapstar a like trap'
    """
    newl = []
    reverselist = j.split()
    reverselist.reverse()
    newl = " ".join(reverselist)
    return newl

#14
def match_ends(k):
    """
    This fucntion will count strings when the first and last chars of the string are the same.
    >>> match_ends(["Gingering","hello","wow"])
    2
    >>> match_ends(["dood","hell","geez"])
    1
    >>> match_ends(["jabz","ana","mom"])
    2
    >>> match_ends(["ssss","oppo","wow"])
    3
    >>> match_ends(["ant","bird","whale"])
    0
    """
    count = 0
    for st in k:
        if len(st) >= 2:
            if st.lower()[0] == st.lower()[-1]:
                count += 1
    return count

#15
def remove_adjacent(t):
    """
    This function will remove one adjacent number if it duplicate.
    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([1, 2, 2, 3, 4, 4])
    [1, 2, 3, 4]
    >>> remove_adjacent([1, 2, 2, 3, 3, 5 ,5])
    [1, 2, 3, 5]
    >>> remove_adjacent([1, 2, 2, 3, 3, 5 , 5, 6 ,6])
    [1, 2, 3, 5, 6]
    >>> remove_adjacent([1, 2, 2, 3, 3, 5 ,5,6 ,6, 7, 7])
    [1, 2, 3, 5, 6, 7]
    """
    after_remove = []
    check = None
    for num in t:
        if num == check:
            continue
        after_remove.append(num)
        check = num 
    return after_remove

