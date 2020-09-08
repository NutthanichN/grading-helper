

def ll_sum(x):
    """
    Return sum of lists of integers.
    >>> ll_sum([[1,3],[4],[2,3]])
    13
    >>> ll_sum([[2,1,2],[2,2,4]])
    13
    >>> ll_sum([[2,4],[3,2],[4,3]])
    18
    >>> ll_sum([[1,2,3]])
    6
    >>> ll_sum([[3,1],[3,2],[3,3]])
    15
    """
    xlist = []
    for i in x:
        for num in i:
            xlist.append(num)
    return sum(xlist)

def cumulative_sum(x):
    """
    Return the cumulative sum.
    >>> cumulative_sum([1,2,3])
    [1, 3, 6]
    >>> cumulative_sum([2,3,4])
    [2, 5, 9]
    >>> cumulative_sum([1,3,5,7])
    [1, 4, 9, 16]
    >>> cumulative_sum([2,4,6,8])
    [2, 6, 12, 20]
    >>> cumulative_sum([3,6,9,12])
    [3, 9, 18, 30]
    """
    total = 0
    sum = []
    for num in x:
        total += num
        sum.append(total)
    return sum

def middle(x):
    """
    Return a new list that contains all except first and the last.
    >>> middle([1,2,3,4])
    [2, 3]
    >>> middle([2,4,6,8])
    [4, 6]
    >>> middle([1,3,5,7,9])
    [3, 5, 7]
    >>> middle([2,4,6,8,10])
    [4, 6, 8]
    >>> middle([5,10,15,20,25,30])
    [10, 15, 20, 25]
    """
    del x[0] 
    l = len(x)
    del x[l-1]
    return x

def chop(x):
    """
    Return list that romoves the first ans last elements, also return None.
    >>> chop([1,2,3,4])
    
    >>> chop([1,1,1])

    >>> chop([2,3,1,5])

    >>> chop([1,2,3,4])

    >>> chop([2,1,3,4])
    
    """
    del x[0]
    l = len(x)
    del x[l-1]

def is_sorted(x):
    """
    Return True if the list is sorted in ascending order and False otherwise.
    >>> is_sorted([1,2,2])
    True
    >>> is_sorted([3,2,1])
    False
    >>> is_sorted([1,2,3])
    True
    >>> is_sorted(['a','b','c','d','e'])
    True
    >>> is_sorted(['a','a','c','b','c','d'])
    False
    """
    l = len(x)
    for i in range(l-1):
        if x[i+1] < x[i]:
            return False
    return True

def front_x(x):
    """
    Return a list with the strings in sorted order except starts with 'x' first.
    >>> front_x(['ant','bird','xex'])
    ['xex', 'ant', 'bird']
    >>> front_x(['xo','cat','dog','elephant'])
    ['xo', 'cat', 'dog', 'elephant']
    >>> front_x(['bring','apple','down','xx','pround'])
    ['xx', 'apple', 'bring', 'down', 'pround']
    >>> front_x(['happy','xoxo','yelly','oxes'])
    ['xoxo', 'happy', 'oxes', 'yelly']
    >>> front_x(['xyz','pig','helmet','tree'])
    ['xyz', 'helmet', 'pig', 'tree']
    """
    xlist = []
    alist = []
    for word in x:
        if word.startswith('x'):
            xlist.append(word)
        else:
            alist.append(word)
    return sorted(xlist) + sorted(alist)

def even_only(lst):
    """
    Return a new list with only even numbers
    >>> even_only([1,2,3])
    [2]
    >>> even_only([2,4,6,8,10])
    [2, 4, 6, 8, 10]
    >>> even_only([3,2,1,0])
    [2, 0]
    >>> even_only([1,2,4,1,8])
    [2, 4, 8]
    >>> even_only([2,5,1,3,6])
    [2, 6]
    """
    ans = []
    for i in lst:
        if i % 2 == 0:
            ans.append(i) 
    return ans

def love(text):
    """
    Return new word with last two word changed to 'love'.
    >>> love('I like you')
    'I love you'
    >>> love('I gonna kill you')
    'I gonna love you'
    >>> love('You need to have me')
    'You need to love me'
    >>> love('I very like my dogs')
    'I very like love dogs'
    >>> love('You like to hate pizza')
    'You like to love pizza' 
    """
    a = text.split( )
    l = (len(a)-2)
    del a[l]
    a.insert(l,"love")
    return ' '.join(a)

def is_anagram(s1, s2):
    """
    Return True if they are anagrams
    >>> is_anagram('fox','xof')
    True
    >>> is_anagram('abcdefg', 'gtesyi')
    False
    >>> is_anagram('helloworld', 'helloword')
    False
    >>> is_anagram('happy', 'ayhpp')
    True
    >>> is_anagram('you', 'u')
    False
    """
    s1 = s1.lower()
    s2 = s2.lower()
    if (sorted(s1) == sorted(s2)):
        return True
    else:
        return False

def has_duplicates(list):
    """
    Return True if there is any element that appears more than once.
    >>> has_duplicates([1,2,3,4,5])
    False
    >>> has_duplicates([2,2,2])
    True
    >>> has_duplicates([1,6,3,4])
    False
    >>> has_duplicates([2,6,5,2,4,3,5])
    True
    >>> has_duplicates([1,4,2,6,4,7,2,1])
    True
    """
    for i in list:
        if list.count(i) > 1:
            return True
        else:
            return False

def average(num):
    """
    Return the mean average of a list of numbers.
    >>> average([1,2,3,4])
    2.5
    >>> average([2,4,6,8])
    5.0
    >>> average([1,3,5,7,9])
    5.0
    >>> average([2,3,4,5,6])
    4.0
    >>> average([1,4,7,2,5,6,1,8])
    4.25
    """
    return sum(num) / len(num)

def centered_average(nums):
    """
    Return a centered average of a list of numbers.
    >>> centered_average([1,1,5,5,10,8,7])
    5.2
    >>> centered_average([2,4,6,5])
    4.5
    >>> centered_average([1,5,2,3,4])
    3.0
    >>> centered_average([2,1,3,6,7,8])
    4.5
    >>> centered_average([3,2,1,8,4,5,5])
    3.8
    """
    maxvalue = nums[0]
    minvalue = nums[0]
    sum = 0
    for x in nums:
        maxvalue = max(maxvalue, x)
        minvalue = min(minvalue, x)
        sum += x
    return (sum - maxvalue - minvalue) / (len(nums) - 2)

def reverse_pair(text):
    """
    Return the reverse pair of the input sentence.
    >>> reverse_pair('I love my dog')
    'dog my love I'
    >>> reverse_pair('You are so cute')
    'cute so are You'
    >>> reverse_pair('i and you')
    'you and i'
    >>> reverse_pair('cooking is mom my')
    'my mom is cooking'
    >>> reverse_pair('you for best is exercise')
    'exercise is best for you'
    """
    newtext = text.split(' ')
    newtext = newtext[-1::-1]
    return ' '.join(newtext)

def match_ends(text):
    """
    Return the count of the number of strings that lenght is over two and the first and the last char are the same.
    >>> match_ends(['wow','boy','bib'])
    2
    >>> match_ends(['hey','yoy','too'])
    1
    >>> match_ends(['wee','rr','toy'])
    1
    >>> match_ends(['you','ses','tot'])
    2
    >>> match_ends(['see','aaaaaa','nunnnn','gunnnn','peep'])
    3
    """
    count = 0
    for i in range(len(text)):
        a = list(text[i])
        if a[0].lower() == a[len(a)-1].lower() and len(text) >=2:
            count += 1
    return count
print (match_ends(['Gingering','hello','wow']))
def remove_adjacent(list):
    """
    Return a lost where all adjacent elements have been reduced to a single element.
    >>> remove_adjacent([1,2,2,3])
    [1, 2, 3]
    >>> remove_adjacent([2,2,3,3,4])
    [2, 3, 4]
    >>> remove_adjacent([1,3,4,2,1])
    [1, 3, 4, 2, 1]
    >>> remove_adjacent([2,3,3,1])
    [2, 3, 1]
    >>> remove_adjacent([1,2,2,3,3,4])
    [1, 2, 3, 4]
    """
    a = []
    for item in list:
        if len(a):
            if a[-1] != item:
                a.append(item)
        else: a.append(item)        
    return a



if __name__ == "__main__":
    import doctest
    doctest.testmod()