# A decorator helps you place a function inside of a function, and decide whether there will be something being printed before or after
def my_decorator(func): # My decorator is going to take a function as its only parameter
    def wrapper(): # it will register a new function called wrapper
        print("Do something here")
        func() # This will execute the original function
        print("Original function is finished")
    return wrapper

@my_decorator  # This help label the argument
def myfunc():
    print("My name is JMR")

myfunc() # This will execute myfunc as its own function