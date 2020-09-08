

import math,sys
# def ll_sum(slist):
#     sum=0
#     if type(slist)!=list and (type(slist) == int or type(slist) == float):
#             sum += slist
#             return sum
#     elif type(slist) == list:
#         for ch in range(len(slist)):
#             sum+= ll_sum(slist[ch])
            
#     return sum
# print(ll_sum([1,[2,3]]))

def ll_sum(lis):  
    """This function will return sum of the component in list also the list in list
    >>> ll_sum([1,2,3])
    6
    >>> ll_sum([1,2,[3,4]])
    10
    >>> ll_sum([1,2,1,[1,2,3],[3],1])
    14
    >>> ll_sum([2,3,4,5,[2,3,4]])
    23
    >>> ll_sum([12,[1,2,3],[12,3],2])
    35
    """
    result = 0
    for i in range(len(lis)):
        if type(lis[i]) == list:
            
            for j in range(len(lis[i])):
                result+= lis[i][j]
        elif type(lis[i]) == int or type(lis[i]) == float:
            result += lis[i] 
            
    return result
# print(ll_sum([1,[2,3],2,3,[4,5,6,7]]))
# my_list = [ [ "ske", 11 ], [ "cpe", 27 ] ]
# print(my_list)
# print(my_list[1])
# print(my_list[1][0])
# print(my_list[1][0][-2])

def cumulative_sum(lis):
    """This function will return the changed value in each list to be Sum of each in front
    >>> cumulative_sum([1,2,3])
    [1, 3, 6]
    >>> cumulative_sum([1,2])
    [1, 3]
    >>> cumulative_sum([1,2,3,4])
    [1, 3, 6, 10]
    >>> cumulative_sum([2,2,2])
    [2, 4, 6]
    
    >>> cumulative_sum([3,2,1])
    [3, 5, 6]
    """
    result = 0
    for i in range(len(lis)):
        real_list_value = lis[i]
        lis[i]+=result
        result += real_list_value
    return lis
# print(cumulative_sum([1,2,3]))

def middle(lis):
    """This function which return the same list that have already cut the first and last
    >>> middle([1,2,3])
    [2]
    >>> middle([1,2,3,4,5])
    [2, 3, 4]
    >>> middle(['a','b','c'])
    ['b']
    >>> middle(['a','s','dd',3,2])
    ['s', 'dd', 3]
    >>> middle(['Im','boom','puvana','yeah'])
    ['boom', 'puvana']
    """
    new = []
    for i in lis:
        if i != lis[0] and i != lis[-1]:
            new.append(i)
    return new
# print(middle([1,2,3,4,5,6,7]))

def chop(lis):
    '''This function will be cut the first and last component, however return nothing
    >>> a = [1,2,2,1]
    >>> chop(a)
    >>> a
    [2, 2]
    >>> b = [1,2,3,4]
    >>> chop(b)
    >>> b
    [2, 3]
    >>> c = [1,2,3,4,5]
    >>> chop(c)
    >>> c
    [2, 3, 4]
    >>> d = ['a','b','c','d','e']
    >>> chop(d)
    >>> d
    ['b', 'c', 'd']
    >>> e = [1,'a1','c',2]
    >>> chop(e)
    >>> e
    ['a1', 'c']
    '''
    lis.pop(0)
    lis.pop(-1)
# lis = [1,2,3,4,5]
# chop(lis)
# print(lis)

def is_sorted(lis):
    """This function return if the component have already sorted
    >>> is_sorted([1,2,2,4])
    True
    >>> is_sorted([2,3,4,1])
    False
    >>> is_sorted(['a','b','c'])
    True
    >>> is_sorted(['a','b','c','a'])
    False
    >>> is_sorted(['a','b','c','d','a','b'])
    False
    """
    sorted_list = []
    for i in  lis :
        sorted_list.append(i)
    sorted_list.sort()
    if sorted_list == lis:
        return True
    else :
        return False
    
# print(is_sorted([1,2,3,4]))
# print(is_sorted([2,3,4,1]))
# print(is_sorted(['a','b','c']))
# print(is_sorted(['a','b','c','a']))
# print(is_sorted(['a','b','c','d','a','b']))

def front_x(lis):
    """This function will put the 'x'infront component to be infront and sorted
    >>> front_x(['assdfg','dddds','xanadu','xyz'])
    ['xanadu', 'xyz', 'assdfg', 'dddds']
    >>> front_x(['mix','xyz','apple','xanadu','aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    >>> front_x(['Abc','ss','xtr','xgh'])
    ['xgh', 'xtr', 'Abc', 'ss']
    >>> front_x(['1','2','3','x'])
    ['x', '1', '2', '3']
    >>> front_x(['1','xy','3','x'])
    ['x', 'xy', '1', '3']
    """
    ans_list = []
    x_list = []
    not_x_lis = []
    for i in lis:
        if i[0] =='x' or i[0] == 'X':
            x_list.append(i)
        else:
            not_x_lis.append(i)
    not_x_lis.sort()
    x_list.sort()
    ans_list = x_list + not_x_lis
    return ans_list
# print(front_x(['assdfg','dddds','xanadu','xyz']))
# print(front_x(['mix','xyz','apple','xanadu','aardvark']))
# print(front_x(['Abc','ss','xtr','xgh']))


def even_only(lis):
    '''function return a even componant in list
    >>> even_only([1,2,3,4,5])
    [2, 4]
    >>> even_only([11,22,33,44,2])
    [22, 44, 2]
    >>> even_only([12,21,33,22])
    [12, 22]
    >>> even_only([5,4,3,2,1])
    [4, 2]
    >>> even_only([111,234,567,890])
    [234, 890]
    '''
    even_list = []
    for i in range(len(lis)):
        if lis[i]%2==0:
            even_list.append(lis[i])
    return even_list

def love(text):
    ''' function change the 'like' to 'love'
    >>> love("I am gonna die if I dont like prog")
    'I am gonna die if I dont love prog'
    >>> love("I am gonna die if I dont eat prog")
    'I am gonna die if I dont love prog'
    >>> love('Do u hate me')
    'Do u love me'
    >>> love('Do u love me')
    'Do u love me'
    >>> love('I hate girl')
    'I love girl'
    '''
    sentence = text.split(" ")
    sentence[-2] = "love"
    ans = " ".join(sentence)
    return ans
# print(love('sdfgh loves sdfghj'))

def is_anagram(a,b):
    '''check if it is a two same string by not think about space or lower/upper alphabet
    >>> is_anagram('abc','ABC')
    True
    >>> is_anagram('asdf','Asf d')
    True
    >>> is_anagram('sdf','sdfg')
    False
    >>> is_anagram('dfgh','FGdH')
    True
    >>> is_anagram('assd','ADDSS')
    False
    '''
    new_a = []
    new_b = []
    a = a.lower()
    b = b.lower()
    for i in a:
        if i in 'asdfghjklzxcvbnmqwertyuiop':
            new_a.append(i)
    for i in b:
        if i in 'asdfghjklzxcvbnmqwertyuiop':
            new_b.append(i)
    new_a = sorted(new_a)
    new_b = sorted(new_b)
    # print(a,b,new_a,new_b)
    return new_a == new_b

# print(is_anagram('sdf','sdfg'))
# print(is_anagram('asdf','Asf d'))
# print(is_anagram('abc','ABC'))
            
def has_duplicates(lis):
    '''check if it duplicated or not
    >>> has_duplicates([1,2,3,4,5,2])
    True
    >>> has_duplicates([1,2,3,4,5])
    False
    >>> has_duplicates([22,2,22,1,3,4])
    True
    >>> has_duplicates([22,2,23,1,3,4])
    False
    >>> has_duplicates([5,4,3,5,4,3])
    True
    '''
    Valid = False
    for i in range(len(lis)):
        # print(f"i = n{i}")
        for j in range(i-1):
            # print(f"i = {i} , j = {j} , {lis[i]} {lis[j]}")
            if lis[i] == lis[j]:
                Valid = True
                break
    return Valid
# print(has_duplicates([1,2,3,4,5,6,1]))

def average(lis):
    '''find the avg of the component in list
    >>> average([1,2,3,4,5])
    3.0
    >>> average([1, 1, 5, 5, 10, 8, 7])
    5.285714285714286
    >>> average([2,2,2,2,2])
    2.0
    >>> average([1,2,3,4])
    2.5
    >>> average([1.0,2.0,3.0,4.0])
    2.5
    '''
    sum = 0
    for i in lis:
        sum+=i
    avg = sum/len(lis)
    return avg
# print(average([1,2,3,4,5]))

def centered_average(lis):
    '''find the avg of the component in list (not included first and last)
    >>> centered_average([1,2,3,4,5])
    3.0
    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([2,2,2,2,2])
    2.0
    >>> centered_average([1,2,3,4])
    2.5
    >>> centered_average([1.0,2.0,3.0,4.0])
    2.5
    '''
    sum = 0
    lis= sorted(lis)
    lis.remove(lis[0])
    lis.remove(lis[-1])
    
    for i in lis:
        sum+=i
    avg = sum/len(lis)
    return avg

def reverse_pair(string):
    """This function return string that reversed
    >>> reverse_pair("a b c")
    'c b a'
    >>> reverse_pair("Boom AND")
    'AND Boom'
    >>> reverse_pair('hello python world')
    'world python hello'
    >>> reverse_pair('Samsung betterthan Apple')
    'Apple betterthan Samsung'
    >>> reverse_pair('Puvana Swatvanith')
    'Swatvanith Puvana'
    """
    new_string = string.split(" ")
    new_string.reverse()
    return (" ".join(new_string))
# print(reverse_pair("aa bb cc"))

# def remove_adjacent(lis):
#     ans = []
#     last = 'aaaaaaaaaaaa4dd4x3f6tgghh8bnjj'
#     for i in lis:
#         if i != last:
#             ans.append(i)
#             last = i
#     return ans
# print(remove_adjacent([1,0,2,2,0,1]))
# print(remove_adjacent([1,0,2,2,3,2,3,1,0,1,'fish']))
# print(remove_adjacent([1,0,2,2,3,'fish',123123,12323,332,322,233,233,2,3,1,0,1,'fish','fish']))

def match_ends(lis):
    """This function will be count how many of the string in list that have same aplhabet in first and alst
    >>> match_ends(["helloH","helloee","wow","wOOO0W"])
    3
    >>> match_ends(["helloH","helloee","wow","wOOO0Wz"])
    2
    >>> match_ends(["hsdi","dfhsfd","helloh","Gogogoeg"])
    3
    >>> match_ends(['asss','assa','cdef'])
    1
    >>> match_ends(['asasas','biob','cococ','dudddedd'])
    3
    """
    count = 0
    for i in lis:
        if i[0].upper() == i[-1].upper() and len(i)>=2:
            count += 1
    return count
# print(match_ends(["helloH","helloee","wow","wOOO0W"]))
# print(match_ends(["helloH","helloee","wow","wOOO0Wz"]))

def remove_adjacent(lis):
    '''This function make any of any component to be single
    >>> remove_adjacent([1,2,3,4,4,2,1])
    [1, 2, 3, 4, 2, 1]
    >>> remove_adjacent([1,2,1])
    [1, 2, 1]
    >>> remove_adjacent([1,0,2,2,0,1])
    [1, 0, 2, 0, 1]
    >>> remove_adjacent([1 ,0,2,2,3,2,3,1,0,1,'fish'])
    [1, 0, 2, 3, 2, 3, 1, 0, 1, 'fish']
    >>> remove_adjacent([1,2,3,4,2,1,'s','p',4,'s'])
    [1, 2, 3, 4, 2, 1, 's', 'p', 4, 's']
    '''
#     ans_list = []
#     for i in lis:
#         if i not in ans_list:
#             ans_list.append(i)
#     return ans_list

# def remove_adjacent(lis):
    ans = []
    last = 'aaaaaaaaaaaa4dd4x3f6tgghh8bnjj'
    for i in lis:
        if i != last:
            ans.append(i)
            last = i
    return ans
# print(remove_adjacent([1,2,3,4,2,1]))
# print(remove_adjacent([1,2,1]))
# print(remove_adjacent([1,0,2,2,0,1]))
# print(remove_adjacent([1 ,0,2,2,3,2,3,1,0,1,'fish']))
# print(remove_adjacent([1,2,3,4,2,1,'s','p',4,'s']))

