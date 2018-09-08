# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 09:31:32 2018

@author: Jonathan
"""

class Dog():
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.\n")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!\n")

my_dog = Dog('raider jenkins', 3.5)
your_dog = Dog('lassie', 65)

print("\nMy dog's name is " + my_dog.name.title() + ".")
print("My dog, " + my_dog.name.title() + ", is "
      + str(my_dog.age) + " years old.\n")
my_dog.sit()
my_dog.roll_over()


print("\nYour dog's name is " + your_dog.name.title() + ".")
<<<<<<< HEAD
print("Your dog, " + your_dog.name.title() + ", is at least "
      + str(your_dog.age) + " years old by now.")
=======
print("Your dog, " + your_dog.name.title() + ", is "
      + str(your_dog.age) + " years old.\n")
>>>>>>> 7ff28be1e15370da0c8cde46ea35bb159fb4a154
your_dog.sit()

