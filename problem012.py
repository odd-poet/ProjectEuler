# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=12
from math import *

def find_divisors(n):
    divs = []
    for d in range(1, int(round(sqrt(n)))):
        if n % d == 0:
            divs.append(d)
            divs.append(n/d)
    divs.sort()
    return divs

def sum_to(n):
    return n*(n+1)/2

x = 1
while 1:
    t = sum_to(x)
    divs = find_divisors(t)
    if len(divs) >= 500:
        print t
        break
    x += 1