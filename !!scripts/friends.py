#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 19:18:33 2018

@author: jonathan
"""

friends = {
        'jonathan': {
                'age':50,
                'birthplace':'jackson, ms',
                'race':'black man',
                },
        'dorn': {
                'age':49,
                'birthplace':'ackerman, ms',
                'race':'strong sista',
                },
        'dick': {
                'age':73,
                'birthplace':'richmond, va',
                'race':'german',
                },
        }

#friends = {
#        
#        }
        
for k, v in sorted(friends.items()):
    print("\n" + k.title())
    for name, detail in v.items():
        print("\t" + name.title() + ": " + str(detail).title())