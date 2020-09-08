

def ll_sum(some_list):
    #This function will return total value of all integers combinded.
    """
    >>> ll_sum([1,2,3])
    6
    >>> ll_sum([5,4,[1,2]])
    12
    >>> ll_sum([[1,2],[2,3],4,[0,1]])
    13
    >>> ll_sum([[1,3],7,[2,[1,3]]])
    17
    >>> ll_sum([[9,[1,[3,2],4]],7])
    26
    """
    result = 0
    if type(some_list) == list: #Check the element is list or not?
        for i in range(len(some_list)):
           result += ll_sum(some_list[i]) # if it's a list call this function 
                                          #so it will call over and over untill it found element that not a list.
    elif type(some_list) == float or type(some_list) == int: #if it's not list return it value.
        result += some_list
    return result

def cumulative_sum(some_list):
    #This function will return new list that every element is the sum of the element before.
    """
    >>> cumulative_sum([1,3,5])
    [1, 4, 9]
    >>> cumulative_sum([2,8,1])
    [2, 10, 11]
    >>> cumulative_sum([7,4,5,11])
    [7, 11, 16, 27]
    >>> cumulative_sum([0,1,0,1,0,1])
    [0, 1, 1, 2, 2, 3]
    >>> cumulative_sum([9,8,7,6,5,4,3])
    [9, 17, 24, 30, 35, 39, 42]
    """
    for i in range(len(some_list)):
        new_list = some_list
        if i > 0: #if it's not the first element in list so it can be sum by element before.
            new_list[i] += new_list[i-1]
        else:
            pass #don't do anything with the first element of the list.
    return new_list

def middle(some_list):
    #This function will return the new list from input list but not have the first element and the last element.
    """
    >>> middle([1,2,3,4,5,])
    [2, 3, 4]
    >>> middle([1,2,3])
    [2]
    >>> middle([2,5,6,7,8,9])
    [5, 6, 7, 8]
    >>> middle([0,"tiger",8,"duck",0])
    ['tiger', 8, 'duck']
    >>> middle(["yolo",191,"oten",99])
    [191, 'oten']
    """
    new_list = [] # Define new_list to cantain element in original list.
    for e in some_list: 
        new_list.append(e)
    new_list.pop(0)
    #print(some_list)
    new_list.pop(-1)
    return new_list

def chop(some_list):
    # This function will take the list and remove the first and last element in list but return None.
    """
    >>> a = [2,3,4,5]
    >>> chop(a)
    >>> a
    [3, 4]
    >>> b = [1,2,3,6,5,4]
    >>> chop(b)
    >>> b
    [2, 3, 6, 5]
    >>> c = [2,5,6,7,8,9,"text","number"]
    >>> chop(c)
    >>> c
    [5, 6, 7, 8, 9, 'text']
    >>> d = [0,"tiger",8,"duck",0]
    >>> chop(d)
    >>> d
    ['tiger', 8, 'duck']
    >>> e = ["yolo",191,"wow",99]
    >>> chop(e)
    >>> e
    [191, 'wow']
    """
    some_list.pop(0)
    some_list.pop(-1)
    return None

def is_sorted(some_list):
    # Check if element in list are sorted.
    """
    >>> is_sorted([1,2,3])
    True
    >>> is_sorted([1,3,2])
    False
    >>> is_sorted(["a","b","c"])
    True
    >>> is_sorted([1,"a",3])
    False
    >>> is_sorted(["b","c","x","a"])
    False
    """
    check = True
    for i in range(len(some_list)):
        if i > 0: #if it's the first element in list, do not thing.
            try:
                if some_list[i] >= some_list[i-1]:
                    pass
                else:
                    check = False
            except:
                check = False
    return check

def front_x(some_list):
    #This funstion will sort every element in list but every element that start with "x" come first.
    """
    >>> front_x(["a","xmas","badass",])
    ['xmas', 'a', 'badass']
    >>> front_x(["xxl","roll","turtle","fool","xter"])
    ['xter', 'xxl', 'fool', 'roll', 'turtle']
    >>> front_x(["cooper","lopez","xavier"])
    ['xavier', 'cooper', 'lopez']
    >>> front_x(["xyz","google","arabic"])
    ['xyz', 'arabic', 'google']
    >>> front_x(["root","trees","leaf"])
    ['leaf', 'root', 'trees']
    """
    new_list = []
    new_list_x = []
    for k in some_list:
        #print(k)
        if k.find("x") == 0:
            #print(k.find("x"))
            new_list_x.append(k) 
        else:
            new_list.append(k)
    return sorted(new_list_x) + sorted(new_list)

def even_only(some_list):
    # This function will take a list of integer and return a list of even number in original list.
    """
    >>> even_only([1,2,3,4,5])
    [2, 4]
    >>> even_only([6,5,4,3,2,1])
    [6, 4, 2]
    >>> even_only([9,2,4,1,1,0,5])
    [2, 4, 0]
    >>> even_only([8,8,8,8,8,1,6])
    [8, 8, 8, 8, 8, 6]
    >>> even_only([-6,10,241,-3,10000])
    [-6, 10, 10000]
    """
    new_list = []
    for d in some_list:
        if d%2 == 0: # if it even add in new list.
            new_list.append(d)
    return new_list

def love(some_text):
    #This function will take a text and change the secound last word to "love".
    """
    >>> love("Hello! my name is Momo and I like dog.")
    'Hello! my name is Momo and I love dog.'
    >>> love("John really like sushi.")
    'John really love sushi.'
    >>> love("Rat doesn't like cheese.")
    "Rat doesn't love cheese."
    >>> love("look like love")
    'look love love'
    >>> love("I hate egg")
    'I love egg'
    """
    sentence = some_text.split()
    #print(sentence)
    sentence[-2] = "love"
    new_text = " ".join(sentence)
    #print(new_text)
    return new_text

def is_anagram(a,b):
    #rhis function will take 2 text and check if they are anagrams return True, if they're not return False.
    """
    >>> is_anagram("Rollerblade","Papaya")
    False
    >>> is_anagram("Blade Runner","dunber laner")
    True
    >>> is_anagram("Police","Liocep")
    True
    >>> is_anagram("Lorex watch","Soldier")
    False
    >>> is_anagram("Marvel","DC")
    False
    """
    list_ch_a,list_ch_b = [],[]
    for ch in a:
        if ch != " ":
            list_ch_a += ch.lower()
    for ch in b:
        if ch != " ":
            list_ch_b += ch.lower()
    if sorted(list_ch_a) == sorted(list_ch_b):
        return True
    else:
        return False

def has_duplicates(some_list):
    # This function will take a list and check is some element appears more than 1 time return True, If not return False.
    """
    >>> has_duplicates([1,2,3,4,5])
    False
    >>> has_duplicates([1,4,6,2,7,8,1])
    True
    >>> has_duplicates([2,5,3,6,4,7])
    False
    >>> has_duplicates([1])
    False
    >>> has_duplicates([23,47,40,61,98,11,57,21,40])
    True
    """
    check = False
    for e in some_list:
        for i in range(len(some_list)):
            #print("{0:>3} {1:<3}".format(f"{e}",f"{some_list[i]}"),end="")
            if e == some_list[i] and some_list.index(e) != i:
                check = True
            else:
                pass
        #print("")
    return check

def average(some_list):
    # This function will take a list and return average of value of element in list.
    """
    >>> average([0,1,2,3,4])
    2.0
    >>> average([4,2,1,0,3])
    2.0
    >>> average([3,3,3])
    3.0
    >>> average([9,1,2,7,8])
    5.4
    >>> average([3,7,0,1,0,0,0,0])
    1.375
    """
    result = 0 # Define result to contain sum of element in list.
    for i in some_list:
        result += i 
    return result/len(some_list)

def centered_average(some_list):
    # Tihs funstion will return average value of list but ignore the largest and smallest number.
    """
    >>> centered_average([1,2,3,4,5])
    3.0
    >>> centered_average([3,5,1,4,2])
    3.3333333333333335
    >>> centered_average([2,2,2,2])
    2.0
    >>> centered_average([4,7,1,8,13,5])
    7.25
    >>> centered_average([67,21,34,52])
    27.5
    """
    sorted(some_list)
    some_list.remove(some_list[0])
    some_list.remove(some_list[-1])
    result = 0
    for i in some_list:
        result += i 
    return result/len(some_list)

def reverse_pair(some_text):
    #This function will return the reverse pair of input sentence.
    """
    >>> reverse_pair("I am your father")
    'father your am I'
    >>> reverse_pair("Lion king")
    'king Lion'
    >>> reverse_pair("Rotten tomato")
    'tomato Rotten'
    >>> reverse_pair("Oscar goes to")
    'to goes Oscar'
    >>> reverse_pair("May the sleep be with you")
    'you with be sleep the May'
    """
    list_text = some_text.split(" ")
    list_text.reverse()
    return " ".join(list_text)

def match_ends(some_list):
    # This function will take a list return number of string in list that have at least 2 char and the first and last char is the same
    """
    >>> match_ends(["lol","bone","pop"])
    2
    >>> match_ends(["yolo","toro","ratatar"])
    1
    >>> match_ends(["diamond","array","O","olo","hanah"])
    3
    >>> match_ends(["troop"])
    0
    >>> match_ends(["gang","ster"])
    1
    """
    num = 0
    for e in some_list:
        if len(e) >= 2:
            if e[0].lower() == e[-1].lower():
                num += 1
    return num

def remove_adjacent(some_list):
    # This function will reduce element that have the same value next to it to single element.
    """
    >>> remove_adjacent([1,2,2,3,3,4])
    [1, 2, 3, 4]
    >>> remove_adjacent([0,1,0,1,0])
    [0, 1, 0, 1, 0]
    >>> remove_adjacent([8,8,9,2,1,1,3,4,5,5])
    [8, 9, 2, 1, 3, 4, 5]
    >>> remove_adjacent([0,0,"fish","fish",1,2])
    [0, 'fish', 1, 2]
    >>> remove_adjacent([2,3,5,1,2])
    [2, 3, 5, 1, 2]
    """
    bucket = []
    for i in range(len(some_list)):
        try:
            #print("{0:>3}-{1:<3}".format(f"{some_list[i]}",f"{some_list[i+1]}"),end="")
            if some_list[i] == some_list[i+1]:
                bucket.append(some_list[i])
                #print("same!!",end="")
        except:
            pass
        #print("")
    for j in bucket:
        some_list.remove(j)
    return some_list



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)