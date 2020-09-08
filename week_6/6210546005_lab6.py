

#1.

def ll_sum(list):
    """

    >>> x = [[4,8],[12,4],[4]]
    >>> ll_sum(x)
    32
    >>> y = [[1,1,2],[4,4],[112],[44]]
    >>> ll_sum(y)
    168
    >>> ll_sum([[1010],[502,301],[207,400],[24],[1500,500]])
    4444
    >>> ll_sum([[100],[10],[2]])
    112
    >>> ll_sum([[44444444444444444444444444444444,4040404040440404404040404040404]])
    48484848484884848848484848484848
    """
    x = 0
    for i in range(len(list)):
        x += sum(list[i])
    return x

# ----------------------------------------------------------------------------------------------------------------------

# 2.

def cumulative_sum(list):
    """

    >>> x = [1,0,1]
    >>> cumulative_sum(x)
    [1, 1, 2]
    >>> y = [4,0,0,0,0,0,0,0,0,0,0]
    >>> cumulative_sum(y)
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    >>> cumulative_sum([4,8,12,16,20,24,28,32,36,40,44])
    [4, 12, 24, 40, 60, 84, 112, 144, 180, 220, 264]
    >>> cumulative_sum([4,44,444,4444,44444,444444])
    [4, 48, 492, 4936, 49380, 493824]
    >>> cumulative_sum([4,40,400,4000,40000,400000,4000000])
    [4, 44, 444, 4444, 44444, 444444, 4444444]
    """
    for i in range(len(list)):
        list[i] += sum(list[i-1:i])
    return list

# ----------------------------------------------------------------------------------------------------------------------

# 3.

def middle(list):
    """

    >>> x = [1,9,8,12,65,4,4,36,88,9,112,69]
    >>> middle(x)
    [9, 8, 12, 65, 4, 4, 36, 88, 9, 112]
    >>> y = [10,4,'^w^','r10']
    >>> middle(y)
    [4, '^w^']
    >>> middle(['cut','show only me!','cut'])
    ['show only me!']
    >>> middle(['r',10])
    []
    >>> middle([1])
    []
    >>> middle([])
    []
    """
    new = list[1:-1]
    return new

# ----------------------------------------------------------------------------------------------------------------------

# 4.

def chop(list):
    """

    >>> x = ['eh!?','middle','again?']
    >>> chop(x)
    >>> x
    ['middle']
    >>> y = ['chop','now','chop','now','chop','chop','chop']
    >>> chop(y)
    >>> y
    ['now', 'chop', 'now', 'chop', 'chop']
    >>> z = ['Mr.Stark','I',"don't",'feel','so','good','.']
    >>> chop(z)
    >>> z
    ['I', "don't", 'feel', 'so', 'good']
    >>> chop(z)
    >>> z
    ["don't", 'feel', 'so']
    >>> chop(z)
    >>> z
    ['feel']
    >>> chop(z)
    >>> z
    []
    >>> o = ['King','Farewell','false king','bye']
    >>> chop(o)
    >>> o
    ['Farewell', 'false king']
    >>> t = ['my score is 100!!','Whoops! my score disappear!?','what happen??']
    >>> chop(t)
    >>> t
    ['Whoops! my score disappear!?']
    """
    new = list[1:-1]
    list[0:len(list)] = new
    return None

# ----------------------------------------------------------------------------------------------------------------------

# 5.

def is_sorted(list):
    """

    >>> is_sorted(['o','t'])
    True
    >>> is_sorted(['egg','chicken'])
    False
    >>> is_sorted([4,4,4,4,4,4])
    True
    >>> is_sorted([4,44,444,44,4444,44444])
    False
    >>> is_sorted(['Old','older','Teen','teenager'])
    False
    """
    new = list[0:len(list)]
    new.sort()
    if list == new:
        return True
    else:
        return False

# ----------------------------------------------------------------------------------------------------------------------

# 6.

def front_x(list):
    """

    >>> x = ['siam','ciao','xiao','nongt']
    >>> front_x(x)
    ['xiao', 'ciao', 'nongt', 'siam']
    >>> y = ['bandori','poppipa','roselia','pas*pale','afterglow','hellohappy']
    >>> front_x(y)
    ['afterglow', 'bandori', 'hellohappy', 'pas*pale', 'poppipa', 'roselia']
    >>> front_x(['coup_de_grace','phantasm','XD','x_mark'])
    ['XD', 'x_mark', 'coup_de_grace', 'phantasm']
    >>> front_x(['BigB','smalls','x is small','X is big','something like that'])
    ['X is big', 'x is small', 'BigB', 'smalls', 'something like that']
    >>> front_x(['sleepy','feel','I','really','zzzz~~~~','xxx then'])
    ['xxx then', 'I', 'feel', 'really', 'sleepy', 'zzzz~~~~']
    """
    x_list = []
    non_x = []
    for i in range(len(list)):
        if (list[i])[0].lower() == 'x':
            x_list.append(list[i])
        else:
            non_x.append(list[i])
    x_list.sort()
    non_x.sort()
    x_list.extend(non_x)
    return (x_list)

# ----------------------------------------------------------------------------------------------------------------------

# 7.

def even_only(list):
    """

    >>> even_only([1,4,9,7,11,15,4,37,69,4,21,33,4,99,87])
    [4, 4, 4, 4]
    >>> even_only([0,5,2,9,4,7,6,87,44])
    [0, 2, 4, 6, 44]
    >>> even_only([49,48,47,46,45,44,43,42,41,40])
    [48, 46, 44, 42, 40]
    >>> even_only([11,22,33,44,55,66,77,88,99])
    [22, 44, 66, 88]
    >>> even_only([99,88,77,66,55,44,33,22,11])
    [88, 66, 44, 22]
    """
    x = []
    for i in range(len(list)):
        if list[i] %2 == 0:
            x.append(list[i])
    return x

# ----------------------------------------------------------------------------------------------------------------------

# 8.

def love(text):
    """

    >>> love('i hate youuu!!!!!')
    'i love youuu!!!!!'
    >>> love('i wanna sleep.')
    'i love sleep.'
    >>> love('love hate love hate love hate love hate love')
    'love hate love hate love hate love love love'
    >>> love('Everyone hate 10')
    'Everyone love 10'
    >>> love('Everyone in jail')
    'Everyone love jail'
    """
    new1 = text.split()
    new1[-2] = 'love'
    new2 = ' '.join(new1)
    return  new2

# ----------------------------------------------------------------------------------------------------------------------

# 9.

def is_anagram(a,b):
    """

    >>> is_anagram('babykaaa','babayaka')
    True
    >>> is_anagram('we are friend','rare if we end')
    True
    >>> is_anagram('santa','satan')
    True
    >>> is_anagram('pokemon','digimon')
    False
    >>> is_anagram('cool','cooler')
    False
    """
    set_a = []
    set_b = []
    for c in a:
        set_a.append(c.lower())
    for c in b:
        set_b.append(c.lower())
    if ' ' in set_a:
        for i in range(set_a.count(' ')):
            set_a.remove(' ')
    if ' ' in set_b:
        for i in range(set_b.count(' ')):
            set_b.remove(' ')
    set_a.sort()
    set_b.sort()
    if set_a == set_b:
        return True
    else:
        return False
# ----------------------------------------------------------------------------------------------------------------------

# 10.

def has_duplicates(list):
    """

    >>> has_duplicates([4,9,8,7,4,3,5,6])
    True
    >>> has_duplicates([1,2,4,9,8,7,11,2])
    True
    >>> has_duplicates([1,4,2,6,8,7,44,11,68])
    False
    >>> has_duplicates([4,44,444,4444])
    False
    >>> has_duplicates([])
    False
    """
    x = False
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i] == list[j] and i != j:
                x = True
    return x


# ----------------------------------------------------------------------------------------------------------------------

# 11.

def average(nums):
    """

    >>> average([4])
    4.0
    >>> average([4,1,9,7,44,32,569,4444])
    638.75
    >>> average([1,23,456,78910])
    19847.5
    >>> average([1,3,5,7,9,11])
    6.0
    >>> average([9,5,16,79,23])
    26.4
    """
    return sum(nums) / len(nums)

# ----------------------------------------------------------------------------------------------------------------------

# 12.

def centered_average(nums):
    """

    >>> centered_average([4,3,4])
    4.0
    >>> centered_average([4,1,9,7,44,32,569,4444])
    110.83333333333333
    >>> centered_average([1,23,456,78910])
    239.5
    >>> centered_average([1,3,5,7,9,11])
    6.0
    >>> centered_average([9,5,16,79,23])
    16.0
    """
    nums.sort()
    nums.remove(nums[0])
    nums.remove(nums[-1])
    return sum(nums) / len(nums)

# ----------------------------------------------------------------------------------------------------------------------

# 13.

def reverse_pair(sentence):
    """

    >>> reverse_pair('lose or win')
    'win or lose'
    >>> reverse_pair('he is she')
    'she is he'
    >>> reverse_pair('i will sleep with you')
    'you with sleep will i'
    >>> reverse_pair('run in the hallway')
    'hallway the in run'
    >>> reverse_pair('back to the future')
    'future the to back'
    """
    new = sentence.split(' ')[::-1]
    reversed = ' '.join(new)
    return reversed

# ----------------------------------------------------------------------------------------------------------------------

# 14.

def match_ends(strings):
    """

    >>> match_ends(['lingering','underwear','pant','t-shirt'])
    1
    >>> match_ends(['sis','bro','dad','mom','papa','mama'])
    3
    >>> match_ends(['no','match','for','you'])
    0
    >>> match_ends(['roar','howl','bite','slash'])
    1
    >>> match_ends(['lol','lul','orz','meme'])
    2
    """
    count = 0
    for i in range(len(strings)):
        if strings[i][0].lower() == strings[i][-1]:
            count += 1
    return count

# ----------------------------------------------------------------------------------------------------------------------

# 15.

def remove_adjacent(nums):
    """

    >>> remove_adjacent([1,3,4,4,6,9])
    [1, 3, 4, 6, 9]
    >>> remove_adjacent([4,4,5,6,6,7])
    [4, 5, 6, 7]
    >>> remove_adjacent([4,4,5,4,4,5])
    [4, 5, 4, 5]
    >>> remove_adjacent([6,9,9,9,6,6,5,4,4])
    [6, 9, 6, 5, 4]
    >>> remove_adjacent([112,44,44,112,69,69,112,112,44])
    [112, 44, 112, 69, 112, 44]
    """
    new = []
    for i in range(len(nums)):
        if nums[i] != nums[i-1]:
            new.append(nums[i])
    return new

# ----------------------------------------------------------------------------------------------------------------------