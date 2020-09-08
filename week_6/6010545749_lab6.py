

def ll_sum(L):
    """
    created variable "total" for collect sum number in array
    use for loop to collect number and use try except TypeError to collect number from nested array.

    >>> print(ll_sum([[1,2,3,4,5],0,[9]]))
    24
    >>> print(ll_sum([[1],0,[0,0]]))
    1
    >>> print(ll_sum([2,5]))
    7
    >>> print(ll_sum([[1],0,[-1,0]]))
    0
    >>> print(ll_sum([[1],0,-5,-666666]))
    -666670
    """
    total = 0
    for i in L:
       try:
           total+=i
       except TypeError:
           total+= ll_sum(i)
    return total


def cumulative_sum(L):
    """
    create variable to collect total sum and variable to collect new list
    if it nested array.
    >>> print(cumulative_sum([1,2,3,4,5]))
    [1, 3, 6, 10, 15]
    >>> print(cumulative_sum([1,-7,8]))
    [1, -6, 2]
    >>> print(cumulative_sum([-1,-7,-8]))
    [-1, -8, -16]
    >>> print(cumulative_sum([0,0,0,0,0,0,0,0,0]))
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    >>> print(cumulative_sum([1,0,-1,0,1,0,-1,0,1]))
    [1, 1, 0, 0, 1, 1, 0, 0, 1]
    """

    new =[]
    total = 0
    for i in L:
            total += i
            new.append(total)

    return new

def middle(L):
    """
    use len to see the last ele in array,use slicing method and return new list
    >>> print(middle([1,5,2,3]))
    [5, 2]
    >>> print(middle([1,5,2]))
    [5]
    >>> print(middle([1,5,2,3,5,5,5,5,5,5,5]))
    [5, 2, 3, 5, 5, 5, 5, 5, 5]
    >>> print(middle([-1,5,3,5,42,-9]))
    [5, 3, 5, 42]
    >>> print(middle([1,5]))
    []
    """

    n = len(L)
    new_list =(L[1:n-1])
    return new_list


def chop(L):
    """
    use function .remove() the first and the last char and return the same list
    >>> print(chop([-1,2,-3]))
    [2]
    >>> print(chop([1,5,2,3,5,5,5,5,5,5,5]))
    [5, 2, 3, 5, 5, 5, 5, 5, 5]
    >>> print(chop([-1,5,3,5,42,-9]))
    [5, 3, 5, 42]
    >>> print(chop([1,5]))
    []
    >>> print(chop([1,5,2,3]))
    [5, 2]
    """
    L.remove(L[0])
    L.remove(L[-1])
    return L

def is_sorted(L):
    """
    create empty list and use for loop to append every ele in array L for "new_sort" after append,use function .sort() to sort it
    use if else to check if new_sort == input list
    >>> is_sorted(["a", "b", "c"])
    True
    >>> is_sorted(["b", "z","a"])
    False
    >>> is_sorted(["ก","ข"])
    True
    >>> is_sorted(["a", "b", "c"])
    True
    >>> is_sorted(["b", "z","a"])
    False
    >>> is_sorted(["ก","ข"])
    True
    """
    new_sort = []
    for ele in L:
        new_sort.append(ele)
        new_sort.sort()
    if new_sort == L:
        return True
    else:
        return False

def front_x(L):
    """
    create two lists ones for normal sort, ones for x in front sort
    use  for loop and in for loop use function startswith() to check if it start with x or not
    if it's start with x so we add it to x_sort else add to normal sort
    when for loop end put x_sort in front and + with normal sort and return after sorted.

    >>> print(front_x(["S","xyz","dragon","my"]))
    ['xyz', 'S', 'dragon', 'my']
    >>> print(front_x(["sas","xyz","xagon","xzz"]))
    ['xagon', 'xyz', 'xzz', 'sas']
    >>> print(front_x(["red","blue"]))
    ['blue', 'red']
    >>> print(front_x(["x","s1","s","c"]))
    ['x', 'c', 's', 's1']
    >>> print(front_x(["X","xyz","dragon","my"]))
    ['xyz', 'X', 'dragon', 'my']
    """
    x_sort =[]
    new_sort =[]
    for i in L:
        if i.startswith("x"):
            x_sort.append(i)
        else:
            new_sort.append(i)
    return sorted(x_sort)+sorted(new_sort)


def even_only(list):
    """create an empty list ,use for loop and use if to check even after that append to the empty list.
    >>> even_only([3,1,4,1,5,9,2,6,5])
    [4, 2, 6]
    >>> even_only([1,3,5,7,9])
    []
    >>> even_only([0])
    [0]
    >>> even_only([-2,2])
    [-2, 2]
    >>> even_only([3,2,-5])
    [2]
    """
    even_list = []
    for i in list:
        if i % 2 == 0:
            even_list.append(i)
    return even_list


def love(text):
    """
    create new list by receive from input list and use function .split() to get each words out.
    and use slicing method to replace the second last word with love after that join them tgt and return.

    >>> love("I like high place")
    'I like love place'
    >>> love("I like dragon")
    'I love dragon'
    >>> love("I despise everything")
    'I love everything'
    >>> love("I love myself")
    'I love myself'
    >>> love("I hate life")
    'I love life'
    """
    w_list = text.split()
    w_list[-2] = "love"
    love = " ".join(w_list)
    return love


def is_anagram(w1,w2):
    """
    make input all to be upper case and make new list after sorted inputs and use while loop to check blank space
    and remove it.
    >>> is_anagram("Billy","Yillb")
    True
    >>> is_anagram("dragon","D gonr")
    False
    >>> is_anagram("dragon","D gonra")
    True
    >>> is_anagram("WWWW","wwww")
    True
    >>> is_anagram("11","111")
    False
    """
    w1 = w1.upper()
    w2 = w2.upper()
    w1_list = sorted(w1)
    w2_list = sorted(w2)
    while " " in w1_list:
        w1_list.remove(" ")
    while " " in w2_list:
        w2_list.remove(" ")
    if w1_list == w2_list:
        return True
    else:
        return False


def has_duplicates(L):
    """
    create "du" variable and use set to remove duplicates
    and use len to count input and that variable we created
    if len(du) < len(input) that mean we got a duplicates.

    >>> has_duplicates([1, 2, 3, 4])
    False
    >>> has_duplicates([1, 2, 2, 4])
    True
    >>> has_duplicates([0 ])
    False
    >>> has_duplicates([1, 2, 3, -3])
    False
    >>> has_duplicates([1, 2, 3, 4,5,1,51])
    True
    """
    du = set(L)
    if len(du)<len(L):
        return True
    else:
        return False


def average(nums):
    """
    use len(nums) and use t = sum(nums) function create variable avg = t/base and return it.

    >>> average([1, 1, 5, 5, 10, 8, 7])
    5.285714285714286
    >>> average([1, 1, 5, 5, 10, 8])
    5.0
    >>> average([1, 1, 5, 5, 10, 8, -1,-10])
    2.375
    >>> average([1,0])
    0.5
    >>> average([1, -1])
    0.0

    """
    base =len(nums)
    t = sum(nums)
    avg = t/base
    return avg


def centered_average(nums):
    """
    sum all number in list ,find max,min and use the mean formula

    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([1, 2, 2, 2, 12, 8, 0])
    3.0
    >>> centered_average([1, 1, 1, 1])
    1.0
    >>> centered_average([1, 1, 5, -5, 10, 8, 7])
    4.4
    >>> centered_average([1,2 ,4,6])
    3.0
    """
    sumt = sum(nums)
    b = len(nums)-2
    lemax = max(nums)
    lemin = min(nums)
    quick_maff =(sumt- lemax-lemin)/b
    return quick_maff


def reverse_pair(words):
    """
    use function split and slicing method to make a list that had been split reverse after that join it together.
    >>> reverse_pair("May the fourth be with you")
    'you with be fourth the May'
    >>> reverse_pair("May I stand unshaken")
    'unshaken stand I May'
    >>> reverse_pair("Finding Paradise")
    'Paradise Finding'
    >>> reverse_pair("deep deep down")
    'down deep deep'
    >>> reverse_pair("OMEGAEZ CLAP")
    'CLAP OMEGAEZ'
    """
    words = words.split(" ")
    words = words[-1::-1]
    re = " ".join(words)
    return re


def match_ends(L):
    """
    create variable for counting a matches and use for loop if to check condition according to the requires.
    >>> match_ends(["Gingering", "hello","wow"])
    2
    >>> match_ends(["no"])
    0
    >>> match_ends(["MIM","wWoW"])
    2
    >>> match_ends(["demon of hell","1111111"])
    1
    >>> match_ends(["essence", "maim","Fattaf"])
    3
    """
    count=0
    for ele in L:
       if len(ele) >=2 :
           s1 =  ele[-1].upper()
           s2 = ele[0].upper()
           if s1 == s2:
            count+=1
    return count


def remove_adjacent(L):
    """
    make input to set to remove adjacent and return it to new list and return.
    >>> remove_adjacent([1, 2,5,2,3])
    [1, 2, 3, 5]
    >>> remove_adjacent([1,1,11,1,11])
    [1, 11]
    >>> remove_adjacent([1, 0,0])
    [0, 1]
    >>> remove_adjacent([55,5,555])
    [555, 5, 55]
    >>> remove_adjacent([1,-1])
    [1, -1]
    """
    new = set(L)
    new_list =list(new)
    return new_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()










