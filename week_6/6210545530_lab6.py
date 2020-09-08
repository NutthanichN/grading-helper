

# 1
def ll_sum(a, b, c):
    """Return sum of the all integers in the lists.

        Args:
            a (list): list one.
            b (list): list two.
            c (list): list three.

        Returns:
            int: the sum of all the number in the input lists.

        Examples:
            >>> ll_sum([1,2], [3], [4,5,6])
            21
            >>> ll_sum([2,0], [0], [0,1])
            3
            >>> ll_sum([2,0], [], [])
            2
            >>> ll_sum([2,0], ['a'], [9,8])
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for +: 'int' and 'str'
            >>> ll_sum([], [], [])
            0
    """
    list_too = []
    for i in a:
        list_too.append(i)
    for j in b:
        list_too.append(j)
    for k in c:
        list_too.append(k)
    return sum(list_too)


# 2
def cumulative_sum(sth):
    """Return a list which contains the same integers but plus all the integers that come before it.

        Args:
            sth (list): an input list.

        Returns:
            list: a new list contains the same integers but plus all the integers that come before it.

        Examples:
            >>> cumulative_sum([1, 2, 3])
            [1, 3, 6]
            >>> cumulative_sum([3, 2, 1])
            [3, 5, 6]
            >>> cumulative_sum([8, 45, 700])
            [8, 53, 753]
            >>> cumulative_sum([-1, -3, -5])
            [-1, -4, -9]
            >>> cumulative_sum([8, 0, -10])
            [8, 8, -2]
    """
    new = []
    count = 0
    for num in sth:
        count += num
        new.append(count)
    return new



# 3
def middle(list_a):
    """Return a new list that is the old list but excluded the first and 
    the last element of the old list.

        Args:
            list_a (list): an input list.

        Returns:
            list: a new list that excluded the first and the last element of the old list.

        Examples:
            >>> middle([1, 2, 3, 4])
            [2, 3]
            >>> middle([1, 3, 5, 7, 'e', 444, 5])
            [3, 5, 7, 'e', 444]
            >>> middle(['a','b','c','gg','k'])
            ['b', 'c', 'gg']
            >>> middle(['a','b'])
            []
            >>> middle(['a'])
            []
    """
    new = []
    for num in list_a[1:-1]:
        new.append(num)
    return new


# 4
def chop(t):
    """Return None

        Args:
            t (list): an input list.

        Returns:
            None

        Examples:
            >>> t = [1, 2, 3, 4]
            >>> chop(t)
            >>> t
            [2, 3]
            
            >>> w = ['a', 'b', 'c']
            >>> chop(w)
            >>> w
            ['b']

            >>> b = ['a', 2, 'b', 3]
            >>> chop(b)
            >>> b
            [2, 'b']
            
            >>> chop('a')
            Traceback (most recent call last):
            ...
            AttributeError: 'str' object has no attribute 'pop'
            
            >>> chop([2, 'e', 4])
            
    """
    t.pop(0)
    t.pop(-1)
    return

# 5
def is_sorted(a_list):
    """Return True if the list is sorted, False if it's not.

        Args:
            a_list  (list): an inout list.

        Returns:
            bool: True if the list is sorted, False if it's not.

        Examples:
            >>> is_sorted([1, 2, 2])
            True
            >>> is_sorted(['b', 'a'])
            False
            >>> is_sorted([0, 0, 0])
            True
            >>> is_sorted([-1, -2, 0, 1, 10])
            False
            >>> is_sorted([1, 2, 3, 'a', 'b', 'c'])
            Traceback (most recent call last):
            ...
            TypeError: '<' not supported between instances of 'str' and 'int'
    """
    new = []
    for element in a_list:
        new.append(element)
    a_list.sort()
    return True if new == a_list else False


# 6
def front_x(a_list):
    """Return a list with the strings in sorted order, except group all the strings 
    that begin with 'x' first.

        Args:
            a_list (list): an input list.

        Returns:
            list: a new list which is a sorted list of the original list and 
            group all the strings that begin with 'x' first.

        Examples:
            >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
            ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
            >>> front_x(['xerox', 'xa', 'cd', 'ab'])
            ['xa', 'xerox', 'ab', 'cd']
            >>> front_x(['x456', 'x123', 'a01w', 'aw01'])
            ['x123', 'x456', 'a01w', 'aw01']
            >>> front_x(['456', '123', 'a', '-2', 'x'])
            ['x', '-2', '123', '456', 'a']
            >>> front_x(['x', 'xx', 'xy', 'xxxx'])
            ['x', 'xx', 'xxxx', 'xy']
    """
    new_x = []
    new_others = []
    for sth in a_list:
        if sth[0] == 'x':
            new_x.append(sth)
        else:
            new_others.append(sth)
    new_x.sort()
    new_others.sort()
    return new_x+new_others


# 7
def even_only(list_one):
    """Return a new list that contains only even numbers.

        Args:
            list_one (list): an input list.

        Returns:
            list: a new list that has only even number.

        Examples:
            >>> even_only([3, 1, 4, 1, 5, 9, 2, 6, 5])
            [4, 2, 6]
            >>> even_only([12, 3, 4, 5, 6, 7, 8, 9, 10])
            [12, 4, 6, 8, 10]
            >>> even_only(['a', 'b', 4, 5, 6])
            Traceback (most recent call last):
            ...
            TypeError: not all arguments converted during string formatting
            >>> even_only([])
            []
            >>> even_only([0])
            [0]
    """
    new = []
    for num in list_one:
        if num % 2 == 0:
            new.append(num)
        else:
            pass
    return new


# 8
def love(a_string):
    """Return a new string which is the same as the old string but the second last word 
    was changed to 'love'.

        Args:
            a_string (str): a string that needed the word change.
        Returns:
            str: a new string that the second last word was changed to 'love'.

        Examples:
            >>> love("I like Python")
            'I love Python'
            >>> love("I really like Python")
            'I really love Python'
            >>> love("IlikePython")
            Traceback (most recent call last):
            ...
            IndexError: list assignment index out of range
            >>> love("like like, like like ,,")
            'like like, like love ,,'
            >>> love(1)
            Traceback (most recent call last):
            ...
            AttributeError: 'int' object has no attribute 'split'
    """
    list_one = a_string.split()
    list_one[-2] = 'love'
    new = " ".join(list_one)
    return new


# 9
def is_anagram(one, two):
    """Return True if the two input strings are anagrams.

        Args:
            one (str): string one.
            two (str): string two.

        Returns:
            bool: True if the two input strings are anagrams.

        Examples:
            >>> is_anagram('arrange', 'Rear Nag')
            True
            >>> is_anagram('I m', 'im')
            True
            >>> is_anagram('234', '432')
            True
            >>> is_anagram('HIGH AND LOW', 'high and low')
            True
            >>> is_anagram('almost alike', 'almost alike.')
            False
    """
    one_use = one.lower()
    two_use = two.lower()
    list_one = []
    list_two = []
    for char in one_use:
        list_one.append(char)
    for ch in two_use:
        list_two.append(ch)
    if " " in list_one:
        list_one.remove(" ")
    if " " in list_two:
        list_two.remove(" ")  
    list_one.sort()
    list_two.sort()  
    return True if list_one == list_two else False


# 10
def has_duplicates(a_list):
    """Return True if there is any element that appears more than once.

        Args:
            a_list (list): an input list.

        Returns:
            bool: True if there is any element that appears more than once in the list.

        Examples:
            >>> has_duplicates([1, 2, 3, 4, 5])
            False
            >>> has_duplicates([1, 2, 3, 4, 5, 2])
            True
            >>> has_duplicates([0, 'a', 'b', 'a', 1])
            True
            >>> has_duplicates([])
            False
            >>> has_duplicates(['Hey', 'lets', 'try', 'Hey'])
            True
    """
    new = []
    for num in a_list:
        if num in new:
            pass
        else:
            new.append(num)
    return True if a_list != new else False


# 11
def average(nums):
    """Return the mean average of a list of numbers.

        Args:
            nums (list): an input list.

        Returns:
            float: average value of the numbers in the list.

        Examples:
            >>> average([1, 1, 5, 5, 10, 8, 7])
            5.285714285714286
            >>> average([0, 0, 1])
            0.3333333333333333
            >>> average([0])
            0.0
            >>> average([])
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero
            >>> average([-2, -1, 0, 5, 8])
            2.0
    """
    return sum(nums)/len(nums)


# 12
def centered_average(nums):
    """Return the mean average of the values that ignores the largest and 
    smallest values in the list.

        Args:
            nums (list): a list of numbers.

        Returns:
            float: average value of all the values in the list except the largest and smallest values.

        Examples:
            >>> centered_average([1,1,5,5,10,8,7])
            5.2
            >>> centered_average([10, 10, 3, 6, 7, -3])
            6.5
            >>> centered_average([0, 0, 0, 0])
            0.0
            >>> centered_average([1,2])
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero
            >>> centered_average([1,2,3])
            2.0
    """
    nums.sort()
    nums.remove(nums[0])
    nums.remove(nums[-1])
    return sum(nums)/len(nums)


# 13
def reverse_pair(string_a):
    """Return the reverse pair of the input sentence.

        Args:
            string_a (str): an input string.

        Returns:
            str: a new string that is a reverse pair of the original string.

        Examples:
            >>> reverse_pair('May the fourth be with you')
            'you with be fourth the May'
            >>> reverse_pair('Hi this is a test')
            'test a is this Hi'
            >>> reverse_pair('a b c d e f g')
            'g f e d c b a'
            >>> reverse_pair('first last')
            'last first'
            >>> reverse_pair('one')
            'one'
    """
    list_a = string_a.split()
    return " ".join(list_a[::-1])


# 14
def match_ends(a_list):
    """Return the number of strings which the string length is 2 or more and 
    the first and last character of the string are the same.

        Args:
            a_list (list): an input list.

        Returns:
            int: number of strings which the string length is 2 or more and the first and 
            last character of the string are the same.

        Examples:
            >>> match_ends(['Gingering', 'hello', 'wow'])
            2
            >>> match_ends(['i', 'l', 't'])
            0
            >>> match_ends(['0iii0', 'lll', 'ttt'])
            3
            >>> match_ends(['More', 'than', 'three', 'is', 'fine', 'too', '!!'])
            1
            >>> match_ends(['vvvvvvv', 'jjason'])
            1
    """
    count = 0
    for sth in a_list:
        if len(sth) >= 2:
            if (a_list[a_list.index(sth)][0]).lower() == (a_list[a_list.index(sth)][-1]).lower():
                count += 1
            else:
                pass
        else:
            pass
    return count   



# 15
def remove_adjacent(a_list):
    """Return a list where all adjacent elements have been reduced to a single element.

        Args:
            a_list (list): an input list.

        Returns:
            list: a new list that all adjacent elements have been reduced to a single element.

        Examples:
            >>> remove_adjacent([1, 2, 2, 3])
            [1, 2, 3]
            >>> remove_adjacent([1, 2, 3, 4, 5, 6, 8, 4, 4, 57 ,6 ,4 ,4 ,5])
            [1, 2, 3, 4, 5, 6, 8, 4, 57, 6, 4, 5]
            >>> remove_adjacent(['list', 'list', 'of', 'strings'])
            ['list', 'of', 'strings']
            >>> remove_adjacent(['list', 'list', 0, 0, 1, 'mix'])
            ['list', 0, 1, 'mix']
            >>> remove_adjacent([1, 1, 1, 1, 1, 1, 1])
            [1]
    """
    new = [a_list[0]]
    for element in a_list:
        if element == new[-1]:
            pass
        else:
            new.append(element)
    return new


# if __name__ == '__main__':
#     import doctest
#
# doctest.testmod(verbose=True)
