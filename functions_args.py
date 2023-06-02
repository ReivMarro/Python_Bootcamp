# In a lot of Python, especially the world of Django, things like this will be seen:
def thing(self, request, *args, **kwargs):
# self comes with classes
# request is a django thing but it could be anything, called positional argument
# args is arguments. The * tells python it is a set of arguments
# kwargs is keyword arguments
# However, for now, we will focus on this:
def add_numbers(*args): # This looks like a tuple and args always come back as a tuple
    print(args) # You can pass in an unlimited number of arguments
    print(type(args)) # Just to check and confirm that this is a tuple we can use this:

add_numbers(1, 3, 5, 7, 9)

def add_numbers(name, *args): # We can now add a positional argument too
    print(args) 
    print(type(args)) 
# The positional argument will have to match in order
add_numbers("JMR", 1, 3, 5, 7, 9)

# More examples on how to use *args
def add_numbers(*args):
    total = 0
    for num in args:
        total = total + num
    return total

total = add_numbers(1, 3, 5, 7, 9)
print(total)
