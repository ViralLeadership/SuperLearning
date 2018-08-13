# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 11:15:05 2018

@author: Jonathan
"""

class Restaurant():
    """A simple attempt to model a restaurant."""
    def __init__(self, name, cuisine):
        """Initialize name and cuisine attributes."""
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Simulate describing the name of the restaurant and the main cuisine."""
        print(self.name.title() + " is known for it's " + self.cuisine.title() + ".")


seafood= Restaurant('california dreaming', 'seafood platter')
bbq = Restaurant('sticky fingers', 'barbecue ribs')

print("\n" + seafood.name.title() + " is my favorite " + seafood.cuisine.title() + " restaurant.")
print(bbq.name.title() + " is my favorite " + bbq.cuisine.title() + " restaurant." + "\n")

seafood.describe_restaurant()
bbq.describe_restaurant()

