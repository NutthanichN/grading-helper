

def ll_sum(t):
    """function that takes a list of lists of integers and adds up the elements from all of the
nested lists.
    >>> ll_sum([[1,2],[3],[4,5,6]])
    21
    >>> ll_sum([[1,2,3,4,5,6],[7,8]])
    36
    >>> ll_sum([[1,2,3,4,5,6],[7,8,9],[2]])
    47
    >>> ll_sum([[7,8,5,4]])
    24
    >>> ll_sum([[700,8,5,4]])
    717
    """
    s=0
    
    for i in t:
        s=s+sum(i)
    return s

def cumulative_sum(t):
    """function that takes a list of numbers and returns the cumulative sum; that is, a new list where the ith element is the sum of the first i + 1 elements from the original list.
    >>> cumulative_sum([1,2,3])
    [1, 3, 6]
    >>> cumulative_sum([4,5,6])
    [4, 9, 15]
    >>> cumulative_sum([7,8,9])
    [7, 15, 24]
    >>> cumulative_sum([700,800,900])
    [700, 1500, 2400]
    >>> cumulative_sum([720,3,4,5,6,7])
    [720, 723, 727, 732, 738, 745]
    """
    total=0
    s=[]
    for i in t:
        total += i
        s.append(total)
    return s

def middle(t):
    """function  that takes a list and returns a new list that contains all but the first and last elements
    >>> middle([1,2,3,4])
    [2, 3]
    >>> middle([1,2,3,4,5])
    [2, 3, 4]
    >>> middle([300,2,4,5,7,1])
    [2, 4, 5, 7]
    >>> middle(["k","k","u","e","a","a"])
    ['k', 'u', 'e', 'a']
    >>> middle([3,4,5,6,7,8,9,0])
    [4, 5, 6, 7, 8, 9]
    """
    new_t=t[1:-1]
    return new_t

def chop(t):
    """function that takes a list, modifies it by removing the first and last elements, and returns None.
    >>> t=[1,2,3,4]
    >>> chop(t)
    >>> t
    [2,3]
    >>> t=["k","u","e","a"]
    >>> chop(t)
    >>> t
    ['u', 'e']
    >>> t=["k","k","u","e","a","a"]
    >>> chop(t)
    >>> t
    ['k', 'u', 'e', 'a']
    >>> t=[2,4,5,6,7,8,9]
    >>> chop(t)
    >>> t
    [4, 5, 6, 7, 8]
    >>> t=['t',2,4,5,6,7,8,9,10000]
    >>> chop(t)
    >>> t
    [2, 4, 5, 6, 7, 8, 9]
    """
    t.remove(t[0])
    t.remove(t[-1])

def is_sorted(t):
    """function that takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise.
    >>> is_sorted([1,2,2])
    True
    >>> is_sorted(['b','a'])
    False
    >>> is_sorted([1,2,4,3])
    False
    >>> is_sorted([1,2,3,4])
    True
    >>> is_sorted(["a","bbb","cc","ddd","c"])
    False
    """
    
    new_t=t[:]
    new_t.sort()
    if new_t==t:
        return True
    else:
        return False


def front_x(t):
    """function that returns a list with the strings in sorted order, except group all the strings that begin with 'x' first.
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    >>> front_x(['mix', "mixer","kuea","aaa"])
    ['aaa', 'kuea', 'mix', 'mixer']
    >>> front_x(['mix', "mixer","kuea","aaa","x"])
    ['x', 'aaa', 'kuea', 'mix', 'mixer']
    >>> front_x(['mix', "mixer","kuea","aaa","x","xander"])
    ['x', 'xander', 'aaa', 'kuea', 'mix', 'mixer']
    >>> front_x(['mix', "mixer","kuea","aaa","x","xander","xxx","xx"])
    ['x', 'xander', 'xx', 'xxx', 'aaa', 'kuea', 'mix', 'mixer']

    """
    xslot=[]
    new=[]
    for i in t:
        if i[0]=="x":
            xslot.append(i)
        
        else:
            new.append(i)    
    xslot.sort()       
    new.sort()
    xslot =xslot+new
    return xslot
def even_only(list):
    """a function that will take a list of integers, and return a new list with only even numbers.
    >>> even_only([3,1,4,1,5,9,2,6,5])
    [4, 2, 6]
    >>> even_only([3,1,4])
    [4]
    >>> even_only([2,4,6,8,10,11])
    [2, 4, 6, 8, 10]
    >>> even_only([1])
    []
    >>> even_only([1,3,4,5,7,9,11])
    [4]
    """
    new=[]
    for i in list:
        if i%2==0:
            new.append(i)
    return new

def love(text):
    """function that will change the second last word to “love”
    >>> love("I like Python")
    "I love Python”
    >>> love("I really like Python")
    "I really love Python"
    >>> love("everyone like python")
    everyone love python
    >>> love("kuea really like econ")
    kuea really love econ
    >>> love("econ like kuea")
    econ love kuea
    """
    text_split=text.split('like')
    text_split.insert(1,'love')
    return "".join(text_split)

def is_anagram(a,b):
    """function that takes two strings and returns True if they are anagrams.
    >>> is_anagram('arrange', 'Rear Nag')
    True
    >>> is_anagram('nag','agn')
    True
    >>> is_anagram("kuea","aeuk")
    True 
    >>> is_anagram("kuea","g10")
    False
    >>> is_anagram("kuea","god")
    False
    """
    new_a=a.lower()
    new_b=b.lower()
    new_a2=new_a.split(" ")
    new_b2=new_b.split(" ")
    new_a3="".join(new_a2)
    new_b3="".join(new_b2)
    new_a4=sorted(new_a3)
    new_b4=sorted(new_b3)
    if new_a4==new_b4:
        return True
    else:
        return False

def has_duplicates(t):
    """a function that takes a list and returns True if there is any element that appears more than once. It should not modify the original list.
    >>> has_duplicates([1, 2, 3, 4, 5])
    False
    >>> has_duplicates([1, 2, 3, 4, 5, 2])
    True
    >>> has_duplicates([1, 2, 3, 4, 5,23,44])
    False
    >>> has_duplicates([1, 2, 3, 4, 5,23,44,1])
    True
    >>> has_duplicates([1, 2, 3, 4, 5,23,44,1,1,22])
    True
    """
    d=set()
    for i in t:
        if i in d: return True
        d.add(i)
    return False

def average(nums):
    """function average(nums) that returns the mean average of a list of numbers.
    >>> average([1, 1, 5, 5, 10, 8, 7])
    5.285714285714286
    >>> average([1,2,3,4])
    2.5
    >>> average([1,2,3])
    2.0
    >>> average([2,2,2])
    2.0
    >>> average([2,200000000,2])
    66666668.0
    """
    average=0
    average=sum(nums)
    average=average/len(nums)
    return average

def centered_average(nums):
    """function that returns a "centered" average of a list of numbers, which is the mean average of the values that ignores the largest and smallest values in the list. If there are multiple copies of the smallest/largest value,
    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([1, 1, 5, 5, 10, 8, 7,11])
    6.0
    >>> centered_average([1,5,4,3,2,1,2])
    2.4
    >>> centered_average([1,20,30,30,40,10000])
    30.0
    >>> centered_average([1,20,30,30,40,1000000000000000000000])
    30.0
    """
    total=0.00
    nums.sort()
    new_nums=nums[1:-1]
    total=sum(new_nums)
    total=total/len(new_nums)
    return total
    
def reverse_pair(t):
    """function that returns the reverse pair of the input sentence.
    >>> reverse_pair("May the fourth be with you")
    you with be fourth the May
    >>> reverse_pair("Kuea love bear")
    bear love Kuea
    >>> reverse_pair("hello o oo")
    oo o hello
    >>> reverse_pair("zoon zoon pad pang")
    pang pad zoon zoon
    >>> reverse_pair("I really like Python")
    Python like really I
    """
    reverse_t =[]
    t=t.split()
    reverse_t=t[::-1]
    return " ".join(reverse_t)

def match_ends(t):
    """function that returns the count of thenumber of strings where the string length is 2 or more and the first and last chars of the string are the same.
    >>> match_ends(["Gingering", "hello","wow"])
    2
    >>> match_ends(["wow"])
    1
    >>> match_ends(["how are youw", "hi"])
    0
    >>> match_ends(["hoh", "hi h"])
    2
    >>> match_ends(["Kuea"])
    0
    """
    count=0
    for i in t:
        if len(i)>=2:
            if i.lower()[0]==i.lower()[-1]:
                count+=1
    return count

def remove_adjacent(t):
    """function that returns a list where all adjacent elements have been reduced to a single element.
    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([1, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([1, 2, 3, 3,6 ,4 ,4 ,5, 6 ,7])
    [1, 2, 3, 6, 4, 5, 6, 7]
    >>> 

    >>> remove_adjacent([1,1,1,1])
    [1]
    """

    new_t=[]
    dup = None
    for i in t:
        if i !=dup:
            new_t.append(i)
        dup=i
    return new_t
# remove_adjacent([1,10,9,6,7])
