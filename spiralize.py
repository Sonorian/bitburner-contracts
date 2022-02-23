from pyperclip import copy

given = [
        [45,50,47, 5,14,19,24, 8,35,17,35,36],
        [12,12,35,14,40,50, 6,13,18,44,21,40],
        [16,41,15, 3,34,22,26,14,40,11,33, 8],
        [17,33, 1,22,37,34,24,36,11,12, 6,20]
    ]

x = len(given[0])
y = len(given)
pos = [0,0]
dir = [1,0]
gap = 0
values = []

for i in range(x*y):
    #print(pos)
    #print(given[pos[1]][pos[0]])
    values.append(given[pos[1]][pos[0]])

    if dir == [0,-1] and pos[1] == gap:
        dir = [1,0]
    if dir == [1,0] and pos[0] == x-gap-1:
        dir = [0,1]
    if dir == [0, 1] and pos[1] == y-gap-1:
        dir = [-1,0]
    if dir == [-1,0] and pos[0] == gap:
        dir = [0,-1]
        gap += 1
    
    pos[0] += dir[0]
    pos[1] += dir[1]

#cleaned = values[:values.index('')]
print(values)
string = f'{values}'
copy(string)

"""
0 0 0 0 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0 0 1 0
0 2 0 0 0 0 0 0 3 0 0
0 0 3 0 0 0 0 0 3 0 0
0 1 0 0 0 0 0 0 0 1 0
0 0 0 0 0 0 0 0 0 0 0
x=4
"""