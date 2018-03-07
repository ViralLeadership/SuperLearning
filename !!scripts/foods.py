#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 23:27:29 2018

@author: jonathan
"""

my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)

my_foods.append("cannoli")
friend_foods.append("ice cream")
print("\nMy favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)