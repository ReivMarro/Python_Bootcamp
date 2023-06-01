def thing1():
    print("Welcome to thing 1")

    def thing2(): #This has been registered inside 'Thing1'
        print("Welcome to thing 2")
    thing2()
# We have 2 functions in 1 here    
thing1()
# This is what is called a decorator

#Here practical example:
def thing1(name): # If there was no variable/parameter/argument inside of its function:
    print("Welcome to thing 1", name) # Then it is going to look for it outside of the function

    def thing2(name): 
        print("Welcome to thing 2", NameError)
    thing2(name)

thing1("JMR")