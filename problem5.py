# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=4
from math import *

def prime_factors(n):
    primes = {}
    x = 2
    m = n
    while True:
        if m < 2 : break
        if m % x == 0 :
            while (m % x == 0) :
                m /= x
                if x in primes : primes[x] += 1
                else : primes[x] = 1
        x+=1
    return primes

def lcm(n, m):
    prime_n = prime_factors(n)
    prime_m = prime_factors(m)
    lcm = 1
    for p in set(prime_n.keys() + prime_m.keys()):
        lcm *= p ** max(prime_n.get(p,1), prime_m.get(p, 1))
    return lcm

lcm_val = 1
for p in range(1, 21):
    lcm_val = lcm(lcm_val, p)

print lcm_val