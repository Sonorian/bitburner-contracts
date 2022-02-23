from sys import argv
from pyperclip import copy

if argv[1]:
    given = argv[1]
else:
    given = '()()a()aaaa()))(a'
#a=      [(()(())(()))(), (()(()(())))(), (((())(())))()]

def gothrough(given):
    arr = list(given)
    good = True
    count = 0
    for x in arr:
        if x == '(':
            count += 1
        if x == ')':
            count -= 1
        if count < 0:
            good = False
    return good



def prepare(given):
    given = given.lstrip(')')
    given = given.rstrip('(')
    if given[0] == 'a':
        given = 'a' + prepare(given[1:])
    if given[-1] == 'a':
        given = prepare(given[:-1]) + 'a'
    if given[0:1] == '()':
        given = '()' + prepare(given[2:])
    if given[-2:-1] == '()':
        given = prepare(given[:-2]) + '()'
    return given

def getDiff(given):
    opens = given.count('(')
    closeds = given.count(')')

    diff = opens-closeds
    return diff

def verify(dupes):
    options = frozenset(dupes)
    for x in options:
        if x != prepare(x) or getDiff(x) != 0:
            dupes.remove(x)
    return list(dupes)

def removeLayer(options, char):
    new = []
    for seq in options:
        for i in range(len(seq)):
            temp = seq.copy()
            if temp.pop(i) == char:
                new.append(temp)
    return new

clean = prepare(given)
diff = getDiff(clean)
sanitized = []
print(f'Cleaned: {clean}')
char = ''
if diff > 0:
    char = '('
elif diff < 0:
    char = ')'
else:
    sanitized.append(clean)

if char:
    print(f'Char: {char} * {abs(diff)}')
    mutable = [list(clean)]
    print(f'Mutable: {mutable}')
    for x in range(abs(diff)):
        mutable = removeLayer(mutable, char)
    
    sanitized = {''.join(o) for o in mutable}

print(f'Sanitized: {sanitized}')
verified = verify(sanitized)
working = {a for a in verified if gothrough(a)}
answer = f'{list(working)}'
submittable = answer.replace("'", '')
print(f'Answer: {submittable}')
copy(submittable)





