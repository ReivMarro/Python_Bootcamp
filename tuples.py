# Tuples and lists seem similar, but a tuple is IMMUTABLE vs a list which is MUTABLE
# Can also be said that one is UNCHANGEABLE vs CHANGEABLE
animals = ["cat", "dog", "bird", "tortoise"]
animals.sort()
# That is how a list works, when entering animals.sort it would be sorted by alphabetical order
# HOWEVER
# with a tuple the items would remain IMMUTABLE
foods = ("pasta", "vegetables", "meat", "seafood",) # It is good practice to end with comma
# Lists start with hard brackets, tuples start with parenthesis. 
# Tuples have limited 'listing' or editing options compared to lists
# Tuples help with memory performance as there are limited variables
for food in foods:
    print("The food is", food)