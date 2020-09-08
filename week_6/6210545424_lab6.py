

#1.

def ll_sum(t):
    """
    take a list of lists and sum all the elements from nested lists

     >>> ll_sum([[1],[2],[1,2]])
     6
     >>> ll_sum([[1],[2,4],[1,2]])
     10
     >>> ll_sum([[1,7,5],[2],[1,2]])
     18
     >>> ll_sum([[1,1,1],[3],[1,2]])
     9
     >>> ll_sum([[1,1,1],[99],[1,2]])
     105

     """
    sum = 0
    for s in t:
        for i in s:
            sum += i

    return sum


#2.

def cumulative_sum(t):
    """
    return the list that each elements is the sum from the previous elements

     >>> cumulative_sum([2,5,6])
     [2, 7, 13]
     >>> cumulative_sum([7,9,6])
     [7, 16, 22]
     >>> cumulative_sum([1,4,6])
     [1, 5, 11]
     >>> cumulative_sum([9,1,5])
     [9, 10, 15]
     >>> cumulative_sum([5,4,2])
     [5, 9, 11]

     """
    sum = 0
    lst = []
    for i in t:
        sum += i
        lst.append(sum)
    return lst


#3.
def middle(t):
    """
    return the new list that cut down the first and last index of list

     >>> middle([3,2,4,5])
     [2, 4]
     >>> middle([1,7,8,9])
     [7, 8]
     >>> middle([4,6,7,0])
     [6, 7]
     >>> middle([1,6,8,9])
     [6, 8]
     >>> middle([1,3,9,2])
     [3, 9]

     """
    mid = t[1:-1]
    return mid

#4.
def chop(t):
    """
    removing the first and last index of list and return none

      >>> chop([1,9,8,9])

      >>> chop([1,9,9,2])

      >>> chop([1,8,7,6])

      >>> chop([3,8,9,4])

      >>> chop([2,1,4,5])


      """
    t.pop(0)
    t.pop(-1)
#5.
def is_sorted(lst):
    """
    take a list as a parameter and returns True for the sorted list and False for otherwise

      >>> is_sorted([1,1,1])
      True
      >>> is_sorted([0,9,8])
      False
      >>> is_sorted([4,5,6])
      True
      >>> is_sorted([5,3,2])
      False
      >>> is_sorted([9,0,1])
      False

      """
    return lst == sorted(lst)

#6.
def front_x(l):
    """
    return a list with the sorted string except group all string that starts with "x"

      >>> front_x(["xylo","bear","pop","xray"])
      ['xray', 'xylo', 'bear', 'pop']
      >>> front_x(["xen","xio","qie","yin"])
      ['xen', 'xio', 'qie', 'xen']
      >>> front_x(["xiao","pie","xis"])
      ['xiao', 'xis', 'pie']
      >>> front_x(["xo","milk","xi","hot"])
      ['xi', 'xo', 'hot', 'milk']
      >>> front_x(["xig","zag","xa","lol"])
      ['xa', 'xig', 'lol', 'xa']

      """
    x_list = []
    l.sort()
    for i in l:
        if i[0] == 'x':
            x_list.append(i)
    l.pop(-1)
    l.pop(-1)
    return x_list+l

#7.
def even_only(lst):
    """
    take a list of integers and return odd numbers

      >>> even_only([1,2,3,4,5,6,5])
      [2, 4, 6]
      >>> even_only([8,8,9,0,3,2])
      [8, 8, 0, 2]
      >>> even_only([5,4,3,2,6,7,3])
      [4, 2, 6]
      >>> even_only([3,4,5,7,2,4])
      [4, 2, 4]
      >>> even_only([8,7,6,5,6])
      [8, 6, 6]

      """
    l = []
    for i in lst:
        if i%2 == 0:
            l.append(i)
    return l
#8.
def love(text):
    """
    change the second last word to love

      >>> love("let kill this like yeah")
      'let kill this love yeah'
      >>> love("what is like ?")
      'what is love ?'
      >>> love("how deep is your like ?")
      'how deep is your love ?'
      >>> love("my momma dont like you")
      'my momma dont love you'
      >>> love("cat eats tuna everyday")
      'cat eats love everyday'

      """
    new_text = text.split(" ")
    new_text[-2] = "love"
    return " ".join(new_text)

#9.
def is_anagram(a,b):
    """
    if you can rearrange the letter from one to spell return True if two words are anagram

      >>> is_anagram("basss","Base")
      True
      >>> is_anagram("Back","black")
      True
      >>> is_anagram("park","Parrk")
      True
      >>> is_anagram("trousser","troussers")
      True
      >>> is_anagram("Mouse","soume")
      True

      """
    a.lower()
    b.lower()
    list_a = a.split()
    list_b = b.split()
    for i in list_a:
        if i == " ":
            list_a.remove(i)
    for i in list_b:
        if i == " ":
            list_b.remove(i)
    if list_a.sort() == list_b.sort():
        return True
    else:
        return False


#10.
def has_duplicates(lst):
    """
    return true if there is a duplicate element in a list

      >>> has_duplicates([1,1,11,3])
      True
      >>> has_duplicates([1,3,12,3,5])
      True
      >>> has_duplicates([1,7,2,1])
      True
      >>> has_duplicates([1,2,3,7])
      False
      >>> has_duplicates([2,3,5,7])
      False

      """
    string = ""
    for i in lst:
        if str(i) in string:
            return True
        else:
            string += str(i)
    return False

#11.
def average(nums):
    """
    return the mean average of elements in a list

      >>> average([2,3,5,7])
      4.25
      >>> average([7,4,6,1])
      4.5
      >>> average([9,8,7,3])
      6.75
      >>> average([2,4,6,8])
      5.0
      >>> average([1,4,7,2])
      3.5

      """
    sum = 0
    for i in nums:
        sum += i
    return sum / len(nums)

#12.
def centered_average(nums):
    """
    return centered average of numbers in list which cut down the first and last index and sorted
    the sequence of elements

       >>> centered_average([1,1,1,1,1,1])
       1.0
       >>> centered_average([2,2,22,2,2,2,2])
       2.0
       >>> centered_average([8,7,8,9,90])
       8.333333333333334
       >>> centered_average([20,21,23,2,2,2])
       11.25
       >>> centered_average([4,5,6,78,9])
       6.666666666666667

       """
    sum = 0
    nums.sort()
    for i in nums[1:-1]:
        sum += i
    return sum / len(nums[1:-1])

#13.
def reverse_pair(sentence):
    """
    reverse the pairs of words to a new sentence

       >>> reverse_pair("May i walk you home")
       'home you walk i May'
       >>> reverse_pair("shall i hold your hand")
       'hand your hold i shall'
       >>> reverse_pair("shut up and dance with me")
       'me with dance and up shut'
       >>> reverse_pair("slowly sinking into you")
       'you into sinking slowly'
       >>> reverse_pair("sunflower alvvays better")
       'better alvvays sunflower'

       """

    new_sentence = sentence.split(" ")
    new_sentence.reverse()
    reversed = " ".join(new_sentence)
    return reversed

#14.
def match_ends(lst):
    """
    count the number of string that the first and last character are the same

       >>> match_ends(["bow","wow","bowie"])
       1
       >>> match_ends(["Jen","nie","kim"])
       0
       >>> match_ends(["round","Pound","pop"])
       1
       >>> match_ends(["heh","huh","yay"])
       3
       >>> match_ends(["tame","fast","omo"])
       1

       """
    sum = 0
    for i in lst:
        if len(i) > 2:
            if i[0].lower() == i[-1].lower():
                sum += 1
    return sum


#15.
def remove_adjacent(lst):
    """
    return a list which cut down the duplicated number that behind the number that duplicate

       >>> remove_adjacent([3,4,5,5])
       [3, 4, 5]
       >>> remove_adjacent([1,2,2,2,4,])
       [1, 2, 4]
       >>> remove_adjacent([4,1,1,2])
       [4, 1, 2]
       >>> remove_adjacent([1,2,3,2,2])
       [1, 2, 3, 2]
       >>> remove_adjacent([5,5,5,6,7])
       [5, 6, 7]

       """
    new_lst = []
    for i in lst:
        if len(new_lst):
            if new_lst[-1] != i:
                new_lst.append(i)
        else:
            new_lst.append(i)
    return new_lst
