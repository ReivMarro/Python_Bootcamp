# Type casting helps us change variables from one thing into another
# string list set dictionary bool tuple, this is normal text and all what has been learned can be casted

age = input("What is your age? ")
data_type = type(age)
print(data_type) 

age = int(age) # This makes whatever is in 'age' an integer, using words will create an error
data_type = type(age)
print(data_type)

print("Your age in dog years is", age * 7)