#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 19:48:04 2018

@author: jonathan
"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])
print(bicycles[-4])
print(bicycles[-4:])

message = "My first bicycle was a " + bicycles[2].title() \
      + "."
print(message)

names = ["Michael", "Chris", "Willie", "Kenneth"]
for name in names:
    greeting = "Hello " + name + ", how are you?"
    print(greeting)
    
vehicles = ["Land Rover", "S-Class Mercedes", \
            "BMW 7-Series", "Volvo S90"]
for vehicle in vehicles:
    statement = "I would love to own a " + vehicle \
                + "."
    print(statement)
    
