# Whereas *args comes back as a tuple and you can loop through the data
# **kwargs come back as a dictionary, can also be looped through them
def person(**kwargs):
    print(kwargs)
    print(type(kwargs))

person(name="JMR", age=30, skill="intermediate") # These are the keyword arguments
# Once printed this it will be shown/put into a dictionary for us

# Ways to use this along with operators
def person(**kwargs): # This is the function
    print(kwargs)
    print(type(kwargs))

    if 'age' in kwargs: # Using a conditional and an 'in' operator
        print("Your age is ", kwarg.get("age")) # Using .get (because it is a dictionary)

person(name="JMR", age=30, skill="intermediate")

# More practical example:
def order_pizza(name, address, **toppings): # Topping made keyword argument
    print(f"Order is for {name}")
    print(f"Deliver it to {address}")
    price = 15.00
    for key, value in toppings.items():
        price = price + 2.00
    print(f"The total price is {price}")
    return price

total_price = order_pizza("MRJ", "Brum", jalapenos=True, extra_cheese=True, ham=True) # The toppings are the keyword arguments