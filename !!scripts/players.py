#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 23:27:33 2018

@author: jonathan
"""

players = ["charles", "martina", "michael", "florence", \
           "eli", "Sandra", "Lori", "Daphne"]
#print(players[0:3])
#print(players[1:4])
#print(players[:4])
#print(players[2:])
#print(players[-6:])

print("Here are the first 4 players on my team:")
for player in players[:4]:
    print(player.title())

print("Here are the last 4 players on my team:")
for player in players[-4:]:
    print(player.title())
