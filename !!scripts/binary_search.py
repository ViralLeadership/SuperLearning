# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 09:42:57 2018

@author: jenkij
"""

def binary_search(alist, item):
    print("\nThere are " + str(len(alist)) + " items in the list.")
    first = 0
    last = len(alist)-1
    found = False
    attempt = 0
    while first<=last and not found:
        attempt = attempt + 1
        print("Attempt # " + str(attempt))
        midpoint = (first + last)//2
        print("Trying the number " + str(alist[midpoint]))
        if alist[midpoint] == item:
            found = True
            print("\nIt took " + str(attempt) + " tries to determine that the " +
                  "number we're looking for, [" + str(item) + 
                  "], was at Python index position number " + 
                  str(midpoint) + " from the list of " + 
                  str(len(alist)) + " numbers.")
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    if found == False:
        print("The number we're looking for, [" + str(item) + 
                 "], is not in the list.")
    return print("\n", found)
	 
def binary_search_reverse(alist, item):
    print("\nThere are " + str(len(alist)) + " items in the list.")
    first = len(alist)-1
    last = 0
    found = False
    attempt = 0
    while last<=first and not found:
        attempt = attempt + 1
        print("Attempt # " + str(attempt))
        midpoint = (first + last)//2
        print("Trying the number " + str(alist[midpoint]))
        if alist[midpoint] == item:
            found = True
            print("\nIt took " + str(attempt) + " tries to determine that the " +
                  "number we're looking for, [" + str(item) + 
                  "], was at Python index position number " + 
                  str(midpoint) + " from the list of " + 
                  str(len(alist)) + " numbers.")
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    if found == False:
        print("The number we're looking for, [" + str(item) + 
                 "], is not in the list.")
    return print("\n", found)

#my_list = [0, 1, 2, 5, 8, 10, 13, 17, 19, 24, 27, 32, 39, 41, 44, 47, 49, 52, 
#           55, 57, 59, 63, 65, 68, 70, 74, 77, 79, 83, 85, 87, 90, 92, 93, 94, 
#           95, 96, 97, 98, 99]
my_list = list(range(0, 101))
my_list2 = sorted(my_list, reverse=True)
#print("\nThe number is at index " + str(binary_search(my_list, 3)))
#print()
#print("\n", binary_search(my_list, 5))

print(binary_search(my_list, 59))
print(binary_search_reverse(my_list2, 41))        