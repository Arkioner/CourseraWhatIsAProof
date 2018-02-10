import operator as op
from functools import reduce

from pip._vendor.requests.packages.urllib3.connectionpool import xrange


def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

total = 0.0
base = 1000
val = 400
limit = 600
while val <= limit:
    total += ncr(base, val)
    val += 1
print(total)

print(total / pow(2, base))