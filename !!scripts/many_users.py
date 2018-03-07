# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 08:46:00 2018

@author: jenkij
"""
import timeit
start = timeit.default_timer()

users = {
        'aeinstein' : {
                'first': 'albert',
                'last': 'einstein',
                'location': 'princeton',
                },
        'mcurie': {
                'first': 'marie',
                'last': 'curie',
                'location': 'paris',
                },
        'jjenkins' : {
                'first' : 'jonathan',
                'last': 'jenkins',
                'location': 'atlanta',
                },
        'cfisher': {
                'first': 'christopher',
                'last': 'fisher',
                'location': 'jackson',
                },
            }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info["first"] + " " + user_info["last"]
    location = user_info["location"]
    
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
    
stop = timeit.default_timer()
runtime = stop - start
print("\nThe runtime of this program was " + str(runtime) + " seconds.")
