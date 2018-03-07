# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 09:24:06 2018

@author: jenkij
"""

import os
import timeit
start = timeit.default_timer()

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print("\n" + message)
    
stop = timeit.default_timer()
runtime = stop - start
print("\nThe runtime of the running program '" \
      + os.path.realpath(__file__) + \
      "' was " \
      + str(runtime) + " seconds.")