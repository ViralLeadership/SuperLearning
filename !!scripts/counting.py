# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 09:09:18 2018

@author: jenkij
"""

import os
import timeit
start = timeit.default_timer()

current_number = 1
count_to = input("Please enter the number you want the computer to count up to: ")
count_to = int(count_to)
count_to += 1

while current_number < count_to:
    print(current_number)
    current_number += 1
    
stop = timeit.default_timer()
runtime = stop - start
print("\nThe runtime of the running program '" \
      + os.path.realpath(__file__) + "' was " 
      + str(runtime) + " seconds.")