# -*- coding: utf-8 -*-

# http://projecteuler.net/index.php?section=problems&id=1

def sum_of_3_5(n):
   sum =0
   for x in range(1, n):
      if x % 3 == 0 or x % 5 ==0 :
         sum += x
   return sum


print sum_of_3_5(1000)
