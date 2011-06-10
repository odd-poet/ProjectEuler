# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=1

N = 1000
rv =  set([s for s in range(3, N, 3)])
for s in range(5, N, 5): rv.add(s)

print sum(rv)
