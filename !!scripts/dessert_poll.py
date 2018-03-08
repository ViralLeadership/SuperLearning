# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 10:02:57 2018

@author: jenkij
"""

responses = {}

#Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    #Prompt for the person's name and response.
    name = input("What is your name? ")
    response = input(name.title() + " what is you favorite dessert? ")
    
    #Store the response in the dictionary
    responses[name] = response
    
    #Determine if anyone else is going to take the poll.
    repeat = input("Is there anyone else that would like to respond? (yes/no) ")
    if repeat == "no":
        polling_active = False
        
#Polling is complete.  Show the results.
print("\nThe respondents to this poll were: ")
for name, response in sorted(responses.items()):
    print(name.title())
print("\nThe favorite desserts cited in this poll were: ")
for name, response in (responses.items()):
    print(response.title())
print("\n--- Poll Results ---")
for name, response in (responses.items()):
    print(name.title() + "'s favorite dessert is " + response.title() + ".")
    
    