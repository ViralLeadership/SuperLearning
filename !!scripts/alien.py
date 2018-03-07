# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_1 = {}
print(alien_1)
alien_1["color"] = "green"
print(alien_1)
alien_1["points"] = 5
print(alien_1)

alien_2 = {"color": "green"}
print("\nThe alien is initially " + alien_1["color"] +".")

alien_2["color"] = "yellow"
print("The alien's color changes to " + alien_2["color"] + ".")



alien_3 = {"x_position": 0, "y_position": 25, "speed": "fast"}
print("Original x-position: " + str(alien_3["x_position"]))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_3["speed"] == "slow":
    x_increment = 1
elif alien_3["speed"] == "medium":
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
    
# The new position is the old position plus the increment.
alien_3["x_position"] = alien_3["x_position"] + x_increment

print("The alien's New x-position is: " + str(alien_3["x_position"]))
