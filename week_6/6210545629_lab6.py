

def ll_sum(เสี่ยโอ):
    """takes a list of lists of integers and adds up the elements from all of the nested lists. For example:
    *** DOCTESTS IS HERE ***
    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> ll_sum(t)
    21
    >>> ll_sum([[1, 2],[3],[4, 5, 6],[7],[8,9],[0,10]])
    55
    >>> ll_sum([[1, 2], [3], [4, 5, 6]])
    21
    >>> ll_sum([[1150],[1150]])
    2300
    >>> ll_sum([])
    0
    """
    """*** CODE IS HERE ***"""
    เสี่ยโอถูกใจสิ่งนี้ = 0
    for i in เสี่ยโอ:
        for j in i:
            เสี่ยโอถูกใจสิ่งนี้ += j
    return เสี่ยโอถูกใจสิ่งนี้

def cumulative_sum(เสี่ยโอ):
    """takes a list of numbers and returns the cumulative sum; that is, a new list where the ith element is the sum of the ﬁrst i + 1 elements from the original list. For example: 
    *** DOCTESTS IS HERE ***
    >>> t = [1, 2, 3]
    >>> cumulative_sum(t)
    [1, 3, 6]
    >>> cumulative_sum([1,2,3,4,5,6,7,8,9,10])
    [1, 3, 6, 10, 15, 21, 28, 36, 45, 90]
    >>> cumulative_sum([1150,1150])
    [1150, 2300]
    >>> cumulative_sum([1150])
    [1150]
    >>> cumulative_sum([])
    []
    """
    """*** CODE IS HERE ***"""
    if len(เสี่ยโอ) <= 1:
        return เสี่ยโอ
    else:
        for i in range(len(เสี่ยโอ)):
            last_num = เสี่ยโอ[-1]
            เสี่ยโอ[-1] = 0
            เสี่ยโอ[i] += เสี่ยโอ[i-1]
        เสี่ยโอ[-1] += last_num+เสี่ยโอ[-2]
        return เสี่ยโอ

def middle(เสี่ยโอ):
    """takes a list and returns a new list that contains all but the ﬁrst and last elements. For example:
    *** DOCTESTS IS HERE ***
    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    >>> middle([0,1,2,3,4,5,6,7,8,9,10])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> middle(["เสี่ย","โอ"])
    []
    >>> middle(["","","",""])
    ['', '']
    >>> middle([[1,2],[3,4]])
    []
    """
    """*** CODE IS HERE ***"""
    เสี่ยโอ.pop(-1); เสี่ยโอ.pop(0); return เสี่ยโอ

def chop(เสี่ยโอ):
    """takes a list, modiﬁes it by removing the ﬁrst and last elements, and returns None. For example:
    *** DOCTESTS IS HERE ***
    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    >>> เสี่ยโอ = [1,3,5,7,9]
    >>> chop(เสี่ยโอ)

    >>> chop(เสี่ยโอ)
    >>> เสี่ยโอ
    [5]
    >>> chop([1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,1,0])
    
    """
    """*** CODE IS HERE ***"""
    เสี่ยโอ.pop(-1); เสี่ยโอ.pop(0); return

def is_sorted(เสี่ยโอ):
    """takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise. For example:
    *** DOCTESTS IS HERE ***
    >>> is_sorted(["mother","ficker"])
    False
    >>> is_sorted([1,3,5,7,5])
    False
    >>> is_sorted([1150])
    True
    >>> is_sorted([1,2,3,4,5,6,7,8,9])
    True
    >>> is_sorted([])
    True
    """
    """*** CODE IS HERE ***"""
    return sorted(เสี่ยโอ) == เสี่ยโอ

def front_x(เสี่ยโอ):
    """returns a list with the strings in sorted order, except group all the strings that begin with 'x' first. For example:
    *** DOCTESTS IS HERE ***
    >>> front_x(["dev","xamarin","c_sharp","xbox"])
    ['xamarin', 'xbox', 'c_sharp', 'dev']
    >>> front_x(["xie o"])
    ['xie o']
    >>> front_x([])
    []
    >>> front_x(["xxx","xbox","xamarin"])
    ['xamarin', 'xbox', 'xxx']
    >>> front_x(["2","1","x"])
    ['x', '1', '2']
    """
    """*** CODE IS HERE ***"""
    เสี่ยโอถูกใจสิ่งนี้ = []
    for i in sorted(เสี่ยโอ):
        if i[0] == "x":
            เสี่ยโอถูกใจสิ่งนี้.append(i)
    for i in sorted(เสี่ยโอ):
        if i[0] != "x":
            เสี่ยโอถูกใจสิ่งนี้.append(i)
    return เสี่ยโอถูกใจสิ่งนี้

def even_only(เสี่ยโอ):
    """that will take a list of integers, and return a new list with only even numbers.
    *** DOCTESTS IS HERE ***
    >>> even_only([1,3,5,7,9,11,13,15,17,19])
    []
    >>> even_only([1,2,3,4,5,6,7,8,9,0])
    [2, 4, 6, 8, 0]
    >>> even_only([2,4,6,8,0])
    [2, 4, 6, 8, 0]
    >>> even_only([])
    []
    >>> even_only([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
    []
    """
    """*** CODE IS HERE ***"""
    เสี่ยโอถูกใจสิ่งนี้ = []
    for i in เสี่ยโอ:
        if i%2 == 0:
            เสี่ยโอถูกใจสิ่งนี้.append(i)
    return เสี่ยโอถูกใจสิ่งนี้

def love(เสี่ยโอ):
    """change the second last word to “love”.
    *** DOCTESTS IS HERE ***
    >>> love("I hate U")
    'I love U'
    >>> love("เสี่ยโอ hate this!")
    'เสี่ยโอ love this!'
    >>> love("คำว่า รัก ในภาษาอังกฤษ ก็คือ fuck ยังไงหละ")
    'คำว่า รัก ในภาษาอังกฤษ ก็คือ love ยังไงหละ'
    >>> love("qweruiop")
    'qweruiop'
    >>> love("เสี่ยโอ เกลียด สิ่งนี้")
    'เสี่ยโอ love สิ่งนี้'
    """
    """*** CODE IS HERE ***"""
    เสี่ยโอ = เสี่ยโอ.split(" ")
    if len(เสี่ยโอ) >= 2:
        เสี่ยโอ = เสี่ยโอ[0:-2] + ["love"] + เสี่ยโอ[-1:]
    return " ".join(เสี่ยโอ)

def is_anagram(เสี่ยโอ,โส่เอีย):
    """takes two strings and returns True if they are anagrams.
    *** DOCTESTS IS HERE ***
    >>> is_anagram("act","Cat")
    True
    >>> is_anagram("","")
    True
    >>> is_anagram("เสี่ยโอ","โส่เอีย")
    True
    >>> is_anagram("justin bieber","bustin jieber")
    True
    >>> is_anagram("country road","west verginia")
    False
    >>> is_anagram("mountain mama","take me home")
    False
    """
    """*** CODE IS HERE ***"""
    เสี่ยโอถูกใจสิ่งนี้ = []
    โส่เอียถูกใจสิ่งนี้ = []
    for i in เสี่ยโอ:
        if i != " ":
            เสี่ยโอถูกใจสิ่งนี้.append(i.lower())
    for i in โส่เอีย:
        if i != " ":
            โส่เอียถูกใจสิ่งนี้.append(i.lower())
    return sorted(เสี่ยโอถูกใจสิ่งนี้) == sorted(โส่เอียถูกใจสิ่งนี้)

def has_duplicates(เสี่ยโอ):
    """takes a list and returns True if there is any element that appears more than once.
    *** DOCTESTS IS HERE ***
    >>> has_duplicates([1,2,2,2,3,3,3,4,4,5,5,6,6,7,8,9,0,1,2,3,4,5,6,7,8])
    True
    >>> has_duplicates([1])
    False
    >>> has_duplicates([])
    False
    >>> has_duplicates([1,1,5,0])
    True
    >>> has_duplicates(list(set(range(999))))
    False
    """
    """*** CODE IS HERE ***"""
    return sorted(เสี่ยโอ) != list(set(เสี่ยโอ))

def average(เสี่ยโอ):
    """returns the mean average of a list of numbers.
    *** DOCTESTS IS HERE ***
    >>> average([1,3,5])
    3.0
    >>> average([0])
    0.0
    >>> average([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
    1.0
    >>> average([1,2,3,4,5,6,7,8,9,10])
    5.5
    >>> average([1150])
    1150.0
    """
    """*** CODE IS HERE ***"""
    return sum(เสี่ยโอ)/len(เสี่ยโอ)

def centered_average(เสี่ยโอ):
    """returns a "centered" average of a list of numbers, which is the mean average of the values that ignores the largest and smallest values in the list. If there are multiple copies of the smallest/largest value, pick just one copy.
    *** DOCTESTS IS HERE ***
    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([1,2,3])
    2.0
    >>> centered_average([1,3,3,5,5,7,7,9,9,10])
    6.0
    >>> centered_average([1150,1150,1150,1150])
    1150.0
    >>> centered_average([1,3,5])
    3.0
    """
    """*** CODE IS HERE ***"""
    เสี่ยโอ.sort()
    เสี่ยโอ.pop(0); เสี่ยโอ.pop(-1)
    return sum(เสี่ยโอ)/len(เสี่ยโอ)

def reverse_pair(เสี่ยโอ):
    """returns the reverse pair of the input sentence.
    *** DOCTESTS IS HERE ***
    >>> reverse_pair("U hate tu")
    'tu hate U'
    >>> reverse_pair("again go we here , shit ah")
    'ah shit , here we go again'
    >>> reverse_pair("o xie")
    'xie o'
    >>> reverse_pair("omae wa shinde")
    'shinde wa omae'
    >>> reverse_pair("จะสิบโมงเช้า นี่ก็ ยังไม่ได้นอน")
    'ยังไม่ได้นอน นี่ก็ จะสิบโมงเช้า'
    """
    """*** CODE IS HERE ***"""
    เสี่ยโอ = เสี่ยโอ.split(" "); เสี่ยโอ.reverse()
    return " ".join(เสี่ยโอ)

def match_ends(เสี่ยโอ):
    """returns the count of the number of strings where the string length is 2 or more and the ﬁrst and last chars of the string are the same.
    *** DOCTESTS IS HERE ***
    >>> match_ends(["Gingering","hello","wow"])
    2
    >>> match_ends(["ขอคืนความสุข","ให้เธอ","ประชาชน"])
    1
    >>> match_ends(["คนแคสเกมก็สามารถรับบริจาค","ที่เรียกว่ารับโดเนท","เช่น green ezqelusia"])
    2
    >>> match_ends(["หมอบ!","!!"])
    1
    >>> match_ends(["  ","  "])
    2
    """
    """*** CODE IS HERE ***"""
    นับเสี่ยโอ = 0
    for i in เสี่ยโอ:
        if i[0].lower() == i[-1].lower():
            นับเสี่ยโอ += 1
    return นับเสี่ยโอ

def remove_adjacent(เสี่ยโอ):
    """returns a list where all adjacent elements have been reduced to a single element.
    *** DOCTESTS IS HERE ***
    >>> remove_adjacent([1,2,2,5,2,2,3])
    [1, 2, 5, 2, 3]
    >>> remove_adjacent([1,1,1,1,1,1,1,1,1,1,1,1,1,2,3,4,5,5,5,5,5,5,5,5,5,6,7,8,8,9,9,10])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> remove_adjacent([1,3,5,7,7,5,5,5,3,3,1,1])
    [1, 3, 5, 7, 5, 3, 1]
    >>> remove_adjacent(["เสี่ยโอ","เสี่ยโอ","เสี่ยโอ","ตู่","ตู่ ภพธร","ตู่","เสี่ยโอ","เสี่ยโอ"])
    ['เสี่ยโอ', 'ตู่', 'ตู่ ภพธร', 'ตู่', 'เสี่ยโอ']
    >>> remove_adjacent([1150])
    [1150]
    """
    """*** CODE IS HERE ***"""
    เสี่ยโอถูกใจสิ่งนี้ = []
    for i in range(len(เสี่ยโอ)-1):
        if เสี่ยโอ[i] != เสี่ยโอ[i+1]:
            เสี่ยโอถูกใจสิ่งนี้.append(เสี่ยโอ[i])
    เสี่ยโอถูกใจสิ่งนี้.append(เสี่ยโอ[-1])
    return เสี่ยโอถูกใจสิ่งนี้