from pyperclip import copy

given = [[24,30],[20,24],[24,34],[25,27],[14,22],[10,18],[13,15]]
firstDict = {}
ordered = []

for i, x in enumerate(given):
    firstDict[tuple(x)] = i

for x in sorted(firstDict):
    ordered.append(given[firstDict[x]])

print(ordered)
merged = []
start = ordered[0][0]
end = ordered[0][1]

for x in ordered:
    if end >= x[0]:
        end = max(end, x[1])
        #print('good')
    else:
        merged.append([start, end])
        start = x[0]
        end = x[1]
        #print('new')
merged.append([start, end])

print(merged)
copy(str(merged))