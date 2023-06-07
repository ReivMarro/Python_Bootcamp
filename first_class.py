# For a function we do something like this:
#def functionname():
#    pass
# And to instantiate a function then we do:
#functionname()

# A class is different. It is an object, just like a function, a file... But they are managed differently:
#class ThisIsAnAnimal: # We give it capitalized words or letters
#    pass
#animal = ThisIsAnAnimal # To instantiate (aka activate) the class this is how it is done
# This previous example will not produce anything, but also it won't create any errors which proves that it is working

# Proper example:
class Animal: # Brand new class
    this_is_a_property = "Something" # We can give the class a property (which is a variable inside a class)

the_animal = Animal() # This will instantiate the class (meaning it will activate the class)
print(the_animal.this_is_a_property) # Looks somewhat like a dictionary object, but we use a dot instead for a class
