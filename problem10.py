# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=10
from math import *

def sum_primes_below(n):
    primes = [2]
    x = 3
    while 1:
        if x >= n :break
        is_prime = True
        for p in primes:
            if p**2 > x : break
            if x % p == 0 :
                is_prime = False
                break
        if is_prime : primes.append(x)
        x += 1
    return sum(primes)
    
print sum_primes_below(2000000)