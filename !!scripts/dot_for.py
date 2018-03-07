# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 09:13:18 2018

@author: jenkij
"""

import numpy as np
from datetime import datetime

a = np.random.randn(100)
b = np.random.randn(100)
T = 100000

def slow_dot_product(a, b):
    result = 0
    for e, f in zip(a, b):
        result += e*f
    return result

runs = 1
stat = []
while runs <= 10:
    t0 = datetime.now()
    for t in range(T):
        slow_dot_product(a, b)
    dt1 = datetime.now() - t0

    t0 = datetime.now()
    for t in range(T):
        a.dot(b)
    dt2 = datetime.now() - t0
    stat.append(dt1.total_seconds() / dt2.total_seconds())
    print( "Run #" + str(runs) + " dt1 / dt2:", dt1.total_seconds() / dt2.total_seconds() )
    runs += 1
print()
print(stat)
np_stat = np.array(stat)
print()
print( np_stat )
print( np_stat.mean() )
print( "\nOn average, the np array is ", np_stat.mean(), \
      " times faster than the \"for loop\"." )
print()