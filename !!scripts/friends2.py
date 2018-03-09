#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 19:18:33 2018

@author: jonathan
"""

friends = {
        'jonathan': [50,'jackson, ms','black man', 'douglasville'],
        'dorn': [49,'ackerman, ms','strong sista'],
        'sandra': [59, 'leland, ms', 'evangelist', 'hiram'],
        'dick': [73,'richmond, va','german', 'peachtree city'],
        }

#friends = {
#        
#        }
        
for k, v in sorted(friends.items()):
    print("\n" + k.title())
    for item in v:
        print("\t" + ": " + str(item).title())