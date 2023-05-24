# Variables that live inside of a function cannot be accessed from outside such function
# This is called scope

name = "JMR"

def myfunc():
    return name # This makes the function look for the variable. First inside the function, then outside

print(myfunc()) # This is making run the function and the command return is making the function look for 'name' elsewhere. This is called closure in JavaScript