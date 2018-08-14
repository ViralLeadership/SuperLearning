# my_pets = ['raider','mustard','rainbow', 7]
# tabs = len(my_pets)
# for petnames in my_pets:
#     print(petnames)

# using the list function, let's store 1 million values in a list
million = list(range(1,1000001))

for i in million:
    print(i)
# unless you have time, don't print the list!!  I'm not certain what happens?
# but we can count the items in the list and print the last 10 values
print()
count = len(million)
print("There are " + str(count) + " values in the list.")

# print the last 10 values in the list
print(million[-10:])
