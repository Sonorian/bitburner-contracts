from sys import argv
from pyperclip import copy

if argv[1]:
    given = argv[1].split(',')
else:
    given = [-8,-4,-2,-6,6,-1,0,8,-4,6,3,9,-5,-3,-6,-7,0,-10,-4,-9,-6,1,6,5,8,7,-4]
#positives = [2, 8, 11, 14, 15]
#            [6, 8, 10,  8,  4]
#between =   [ -20,-12, -6, 0]


simple = []
positive = True
current = 0
for x in given:
    if positive:
        if x >= 0:
            current += x
        else:
            positive = False
            simple.append(current)
            current = x
    else:
        if x <= 0:
            current += x
        else:
            positive = True
            simple.append(current)
            current = x
simple.append(current)

def stripl(numbers):
    if numbers[0] <= 0:
        return stripl(numbers[1:])
    else:
        return numbers

def stripr(numbers):
    if numbers[-1] <= 0:
        return stripl(numbers[:-1])
    else:
        return numbers

simple = stripl(stripr(simple))
print(simple)

def findMaxOption(numbers, start):
    trial = numbers[start]
    loptions = [trial]
    roptions = [trial]

    try: 
        for x in range(start-2, 0, -2):
            loptions.append(loptions[-1] + simple[x] + simple[x+1])
    except IndexError:
        print("hit an indexerror l")
    try:
        for x in range(start+2, len(simple), 2):
            roptions.append(roptions[-1] + simple[x] + simple[x-1])
    except IndexError:
        print("hit an indexerror r")

    maxmaybe = -trial
    if loptions:
        maxmaybe += max(loptions)
    if roptions:
        maxmaybe += max(roptions)
    return maxmaybe

options = []
for x in range(0, len(simple), 2):
    options.append(findMaxOption(simple, x))

print(max(options))
copy(max(options))