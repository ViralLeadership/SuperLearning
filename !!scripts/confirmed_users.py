# Start out with some users that need to be verified,
#  and an empty list to hold confirmed users.
potential_users = ['jonathan', 'dorn', 'katie', 'phillip', 'brian', 
                     'sandra', 'lori', 'alice', 'brian', 'charlie', 'john', 
                     'louritha', 'peter', 'larry', 'candace']
unconfirmed_users = []
confirmed_users = []
still_potentials = []

print(type(potential_users))
print(type(unconfirmed_users))
print(type(confirmed_users))
print(type(still_potentials))

# Verify each user, until there are no more unconfirmed users.
#  Move each verified user into the list of confirmed users.
while potential_users:
    for potential_user in potential_users:
        current_user = potential_users.pop()
        check = input("\nHas " + current_user.title() + 
                      " been confirmed? (yes or no)? ")
        check = check.lower()
        if check == "no":
            print("\n" + current_user.title() + " is not confirmed.")
            unconfirmed_users.append(current_user)
        elif check == "yes":
            print("\nVerifying user: " + current_user.title())
            confirmed_users.append(current_user)
        else:
            print("You did not enter an acceptable yes or no response.")
            still_potentials.append(current_user)

# Display all unconfirmed users.
print("\nThe following users are unconfirmed:")
for unconfirmed_user in unconfirmed_users:
    print(unconfirmed_user.title())
    
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Display still potential users.
print("\nThe following users are neither confirmed or unconfirmed:")
for potential in still_potentials:
    print(potential.title())
