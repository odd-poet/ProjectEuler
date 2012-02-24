# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=2

class FiboSeq:
   def __init__(self):
      self.pprev_value = 0
      self.prev_value = 1
      
   
   def __iter__(self):
      return self
   
   def next(self):
      next_value = self.prev_value + self.pprev_value
      self.pprev_value = self.prev_value
      self.prev_value = next_value
      return self.pprev_value

def solve(n):
   sum =0
   for f in FiboSeq():
      if f > n: break
      if f % 2 ==0 : sum += f
   return sum
   
import profile
profile.run('print solve(4000000)')
