

def ll_sum(t):
   """
   this function is used to calculate the sum of number in each list combined.
   >>> t = [[1],[1,2],[1,2,3]]
   >>> ll_sum(t)
   10

   >>> t = [[3],[1,2],[4,5,6]]
   >>> ll_sum(t)
   21

   >>> t = [[0],[1,2,4],[10,2,3]]
   >>> ll_sum(t)
   22

   >>> t = [[1],[1,2],[4,4,0]]
   >>> ll_sum(t)
   12

   >>> t = [[7],[7,7],[7,7,8]]
   >>> ll_sum(t)
   43

   """
   result = 0
   for num in t:
     result += sum(num)
   return result 


def cumulative_sum(t):
    """
    this funtion display new list where the ith element is the sum of the first i + 1 elements from the original list.

    >>> t = [1,2,3]
    >>> cumulative_sum(t)
    [1, 3, 6]

    >>> t = [1,3,5]
    >>> cumulative_sum(t)
    [1, 4, 9]

    >>> t = [1,8,9,1]
    >>> cumulative_sum(t)
    [1, 9, 18, 19]

    >>> t = [1,1,2]
    >>> cumulative_sum(t)
    [1, 2, 4]

    >>> t = [1,7,4]
    >>> cumulative_sum(t)
    [1, 8, 12]
    """
    a = []
    result = 0
    for num in t:
        result = result + num
        a.append(result)
    return a  

def middle(t):
    """
    funtion that return newlist that contain all but not the first and the last.

    >>> t =[1,2,3,4]
    >>> middle(t)
    [2, 3]

    >>> t =[1,4,1,2]
    >>> middle(t)
    [4, 1]

    >>> t =[6,2,3,4,9]
    >>> middle(t)
    [2, 3, 4]

    >>> t =[1,6,9,4]
    >>> middle(t)
    [6, 9]

    >>> t =[7,1,1,7,5]
    >>> middle(t)
    [1, 1, 7]

    """   

    a = []
    for num in t[1:len(t)-1]:
        a.append(num)
    return a


def chop(t):
    """
   funtion that return all but chop the first and the last.

    >>> t =[1,2,3,4]
    >>> chop(t)
    [2, 3]

    >>> t =[1,4,1,2]
    >>> chop(t)
    [4, 1]

    >>> t =[6,2,3,4,9]
    >>> chop(t)
    [2, 3, 4]

    >>> t =[1,6,9,4]
    >>> chop(t)
    [6, 9]

    >>> t =[7,1,1,7,5]
    >>> chop(t)
    [1, 1, 7]
    """
    return t[1:len(t)-1]

def is_sorted(t):
    """
    function that returns True if the list is sorted in ascending order and False otherwise.

    >>> is_sorted([1,2,2])
    True
    >>> is_sorted(['b','a'])
    False
    >>> is_sorted([3,2,1])
    False
    >>> is_sorted([1,1,2])
    True
    >>> is_sorted(['a','b','c'])
    True
    """
    a = t.copy()
    t.sort()  
    if t == a:
        return True
    else:
        return False     

def front_x(l):
   """
   function that returns list with the sorted string, but all the strings that begin with 'x' come first.

    >>> front_x(['mix','xyz','apple'])
    ['xyz', 'apple', 'mix']
    >>> front_x(['xray','xtent','john'])
    ['xray', 'xtent', 'john']
    >>> front_x(['xxx','pipe','loli','kiki'])
    ['xxx', 'kiki', 'loli', 'pipe']
    >>> front_x(['spatan','fucking','noob','xd'])
    ['xd', 'fucking', 'noob', 'spatan']
    >>> front_x(['xceed','is','super','good'])
    ['xceed', 'good', 'is', 'super']

   """ 
   l.sort()
   a =[]
   b= []
   for i in (l):
       if 'x' in (i[0]):
          a.append(i)
       else:
          b.append(i)     
   # print(a + b)
   return a + b




def even_only(l):
    """
    function the return only even number

    >>> even_only([3,1,4,1,5,9,2,6,5])
    [4, 2, 6]
    >>> even_only([1,3,5,7,8,10,11,12])
    [8, 10, 12]
    >>> even_only([2,4,6,8,10,21,23,29])
    [2, 4, 6, 8, 10]
    >>> even_only([1,2,3,4,5])
    [2, 4]
    >>> even_only([10,20,30,40,15,17,19])
    [10, 20, 30, 40]
    """
    a = []
    for i in l:
        if i%2 == 0:
            a.append(i)
    # print(a)
    return a

def love(text):
   """
   a function that will change the second last word to “love”

   >>> love('I like python')
   I love python
   >>> love('I really like python')
   I really love python
   >>> love('like father like son')
   like father love son
   >>> love("I'm your father")
   I'm love father
   >>> love('I like you')
   I love you
   """
   a = text.split(' ')
   a[-2] = 'love'
   # print(' '.join(a))
   return ' '.join(a)
   


def is_anagram(str1,str2):
   """
   this function check if the two string is anagram or not if not return False else return True

   >>> is_anagram('arrange','Rear Nag')
   True
   >>> is_anagram('ant','abe')
   False
   >>> is_anagram('bird','dirb')
   True
   >>> is_anagram('evil','live')
   True
   >>> is_anagram('hulk','herby')
   False
   """
   a = []
   b = []
   for char in str1:
      a.append(char.lower())
   for char in str2:
      b.append(char.lower()) 
   if (char in a) == (char in b):
      return True
   else:
      return False  


def has_duplicates(l):
   """
   a function  that takes a list and returns True if there is any element that
   appears more than once.

   >>> has_duplicates([1,2,3,4,5])
   False
   >>> has_duplicates([1,2,3,4,5,2])
   True
   >>> has_duplicates([1,3,5,7,5])
   True
   >>> has_duplicates([1,2,3,4,5,6])
   False
   >>> has_duplicates([1,1,0,2,0,0])
   True

   """

   a =[]
   for i in l:
      if i not in a:
         a.append(i)
         if len(a) == len(l):
            return False
      else:
         return True


has_duplicates([1,2,3,4,5])
has_duplicates([1,2,3,4,5,2])
            
def average(l):
   """
   a function that returns the mean average of a list of numbers.

   >>> average([1,1,5,5,10,8,7])
   5.285714285714286
   >>> average([1,1,5,5,10,5,5])
   4.571428571428571
   >>> average([1,1,0,2,0,0,3])
   1.0
   >>> average([1,3,5,7,8,9])
   5.5
   >>> average([4,1,3,5,10,8,27])
   8.285714285714286
   """
   return sum(l)/len(l)

def centered_average(l):
   """
   a function that calculate average of list that exclude max and min

   >>> centered_average([1,1,5,5,10,8,7])
   5.2
   >>> centered_average([1,3,7,9])
   5.0
   >>> centered_average([2,4,6,8])
   5.0
   >>> centered_average([2,4,6,8,9,10,11])
   7.4
   >>> centered_average([1,1,0,2,0,0])
   0.5
   """
   l.sort()
   return sum(l[1:len(l)-1])/(len(l)-2)


def reverse_pair(text):
   """
   a function that returns the reverse pair of the input sentence.

   >>> reverse_pair('May the fourth be with You')
   'You with be fourth the May'
   >>> reverse_pair('me love you do')
   'do you love me'
   >>> reverse_pair('kaopun love jitti')
   'jitti love kaopun'
   >>> reverse_pair('borrabeam eat the world')
   'world the eat borrabeam'
   >>> reverse_pair('king kill bill chill boom')
   'boom chill bill kill king'

   """

   a = text.split(' ')
   return (' '.join(a[::-1]))

def match_ends(l):
   """
   function that count number of strings when the string length is 2 or more and the first and last
   chars of the string are the same.

   >>> match_ends(['gingering','wow','hello'])
   2
   >>> match_ends(['greek','nan','love'])
   1
   >>> match_ends(['bob','nan','sixties'])  
   3
   >>> match_ends(['greek','nany','love'])
   0
   >>> match_ends(['greekg','nany','level','go'])
   2

   """

   count = 0
   for char in l:
      if len(l) >= 2:
         if char[0] == char[-1]:
            count += 1
      else:
         count += 0
   return count      

def remove_adjacent(l):
   """
   a function that removes adjacent and return list without adjacent.

   >>> remove_adjacent([1,2,2,3])
   [1, 2, 3]
   >>> remove_adjacent([1,3,7,9])
   [1, 3, 7, 9]
   >>> remove_adjacent([1,1,0,2])
   [1, 0, 2]
   >>> remove_adjacent([1,2,2,3])
   [1, 2, 3]
   >>> remove_adjacent([2,4,6,8,8])
   [2, 4, 6, 8]
   >>> remove_adjacent([0,1,2,4,2,0,2,4])
   [0, 1, 2, 4]
   """

   a =[]
   for i in l:
      if i not in a:
         a.append(i)
   return(a)    





  
       
         

    