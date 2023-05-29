my_thing = True
if my_thing:
    print("Thing was true")

# If we wanted the exact opposite, option 1 is:
my_thing = False
if my_thing: # Since my_thing is false then the pass is going to be executed and print 'else'
    pass
else:
    print("This is not true")

# Another way to see this:
my_thing = False
if my_thing != True: # This is the same command as the example above
    print("Thing is not true")

# The way to do this with the 'not' operator
my_thing = False
if not my_thing: # This just means the same as above. If my_thing is false, then print the statement.
    print("Sorry, thing was false")

# More uses
name = "Ja Marro"
if name not in ["JMR", "RMJ", "JRM"]: # This means, if the name is not in that particular list, then do a thing
    print("Ja Marro is not registered")

# When comparing different strings it works slightly different to using the 'not' operator with a list
name1 = "MR"
name2 = "JM"
if name1 != name2:
    print("Different names")