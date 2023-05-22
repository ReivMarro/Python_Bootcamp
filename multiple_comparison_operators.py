age = 33
name = "JMR"

# Option 1
if age >= 18 and name == "JMR": # Using 'and' both items must be true for the statement to be printed
    print("You can vote and drink")

else:
    print("Access not granted")

# Option 2
if age >= 18 or name == "Sarah": # Using 'or' just one item must be true for the statement to be printed
    print("You can vote and drink")

else:
    print("Access not granted")