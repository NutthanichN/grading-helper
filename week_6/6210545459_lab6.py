

#no1
def ll_sum(num_list):
    """
    >>> t = [[5, 6], [3], [4, 5, 6]]
    >>> ll_sum(t)
    29

    >>> ta = [[99, 11,55 ,45 ,12 ,88]]
    >>> ll_sum(ta)
    310

    >>> too = [[44,44,44 ], [44,44 ,0]]
    >>> ll_sum(too)
    220

    >>> pom = [[0,0,0 ], [9,88 ,1]]
    >>> ll_sum(pom)
    98

    >>> pedkob = [[123],[456],[789],[12],[345]]
    >>> ll_sum(pedkob)
    1725
    """
    hippo=0
    for justin in range(len(num_list)):
        for bustin in range(len(num_list[justin])):
            hippo=hippo+num_list[justin][bustin]
    return hippo

#no2
def cumulative_sum(tualake):
    """
    >>> tomas = [1, 2, 3]
    >>> cumulative_sum(tomas)
    [1, 3, 6]

    >>> tommy = [0, 3, 5]
    >>> cumulative_sum(tommy)
    [0, 3, 6]

    >>> timber = [1, 0, 1]
    >>> cumulative_sum(timber)
    [1, 1, 2]

    >>> tubby = [4, -2, 2]
    >>> cumulative_sum(tubby)
    [4, 2, 4]

    >>> tetra = [11, 22, 33,44,55]
    >>> cumulative_sum(tetra)
    [11, 33, 66, 110, 220]


    """
    for i in range(len(tualake)):
        tuasudtai=tualake[-1]
        tualake[-1]=0
        tualake[i]=tualake[i]+tualake[i-1]
    tualake[-1]=tualake[-1]+tuasudtai+tualake[-2]
    return tualake

#no3
def middle(hippo):
    """
    >>> twt = [5, 2, 3, 9]
    >>> middle(twt)
    [2, 3]

    >>> toss = [1999999999999,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,4474578457845784785]
    >>> middle(toss)
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]

    >>> tip = [0,1,1,2,9]
    >>> middle(tip)
    [1, 1, 2]

    >>> tames = [0,0,7]
    >>> middle(tames)
    [0]

    >>> tammy = [4,4,4,5,5,5,5,5,99,9,9,9,9,9,9,333]
    >>> middle(tammy)
    [4, 4, 5, 5, 5, 5, 5, 99, 9, 9, 9, 9, 9, 9]

    >>> t = [44444444444, 8888888888, 121212121212121212121212, 16161616161616161616]
    >>> middle(t)
    [8888888888, 121212121212121212121212]

    """
    hippo.pop(0)
    hippo.pop(-1)
    return hippo

#no4 มันคือ3แบบเปลืองอีกบรรทัดนึง
def chop(hippo):
    """
    >>> anne = [1, 6, 7, 4]
    >>> chop(anne)
    >>> anne
    [6, 7]

    >>> anna = [1,3]
    >>> chop(anna)
    >>> anna
    []

    >>> aom = [2,8,1]
    >>> chop(aom)
    >>> aom
    [8]

    >>> pravit = [2,8,10,10,50,20,30,40,50,30,99,1]
    >>> chop(pravit)
    >>> pravit
    [8, 10, 10, 50, 20, 30, 40, 50, 30, 99]

    >>> snape = [0,0,0,0,0,0,0,0,0,0,0]
    >>> chop(snape)
    >>> snape
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    """
    hippo.pop(0)
    hippo.pop(-1)
    return

#no5
def is_sorted(hippo):
    """
    >>> is_sorted([99, 999, 999999999])
    True
    >>> is_sorted(['udon','burapha', 'tuksin'])
    False
    >>> is_sorted(['AA','Jutiporn','moka'])
    True
    >>> is_sorted(['moka','AA','Jutiporn'])
    False
    >>> is_sorted([44,112,277])
    True
    """
    if sorted(hippo)==hippo:
        return True
    elif sorted(hippo)!=hippo:
        return False

#no6
def front_x(hippo):
    """
    >>> front_x(['xhamster','kim','xmen','zebra'])
    ['xhamster', 'xmen', 'kim', 'zebra']
    >>> front_x(['xter','ant','bird','xray'])
    ['xter', 'xray', 'ant', 'bird']
    >>> front_x(['xia','exe','xtreme','dog'])
    ['xia', 'xtreme', 'exe', 'dog']
    >>> front_x(['xaa','exe','xee','dog','frog'])
    ['xaa', 'xee', 'exe', 'dog', 'frog']
    >>> front_x(['pb','garena','bbgun','xshot'])
    ['xshot', 'pb', 'garena', 'bbgun']
    """
    pipho=[]
    for i in range(len(hippo)):
        if hippo[i][0]=="x":
            pipho.append(hippo[i])
    for i in range(len(hippo)):
        if hippo[i][0]!="x":
            pipho.append(hippo[i])
    return pipho

#no7
def even_only(hippo):
    """
    >>> even_only([3, 1, 4, 1, 5, 9, 2, 9, 0])
    [4, 2, 0]
    >>> even_only([4,4,5,4,5,4,5,4,56])
    [4, 4, 4, 4, 4, 56]
    >>> even_only([66,66,66,66,66,66,55,55])
    [66, 66, 66, 66, 66, 66]
    >>> even_only([44,66,88,22,55,77,44])
    [44, 66, 88, 22, 44]
    >>> even_only([123,456,789,12,345,678,44])
    [456, 12, 678, 44]
    >>> even_only([0,112,44,277,289,317,389])
    [0, 112, 44]

    """
    pipho=[]
    for i in range(len(hippo)):
        if hippo[i]%2!=1:
            pipho.append(hippo[i])
    return pipho

#no8
def love(hippo):
    """
    >>> love("I like Pycharm")
    'I love Pycharm'
    >>> love("I like bus")
    'I love bus'
    >>> love("I want like her")
    'I want love her'
    >>> love("You like car")
    'You love car'
    >>> love("we like pattaya")
    'we love pattaya'


    """

    hippo=hippo.split(" ")
    hippo=hippo[0:-2:1]+["love"]+hippo[-1::1]
    hippo=" ".join(hippo)
    return hippo

#no9
def is_anagram(hippo,pipho):
    """

    >>> is_anagram('arrange','Rear Nag')
    True
    >>> is_anagram('pepper','perpep')
    True
    >>> is_anagram('super','supper')
    False
    >>> is_anagram('acc','cca')
    True
    >>> is_anagram('TRUE','AIS')
    False

    """
    hippopo=[]
    piphoho=[]
    for i in hippo:
        if i!=" ":
            hippopo.append(i.lower())
    for i in pipho:
        if i!=" ":
            piphoho.append(i.lower())
    if sorted(hippopo)==sorted(piphoho):
        return True
    else:
        return False

#no10?????

def has_duplicates(hippo):
    """
    >>> has_duplicates([1,2,3,4,5])
    False
    >>> has_duplicates([1,2,3,4,5,3])
    True
    >>> has_duplicates([1,3,5,7,8,9])
    False
    >>> has_duplicates([1435,134534,434543,5345,5345,2222])
    True
    >>> has_duplicates([1,2,3,4,5,7,6,5,4,3,2])
    True
    """
    if list(set(hippo)) != sorted(hippo):
        return True
    else:
        return False

#no11
def average(hippo):
    """
    >>> average([2, 5, 5, 5, 10, 8, 7])
    6.0
    >>> average([15, 30, 45, 60, 75, 90])
    52.5
    >>> average([200, 500, 500, 5000, 10000, 8765, 756756])
    111674.42857142857
    >>> average([11, 11, 11, 11, 11, 11, 11])
    11.0
    >>> average([911, 199, 911, 1669, 112, 991, 555])
    764.0
    """
    hippopo=sum(hippo)/len(hippo)
    return hippopo

#no12

def centered_average(hippo):
    """

    >>> centered_average([145345345, 1, 5, 5, 10, 8, 7345345435])
    29069074.6
    >>> centered_average([423, 190, 939, 5, 10, 8, 6433])
    314.0
    >>> centered_average([111, 190, 939, 5, 10, 8, 111])
    86.0
    >>> centered_average([222, 10, 20, 30, 40, 50, 393])
    72.4
    >>> centered_average([333, 3.14, 6.28, 9.42, 10.01, 8.99, 43534])
    73.53999999999999
    """
    hippo=sorted(hippo)
    hippo.pop(0)
    hippo.pop(-1)
    hippo=sum(hippo)/len(hippo)
    return hippo

#no13>>>?????

def reverse_pair(hippo):
    """
    >>> reverse_pair("May the fourth be with you")
    'you with be fourth the May'

    >>> reverse_pair("Help me pls.")
    'pls. me Help'

    >>> reverse_pair("Ped dai cup league")
    'league cup dai Ped'

    >>> reverse_pair("tit F GG")
    'GG F tit'

    >>> reverse_pair("moo hed ped kai")
    'kai ped hed moo'

    """
    hippo=hippo.split(" ")
    hippo.reverse()
    hippo=" ".join(hippo)
    return hippo

#no14

def match_ends(hippo):
    """
    >>> match_ends(["Gingering", "hello","wow"])
    2
    >>> match_ends(["google", "ducky","idunno"])
    0
    >>> match_ends(["google", "UwU","OwO"])
    2
    >>> match_ends(["america", "LOL","DUUD","GOG"])
    4
    >>> match_ends(["goog", "tommy","thomaspoonpoon"])
    1
    """
    hippopo = 0
    for i in range(len(hippo)):
        if hippo[i][0].lower()==hippo[i][-1].lower():
            hippopo=hippopo+1
    return hippopo

#no15

def remove_adjacent(hippo):
    """
    >>> remove_adjacent([1,2,3,4,4,4,5])
    [1, 2, 3, 4, 5]
    >>> remove_adjacent([11,22,333,333,4,455,5])
    [11, 22, 333, 4, 455, 5]
    >>> remove_adjacent([112,112,222,222,422,422,511])
    [112, 222, 422, 511]
    >>> remove_adjacent([1,1,1,1,11,1,1,11,1,1,1,1])
    [1, 11, 1, 11, 1]
    >>> remove_adjacent([100,101,101,103,104,105])
    [100, 101, 103, 104, 105]

    """
    hippopo = []
    for i in range(len(hippo) - 1):
        if hippo[i] != hippo[i + 1]:
            hippopo.append(hippo[i])
    hippopo.append(hippo[-1])
    return hippopo