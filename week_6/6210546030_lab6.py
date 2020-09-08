

def ll_sum(list_in_list):
    '''
    This function will gonna sum all the inlist member that is
    list in list and return the value in int by using only one parameter
    'list_in_list'(list that have list inside)

    >>> ll_sum([[1,2],[3],[4,5,6]])
    21
    >>> ll_sum([[3,4],[7],[8,1,9]])
    32
    >>> ll_sum([[6,2,5],[3,4],[4,5,6]])
    35
    >>> ll_sum([[1],[3],[5]])
    9
    >>> ll_sum([[1,2],[3,4],[5,6]])
    21
    '''
    list_new = []
    for i in list_in_list:
        a = sum(i)
        list_new.append(a)
    return(sum(list_new))

def cumulative_sum(list_number):
    '''
    This function will gonna return the list by each character is 
    the cumulative sum from their front number by using only one
    parameter 'list_number'(list of the number)

    >>> cumulative_sum([1,5,6])
    [1, 6, 12]
    >>> cumulative_sum([2,8,9])
    [2, 10, 19]
    >>> cumulative_sum([2,4,6,8])
    [2, 6, 12, 20]
    >>> cumulative_sum([3,6,7,8,9,10])
    [3, 9, 16, 24, 33, 43]
    >>> cumulative_sum([1,2,3,4,5,6,7,8,9])
    [1, 3, 6, 10, 15, 21, 28, 36, 45]
    '''
    list_new = []
    new2 = []
    for i in list_number:
        list_new.append(i)
        a = sum(list_new)
        new2.append(a)
    return new2


def middle(list_number):
    '''
    This function will gonna return the list of number except the
    first index and last index by using only one parameter
    'list_number'(list of number)

    >>> middle([2,4,7])
    [4]
    >>> middle([1,2,5,7,8,9])
    [2, 5, 7, 8]
    >>> middle([9,8,7,4,5,6,1,2])
    [8, 7, 4, 5, 6, 1]
    >>> middle([4,5,6,7])
    [5, 6]
    >>> middle([11,15,46,7,8])
    [15, 46, 7]
    '''
    timing = 0
    list_new = []
    for i in list_number:
        len_num= len(list_number)
        if timing>0 and timing<len_num-1:
            list_new.append(i)
        timing +=1
    return list_new

def chop(list_number):
    '''
    This is just the same as the "middle()" but it only cut but not return
    the value. It require to call the function first then print the value
    outside the function
    Ex. a = chop([1,2,3])
        print(a)->[2]

    >>> a = [1,2,3,4] ;chop(a) ;print(a)
    [2, 3]
    >>> a = [1,5,6,7,8] ;chop(a) ;print(a)
    [5, 6, 7]
    >>> a = [7,8,9,5,6,2] ;chop(a) ;print(a)
    [8, 9, 5, 6]
    >>> a = [10,11,12,15,6] ;chop(a) ;print(a)
    [11, 12, 15]
    >>> a = [78,9,5,1,2] ;chop(a) ;print(a)
    [9, 5, 1]
    '''
    list_number.pop(0)
    list_number.pop(-1)

def is_sorted(list_number):
    '''
    This function gonna check the list that this list is sorted or not
    if it sorted return true but if not return false by using only one 
    parameter 'list number'(list of number)

    >>> is_sorted([1,2,3,4,5])
    True
    >>> is_sorted([8,7,5,9])
    False
    >>> is_sorted([7,4,5,6])
    False
    >>> is_sorted([1,2,4,5])
    True
    >>> is_sorted([5,6,8,7,9])
    False
    '''
    sort_list = []
    for i in list_number:
        sort_list.append(i)
    sort_list.sort()
    if sort_list == list_number:
        return True
    else:
        return False


def front_x(list_text):
    '''
    This function gonna sort the text function but it gonna append string
    with 'x' is the first character append in the front and all the string 
    eventhough the 'x'string is all sorted using only one parameter 
    'list_text'(list of text)

    >>> front_x(['apple','income','bubble','xerath'])
    ['xerath', 'apple', 'bubble', 'income']
    >>> front_x(['ball','wave','bang','xayah'])
    ['xayah', 'ball', 'bang', 'wave']
    >>> front_x(['gragas','rekneton','jhin','xborg','xanadu'])
    ['xanadu', 'xborg', 'gragas', 'jhin', 'rekneton']
    >>> front_x(['leona','lulu','malphite','kogmaw','xerox','xylophone'])
    ['xerox', 'xylophone', 'kogmaw', 'leona', 'lulu', 'malphite']
    >>> front_x(['zonya','xpeke','back','door'])
    ['xpeke', 'back', 'door', 'zonya']
    '''
    sort_list = []
    unsort_list = []
    for i in list_text:
        if 'x' in i[0].lower() :
            sort_list.append(i)
            sort_list.sort()
        else:
            unsort_list.append(i)
            unsort_list.sort()
    return sort_list+unsort_list

def even_only(list_number):
    '''
    This function return only even number in the list using only 
    one parameter 'list_number'(list of number) 

    >>> even_only([1,2,3,4,5,6,7,8,9,10])
    [2, 4, 6, 8, 10]
    >>> even_only([22,25,23,24,28,30])
    [22, 24, 28, 30]
    >>> even_only([31,33,35,36])
    [36]
    >>> even_only([87,88,89,90])
    [88, 90]
    >>> even_only([56,40,38])
    [56, 40, 38]
    '''
    odd_list = []
    even_list = []
    for i in list_number:
        if i%2 !=0:
            odd_list.append(i)
        else:
            even_list.append(i)
    return even_list


def love(text):
    '''
    This function gonna change the second last index character to 'love'
    by using only one parameter 'text'

    >>> love('Indeed a wise choice')
    'Indeed a love choice'
    >>> love('The unseen blade is the deadliest')
    'The unseen blade is love deadliest'
    >>> love('Dont you trust me')
    'Dont you love me'
    >>> love('Fear the assassin with no master')
    'Fear the assassin with love master'
    >>> love('Nothing can hold me back')
    'Nothing can hold love back'
    '''
    split_text = text.split(' ')
    list_new = []
    for i in split_text:
        list_new.append(i)
    list_new.pop(-2)
    list_new.insert(-1,'love')
    return ' '.join(list_new)

def is_anagram(a,b):
    '''
    This function gonna check that this is anagram or not if it's anagram
    it gonna return True otherwise return False by using two parameter
    'a'(The compared text) and 'b'(The anagram)

    >>> is_anagram('karma','ARkam') 
    True
    >>> is_anagram('Alistar','Star Ali')
    True
    >>> is_anagram('Camille','Maille')
    False
    >>> is_anagram('maoKai','kaioMn')
    False
    >>> is_anagram('Grave','G R a V e')
    True
    '''
    a.lower()
    list_a,list_b = [],[]
    for i in a:
        list_a.append(i.lower())
    for i in b:
        if i != ' ':
            list_b.append(i.lower())
    list_a.sort()
    list_b.sort()
    if list_a == list_b:
        return True
    else:
        return False

def has_duplicates(list_number):
    '''
    This function gonna find that this list has the duplicate number
    or not if it has return True, else return False by using one parameter
    'list_number'(list of number) 

    >>> has_duplicates([1,2,3,5,5,6])
    True
    >>> has_duplicates([5,4,3,2,1,1])
    True
    >>> has_duplicates([9,8,7,65,])
    False
    >>> has_duplicates([8,9,0])
    False
    >>> has_duplicates([5,5,5,5])
    True
    '''
    idex = 1
    list_number.sort()
    count = 0
    while idex < len(list_number):
        if list_number[idex-1] == list_number[idex]:
            count+=1
        idex += 1
    
    if count >= 1:
        return True
    else:
        return False

def average(a):
    '''
    This function calculate the average value in list by using one 
    parameter 'a'(list_of_number)

    >>> average([4,5,6])
    5.0
    >>> average([10,10,10,10,10,10])
    10.0
    >>> average([1,2,3,3,2,1])
    2.0
    >>> average([7,8,2,5,4,3])
    4.833333333333333
    >>> average([6,8,7,9])
    7.5
    '''
    count = 0
    list_new = []
    for i in a:
        if type(i)==int:
            list_new.append(i)
            count+=1
    return sum(list_new)/count
        


def centered_average(a):
    '''
    This function calculate the average only the second to the second last
    number(centered average) by using only one parameter 'a'(list of number)

    >>> centered_average([10,20,30,40,50])
    30.0
    >>> centered_average([80,79,56,200])
    79.5
    >>> centered_average([1,3,5,2,4,6])
    3.5
    >>> centered_average([56,47,20,23,80])
    42.0
    >>> centered_average([9,8,7,6,5,4,3,2,1])
    5.0
    '''
    a.sort()
    count = 0
    list_new=[]
    list_newer =[]
    for i in a:
        list_new.append(i)
    for num in list_new:
        if num != list_new[0] and num != list_new[-1]:
            list_newer.append(num)
            count+=1
    return sum(list_newer)/count


def reverse_pair(text):
    '''
    This function gonna print out the reverse sentence
    by using only one parameter 'text'(sentence)

    >>> reverse_pair('Time to troll')
    'troll to Time'
    >>> reverse_pair('Embrace the darkness')
    'darkness the Embrace'
    >>> reverse_pair('Only you can hear me summoner')
    'summoner me hear can you Only'
    >>> reverse_pair('Dead man walkin')
    'walkin man Dead'
    >>> reverse_pair('If you buying Im in')
    'in Im buying you If'
    '''
    split_text = text.split(' ')
    list_new =[]
    for i in split_text:
        list_new.append(i)
    list_new.reverse()
    return ' '.join(list_new)

def match_ends(text):
    '''
    This function count the text which character more than two 
    and the string has the same character at the front and the last
    by using only one parameter 'text'(list of text)

    >>> match_ends(['loom','kok','Ganging'])
    2
    >>> match_ends(['stone','yey','wow','gong'])
    3
    >>> match_ends(['Rock','Solid','pop'])
    1
    >>> match_ends(['Embrace','lol'])
    2
    '''
    count = 0
    for i in text:
        if len(i) > 2:
            if i[0].lower() == i[-1].lower():
                count +=1
    return count
    
def remove_adjacent(t):
    '''
    This function remove the adjacent number in list by using only
    one parameter 't'(list of number)

    >>> remove_adjacent([1,2,2,3,3])
    [1, 2, 3]
    >>> remove_adjacent([2,2,2,3,8])
    [2, 3, 8]
    >>> remove_adjacent([9,8,7,6,6])
    [9, 8, 7, 6]
    >>> remove_adjacent([1,2,3,4,4])
    [1, 2, 3, 4]
    >>> remove_adjacent([7,8,8,8])
    [7, 8]
    '''
    list_new = []
    index = 0
    count = 0
    list_newer = []
    for i in t:
        list_new.append(i)
        count +=1
        if count >=1:
            if list_new[index] != list_new[index-1]:
                list_newer.append(i)
        index +=1
    if list_new[0] != list_newer[0]:
        list_newer.insert(0,list_new[0])
    return list_newer
  



    

        
        

    





            



    
