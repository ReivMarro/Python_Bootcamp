#programs need paths to execute commands
# if something == something_else:
#    do a thing
# if something != something_else:
#    do something else

can_code = True
# This statement can be made False and that will trigger 'else:'
if can_code == True:
    print("You coded it!")
else:
    print("Not quite yet")

# Practical examples
teacher = "JMR"

if teacher == "JMR": # The True statement must match identically
    print("Access granted")
else:
    print("Acces dennied")
# HOWEVER, this can be amended so the computer recognizes slight differences
student = "RMJ"

if student.lower() == "rmj": # The True statement does not need to match identically due to the variable
    print("Success")
else:
    print("Failure")
# This can be mixed with user input, for example
name = input("What is your name? ")
if name == "Saverio":
    print("For the emperor!")
    bring_food = "meat"
elif name == "JMR": # Can do unlimited elif statements
    print("Welcome back")
    bring_food = "paella"
else:
    print("Heretic!")
    bring_food = "vegetables"
# The code has been split, similar to a fork in the road
print(f"You are eating {bring_food}") # Do not forget the f before the statement

#There are other ways to word the statement

name = input("What is your name? ")

name = name.lower()

if name != "MR":
    print("Exit immediately")
else:
    print("Entry granted")

# This can be done with a range of values
age = 18
if age >= 18:
    print("You can vote")