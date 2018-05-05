# fix this code
from math import gcd

def squares(n, m):
    if n == m:
        return 1
    gcdv = gcd(n, m)
    return (n / gcdv) * (m / gcdv)

