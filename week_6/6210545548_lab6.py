

'''
--------------------------------------------------| NOTE: QUESTION 1
'''
def ll_sum(value):
    """ This function RETURN the total sum of int values inside list, with recursion
        implemented the parameter send to the function can be any layer of list or types.

    Example:
        >>> print(ll_sum([[1, 2], [3], [4, 5, 6]]))
        21
        >>> print(ll_sum([1,2,[1,2,[3,[4,[5]]]]]))
        18
        >>> print(ll_sum([69,[69],'SixtyNine',["6ix9ine",[69,True,[69]]]]))
        276
        >>> print(ll_sum(['I','AM','LEGEND']))
        0
        >>> print(ll_sum([1,2,3,4,5]))
        15
    """
    total,index = 0,0
    while index < len(value):
        if type(value[index]) == int: # Check type.
            total += value[index]
        elif type(value[index]) == list: # Check type.
            total += ll_sum(value[index]) # Recursion tryout.
        index += 1
    return total
'''
--------------------------------------------------| NOTE: QUESTION 2
'''
def cumulative_sum(value):
    """ This function RETURN the List values which the front and last index value
        had been cut off.

    Example:
        >>> print(cumulative_sum([1, 2, 3]))
        [1, 3, 6]
        >>> print(cumulative_sum([6, 9, 0, 6, 9]))
        [6, 15, 15, 21, 30]
        >>> print(cumulative_sum([1, 2, True]))
        [1, 3, 4]
        >>> print(cumulative_sum([1, 2, 1, 2, 3, 1, 2, 1, 2, 1]))
        [1, 3, 4, 6, 9, 10, 12, 13, 15, 16]
        >>> print(cumulative_sum([False, True, True, False, True]))
        [0, 1, 2, 2, 3]
    """
    box,index,total = [],0,0
    while index < len(value):
        total += value[index]
        box.append(total)
        index += 1
    return box
'''
--------------------------------------------------| NOTE: QUESTION 3
'''
def middle(value):
    """ This function RETURN the List of values which are sum of original list shown
        step by step in the foam of list order.

    Example:
        >>> print(middle([1, 2, 3]))
        [2]
        >>> print(middle([5,4,64,8,4,354,4,74,8,5]))
        [4, 64, 8, 4, 354, 4, 74, 8]
        >>> print(middle([1, 1, 1, 1, 1]))
        [1, 1, 1]
        >>> print(middle([6, 9, 6, 9, 6, 9]))
        [9, 6, 9, 6]
        >>> print(middle([1, 2, 1, 2, 3, 1, 2, 1]))
        [2, 1, 2, 3, 1, 2]
    """
    new = []
    count = 0
    for element in value:
        if count > 0 and count < len(value)-1:
            new.append(element)
        count += 1
    return new
'''
--------------------------------------------------| NOTE: QUESTION 4
'''
def chop(value):
    """ This function chop the first and last index values off the original list. [No returning value]

    Example:
        >>> t = [1,2,3]; chop(t); print(t)
        [2]
        >>> t = [11,22,33,44,55,66,77,88,99,00]; chop(t); print(t)
        [22, 33, 44, 55, 66, 77, 88, 99]
        >>> t = [6,9,0,6,9,0,6,9]; chop(t); print(t)
        [9, 0, 6, 9, 0, 6]
        >>> t = [9,9,8,8,7,7,4,4,5,6,3,2,5,1,4,7,5,89,5]; chop(t); print(t)
        [9, 8, 8, 7, 7, 4, 4, 5, 6, 3, 2, 5, 1, 4, 7, 5, 89]
        >>> t = [1,1,1,1,1]; chop(t); print(t)
        [1, 1, 1]
    """
    temp = value[1:-1]
    value.clear()
    value.extend(temp)
'''
--------------------------------------------------| NOTE: QUESTION 5
'''
def is_sorted(value):
    """ This function RETURN Boolean value of True or False, if values are in order then
        return True otherwise return False.

    Example:
        >>> print(is_sorted([1,2,3,4,5]))
        True
        >>> print(is_sorted([5,4,3,2,1]))
        False
        >>> print(is_sorted(['A','b','C']))
        False
        >>> print(is_sorted(['a','b','c']))
        True
        >>> print(is_sorted(['bommy','is','the','best']))
        False
    """
    count = 1
    while count < len(value):
        if value[count-1] > value[count]:
            return False
        count += 1
    return True
'''
--------------------------------------------------| NOTE: QUESTION 6
'''
def front_x(value):
    """ This function RETURN a list of strings that is sorted and all string started
        with 'x' will be brought to the front of the list.

    Example:
        >>> print(front_x(['Hello','There','Xmen']))
        ['Xmen', 'Hello', 'There']
        >>> print(front_x(['abc','xyz','xxx','video','hola']))
        ['xxx', 'xyz', 'abc', 'hola', 'video']
        >>> print(front_x(['xtc','Xrf','Xmen']))
        ['Xmen', 'Xrf', 'xtc']
        >>> print(front_x(['abc','def','ijk','lmn','opq']))
        ['abc', 'def', 'ijk', 'lmn', 'opq']
        >>> print(front_x(['123','234','543','321','222']))
        ['123', '222', '234', '321', '543']
    """
    value.sort(); new = []
    for element in value:
        if element[0].lower() == 'x': new.append(element)
    for element in value:
        if element[0].lower() != 'x': new.append(element)
    return new
'''
--------------------------------------------------| NOTE: QUESTION 7
'''
def even_only(value):
    """ This function RETURN a new list consists of only even numbers from the original list.

    Example:
        >>> print(even_only([1,2,3,4,5]))
        [2, 4]
        >>> print(even_only([1,3,5,7,9]))
        []
        >>> print(even_only([2,4,6,8,10]))
        [2, 4, 6, 8, 10]
        >>> print(even_only([1,5,9,7,5,3,2,4,6,8]))
        [2, 4, 6, 8]
        >>> print(even_only([0,-1,-2,-3,-4,-5]))
        [0, -2, -4]
    """
    index,new = len(value),[]
    while index > 0:
        if value[index-1] % 2 == 0:
            new.insert(0,value[index-1])
        index -= 1
    return new
'''
--------------------------------------------------| NOTE: QUESTION 8
'''
def love(text):
    """ This function RETURN a string of original text but swapped out the second last word to 'love'.

    Example:
        >>> print(love('I think I hate you.'))
        I think I love you.
        >>> print(love('You are the best ones.'))
        You are the love ones.
        >>> print(love('Love Hate.'))
        love Hate.
        >>> print(love('Porn Hub.'))
        love Hub.
        >>> print(love('Happy birthday to you.'))
        Happy birthday love you.
    """
    new,count,box = text.split(' '),0,[]
    while new[count] != new[-2]:
        box.append(new[count])
        count += 1
    box.append(new[-1])
    box.insert(-1, 'love')
    return ' '.join(box)
'''
--------------------------------------------------| NOTE: QUESTION 9
'''
def is_anagram(word_1,word_2):
    """ This function RETURN a Boolean True of 2 words are anagrams, else return False.

    Example:
        >>> print(is_anagram('arrange','Rag Near'))
        True
        >>> print(is_anagram('Hello','MOFO'))
        False
        >>> print(is_anagram('Hello','H E L L O'))
        True
        >>> print(is_anagram('Bommy','My Bom'))
        True
        >>> print(is_anagram('Ma Girl','La Migr'))
        True
    """
    main_list,temp_list = [word_1,word_2],[]
    for element in main_list:
        for char in element:
            if char != ' ':
                temp_list.append(char.lower())
    temp_list.sort()
    index,even,odd = 0,'',''
    if len(temp_list) % 2== 0:
        for soul in temp_list:
            if index % 2 == 0:
                even += soul
            else:
                odd += soul
            index += 1
        if even == odd:
            return True
        else: return False
    else: return False
'''
--------------------------------------------------| NOTE: QUESTION 10
'''
def has_duplicates(value):
    """ This function RETURN a Boolean True if there is a duplicate in the list. else return False.

    Example:
        >>> print(has_duplicates([1,2,3,4,5]))
        False
        >>> print(has_duplicates([1,2,3,4,5,2]))
        True
        >>> print(has_duplicates([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]))
        True
        >>> print(has_duplicates([1]))
        False
        >>> print(has_duplicates([0,1,2,0]))
        True
    """
    string = ''
    for element in value:
        if str(element) not in string:
            string += str(element)
        else:
            return True
    return False
'''
--------------------------------------------------| NOTE: QUESTION 11
'''
def average(value):
    """ This function RETURN an average of total sum of values in the list.

    Example:
        >>> print(average([1, 1, 5, 5, 10, 8, 7]))
        5.285714285714286
        >>> print(average([0, 1, 2, 3]))
        1.5
        >>> print(average([0, 0, 0]))
        0.0
        >>> print(average([1, 1]))
        1.0
        >>> print(average([1]))
        1.0
    """
    return sum(value)/len(value)
'''
--------------------------------------------------| NOTE: QUESTION 12
'''
def centered_average(value):
    """ This function RETURN an average of total sum of values in the list.
        Except we exclude min and max value.

    Example:
        >>> print(centered_average([1, 1, 5, 5, 10, 8, 7]))
        5.2
        >>> print(centered_average([1, 1, 1]))
        1.0
        >>> print(centered_average([1, 2, 3, 4, 5]))
        3.0
        >>> print(centered_average([0, 0, 0]))
        0.0
        >>> print(centered_average([2, 4, 6, 8, 10]))
        6.0
    """
    value.sort()
    return sum(value[1:-1])/len(value[1:-1])
'''
--------------------------------------------------| NOTE: QUESTION 13
'''
def reverse_pair(value):
    """ This function RETURN a string that reverse thw word orders of the original one.

    Example:
        >>> print(reverse_pair("May the fourth be with you"))
        you with be fourth the May
        >>> print(reverse_pair("Let me be by your side"))
        side your by be me Let
        >>> print(reverse_pair("OMAE WA MOU SHIN DEIRU NANI"))
        NANI DEIRU SHIN MOU WA OMAE
        >>> print(reverse_pair("You are so high"))
        high so are You
        >>> print(reverse_pair("No I am not"))
        not am I No
    """
    box = value.split(' ')
    front,back,half = 0,len(box)-1,len(box)/2
    while front < half:
        temp = box[front]
        box[front] = box[back]
        box[back] = temp
        front += 1
        back -= 1
    return ' '.join(box)
'''
--------------------------------------------------| NOTE: QUESTION 14
'''
def match_ends(value):
    """ This function RETURN an integer value of the occurance for the word in list
        that has the same first and last character.

    Example:
        >>> print(match_ends(["Gingering", "hello","wow"]))
        2
        >>> print(match_ends(["lol", "lmao","pop"]))
        2
        >>> print(match_ends(["rip", "Bittttch","zed"]))
        0
        >>> print(match_ends(["Yasuo", "Lux","HUH"]))
        1
        >>> print(match_ends(["Like", "Love","Garghing"]))
        1
    """
    occur = 0
    for element in value:
        if len(element) > 2:
            if element[0].lower() == element[-1].lower():
                occur += 1
    return occur
'''
--------------------------------------------------| NOTE: QUESTION 15
'''
def remove_adjacent(value):
    """ This function RETURN a list that has no adjacent in the list.

    Example:
        >>> print(remove_adjacent([1, 2, 2, 3]))
        [1, 2, 3]
        >>> print(remove_adjacent([1, 1, 1, 1, 1]))
        [1]
        >>> print(remove_adjacent([3, 2, 4, 0, 3, 1, 2, 3]))
        [3, 2, 4, 0, 3, 1, 2, 3]
        >>> print(remove_adjacent([69, 6, 6, 9, 9, 69]))
        [69, 6, 9, 69]
        >>> print(remove_adjacent([88, 8, 888, 8, 8, 88, 88, 888]))
        [88, 8, 888, 8, 88, 888]
    """
    count = 1
    while count < len(value):
        if value[count] == value[count-1]:
            value.pop(count)
            count -= 1
        count += 1
    return value
'''
--------------------------------------------------| NOTE: DOCTEST
'''
if __name__ == '__main__':
    import doctest
    doctest.testmod()