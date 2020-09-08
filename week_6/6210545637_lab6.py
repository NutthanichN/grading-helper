

# 1
def ll_sum(list):
    """
    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> ll_sum(t)
    21

    >>> t = [[1, 2, 6], [9], [4, 5, 6]]
    >>> ll_sum(t)
    33

    >>> t = [[1], [2,3,4],[5],[6,7]]
    >>> ll_sum(t)
    28

    >>> t=[[2,5,7],[9]]
    >>> ll_sum(t)
    23

    >>> t=[[1,10,100],[1000],[200,300]]
    >>> ll_sum(t)
    1611

    list=list of lists of integers
    this function job is to sum numbers from all of the nested lists


    """


    sum=0
    for i in range(len(list)):
        for j in range(len(list[i])):
            sum += list[i][j]
    return sum


# 2
def cumulative_sum(list):
    """
    >>> cumulative_sum([2,4,6,8])
    [2, 6, 12, 20]
    >>> cumulative_sum([1,1,1,1,1])
    [1, 2, 3, 4, 5]
    >>> cumulative_sum([100,200,300,400])
    [100, 300, 600, 1000]
    >>> cumulative_sum([2,88])
    [2, 90]
    >>> cumulative_sum([89,98,13])
    [89, 187, 200]
    >>> cumulative_sum([1])
    [1]


    list = list of number that you want to the cumulative sum of the number
    this function job is  to cumulative sum number and show it by  sum of 2 number and show it then do the same thing with another number until the last number
    """



    sum=list[0]
    for i in range(len(list)-1):
        sum+=list[i+1]
        list[i+1]=sum
    return list

# 3
def middle(list):
    """
    >>> middle([1,3,5,6,9])
    [3, 5, 6]
    >>> middle([100,200,399])
    [200]
    >>> middle([9,6,6,6,9])
    [6, 6, 6]
    >>> middle([1,1])
    []
    >>> middle([0,8,1,2,6,4,1,7,5,8])
    [8, 1, 2, 6, 4, 1, 7, 5]
    >>> middle([1])
    []



    list = list of element
    this function job is to delete first element and last element and then show it

    :return:
    """
    new = []
    if len(list)<3:
        return new
    else:
        del list[0]
        del list[-1]
        return list

# 4
def chop(list):
    """
    >>> t = [2,3,4,5]
    >>> middle(t)
    [3, 4]

    >>> t= [9,1,1,1,9]
    >>> middle(t)
    [1, 1, 1]

    >>> t=[47,4,7]
    >>> middle(t)
    [4]

    >>> t=[1,2]
    >>> middle(t)
    []

    >>> t=[1]
    >>> middle(t)
    []

    >>> t=[2,3,10,8,9]
    >>> middle(t)
    [3, 10, 8]



    list = list of element
    this function job is to remove first element and last element then return nothing

    """
    if len(list) == 1:
        del list[0]
        return None
    else:
        del list[0]
        del list[-1]
        return None

# 5
def is_sorted(list):
    """
    >>> is_sorted([1, 2, 1, 3])
    False

    >>> is_sorted([100,300,200,500])
    False
    >>> is_sorted([2,4,6,8])
    True
    >>> is_sorted([3,6,9,12,15])
    True
    >>> is_sorted(['z','x''c'])
    False
    >>> is_sorted(["a","b"])
    True

    list = list of element
    This function job is to sort the list of the element like if it is number it sorts small number to big number
    if it is character or sentence it sorts from first character to last character

    """
    b=list.copy()
    b.sort()
    if list == b:
        return True
    else:
        return False



# 6
def front_x(list):
    """
    >>> l = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
    >>> front_x(l)
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']

    >>> l = ['abccxaz','xdrake','ydragon','xzzzz']
    >>> front_x(l)
    ['xdrake', 'xzzzz', 'abccxaz', 'ydragon']

    >>> l=['a','bv','ba','xx']
    >>> front_x(l)
    ['xx', 'a', 'ba', 'bv']

    >>> l=['y', 'z', 'a' ]
    >>> front_x(l)
    ['a', 'y', 'z']

    >>> z=['x','xz','xxz','xy','xx']
    >>> front_x(z)
    ['x', 'xx', 'xxz', 'xy', 'xz']

    

    list=list of satrings
    this function job is to sort a list of strings by strings that begin with x first
    """
    ans=[]
    l=0


    for i in list:

        if i[0] == 'x':
            ans.append(list[l])
            del list[l]
        l += 1
    ans.sort()
    list.sort()
    list1=ans + list

    return list1

#7
def even_only(list):
    """
    >>> even_only([3,1,4,1,5,9,2,6,5])
    [4, 2, 6]
    >>> even_only([2,4,6,8,10])
    [2, 4, 6, 8, 10]
    >>> even_only([1,2,5,6,7])
    [2, 6]
    >>> even_only([1])
    []
    >>> even_only([10,2033,30])
    [10, 30]
    >>> even_only([66])
    [66]

    list = list of number
    this function job is to find the even number and return it in a new list

    """
    a=[]
    for i in list:
        if i%2==0:
            a.append(i)
    return a
# 8
def love(text):
    """
    >>> love("I like Python")
    'I love Python'
    >>> love('I hate U')
    'I love U'
    >>> love('I eat Hotdog')
    'I love Hotdog'
    >>> love('I really like this cake')
    'I really like love cake'
    >>> love('The dog eat Hotdog')
    'The dog love Hotdog'

    text:text
    this function job is to change the second last word to love
    """
    b = text.split()

    c=text.replace(b[-2],"love")
    return c
# 9
def is_anagram(w,w1):
    """
    >>> is_anagram('arrange', 'Rear Nag')
    True
    >>> is_anagram('a','ascasfew')
    False
    >>> is_anagram('a','aa')
    False
    >>> is_anagram('dog','d o g')
    True
    >>> is_anagram("cAT","C AT")
    True

    w=  word1
    w1= word2
    this function job is to check that two words are anagrams or not if it is, then return true else return false

    """
    w=w.lower()
    w1=w1.lower()
    w=w.replace(" ","")
    w1 = w1.replace(" ", "")
    w= sorted(w)
    w1 = sorted(w1)
    if w == w1:
        return True
    else:
        return False

#10
import sys
def has_duplicates(list):
    """
    >>> has_duplicates([1,2,3,4,5])
    False
    >>> has_duplicates([1,2,3,4,5,2])
    True
    >>> has_duplicates([1,2,1,3])
    True
    >>> has_duplicates(['a','asdqf','a'])
    True
    >>> has_duplicates(['dog','cat','zebra','dog'])
    True
    >>> has_duplicates([10,20,30])
    False

    list= list of elements
    this function job is to find any element that appears more than once
    """
    for i in range(len(list)):
        for j in range(len(list)):
            if i != j and list[i] == list[j]:
                return True
                sys.exit()
    return False

# 11
def average(list):

    """
    >>> average([1,2,3,4,5])
    3.0
    >>> average([1,1,3])
    1.6666666666666667
    >>> average([0,0,0])
    0.0
    >>> average([3,3,3,3,3])
    3.0
    >>> average([2,4,6,8,10])
    6.0

    list = list of numbers
    this function job is to find the mean average of a list of numbers and return it
    """


    ans = sum(list)/len(list)

    return ans

# 12
def centered_average(list):
    """
    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([1,2,3,4])
    2.5
    >>> centered_average([3,3,6,6,9,9])
    6.0
    >>> centered_average([1,3,5])
    3.0
    >>> centered_average([5,7,7])
    7.0

    list = list of numbers
    this function job is to find the average of the values that ignore the largest and smallest number in the list.if there are multiple copies of the smallest/largest number
    """
    max=list[0]
    min=list[0]
    for i in list:
        if i > max:
            max=i
        if i<min:
            min=i
    num=sum(list)-max-min
    return num/(len(list)-2)

# 13
def reverse_pair(text):
    """
    >>> reverse_pair("May the fourth be with you")
    'you with be fourth the May'
    >>> reverse_pair('I go to zoo')
    'zoo to go I'
    >>> reverse_pair('i want to pee')
    'pee to want i'
    >>> reverse_pair('I sit')
    'sit I'
    >>> reverse_pair('Monkey king in the sky')
    'sky the in king Monkey'

    text = sentence
    this function job is to reverse the sentence
    """
    text = text.split()
    # print(text)
    text=text[-1::-1]
    # print(text)
    output = ' '.join(text)
    # print(output)
    return output

# 14
def match_ends(list):
    """
    >>> match_ends(["Gingering", "hello","wow"])
    2
    >>> match_ends(['aa','dog','z','cat'])
    1
    >>> match_ends(['zebra','zzz','gg'])
    2
    >>> match_ends(['asx'])
    0
    >>> match_ends(['wow','xx','mamamoo'])
    2

    list = list of strings
    this function job is to count the number of strings that length is more than 2 and the first and last character of the string is the same


    """
    num=0
    for i in list:

        if len(i)>1 and i[0].lower()==i[-1].lower():
            num+=1

    return num

# 15
def remove_adjacent(list):
    """
    >>> remove_adjacent([1,2,2,3])
    [1, 2, 3]
    >>> remove_adjacent([1,2,2,2])
    [1, 2]
    >>> remove_adjacent([0,8,1,2,6,4,1,7,5,8])
    [0, 8, 1, 2, 6, 4, 1, 7, 5, 8]
    >>> remove_adjacent([1,1,1])
    [1]
    >>> remove_adjacent([3,3,3,3,3,3])
    [3]


    list = list of numbers
    this function job is to remove adjacent numbers to a single number
    """
    list1 = []

    for i in range(len(list)-1):
        if list[i]!=list[i+1]:
            list1.append(list[i])
    list1.append(list[-1])


    return list1



    # clone = list.copy()
    #
    # for in range(len(list)-1):
    #     if list[i]==list[i+1]:
    #         del clone[i]
    # return clone








































































