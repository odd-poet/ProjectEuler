# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=4
from math import *


sum_of_sqr = 0
for n in range(1, 101):
    sum_of_sqr += n ** 2
sqr_of_sum = sum(range(1, 101)) ** 2

print sqr_of_sum - sum_of_sqr
