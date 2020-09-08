

#####################################Lab_6#######################################################
def ll_sum(a):
    """
    takes a list of lists of integers and adds up the elements from all of the nested lists.
    >>> t = [[1,2],[3],[4,5,6]]
    >>> ll_sum(t)
    21
    >>> t = [[3,5],[1,2],[1,4,6]]
    >>> ll_sum(t)
    22
    >>> t = [[10,0],[0]]
    >>> ll_sum(t)
    10
    >>> t = [[4,6],[0,3],[1,2,3,4,5]]
    >>> ll_sum(t)
    28
    >>> t = [[1000,4]+[10.2]+[1]]
    >>> ll_sum(t)
    1015.2
    """
    B=0
    for i in range(len(a)):
        A=a[i]
        B +=sum(A)
    return B
#################################################################################################
def cumulative_sum(a):
    '''
    takes a list of numbers and returns the cumulative sum
    >>> c=[1,2,3]
    >>> cumulative_sum(c)
    [1, 3, 6]
    >>> c=[2,4,6]
    >>> cumulative_sum(c)
    [2, 6, 12]
    >>> c=[10,1,0]
    >>> cumulative_sum(c)
    [10, 11, 11]
    >>> c=[101,101,101]
    >>> cumulative_sum(c)
    [101, 202, 303]
    >>> c=[5,4,3]
    >>> cumulative_sum(c)
    [5, 9, 12]
    '''
    for i in range(len(a)):
        if i !=0:
            A=a[i]+a[i-1]
            a[i]=A
    return a
#################################################################################################
def middle(N):
    '''
     returns a new list that contains all but the first and last elements are removing.
    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    >>> t = [2,1,3,4]
    >>> middle(t)
    [1, 3]
    >>> t =[10,50,31,5]
    >>> middle(t)
    [50, 31]
    >>> t =[0]
    >>> middle(t)
    'need more than 2'
    >>> t =[1,2,4]
    >>> middle(t)
    [2]
    '''
    New = N
    if len(New)<=2:
        return "need more than 2"
    else:
        New[0:1]=[]
        New[len(New)-1:len(New)]=[]
        return New
#################################################################################################
def chop(O):
    '''
    removing the first and last elements in same list, and returns None.
    >>> t=[1,2,3,4]
    >>> chop(t)
    >>> print(t)
    [2, 3]
    >>> t=[1,2,3,4,5,6]
    >>> chop(t)
    >>> print(t)
    [2, 3, 4, 5]
    >>> t=[1,2]
    >>> chop(t)
    >>> print(t)
    [1, 2]
    >>> t=[1,3,5]
    >>> chop(t)
    >>> print(t)
    [3]
    >>> t=[50,15,30,45]
    >>> chop(t)
    >>> print(t)
    [15, 30]
    '''
    if len(O)<=2:
        return
    O[0:1]=[]
    O[len(O)-1:len(O)]=[]
    return
#################################################################################################
def is_sorted(C):
    '''
    returns True if the list is sorted in ascending order and False otherwise.
     >>> is_sorted([1, 2, 2])
     True
     >>> is_sorted(['b', 'a'])
     False
     >>> is_sorted([10,9,8])
     False
     >>> is_sorted(['abc','bcd'])
     True
     >>> is_sorted([10.1,10.2,10.3])
     True
    '''
    A=sorted(C)
    if A==C:
        return True
    return False
#################################################################################################
def front_x(A):
    '''
    returns a list with the strings in sorted order, except group all the strings that begin with 'x' first.
    >>> l = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
    >>> front_x(l)
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    >>> l = ['abcd','cab','xyx','bac']
    >>> front_x(l)
    ['xyx', 'abcd', 'bac', 'cab']
    >>> l = ['abc','bac','cba']
    >>> front_x(l)
    ['abc', 'bac', 'cba']
    >>> l = ['xay','xba','xqa','x']
    >>> front_x(l)
    ['x', 'xay', 'xba', 'xqa']
    >>> l = ['abc','abc','xyz']
    >>> front_x(l)
    ['xyz', 'abc', 'abc']
    '''
    x=[]
    no_x=[]
    for i in A:
        if i[0]=="x":
            x.append(i)
        else:
            no_x.append(i)
    x.sort()
    no_x.sort()
    return x+no_x
#################################################################################################
def even_only(E):
    '''
    return a new list with only even numbers.
    >>> even_only([3,1,4,1,5,9,2,6,5])
    [4, 2, 6]
    >>> even_only([1,3,5,7,9,11,13,45])
    []
    >>> even_only([2,3,4,5,6,8,9])
    [2, 4, 6, 8]
    >>> even_only([11,22,33,44,55])
    [22, 44]
    >>> even_only([-21,-22,-24,-25])
    [-22, -24]
    '''
    A=[]
    for i in E:
        if i %2==0:
            A+=[i]
    return A
#################################################################################################
def love(V):
    '''
    this function that will change the second last word to “love”.
    >>> love("I like Python")
    'I love Python'
    >>> love("I really like Python")
    'I really love Python'
    >>> love("I like everyone")
    'I love everyone'
    >>> love("I hate you")
    'I love you'
    >>> love("She love him")
    'She love him'
    '''
    Point=[]
    for i in range(len(V)):
        if V[i-1] ==" ":
            Point+=[i]
    A=(Point[len(Point)-2])
    B=(Point[len(Point)-1])
    C=V[A:B-1]
    V=V.replace(C,'love')
    return V
#################################################################################################
def is_anagram(a,b):
    '''
    takes two strings and returns True if they are anagrams.
    >>> is_anagram('arrange', 'Rear Nag')
    True
    >>> is_anagram('mark','a r k')
    False
    >>> is_anagram('piggr','gg rip')
    True
    >>> is_anagram('mark','')
    False
    >>> is_anagram('P i c','C o p')
    False
    '''
    a=a.lower()
    b=b.lower()
    for i in a:
        if i in b:
            C=True
        else:
            return False
    return C
#################################################################################################
def has_duplicates(N):
    '''
    returns True if there is any element that appears more than once.
    >>> has_duplicates([1, 2, 3, 4, 5])
    False
    >>> has_duplicates([1, 2, 3, 4, 5, 2])
    True
    >>> has_duplicates([10,-10,11,-11,12,-12])
    False
    >>> has_duplicates([1101,1110,1001,1000])
    False
    >>> has_duplicates([1,1,2,2,3,3,4,4,5,5,6,6])
    True
    '''
    for i in range(len(N)):
        if N[i] in N[0:i]+N[i+1:]:
            return True
        else:
            C=False
    return C
#################################################################################################
def average(nums):
    '''
    returns a average of a list of numbers.
    >>> average([1, 1, 5, 5, 10, 8, 7])
    5.285714285714286
    >>> average([1,1,1,1,1,1,1])
    1.0
    >>> average([4,8,16,32.1,4,7])
    11.85
    >>> average([5,7,9,11,55,44])
    21.833333333333332
    >>> average([100,-300,55,-31,44,79,87,9,46,48,21,34,-6])
    14.307692307692308
    '''
    Sum=0
    for i in range(len(nums)):
        A=nums[i]
        Sum+=A
    aver=Sum/len(nums)
    return aver
#################################################################################################
def centered_average(nums):
    '''
    returns a average of a list of numbers,that ignores the largest and smallest values in the list.
    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([4,3,7,5,7,6,4,5,6])
    5.285714285714286
    >>> centered_average([1,1,1,1,1,1,1])
    1.0
    >>> centered_average([100,0,4,5,6,7,8])
    6.0
    >>> centered_average([1,1,2,2])
    1.5
    '''
    Sum=0
    nums.sort()
    nums[0:1]=[]
    nums[len(nums)-1:len(nums)]=[]
    for i in range(len(nums)):
        A = nums[i]
        Sum += A
    aver = Sum / len(nums)
    return aver
#################################################################################################
def reverse_pair(W):
    '''
    returns the reverse pair of the input sentence.
    >>> reverse_pair("May the fourth be with you")
    'you with be fourth the May'
    >>> reverse_pair("the sun and the moon")
    'moon the and sun the'
    >>> reverse_pair("and")
    'and'
    >>> reverse_pair("like or love")
    'love or like'
    >>> reverse_pair("Oo oO ooO Ooo")
    'Ooo ooO oO Oo'
    '''
    R=W.split(" ")
    R.reverse()
    R_S=(" ").join(R)
    return R_S
#################################################################################################
def match_ends(W):
    '''
    returns the count of the number of strings where the string length is 2 or more and the first and last
    chars of the string are the same.
    >>> match_ends(["Gingering","hello","wow"])
    2
    >>> match_ends(["Engineer","lol","A"])
    1
    >>> match_ends(["mo","me","mon"])
    0
    >>> match_ends(["qooq","mind","Pop","Ana"])
    3
    >>> match_ends(["202","sister","my","101"])
    2
    '''
    sum=0
    for i in W:
        if len(i)>1:
            if i[0].lower()==i[-1].lower():
                sum+=1
    return sum
#################################################################################################
def remove_adjacent(S):
    '''
    returns a list where all adjacent elements have been reduced to a single element.
    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([1,4,5,6])
    [1, 4, 5, 6]
    >>> remove_adjacent([3,5,5,7,9,5,])
    [3, 5, 7, 9]
    >>> remove_adjacent([1,1,1])
    [1]
    >>> remove_adjacent([-1,1,-2,2,3,3,4,-4])
    [-1, 1, -2, 2, 3, 4, -4]
    '''
    for i in range(len(S)-1):
        if S[i] in S[0:i]+S[i+1:]:
            S[i:i+1]=[]
    return S
#################################################################################################
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)






