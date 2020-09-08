import difflib
from pathlib import Path

differ = difflib.Differ()


def task(student_id: int, task: int) -> Path:
    return Path() / 'files' / (str(student_id) + '_''task' + str(task) + '.py')


def elab_zip(code: int, student_id: int) -> Path:
    return Path() / 'files' / f'code{code}' / f'b{student_id}' / 'a{code}.py'


def v2(student_id: int) -> Path:
    return elab_zip(17262, student_id)


def v3(student_id: int) -> Path:
    return elab_zip(172623, student_id)


f1 = task(6210546668, 2).open()
f2 = task(6210545963, 2).open()

d = {
    '+': 0,
    '-': 0,
    ' ': 0,
    '?': 1,
}

for line in differ.compare(
    f1.read().splitlines(), f2.read().splitlines()
):
    print(line)
    d[line[0]] += 1

f1 = task(6210546668, 2).open()
f2 = task(6210545963, 2).open()

# sys.stdout.writelines(difflib.context_diff(
#     f1.read().splitlines(), f2.read().splitlines()
# ))

print(difflib.SequenceMatcher(a=f1.read(), b=f2.read()).ratio())
print((d[' '] + d['?']/2)/sum(d.values()))
