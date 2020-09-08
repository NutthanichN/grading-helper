import difflib
import open_csv as csv
from pathlib import Path
import itertools
import datetime


def elab_zip(code: int, student_id: int) -> Path:
    return Path() / 'files' / f'code{code}' / f'b{student_id}' / f'a{code}.py'


def v2(student_id: int) -> Path:
    return elab_zip(17262, student_id)


def v3(student_id: int) -> Path:
    return elab_zip(17263, student_id)


# def task(student_id: int, num: int) -> Path:
#     return Path() / 'files' / '{}_task{}.py'.format(student_id, num)


def elab_task(directory: str, student_id: int, num: int) -> Path:
    return Path() / '..' / 'elab_grading' / f'{directory}' / f'b{student_id}' / f'a{num}.py'


def lab(student_id: int, num: int) -> Path:
    return Path() / '..' / 'week_6' / '{}_lab{}.py'.format(student_id, num)

# print(task(6010545749, 3))
# print(lab(6010545749, 6))
# print(elab_task('restaurant_v2', 5710547221, 17262))


def check_diff(f1_: Path, f2_: Path):
    differ = difflib.Differ()
    d = {
        '+': 0,
        '-': 0,
        ' ': 0,
        '?': 0,
    }
    f1 = f1_.open(encoding='utf-8')
    f2 = f2_.open(encoding='utf-8')

    for line in differ.compare(
            f1.read().splitlines(), f2.read().splitlines()
    ):
        # print(line)
        d[line[0]] += 1

    f1 = f1_.open('r', encoding='utf-8')
    f2 = f2_.open('r', encoding='utf-8')
    return d, difflib.SequenceMatcher(a=f1.read(), b=f2.read()).ratio()


students = csv.read(Path() / 'comprog19-students.csv')
combinations = itertools.combinations(students, 2)
codes = []


def f(elem):
    return elem[0].id, elem[1].id


# combinations = [elem for elem in combinations if f(elem) in (
#     ('6110545431', '6210545629'),
#     # ('6210545947', '6210545521'),
#     # ('6210545581', '6210545432'),
#     # ('6210545521', '6210546421'),
# )]

# ['6210545629', '6210545459']
# ['6210545947', '6210546439']
# ['6210546668', '6210545963']
# ['6210546676', '6110545996', '6210545416']

# combinations = [elem for elem in combinations if f(elem) in (
#     ('6210546650', '6210546455'),
#     # ('6210545700', '6210546005'),
# )]


directory = 'week_6'
# record_file = open(f'{Path()}/../elab_grading/{directory}/{directory}_copy_record.txt', 'w')
record_file = open(f'{Path()}/../{directory}/{directory}_copy_record.txt', 'w')
record_file.write(f'{datetime.datetime.now()}\n')

max_sim = {}

for s1, s2 in combinations:
    try:
        d, r = check_diff(lab(s1.id, 6), lab(s2.id, 6))
        # d, r = check_diff(elab_task(directory, s1.id, 17443), elab_task(directory, s2.id, 17443))
        # cutoff
        if r > -1:
            for code in codes:
                if s1 in code:
                    code.add(s2)
                    break
            else:
                codes.append({s1, s2})
            print(s1.id, s2.id, end=' ')
            print(d, round(r, 2))
            record_file.write(f'{s1.id} {s2.id} {d} {round(r, 2)}\n')
            if s1 in max_sim:
                if max_sim[s1][1] < r:
                    max_sim[s1][0] = s2
                    max_sim[s1][1] = r
            else:
                max_sim[s1] = [s2, r]
            if s2 in max_sim:
                if max_sim[s2][1] < r:
                    max_sim[s2][0] = s1
                    max_sim[s2][1] = r
            else:
                max_sim[s2] = [s1, r]
    except FileNotFoundError as e:
        # print(e)
        pass
print()
record_file.write('\n')
for code in codes:
    print([s.id for s in code])
    record_file.write(f'{[s.id for s in code]}\n')
print()
record_file.write('\n')
for s1, v in max_sim.items():
    s2, r = v
    print(s1.id, s2.id, f'{r:.2f}')
    record_file.write(f'{s1.id} {s2.id} {round(r, 2)}\n')
record_file.close()
