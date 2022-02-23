from sys import argv
from pyperclip import copy

if argv[1]:
    text = argv[1]
else:
    given = 6176244199
    text = str(given)

base = tuple([3,3,3,3])
splits = set()
splits.add(base)

for i in range(12-len(text)):
    new = set()
    for j in range(4):
        for k in splits:
            ed = list(k)
            ed[j] -= 1
            if ed[j] > 0:
                new.add(tuple(ed))
    splits = new

print(splits)
options = []
for s in splits:
    option = []
    pos = 0
    for n in s:
        slic = text[pos:pos+n]
        option.append(slic)
        pos += n
    options.append(option)
#print(options)
final = []
for x in options:
    if not any(int(o) > 255 or o[0] == '0' for o in x):
        final.append('.'.join(x))
#print(final)
submittable = f'{final}'
actual = submittable.replace("'", '')
print(actual)
copy(actual)
#elif len(text) == 12:
#    sub = ['.'.join([text[0:3], text[3:6], text[6:9], text[9:12]])]
#    subi = f'{sub}'
#    print(subi.replace("'", ''))

#else:
#    print('fix your damn code')