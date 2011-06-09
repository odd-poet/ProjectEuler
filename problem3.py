# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=3
import math

N = 600851475143

prime = [2, 3]
def next_prime():
   x = prime[len(prime)-1] + 2
   sqrtx = math.sqrt(x)
   while True:
      is_prime = True
      for i in prime:
         if i > sqrtx:
            break
         if x % i == 0:
            is_prime = False
            break
      if is_prime :
         prime.append(x)
         return x
      else :
         x+=2
         
def make_primes(n):
   while next_prime() < (n/2): continue
      

def find_prime_factors(n):
   rv = []
   make_primes(n)
   for p in prime:
      if n % p == 0:
         rv.append(p)
   return rv
   
n_primes = find_prime_factors(100)
print n_primes
sum = 0
for i in n_primes:
   sum += i
print sum


