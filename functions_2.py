def user(name="None", food="pasta"): 
    if name is None:
        name = "Snow"

        person_type = "human" # This is an internal variable and cannot be set from outside the function
        if name == "Snow":
            person_type = "Cat"
        
        print(person_type)

        print("Welcome boss")
    print(f"Hello {name}, you have ordered {food}.")

some_var = user() # If we wanted to store the result of a function in a variable
print("The variable is", some_var)

# Calculator example
def exp(num1, num2):
    total = num1 ** num2
    return total

big_number = exp(33, 6)