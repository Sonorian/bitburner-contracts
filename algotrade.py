from sys import argv
from pyperclip import copy

if argv[2]:
    prices = argv[2].split(',')
    prices = [int(p) for p in prices]
else:
    prices = [52,126,79,62,25,27,136,199,19,73,94,46,80,39,8,138,21,82,86,101,9]


#prices = [102,57,74,87,28,85,77,194,177,25,116,150,38,42,102,26,146,171,84,103,186,194,123,135] # (335, (4,7), (9,21))
#priceDict = dict(zip(range(len(prices)), prices))
#print(priceDict)
if argv[1]:
    transactions = int(argv[1])
else:
    transactions = 2


#print(tuple([4,7]) in trades)


def getBest(prices):
    trades = []
    ima = []
    start = max(prices)
    end = 0
    for p in prices:
        if p < end:
            trades.append([start, end])
            start = p
            end = 0
        if p > end:
            end = p
        if p < start:
            start = p
    trades.append([start, end])
    trades = [t for t in trades if t[0] != t[1]]
    for t in trades:
        ima.append(t[0])
        ima.append(t[1])
    profit = 0
    for t in trades:
        profit += t[1] - t[0]
    return trades, ima, profit

def removeOne(prices):
    mP = 0
    mT = []
    mM = []
    for i, n in enumerate(prices):
        shallow = prices.copy()
        del shallow[i]
        t, m, p = getBest(shallow)
        #print(f'Current: {p} from {m}')
        if p > mP:
            mT = t
            mM = m
            mP = p
            #print('Updating')
    return mT, mM, mP


trades, ima, profit = getBest(prices)

if len(trades) <= transactions or transactions == 0:
    start = f'Max profit is {profit}, from trades '
    info = [f'{t[0]} to {t[1]} ' for t in trades if t[0] != t[1]]
    infos = ', '.join(info)
    out = start + infos
    print(out)
    copy(profit)
else:
    fProfit = 0

    for i in range(len(ima)):
        bT, bM, bP = removeOne(ima)
        #print(f'Best: {bP} from {bM}')
        if len(bT) <= transactions:
            if bP > fProfit:
                fProfit = bP
                fTrades = bT
            elif bP < fProfit:
                break
        ima = bM
    
    start = f'Max profit is {fProfit}, from trades '
    info = [f'{t[0]} to {t[1]} ' for t in fTrades if t[0] != t[1]]
    infos = ', '.join(info)
    out = start + infos
    print(out)
    copy(fProfit)