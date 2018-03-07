#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 22:43:13 2018

@author: jonathan
"""

squares1 = []
for value in range(1, 11):
    square = value**2
    squares1.append(square)
    
print(squares1)

print()

squares2 = []
for value in range(1, 11):
    squares2.append(value**2)

print(squares2)

print()

squares3 = [value**2 for value in range(1, 11)]
print(squares3)

million = [number for number in range(1, 1000001)]
#for number in million:
#    print(number)
print(min(million))
print(max(million))
print(sum(million))