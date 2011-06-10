# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=7
from math import *

def nth_prime(n):
    primes = [2]
    x = 3
    while 1:
        is_prime = True
        for p in primes:
            if p**2 > x : break
            if x % p == 0 :
                is_prime = False
                break
        if is_prime : primes.append(x)
        if len(primes) == n : return x
        x += 1

print nth_prime(10001)
                
            
        