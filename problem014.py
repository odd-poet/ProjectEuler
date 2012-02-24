# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=14


def f(n):
    if n == 1 : return 1
    if n % 2 == 0 : return n / 2
    else : return 3*n + 1

f_cache ={}
def f_chain(n):
    chain = [n]
    x = n
    size = 1
    while x != 1:
        x = f(x)
        if x in f_cache:
            size += f_cache[x]
            break
        chain.append(x)
        size += 1
    for x in chain:        
        f_cache[x] = size
        size -= 1
    return f_cache[n]
    
def find_max_chain(limit):
    max_chain =0
    max_chain_num =0
    for x in range(limit,1, -1):
        v = f_chain(x)
        if v == max(v, max_chain):
            max_chain, max_chain_num = v, x
    return max_chain, max_chain_num

print find_max_chain(1000000)
