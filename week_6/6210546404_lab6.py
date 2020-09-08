

#1
def ll_sum(t):
    """ sum num list of lists
    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> ll_sum(t)
    21
    >>> t = [[5, 5], [4, 3], [2]]
    >>> ll_sum(t)
    19
    >>> t = [[1], [4, 3, 5, 6], [2, 6, 7, 3, 7]]
    >>> ll_sum(t)
    44
    >>> t = [[5,7], [6,6], [8], [7,4]]
    >>> ll_sum(t)
    43
    >>> t = [[9,7], [2,1,4,8], [7,4,8,9]]
    >>> ll_sum(t)
    59
    """
    p = 0
    for element in t:
        p += sum(element)
    return p

#2
def cumulative_sum(t):
    """
    this function take a list of numbers and return
    the cumulative sum of numbers in a list
    >>> cumulative_sum([1,2,3])
    [1, 3, 6]
    >>> cumulative_sum([2,3,4])
    [2, 5, 9]
    >>> cumulative_sum([7,4,1])
    [7, 11, 12]
    >>> cumulative_sum([4,6,4,1])
    [4, 10, 14, 15]
    >>> cumulative_sum([5,1,8,9])
    [5, 6, 14, 23]
    """
    sum_list = []
    a = 0
    for element in t:
        a += element
        sum_list.append(a)
    return sum_list

#3
def middle(t):
    """
    take a list and return a new list that contain all
    except first and last elements.
    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    >>> t = ["Wow", "Psycho", "Congratulations", "Goodbyes", "Better Now"]
    >>> middle(t)
    ['Psycho', 'Congratulations', 'Goodbyes']
    >>> t = [420]
    >>> middle(t)
    []
    >>> t = [1, 5, 7, 15, 18]
    >>> middle(t)
    [5, 7, 15]
    >>> t = ["me", "myself", "and", "I"]
    >>> middle(t)
    ['myself', 'and']
    """
    return t[1:len(t)-1]

#4
def chop(t):
    """ 
    take a list and removing the first and last elements
    and returns None.
    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    >>> t = ["One", "Two", "Three", "Four", "Five"]
    >>> chop(t)
    >>> t
    ['Two', 'Three', 'Four']
    >>> t = ["SAD!"]
    >>> chop(t)
    >>> t
    []
    >>> t = ["o", "p", "u", "y"]
    >>> chop(t)
    >>> t
    ['p', 'u']
    >>> t = [1, 7, 8, 9, 5]
    >>> chop(t)
    >>> t
    [7, 8, 9]
    """
    t[0:1] = []
    t[len(t)-1:] = []

#5
def is_sorted(t):
    """
    take a list as a patameter and retur True 
    if the list is sorted in ascending order and
    False otherwise.
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    >>> is_sorted([5, 9, 15, 14])
    False
    >>> is_sorted(["too", "cat", "bu"])
    False
    >>> is_sorted(["dog", "elo", "flu"])
    True
    """
    p = t.copy()
    t.sort()
    if t == p:
        return True
    else:
        return False

#6
def front_x(t):
    """
    take a list in this function and return a list
    with the string in sorted order,except the string
    the begin with "x" sort that first and put that
    group in front of list.
    >>> l = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] 
    >>> front_x(l)
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    >>> l = ["xxxtentacion", "xiaomi", "xanax", "lean", "crack"]
    >>> front_x(l)
    ['xanax', 'xiaomi', 'xxxtentacion', 'crack', 'lean']
    >>> l = ["xpack", "adobe", "boss", "coke", "zabra"]
    >>> front_x(l)
    ['xpack', 'adobe', 'boss', 'coke', 'zabra']
    >>> l = ["xbo", "xaf", "xio", "foo", "go"]
    >>> front_x(l)
    ['xaf', 'xbo', 'xio', 'foo', 'go']
    >>> l = ["up", "ufa", "deo", "buff"]
    >>> front_x(l)
    ['buff', 'deo', 'ufa', 'up']
    """
    x_front = []
    not_x_front = []
    for element in t:
        if element[0] == "x":
            x_front.append(element)
        else:
            not_x_front.append(element)
    x_front.sort()
    not_x_front.sort()
    return x_front + not_x_front

#7
def even_only(l):
    """
    take a list of numbers, and return new list with 
    only even numbers.
    >>> even_only([3,1,4,1,5,9,2,6,5])
    [4, 2, 6]
    >>> even_only([11, 12, 14, 49, 18, 26, 71])
    [12, 14, 18, 26]
    >>> even_only([1,3,7,9,11,5,17])
    []
    >>> even_only([5,4,8,6,17])
    [4, 8, 6]
    >>> even_only([4,8,12,5,17,48])
    [4, 8, 12, 48]
    """
    num_stock = []
    for num in l:
        if num % 2 == 0:
            num_stock.append(num)
    return num_stock

#8
def love(text):
    """
    this function will change the secord last word to "love"
    >>> love("I like Python")
    'I love Python'
    >>> love("I really like Python")
    'I really love Python'
    >>> love("I very very very freaking hate Python")
    'I very very very freaking love Python'
    >>> love("I like dog")
    'I love dog'
    >>> love("I like fish")
    'I love fish'
    """
    p = text.split()
    new_text = p[0:-2] + ["love"] + p[-1:]
    s = " ".join(new_text)
    return s

#9
def is_anagram(t1,t2):
    """
    this function return true if they are anagrams.
    >>> is_anagram('arrange', 'Rear Nag')
    True
    >>> is_anagram("Amorn", "MoN R a")
    True
    >>> is_anagram("second", "Don f S")
    False
    >>> is_anagram("function","O F unc IT n")
    True
    >>> is_anagram("pom", "Pi M")
    False
    """
    new_t1 = t1.lower()
    new_t2 = t2.lower()
    new_t1_v2 = list(new_t1)
    new_t2_v2 = list(new_t2)
    new_t1_v2.sort()
    new_t2_v2.sort()
    new_t2_v3 = ' '.join(new_t2_v2).split()
    if new_t1_v2 == new_t2_v3:
        return True
    else:
        return False

#10
def has_duplicates(t):
    """
    this function take a list and return True if 
    there is any element that appears more then once.
    >>> has_duplicates([1,2,3,4,5])
    False
    >>> has_duplicates([1,5,1,1,8,4])
    True
    >>> has_duplicates(["o", "o", "eiei", "pom"])
    True
    >>> has_duplicates(["both", "both", "both", "only"])
    True
    >>> has_duplicates(["tu", "pom", "side", "go"])
    False
    """
    same = []
    for element in t:
        if element not in same:
            same.append(element)
    if t == same:
        return False
    else:
        return True

#11
def average(nums):
    """
    this function calculate average of list
    >>> average([1, 1, 5, 5, 10, 8, 7])
    5.285714285714286
    >>> average([1,7,8,4])
    5.0
    >>> average([5,4,9,2,8,7])
    5.833333333333333
    >>> average([4,9,8,7,5])
    6.6
    >>> average([1,2])
    1.5
    """
    return sum(nums)/len(nums)

#12
def centered_average(nums):
    """
    this function calculate average of list that
    ignores the largest and smallest values in the list
    ,but if there are mutiple copies of the smallest/largest
    value,pick jut one copy
    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([4, 5, 3, 2, 2, 5])
    3.5
    >>> centered_average([3, 6, 4, 3, 4, 6, 6, 1])
    4.0
    >>> centered_average([4, 8, 3, 8, 9, 4, 12])
    6.6
    >>> centered_average([14, 19, 7, 19, 4, 12, 3, 14])
    11.666666666666666
    """
    nums.sort()
    x = nums.count(nums[0])
    y = nums.count(nums[-1])
    if x > 1 and y > 1:
        new_nums = [nums[0], nums[-1]]
        for element in nums:
            if element != nums[0]:
                if element != nums[-1]:
                    new_nums.append(element)
        return sum(new_nums)/len(new_nums)
    if x > 1 and y <= 1:
        new_nums = [nums[0]]
        for element in nums:
            if element != nums[0]:
                if element != nums[-1]:
                    new_nums.append(element)
        return sum(new_nums)/len(new_nums)
    if x <= 1 and y > 1:
        new_nums = [nums[-1]]
        for element in nums:
            if element != nums[0]:
                if element != nums[-1]:
                    new_nums.append(element)
        return sum(new_nums)/len(new_nums)
    if x <= 1 and y <= 1:
        new_nums = []
        for element in nums:
            if element != nums[0]:
                if element != nums[-1]:
                    new_nums.append(element)
        return sum(new_nums)/len(new_nums)

#13
def reverse_pair(t):
    """
    this function return the reverse pair of the input
    sentence
    >>> reverse_pair("May the fourth be with you")
    'you with be fourth the May'
    >>> reverse_pair("Who am I")
    'I am Who'
    >>> reverse_pair("Some one that is afraid to let go")
    'go let to afraid is that one Some'
    >>> reverse_pair("You decide if you are ever gonna let me know")
    'know me let gonna ever are you if decide You'
    >>> reverse_pair("Suicide if you ever try to let go")
    'go let to try ever you if Suicide'
    """
    x = t.split()
    x.reverse()
    new_text = " ".join(x)
    return new_text

#14
def match_ends(t):
    """
    this function returns the count of the number 
    of string that first and last chars of the string
    are the same.
    >>> match_ends(["Gingering", "hello","wow"])
    2
    >>> match_ends(["Anna","Bingo","snake"])
    1
    >>> match_ends(["neon","speechless","Sleepless","disney"])
    3
    >>> match_ends(["cocacola", "zelda", "gembling", "Star Wars", "plantain", "Racecar"])
    3
    >>> match_ends(["sell","eat","bammm","same"])
    0
    """
    count = 0
    for element in t:
        x = element.lower()
        if x[0] == x[-1]:
            count += 1
    return count

    

#15
def remove_adjacent(t):
    """
    this function return a list where all adjacent 
    elements have been reduced to a single element.
    >>> remove_adjacent([1,2,2,3])
    [1, 2, 3]
    >>> remove_adjacent([1,1,1,2,2,2,3,3,3])
    [1, 2, 3]
    >>> remove_adjacent([1,5,5,2,2,4,5,5])
    [1, 5, 2, 4, 5]
    >>> remove_adjacent([2,2,1,5,4,9,9])
    [2, 1, 5, 4, 9]
    >>> remove_adjacent([8,5,4,9,1,4,4,6,6,1])
    [8, 5, 4, 9, 1, 4, 6, 1]
    """
    new_list = []
    x = None
    for element in t:
        if element == x:
            continue
        new_list.append(element)
        x = element
    return new_list

        
        






