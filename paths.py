from pyperclip import copy

blockers = [[0,0,0,0,1,0,0],[0,0,1,0,0,0,0],[0,1,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,0,0,0,0]]

if blockers:
    dims = [len(blockers[0]), len(blockers)]
else:
    dims = [8, 7]
    brow = [0]
    brow *= dims[0]
    blockers = []
    for x in range(dims[1]):
        blockers.append(brow)

bottom = [1]
bottom *= dims[0]
char = 1
for i in range(len(bottom)):
    if blockers[0][i] == 1:
        char = 0
    bottom[i] = char
field = [bottom]

#blockPrint = f'{blockers}'
#print(blockPrint.replace('],', '],\n'))

for y in range(1, dims[1]):
    row = []
    for x in range(dims[0]):
        try:
            #print(f'{x}, {y}')
            paths = row[x-1] + field[y-1][x]
        except IndexError:
            paths = field[y-1][x]
        if blockers[y][x] == 1:
            paths = 0
        row.append(paths)
    field.append(row)


#output = f'{field}'
#print(output.replace('],', '],\n'))
print(field[-1][-1])
copy(field[-1][-1])