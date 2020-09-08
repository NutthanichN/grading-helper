

#1
def ll_sum(t):
    """takes a list of lists of integers and adds up the elements from all of the nested lists.

    Arg:
        list you want to calculate
    Return:
        totalsum

    >>> ll_sum([[1],[1,2],[1,2,3]])
    10
    >>> ll_sum([[1],[2,3],[4,5]])
    15
    >>> ll_sum([[1],[2],[3]])
    6
    >>> ll_sum([[1],[1,2,3],[1,2,3,4,5]])
    22
    >>> ll_sum([[11,22],[33,33],[34,45]])
    178

    Note: Sum all the value in the list then sum all the sum of nested list and return it's value.
    """

    sum = 0
    for i in range (len(t)):
        for j in range (len(t[i])):
            sum += t[i][j]
    return sum

#2
def cumalative_sum(t):
    """returns the cumulative sum; that is, a new list where the ith element is the sum of the first i + 1 elements
    from the original list.

    Arg:
        list you want to calculate
    Return:
        list that contain cumalative sum

    >>> cumalative_sum([1,2,3,4])
    [1, 3, 6, 10]
    >>> cumalative_sum([1,3,5,7,9])
    [1, 4, 9, 16, 25]
    >>> cumalative_sum([1,1,1,1])
    [1, 2, 3, 4]
    >>> cumalative_sum([11,22,33,44])
    [11, 33, 66, 110]
    >>> cumalative_sum([12313,13452,5663,654])
    [12313, 25765, 31428, 32082]

    Note: I used repetition to replace element by sum the previous element with current element (do this until last element)
    then return all of them.
    """

    for i in range (len(t)-1):
        t[i+1] = t[i]+t[i+1]
    return t

#3
def middle(t):
    """returns a new list that contains all but the first and last elements.

    Arg:
        list you want to remove first and last elements
    Return:
        a new list that contains all but the first and last elements.

    >>> middle([1,2,3,4,5])
    [2, 3, 4]
    >>> middle([1,4,5,8,9,8])
    [4, 5, 8, 9]
    >>> middle([1,2,34,66,23])
    [2, 34, 66]
    >>> middle([4,6,7,8,0,0])
    [6, 7, 8, 0]
    >>> middle([44,55.3,34,44,6])
    [55.3, 34, 44]

    Note: return only second element to before the last element.
    """

    return t[1:-1]

#4
def chop(t):
    """removing the first and last elements, and returns None.

    Arg:
        list you want to chop first and last letter
    Return:
        chopped list

    >>> t = [1,2,3,4]
    >>> chop(t)
    >>> t
    [2, 3]
    >>> x = [1,2,3,4,5,6,7]
    >>> chop(x)
    >>> x
    [2, 3, 4, 5, 6]
    >>> u = ['a','b','c','d']
    >>> chop(u)
    >>> u
    ['b', 'c']

    Note: remove first character and last character then return the result.
    """

    t.remove(t[0])
    t.remove(t[-1])

#5
def is_sorted(t):
    """takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise.

    Arg:
        list you want to calculate
    Return:
        True or False due to the list thru the condition.

    >>> is_sorted([1,2,3,4,5])
    True
    >>> is_sorted([1,2,2,2,3])
    True
    >>> is_sorted(['a','b','c','d'])
    True
    >>> is_sorted(['a','c','b'])
    False
    >>> is_sorted([1,3,4,5,2])
    False

    Note: check the list by using repetition and break the loop when the next adjacent element is less than
    or equal and return False. If all element in list not in that condition until end, return True.
    """

    answer = True
    for i in range(len(t)-1):
        try:
            if t[i+1]>=t[i]:
                answer = True
            else:
                answer = False
                break
        except:
            return False
    return answer

#6
def front_x(t):
    """returns a list with the strings in sorted order, except group all the strings that begin with 'x' first.

    Arg:
        list you want to sort
    Return:
        sorted list
    >>> l = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
    >>> front_x(l)
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    >>> k = ['sand','fire','water','wind','xyz']
    >>> front_x(k)
    ['xyz', 'fire', 'sand', 'water', 'wind']
    >>> h = ['aa','c','ab','xa','ax','hand']
    >>> front_x(h)
    ['xa', 'aa', 'ab', 'ax', 'c', 'hand']

    Note: Sort the list then put the strings that begin with 'x' by set a count variable equal to zero and create a loop
    that when the program found a string that begin with 'x' it will add that string at index-count on the same list,
    add value to count variable by 1 and delete the string that at old index.
    """

    t.sort()
    count = 0
    for i in range(len(t)):
        if t[i][0]=='x':
            t.insert(count,t[i])
            count += 1
            del t[i+1]
    print (t)

#7
def even_only(list):
    """take a list of integers, and return a new list with only even numbers.

    Arg:
        list of integers
    Return:
        newlist that contain only even number.

    >>> even_only([1,2,3,4,5,6])
    [2, 4, 6]
    >>> even_only([1,1,1,1])
    >>> even_only([1,2,3,5])
    [2]
    >>> even_only([1,1,1,2])
    [2]

    Note: create a new empty list and add it with even number(s) from initial list.
    """

    newlist=[]
    for i in range(len(list)):
        if list[i]%2==0:
            newlist.append(list[i])
    if len(newlist)>0:
        return newlist
    else:
        return None

#8
def love(list):
    """change the second last word to “love”.

    Arg:
        list you want to change.
    Return:
        list that changed second last word.

    >>> love("I like Python")
    "I love Python”
    >>> love("I really like Python")
    "I really love Python"
    >>> love("I don't like Python")
    "I don't love Python"

    Note: create an empty list to store index of space then return new string which contain only
    first letter from list to index that second the last space and plus 'love' word and plus word
    after last space.
    """

    checkspace = []
    for i in range(len(list)):
        if list[i]==' ':
            checkspace.append(i)
    newmsg = list[:checkspace[-2]]+' love'+list[checkspace[-1]:]
    return newmsg

#9
def is_anagram(msg1,msg2):
    """Two words are anagrams if you can rearrange the letters from one to spell the other.
    Returns True if they are anagrams.

    Arg:
        2 message you want to check
    Return:
        True or False due to the list thru the condition.

    >>> is_anagram('orange', 'Rear Nag')
    False
    >>> is_anagram('arrange', 'Rear Nag')
    True
    >>> is_anagram('John Lennon','Jennon Lohn')
    True
    >>> is_anagram('Singer','Gin ser')
    True

    Note: Remove all space(s) from two strings and sort them then check if they are the same
    """

    if sorted(''.join(msg1.split()).lower()) == sorted(''.join(msg2.split()).lower()):
        return True
    else:
        return False

#10
def has_duplicates(list):
    """returns True if there is any element that appears more than once.

    Arg:
        list you want to check
    Return:
        True or False due to the list thru the condition.

    >>> has_duplicates([1, 2, 3, 4, 5])
    False
    >>> has_duplicates([1, 2, 3, 4, 5, 2])
    True
    >>> has_duplicates(['a', 2, 3, 4, 'a'])
    True
    >>> has_duplicates([1, 2, 3, 3, 5])
    True

    Note: create a new empty list check and append the duplicate string to the list
    if the list is not empty then return True. If not, return False.
    """

    repeated = []
    for i in range(len(list)):
        k = i + 1
        for j in range(k,len(list)):
            if list[i] == list[j] and list[i] not in repeated:
                repeated.append(list[i])
    if len(repeated)>=1:
        return True
    else:
        return False

#11
def average(list):
    """returns the mean average of a list of numbers.

    Arg:
        list you want to calculate an average
    Return:
        average of the list

    >>> average([1,2,3,4])
    2.5
    >>> average([1,1,1,1,1,1])
    1.0
    >>> average([11,22,33,22,11])
    19.8
    >>> average([5,5,5,3,3,3])
    4.0
    >>> average([1, 1, 5, 5, 10, 8, 7])
    5.285714285714286

    Note: Sum all element in list and divide them by the list's size and return the result.
    """

    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum/len(list)

#12
def centered_average(nums):
    """returns a "centered" average of a list of numbers, which is the mean average of the values
    that ignores the largest and smallest values in the list. If there are multiple copies of
    the smallest/largest value, pick just one copy.

    Arg:
        list you want to calculate an centered average
    Return:
        average number of the centered list

    >>> centered_average([2, 1, 6, 5, 10, 8, 7, 7])
    5.75
    >>> centered_average([2, 1, 6, 8, 11, 8, 7, 9])
    6.5
    >>> centered_average([42, 11, 16, 52, 10, 82, 74, 27])
    39.25

    Note: sort the list and create a list that contain only unduplicated string(s) and return
    list which contain only element from the sorted list from index that the first string minus one to
    the last string plus one from the unique string list.
    """

    nums = sorted(nums)
    same = list(dict.fromkeys(nums))
    newlist = nums[nums.index(same[1])-1:nums.index(same[-1])+1]
    sum = 0
    for i in range(len(newlist)):
        sum += newlist[i]
    return sum / len(newlist)

#13
def reverse_pair(msg):
    """returns the reverse pair of the input sentence.

    Arg:
        Sentence you want to reverse it
    Return:
        Revered sentence

    >>> reverse_pair("May the fourth be with you")
    'you with be fourth the May'
    >>> reverse_pair("I'm your father")
    "father your I'm"
    >>> reverse_pair("Python 3.7.4 Shell")
    'Shell 3.7.4 Python'

    Note: Split the string by space ,reverse it and return the list and join them by space
    into one string and return it.
    """

    list = msg.split()
    list.reverse()
    return (" ".join(list))

#14
def match_ends(list):
    """returns the count of the number of strings where the string length is 2 or more and the first and last
    chars of the string are the same.

    Arg:
        list you want to count due to the condition
    Return:
        counted number due to the condition

    >>> match_ends(["Gingering", "hello","wow"])
    2
    >>> match_ends(["wow", "wow","wow"])
    3
    >>> match_ends(["Bingering", "hello","pow"])
    0

    Note: count the number of elements in list which first and last letter are the same.
    """

    count = 0
    for i in range(len(list)):
        if len(list[i])>=2:
            if list[i][0].lower() == list[i][-1].lower():
                count += 1
        else:
            return ("Error")
    return count

#15
def remove_adjacent(list):
    """ returns a list where all adjacent elements have been reduced to a single element.

    Arg:
        list you want to remove adjacent
    Return:
        list that removed adjacent

    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([1, 2, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([1, 2, 2, 3, 2, 4, 4])
    [1, 2, 3, 2, 4]

    Note: Change the adjacent word to a specific word then remove all of that word from the list then return the list.
    """

    count = 0
    for i in range(len(list)-1):
        if list[i]==list[i+1]:
            list[i] = 'pre'
            count +=1
    for i in range(count):
        list.remove('pre')
    return list