# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=9
from math import *

N = 1000
sq = set([s**2 for s in range(1, N/2)])

for c2 in sq:    
    x = set(map(lambda i: i+c2, sq))
    y = x & sq
    for z in y:
        c = int(sqrt(c2))
        a = int(sqrt(z))
        b = int(sqrt(z - c2))
        if a+b+c == N and b>c:
            print "%s x %s x %s = %s" % (a, b, c, a*b*c)
    del x        
        
    