#creating an empty list for my even integers and initializing my count of even integers
even_integers = []
even_integers_count = -10

# using a while loop that will run until my list of even integers contains 1000 items
while len(even_integers) <= 1000:
    # using an if statement to check whether the current integer is even or not
    if even_integers_count % 2 == 0:
        # appending even integers to my list
        even_integers.append(even_integers_count)
        # incrementing my while loop to the next integer
        even_integers_count = even_integers_count + 1

# calculating the sum of my list of even integers and printing this out.
sum_even_integers = sum(even_integers)
print("The sum of the first " + str(len(even_integers)) + " even integers is equal to "  + str(sum_even_integers) + ".\n")

# calculating the average of my list of even integers and printing this out.
avg_even_integers = sum_even_integers / float(len(even_integers))
print("The average of the first " + str(len(even_integers)) + " even integers is equal to " + str(avg_even_integers) + ".\n")
