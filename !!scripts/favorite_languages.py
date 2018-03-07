010822# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 09:34:21 2018

@author: jenkij
"""

favorite_languages = {
        'jen': ['python'],
        'sarah': ['r', 'c', 'd'],
        'jonathan': ['python', 'r', 'scala', 'c++'],
        'edward': ['ruby'],
"""
        'charlie': ['go'],
"""
        'brian': ['go', 'd', 'c++', 'c', 'c#', 'python'],
        'phil': ['python'],
        'ashton': ['c', 'lua', 'elixir', 'rust'],
        }

"""
print("\nSarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")

print("\nBrian's favorite language is " +
      favorite_languages['brian'].title() +
      ".")

print("\nJonathan's favorite language is " +
      favorite_languages['jonathan'].title() +
      ".")
"""
for name, languages in sorted(favorite_languages.items()):
    if len(languages) > 1:
        print("\n" + name.title() + "'s " + str(len(languages)) \
              + " favorite languages in alphabetical order are:")
        for language in sorted(languages):
            print("\tThe '" + language.title() + "' programming language.")
    else:
        print("\n" + name.title() + "'s favorite language is the '" \
              + language.title() + "' programming language.")

