my_name = "Jonathan A. Jenkins"
my_age = 51
my_height = 72.0
my_weight = 246.5
my_eyes = "Brown"
my_teeth = "White"
my_hair = "Bald"

print()
print("Let's talk about %s." % my_name)
print("\nHe's %f inches tall." % my_height)
print("\nHe's %f pounds heavy." % my_weight)
print("\nActually that's not too heavy, but it ain't light either.")
print("\nHe's got %s eyes and wears his head %s." % (my_eyes, my_hair))
print("\nHis teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print("\nIf I add %d, %f, and %f I get %d." % (
          my_age, my_height, my_weight, my_age + my_height + my_weight))

