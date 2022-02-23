from pyperclip import copy

"""
[
      [8], 1 0
     [6,7], 2 1
    [3,8,2], 4 2
   [4,7,3,1], 8 3
  [1,7,2,8,8] 16 4

  0: 0,1
  0: 0,1 1:1,2
]
"""
field = [
           [4],
          [6,3],
         [9,1,2],
        [4,9,1,6],
       [6,2,3,3,5],
      [4,7,5,9,6,4],
     [3,5,2,5,3,6,2],
    [8,1,3,3,9,6,7,3],
   [3,7,2,5,7,3,2,3,2],
  [6,1,1,5,8,4,5,9,1,6]
]

sums = []
for p in range(2**(len(field))):
    #p=0: p=0000
    #p=15: p=1111
    place = 0
    sum = 0
    path = []
    for row in range(len(field)):
        sum += field[row][place]
        path.append(field[row][place])
        if p & (2**row):
            place += 1
    sums.append(sum)
    print(f'{path} : {sum}')

sums.sort()
#print(sums)
print(min(sums))
copy(str(min(sums)))