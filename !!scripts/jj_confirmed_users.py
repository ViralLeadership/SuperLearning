# Start out with some users that need to be verified,
#  and an empty list to hold confirmed users.
potential_users = ['alice', 'jonathan', 'charlie', 'sandra', 'brian', 'hank', 
                   'paula', 'michael', 'candace']
unconfirmed_users = []
confirmed_users = []
still_alive_users = []

# Verify each user, until there are no more potential users.
#  Move each verified user into the list of confirmed users.
#  Move each unconfirmed user into the list of unconfirmed users.
#  Move users that are neither confirmed or unconfirmed into still alive users.
while potential_users:
    for potential_user in potential_users:
        current_user = potential_users.pop()
        check = input("\nHas " + current_user.title() + 
                      " been confirmed? (Please enter yes or no.): ")
        check = check.lower()
        if check == "no":
            unconfirmed_users.append(current_user)
        elif check == "yes":
            print("Verifying user: " + current_user.title())
            confirmed_users.append(current_user)
        else:
            print("You did not enter yes or no for " + 
                  current_user.title() + ".")
            still_alive_users.append(current_user)
        
# Display all unconfirmed users.
print("\nThe following users are still unconfirmed:")
for unconfirmed_user in sorted(unconfirmed_users):
    print(unconfirmed_user.title())

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in sorted(confirmed_users):
    print(confirmed_user.title())

# Display user that are neither confirmed or unconfirmed.
print("\nThe following users are neither confirmed or unconfirmed:")
for still_alive_user in sorted(still_alive_users):
    print(still_alive_user.title())