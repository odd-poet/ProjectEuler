# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=4
from math import *

def isABA(n):
    """주어진 정수 n의 각 자리수가 역순과 동일한지 판별한다."""
    sn = str(n)
    rsn = [s for s in sn]
    rsn.reverse()
    return sn == "".join(rsn)

def prime_factors(n):
    "n의 소인수를 구한다. "
    primes = []
    x = 2
    m = n
    while True:
       if m == 1 : break
       if m % x == 0 :
          while (m % x == 0) :
             m /= x
             primes.append(x)
       x+=1
    return primes

def nnnXnnn(primes):
    """주어진 소인수 배열을 이용하여 두개의 세자리 정수를 구한다.
    
    return : 세자리 두 정수
	 세자리 두 정수를 구하지 못할 경우 None을 리턴한다.
	 
    """
    nm = (1, 1)
    primes.sort(reverse=True)
    for p in primes:
        nm = (min(nm) * p, max(nm))
    if reduce(lambda s, i: s and i < 1000 and i >=100, nm, True):
        return nm

for n in range(10**6, 10**4, -1):
    if isABA(n) :
        primes = prime_factors(n)
        nxn = nnnXnnn(primes)
        if nxn:
            print "%s = %s x %s" % (n, nxn[0], nxn[1])
            break


