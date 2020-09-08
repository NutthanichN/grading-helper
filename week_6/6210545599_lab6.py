

# Program by Phuwanut Jiamwatthanaloet 6210545599
def ll_sum(a_list):
    """This function add all the number in the nested list and return it.
    >>> ll_sum([[1,2],[1,2]])
    6
    >>> ll_sum([[4],1,2,3])
    10
    >>> ll_sum([1,2,[3,4,15]])
    25
    >>> ll_sum([1,1,1,[1,1,1],1,1,[1]])
    9
    >>> ll_sum([5,[10],[25]])
    40
    """
    result = 0
    for i in a_list:
        if type(i)==list:
            for j in i :
                result += float(j)
        else:
            result+=float(i)
    return int(result)


def cumulative_sum(b_list):
    """This function take a list of integer and return its cumulative sum.
    >>> cumulative_sum([1,2,3,4])
    [1, 3, 6, 10]
    >>> cumulative_sum([2,4,6])
    [2, 6, 12]
    >>> cumulative_sum([17,19,6])
    [17, 36, 42]
    >>> cumulative_sum([1,2,3,4,5,6,7,8,9,10])
    [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    >>> cumulative_sum([0,3,9,12])
    [0, 3, 12, 24]
    """
    for i in range(len(b_list)):
        if i == 0:
            pass
        else:
            b_list[i] = int(b_list[i])+int(b_list[i-1])
    return b_list


def middle(c_list):
    """This function return a new list that contain all but not the first and last element.
    >>> middle([1,2,3])
    [2]
    >>> middle([1,2,3,4,5,6])
    [2, 3, 4, 5]
    >>> middle([7,2,8,9,5])
    [2, 8, 9]
    >>> middle([6,5,4,3,2,1])
    [5, 4, 3, 2]
    >>> middle([1,3,7,9,5,2])
    [3, 7, 9, 5]
    """
    new_list = []
    for i in c_list:
        if i==c_list[0] or i==c_list[-1]:
            pass
        else:
            new_list.append(i)
    return new_list


def chop(d_list):
    """This function modified a list by cutting the first and last element, and return None
    >>> t = [1,2,3,4,5]
    >>> chop(t)
    >>> t
    [2, 3, 4]
    >>> t = [2,4,6,8,10]
    >>> chop(t)
    >>> t
    [4, 6, 8]
    >>> t = [1,3,5,7,9,11]
    >>> chop(t)
    >>> t
    [3, 5, 7, 9]
    >>> t = [15,10,5]
    >>> chop(t)
    >>> t
    [10]
    >>> chop([1,2,3])

    """
    d_list.remove(d_list[0])
    d_list.remove(d_list[-1])
    return None


def is_sorted(e_list):
    """This function return True if the list is sorted and return False if it isn't.
    >>> is_sorted([1,2,3,4,5])
    True
    >>> is_sorted([9,8,7])
    False
    >>> is_sorted([3.14,3.15])
    True
    >>> is_sorted(['z','f'])
    False
    >>> is_sorted(['a','b','c'])
    True
    """
    if e_list==sorted(e_list):
        return True
    else :
        return False


def front_x(f_list):
    """This function group all the string that start with 'x' at the beginning of the list and return string in sorted order
    >>> front_x(['python','xandar','hello'])
    ['xandar', 'hello', 'python']
    >>> front_x(['x-men','essential','pi','x-force'])
    ['x-force', 'x-men', 'essential', 'pi']
    >>> front_x(['xylan','xenon'])
    ['xenon', 'xylan']
    >>> front_x(['xyster','xander','test'])
    ['xander', 'xyster', 'test']
    >>> front_x(['yolk','xeroces'])
    ['xeroces', 'yolk']
    """
    new_list = []
    old_list = list(f_list)
    for i in range(len(f_list)):
        if f_list[i][0]=='x':
            new_list.append(f_list[i])
            old_list.remove(f_list[i])
    list_start_with_x = sorted(new_list)
    return list_start_with_x+sorted(old_list)


def even_only(g_list):
    """This function return a new list with even number only.
    >>> even_only([1,2,3,4,5])
    [2, 4]
    >>> even_only([1,3,5,7,9])
    []
    >>> even_only([2,4,6,8,9])
    [2, 4, 6, 8]
    >>> even_only([5,10,15,20])
    [10, 20]
    >>> even_only([21656,12345,7984564])
    [21656, 7984564]
    """
    new_list=[]
    for i in g_list:
        if i%2!=0:
            pass
        else :
            new_list.append(i)
    return new_list


def love(text_input):
    """This function change the second to last word to 'love'.
    >>> love('You hate me')
    'You love me'
    >>> love('I really like chocolate')
    'I really love chocolate'
    >>> love('He hate it')
    'He love it'
    >>> love('She likes to read that book')
    'She likes to read love book'
    >>> love('Test Test Test')
    'Test love Test'
    """
    text_to_list = str(text_input).split(' ')
    text_to_list[-2] = 'love'
    return ' '.join(text_to_list)


def is_anagram(text_1,text_2):
    """This function return True if 2 words are anagram and False otherwise.
    >>> is_anagram('Python','not yph')
    True
    >>> is_anagram('Computer','PTREUCMO')
    True
    >>> is_anagram('python','nitypa')
    False
    >>> is_anagram('knowledge','sklgjd')
    False
    >>> is_anagram('prefix','xifepr')
    True
    """
    text_1_list = list(text_1.lower())
    text_2_list = list(text_2.lower())
    for i in text_1_list:
        if i == ' ':
            text_1_list.remove(i)
    for i in text_2_list:
        if i == ' ':
            text_2_list.remove(i)
    if sorted(text_1_list) == sorted(text_2_list):
        return True
    else:
        return False


def has_duplicates(h_list):
    """This function return True if there is element that appear more than once and False otherwise.
    >>> has_duplicated([1,2,2,2,3,4,5,6])
    True
    >>> has_duplicated([5,6,7,8,9,10])
    False
    >>> has_duplicated([3,3])
    True
    >>> has_duplicated([1,4,9,16,25])
    False
    >>> has_duplicated([2,2,3,4,2,4])
    True
    """
    count = 0
    for i in h_list:
        if h_list.count(i) > 1:
            count+=1
    if count >= 1 :
        return True
    else :
        return False


def average(i_list):
    """This function return the average of a list of number.
    >>> average([1,2,3])
    2.0
    >>> average([1,2,3,4,5,6,7,8,9,10])
    5.5
    >>> average([3,66,12])
    27.0
    >>> average([5,5,5,5,5,5])
    5.0
    >>> average([10,150,300,45,95,85,20,65])
    96.25
    """
    result = 0
    count = 0
    for i in i_list:
        result+=i
        count+=1
    return (result/count)


def centered_average(j_list):
    """This function return the average of a list of number ignoring the largest and smallest value.
    >>> centered_average([1,2,3,4,5])
    3.0
    >>> centered_average([2,3,1,5,4])
    3.0
    >>> centered_average([4,2,4,2,6,8,10,2])
    4.333333333333333
    >>> centered_average([2,4,6])
    4.0
    >>> centered_average([3,9,4,5,6])
    5.0
    """
    j = sorted(j_list)
    j_list.remove(j[0])
    j_list.remove(j[-1])
    result = 0
    count = 0
    for i in j_list:
        result+=i
        count+=1
    return (result/count)


def reverse_pair(text_input):
    """This function return a reverse pair of the input sentence.
    >>> reverse_pair('Hello there')
    'there Hello'
    >>> reverse_pair('Do or do not there is no try')
    'try no is there not do or Do'
    >>> reverse_pair('How are you')
    'you are How'
    >>> reverse_pair('Thank you very much')
    'much very you Thank'
    >>> reverse_pair('Is that true')
    'true that Is'
    """
    new_text_input = str(text_input).split(' ')
    new_text_input_2 = reversed(new_text_input)
    return " ".join(new_text_input_2)


def match_ends(k_list):
    """This function return the count of the number of strings where the string lenght is 2 or more and the first and last
    character of the string are the same.
    >>> match_ends(['croc','hello'])
    1
    >>> match_ends(['wow','smashs'])
    2
    >>> match_ends(['Test','Python'])
    0
    >>> match_ends(['rarer','computer','yay','lol'])
    3
    >>> match_ends(['gg'])
    1
    """
    count=0
    for i in k_list:
        if i[0] == i[-1] and len(i)>=2:
            count += 1
    return count


def remove_adjacent(l_list):
    """This function return a list where all adjacent elements that are the same to a single element.
    >>> remove_adjacent([1,2,2,3,3,3,2,2,1])
    [1, 2, 3, 2, 1]
    >>> remove_adjacent([5,5,4,5,5,6,7])
    [5, 4, 5, 6, 7]
    >>> remove_adjacent([1,1,1,2,2,3])
    [1, 2, 3]
    >>> remove_adjacent([5,1,2,3,4,5,5])
    [5, 1, 2, 3, 4, 5]
    >>> remove_adjacent([0,8,1,7,5,5,0,8,3,3])
    [0, 8, 1, 7, 5, 0, 8, 3]
    """
    new_list = []
    if l_list[0] == l_list[-1]:
        new_list.append(l_list[0])
    for i in range(len(l_list)):
        if l_list[i] == l_list[i-1]:
            pass
        else :
            new_list.append(l_list[i])
    return new_list


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

