# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 12:24:58 2018


@author: Cobbadmin
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 11:15:05 2018

@author: Jonathan Jenkins
"""

class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.upper()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attemps to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

my_new_car = Car("hummer", "h3t", 2019)
print("\n" + my_new_car.get_descriptive_name())
my_new_car.update_odometer(15)
my_new_car.read_odometer()

