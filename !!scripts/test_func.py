# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 12:07:45 2018

@author: jenkij
"""

potential_users = {
        'alice': 'no', 
        'jonathan': 'no',
        'charlie': 'yes',
        'sandra': 'yes',
        'brian': 'yes',
        'hank': 'no',
        'paula': 'no',
        'michael': 'yes',
        'candace': 'no',
        }
unconfirmed_users = {}
confirmed_users = []
still_alive_users = []

print("All potential users: ")
for name, response in potential_users.items():
    print(name.title() + ": ")
    

def verify(mydict):
    for name, response in mydict.items():
        print("\n" + name.title() + ": " + response.upper() + "\n")
        if response == "no":
            unconfirmed_users.update(name[response])
        elif response == "yes":
            print("Verifying user: " + name.title())
            confirmed_users.append(name[response])
        else:
            print("You did not enter yes or no for " + 
                  current_user[name].title() + ".")
            still_alive_users.append(current_user)
    #Display all unconfirmed users.
    print("\nThe following users are still unconfirmed:")
    for unconfirmed_user in sorted(unconfirmed_users):
        print(unconfirmed_user.title())
    
    # Display all confirmed users.
    print("\nThe following users have been confirmed:")
    for confirmed_user in sorted(confirmed_users):
        print(confirmed_user.title())
        
        # Display user that are neither confirmed or unconfirmed.
        print("\nThe following users are neither confirmed or unconfirmed:")
        for still_alive_user in sorted(still_alive_users):
            print(still_alive_user.title())

verify(potential_users)
        