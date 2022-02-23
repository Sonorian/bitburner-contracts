from sys import argv
from pyperclip import copy

if argv[1]:
    case = argv[1]
else: 
    case = '11089817'
if argv[2]:
    target = int(argv[2])
else:
    target = 25

def eval(expr):
    numbers = [expr]
    opers = ['+', '-', '*']
    for op in opers:
        new = []
        for e in numbers:
            new.extend(e.split(op))
        numbers = new
    ops = []
    if numbers[0] == '':
        del numbers[0]
    else:
        ops.append('+')

    if any(i[0] == '0' and len(i) > 1 for i in numbers):
        return None
    numbers = [int(n) for n in numbers]
    
    for c in expr:
        if c in opers:
            ops.append(c)
    
    multed = []
    for i, o in enumerate(ops):
        if o == '-':
            numbers[i] *= -1
        if o == '*':
            multed[-1] *= numbers[i]
        else:
            multed.append(numbers[i])
    return sum(multed)


def build(pair):
    opers = ['+', '-', '*']
    start = pair[0]
    char = pair[1][0]
    new = []
    tail = pair[1][1:]
    for o in opers:
        new.append([start + o + char, tail])
    new.append([start + char, tail])
    return new


#case = '102345'
exprs = []
unchecked = [[case[0], case[1:]]]
while unchecked:
    new = []
    for x in unchecked:
        try:
            new.extend(build(x))
        except IndexError:
            pass
    exprs.extend(unchecked)
    unchecked = new

allExpressions = [e[0] for e in exprs if e[1] == '']
negatives = ['-'+e for e in allExpressions]
allExpressions.extend(negatives)
#print(allExpressions)
answers = [eval(r) for r in allExpressions]
working = [r for r in allExpressions if eval(r) == target]
submittable = f'{working}'

#print('1*0*2345' in allExpressions)

#print(answers)
actual = submittable.replace("'",'')
print(actual)
copy(actual)
