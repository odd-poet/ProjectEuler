# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=3
import math

def prime_factors(n):
   primes = []
   x = 2
   m = n
   while True:
      if m == 1 : break
      if m % x == 0 :
         primes.append(x)
         while (m % x == 0) : m /= x
      x+=1
   return primes

print prime_factors(13195)
print prime_factors(600851475143)
