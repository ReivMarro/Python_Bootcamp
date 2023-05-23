# DRY - Don't Repeat Yourself

def user(name, food): # This is defining a function, in brackets we have the 'arguments/parameters'
    print(f"Hello {name}, you have ordered {food}.") # We are executing the function but the parameter used is within the function. In this case 'name'

user("Zodd", "ribs") # This is called and argument/parameter

# We can also add a default value to the arg
def user(name, food="steak"): # This default parameter can be overwritten 
    print(f"Hello {name}, you have ordered {food}.")
# name and food in this case are key word argument and look for some sort of value
user("Zodd")

# We can also add loops to this
def user(name, food="steak"): # This default parameter can be overwritten 
    if name.lower() == "jmr":

        print("Welcome boss")
    print(f"Hello {name}, you have ordered {food}.")
# this makes the function look for the first value and print it or/and move onto the next one
user("jmr")