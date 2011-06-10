# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=2

class FiboSeq:
   def __init__(self):
      self.pprev_value = 0
      self.prev_value = 1
      
   def next(self):
      next_value = self.prev_value + self.pprev_value
      self.pprev_value = self.prev_value
      self.prev_value = next_value
      return next_value
   
   def value(self):
      return self.prev_value 
   

fib = FiboSeq()
sum = 0
while fib.next() < 4000000 :
   if fib.value() % 2 ==0:
      sum += fib.value()
   
print sum 
