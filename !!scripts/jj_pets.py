# =============================================================================
# pets = ['dog', 'gerbil', 'snake', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print()
# print(pets)
# 
# while 'cat' in pets:
#     pets.remove('cat')
# 
# print()    
# print(pets)
# 
# =============================================================================

pets = ['dog', 'goldfish', 'gerbil', 'goat', 'snake', 'chicken', 'cat', 'dog'
        'snake', 'snake', 'chicken', 'goldfish', 'cat', 'rabbit', 'chicken', 
        'goat', 'cat', 'dog', 'gerbil']
print()
print(pets)

trimmed = []
redundant = []

pets_out = []
while True:
    check = input("Please type in pet to be removed: (enter 'quit' when done): ")
    check = check.lower()
    if check == "quit":
        break
    else:
        pets_out.append(check)

print("Pets to be removed:")
for pet in pets_out:
    print(pet)


while pet in pets_out:
    pets.remove(pet)

print(pets)

for pet in pets:
#    current_pet = pets.pop()
    if pet not in trimmed:
        trimmed.append(pet)
    else:
        redundant.append(pet)
# =============================================================================
#     else:
#         trimmed.append(current_pet)
# 
# =============================================================================
print()    
for pet in sorted(trimmed):
    print(pet)

print()    

for pet in sorted(redundant):
    print(pet)
