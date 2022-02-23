
import timeit
from math import sqrt
from sys import argv
from pyperclip import copy

if argv[1]:
    given = argv[1]
else:
    given = 804462184 #365198078

def getPrimes(primes, period):
    bad = {p*i for p in primes for i in range(int(lower/p),int(upper/p))}
    diff = period-bad
    newprimes = set()
    for n in diff:
        if all(n%p != 0 for p in primes):
            newprimes.add(n)
        
    return newprimes


primes = set()
newprimes = set([2,3,5,7])
factorization = {}
div = given
while True:
    for n in newprimes:
        count = 0
        while div % n == 0:
            div = div/n
            count += 1
            factorization[n] = count
    lower = max(newprimes)
    print(f'current div: {div}')
    print(f'biggest prime tested: {lower}')
    if sqrt(div) < lower:
        factorization[int(div)] = 1
        break
    upper = lower*2-2
    period = set(range(lower, upper))
    primes.update(newprimes)
    newprimes = getPrimes(primes, period)
print(int(div))
copy(int(div))
print(factorization)
product = 1
for key, value in factorization.items():
    product *= key**value
print(product == given)


"""tests = [x for x in getPrimes(given)]
tests.sort()
tests.reverse()

print(tests)
factors = []
for p in tests:
    if given%p == 0:
        factors.append(p)

print(factors)

div = given
factorization = {}
for x in factors:
    count = 0
    while(div%x == 0):
        count += 1
        div = div/x
    factorization[x] = count

print(factorization)"""


