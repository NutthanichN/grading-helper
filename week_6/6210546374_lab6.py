

##################################### KONGTAPP VEERAWATTANANUN ##########################################
############################################ 6210546374 #################################################
# lab6 Teacher Paruj Ratanaworabhan #

# Exercise1 #
def ll_sum(lista):
    """
    Write a function called ll_sum that takes a list of lists of integers and adds up the elements from all of the nested lists.
    Example:
    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> ll_sum(t)
    21
    >>> u = [[1, 2], [4, 4, 5], 3]
    >>> ll_sum(u)
    19
    >>> v = [[5, 5], [4,2], [-3,7]]
    >>> ll_sum(v)
    20
    >>> w = [[1,1], [0], [5, 1]]
    >>> ll_sum(w)
    8
    >>> x = [[7, 7, 5],[3,2]]
    >>> ll_sum(x)
    24
    """
    total = 0
    for j in range(len(lista)):
        if type(lista[j]) == list:    
            total += ll_sum(lista[j])
        else:
            total += lista[j]
    return total

# Exercise2 #
def cumulative_sum(listz):
    """
    This function takes a list of numbers and returns the cumulative sum; that is, a new list where 
    the ith element is the sum of the ﬁrst i + 1 elements from the original list.
    Example:
    >>> cumulative_sum([1,2,3])
    [1, 3, 6]
    >>> cumulative_sum([3,5,7,9])
    [3, 8, 15, 24]
    >>> cumulative_sum([4,14,24,34,44])
    [4, 18, 42, 76, 120]
    >>> cumulative_sum([1,5,9,13])
    [1, 6, 15, 28]
    >>> cumulative_sum([2,4,6,8,10])
    [2, 6, 12, 20, 30]
    """
    new_list = []
    new_str = 0
    for i in listz:
        if type(i) == list:
            new_list += cumulative_sum
        else:
            new_str += i
            new_list.append(new_str)
    return new_list

# Exercise3 #
def middle(listc):
    """
    This function takes a list and returns a new list that contains all but the ﬁrst and last elements.
    Example:
    >>> middle([1,2,3,4])
    [2, 3]
    >>> middle(['duck', 'dog', 'dragon'])
    ['dog']
    >>> middle(['violet','velvet','peridot','silver'])
    ['velvet', 'peridot']
    >>> middle(['king', 'queen', 'bishop', 'knight', 'rook', 'pawn'])
    ['queen', 'bishop', 'knight', 'rook']
    >>> middle([41, 16, 96, 44, 66, 11, 0])
    [16, 96, 44, 66, 11]
    """
    new_list = []
    count = 0
    for ch in listc:
        if count == 0 or count == len(listc)-1 :
            count += 1
        else:
            count += 1
            new_list.append(ch)
    return new_list

# Exercise4 #
def chop(lists):
    """
    This function takes a list, modiﬁes it by removing the ﬁrst and last elements, and returns None.
    Example:
    >>> chop([1,2,3,4])
    [2, 3]
    >>> chop([4,5,6,8,7])
    [5, 6, 8]
    >>> chop(["Hello", "World", 123, 5555, [1, 2, 3]])
    ['World', 123, 5555]
    >>> chop([['set', 'word'] , 'Python', 'is' , 'easy', 'nice'])
    ['Python', 'is', 'easy']
    >>> chop([5, 6, 8, 1, 4, 3])
    [6, 8, 1, 4]
    """
    lists.remove(lists[0])
    lists.remove(lists[-1])


# Exercise5 #
def is_sorted(listb):
    """
    This function takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise
    Example:
    >>> is_sorted([[1, 2, 3, 4]])
    True
    >>> is_sorted([1, 2, 2]) 
    True
    >>> is_sorted(['b', 'a'])
    False
    >>> is_sorted(['jhin', 'zed', 'shen', 'akali', 'kennen', 'sona'])
    False
    >>> is_sorted(['Dota', 'LOL', 'ROV'])
    True
    """
    new_list = []
    for ch in listb:
        new_list.append(ch)
    listb.sort()

    if new_list == listb:
        return True
    else:
        return False

# Exercise6 #
def front_x(listx):
    """
    This function returns a list with the strings in sorted order, except group all the strings that begin with 'x' ﬁrst
    Example:
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    >>> front_x(['pun', 'nut', 'yo', 'pee', 'xuk'])
    ['xuk', 'nut', 'pee', 'pun', 'yo']
    >>> front_x(['zoe', 'rakan', 'xayah', 'aurelion sol'])
    ['xayah', 'aurelion sol', 'rakan', 'zoe']
    >>> front_x(['jhin', 'zed', 'shen', 'akali', 'kennen', 'xerath', 'azir', 'nasus', 'renekton'])
    ['xerath', 'akali', 'azir', 'jhin', 'kennen', 'nasus', 'renekton', 'shen', 'zed']
    >>> front_x(['pyke', 'gangplank', 'twisted fate', 'graves', 'miss fortune'])
    ['gangplank', 'graves', 'miss fortune', 'pyke', 'twisted fate']
    """
    list1 = []
    list2 = []
    list_mix = []
    for i in listx:
        if i[0] == 'x':
            list1.append(i)
        else:
            list2.append(i)
    list1.sort()
    list2.sort()
    return list1 + list2

# Exercise7 #
def even_only(listk):
    """
    This function will take a list of integers, and return a new list with only even numbers.
    >>> even_only([3,1,4,1,5,9,2,6,5])
    [4, 2, 6]
    >>> even_only(['ahri', 'rengar', 'gnar', 'warwick', 'nidalee'])
    'error:type is not integer!'
    >>> even_only([44,55,66,77,88,4,2,3,444,4])
    [44, 66, 88, 4, 2, 444, 4]
    >>> even_only([1,4,6,8,2,6,4,33,8,0,1])
    [4, 6, 8, 2, 6, 4, 8, 0]
    >>> even_only([1,3,5,7,9,11,13,15])
    []
    """
    even_list = []
    for e in listk:
        if type(e) != int:
            return 'error:type is not integer!'
        elif e % 2 == 0:
            even_list.append(e)       
    return even_list

# Exercise8 #
def love(text):
    """
    This function will change the second last word to “love”.
    Example:
    >>> love("I really like Python")
    'I really love Python'
    >>> love("I like Python")
    'I love Python'
    >>> love("What is Love Baby don't hurt me Baby don't hurt me No more")
    "What is Love Baby don't hurt me Baby don't hurt me love more"
    >>> love("Swear to My Bones")
    'Swear to love Bones'
    >>> love("The New Beginning")
    'The love Beginning'
    """
    new_list = []
    new_list = text.split()
    new_list[-2] = "love"
    return " ".join(new_list)

# Exercise9 #
def is_anagram(str1, str2):
    """
    Two words are anagrams if you can rearrange the letters from one to spell the other. 
    This function takes two strings and returns True if they are anagrams. 
    Example:
    >>> is_anagram('arrange', 'Rear Nag')
    True
    >>> is_anagram('Rengar', 'Garen')
    False
    >>> is_anagram('dog', 'GOD')
    True
    >>> is_anagram('Silent', 'Listen')
    True
    >>> is_anagram('Delta Rune', 'UnderTale')
    True
    """
    lista = []
    listb = []
    for a in str1.lower():
        if a != " ":
            lista.append(a)
    for b in str2.lower():
        if b != " ":
            listb.append(b)
    lista.sort()
    listb.sort()
    if lista == listb:
        return True
    else:
        return False
  
# Exercise10 #
def has_duplicates(listt):
    """
    This function takes a list and returns True if there is any element 
    that appears more than once. It should not modify the original list. 
    Example:
    >>> has_duplicates([1,2,3,4,5,2])
    True
    >>> has_duplicates([1,2,3,4,5])
    False
    >>> has_duplicates([5,6,4,8,1,2])
    False
    >>> has_duplicates([4,44,4444,44,4])
    True
    >>> has_duplicates(['Jhin','jhin','4','44'])
    False
    """
    new_list = listt
    new_list.sort()
    A = False
    for i in range(len(new_list)):
            if new_list[i] == new_list[i-1]:
                A = True
            if A == True:
                break
    return A
    
# Exercise11 #
def average(listn):
    """
    This function returns the mean average of a list of numbers. 
    Example:
    >>> average([1, 1, 5, 5, 10, 8, 7])
    5.285714285714286
    >>> average([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11, 12 , 13, 14])
    7.5
    >>> average([9, 19, 9, 19, 5, 4, 3])
    9.714285714285714
    >>> average([8, 4, 6, 11, 14])
    8.6
    >>> average([10, 20, 30, 14, 7, 5])
    14.333333333333334
    """
    return sum(listn) / len(listn)

# Exercise12 #
def centered_average(listo):
    """
    This function returns a "centered" average of a list of numbers, 
    which is the mean average of the values that ignores the largest and smallest values in the list. 
    If there are multiple copies of the smallest/largest value, pick just one copy
    Example:
    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([-8, -4, 5, 2, 3, 4])
    1.25
    >>> centered_average([4, 8, -5, -2, -3, -4, 14])
    0.6
    >>> centered_average([64.2, 172, 34, 10.5])
    49.1
    >>> centered_average([84, 6, 54, 43, 72])
    56.333333333333336
    """
    listo.sort()
    listo.remove(listo[0])
    listo.remove(listo[-1])
    return sum(listo) / len(listo)

# Exercise13 #
def reverse_pair(yoda):
    """
    Two sentences are a “reverse pair” if each is the reverse of the other. 
    Write a function reverse_pair that returns the reverse pair of the input sentence.
    Example:
    >>> reverse_pair("May the fourth be with you")
    'you with be fourth the May'
    >>> reverse_pair("Welcome to Kasetsart Food Festival")
    'Festival Food Kasetsart to Welcome'
    >>> reverse_pair("Python is really easy")
    'easy really is Python'
    >>> reverse_pair("What is your name?")
    'name? your is What'
    >>> reverse_pair("What should we eat?")
    'eat? we should What'
    """
    l = yoda.split()
    return " ".join(l[::-1])

# Exercise14 #
def match_ends(listm):
    """
    This function returns the count of the number of strings 
    where the string length is 2 or more and the ﬁrst and last chars of the string are the same.
    Example:
    >>> match_ends(["Gingering", "hello","wow"])
    2
    >>> match_ends(["Kongtapp","Veerawattananun","Parima","On-in","Earn","Pun"])
    0
    >>> match_ends(["Hydrogen","Oxygen","Nitrogen","Carbon"])
    1
    >>> match_ends(["GG","a","Nice"])
    'Error:The string length must be 2 of more.'
    >>> match_ends(["Silver","Gold","Platinum","Diamond","Pearl"])
    1
    """
    count = 0
    for i in listm:
        if i[0].lower() == i[-1].lower():
            count = count + 1
        if len(i) < 2:
            return 'Error:The string length must be 2 of more.'
    return count

# Exercise15 #
def remove_adjacent(numm):
    """
    This function returns a list where all adjacent elements have been reduced to a single element. 
    Example:
    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([4, 44, 444, 44, 4, 44, 4, 44, 44, 44, 44])
    [4, 44, 444, 44, 4, 44, 4, 44]
    >>> remove_adjacent([1, 5, 66, 8, 8, 4, 1, 1, 1, 1])
    [1, 5, 66, 8, 4, 1]
    >>> remove_adjacent([0, 12, 14, 14, 5, 5, 6, 7])
    [0, 12, 14, 5, 6, 7]
    >>> remove_adjacent([0, 0, 2, 3, 4, 6, 1, 5])
    [0, 2, 3, 4, 6, 1, 5]
    """
    new_list = []
    count = 0
    for i in range(len(numm)):
        if count == 0:
            new_list.append(numm[i])
            count += 1
        elif numm[i-1] != numm[i]:
            new_list.append(numm[i])
    return new_list
