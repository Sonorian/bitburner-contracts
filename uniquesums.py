from math import ceil, floor
from sys import argv
from pyperclip import copy

if argv[1]:
    target = int(argv[1])
else:
    target = 51
#print(start)

#series = [0, 0, 1, 2, 4, 6, 10, 14, 21, 29, 41, 55, 76, 100, 134, 175, 230, 296, 384, 489, 626, 791, 1001, 1254, 1574, 1957, 2435, 3009, 3717, 4564, 5603, 6841, 8348, 10142, 12309, 14882, 17976, 21636, 26014, 31184, 37337, 44582, 53173, 63260, 75174, 89133, 105557, 124753, 147272, 173524, 204225, 239942, 281588, 329930, 386154, 451275, 526822, 614153, 715219, 831819, 966466, 1121504]
cache = {2:[0,1,1], 3:[0,2,1,1]}

def buildLayer(cache, number):
    #print(number)
    bound = number/2
    ables = []
    for x in range(ceil(bound)):
        ables.append(1)
    for x in range(floor(bound), 0, -1):
        #print(ables)
        #print(x)
        ables.append(ables[-1] + cache[number-x][x])
    ables.append(0)
    ables.reverse()
    #print(ables)
    return ables

for x in range(4,target+1):
    #print(cache)
    cache[x] = buildLayer(cache, x)

print(cache[target][1])
copy(cache[target][1])
#print(cache[target][1] == series[target])


