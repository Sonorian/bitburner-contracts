from pyperclip import copy

given = [4,0,6,7,3,2,5,0,5,9,6,0,0,2,10,1,6,9,0]

options = [0]

def findPaths(position, field):
    new = []
    speed = field[position]
    #print(f'From pos {position} with speed {speed}')
    if speed == 1:
        if field[position + 1] != 0:
            return [position + 1]
        else:
            return []
    for i, s in enumerate(field[position+1:position+speed]):
        #print(f'{position+1+i}, {s}')
        if s != 0:
            if position+1+i+s >= len(field) - 1:
                copy('1')
                raise Exception('it works')
            new.append(position+1+i)
    return new

if given[0] != 0:
    while options:
        options.extend(findPaths(options.pop(), given))

print('All options exhausted, nothing found')