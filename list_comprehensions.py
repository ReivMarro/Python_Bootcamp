# A list comprehension it is a method of writing a for loop and putting all of that data into a list
numbers = []
for num in [1, 3, 5, 7, 9]:
    numbers.append(num**2)
print(numbers) # All we did is exponent the number against the power of 2

# There is a quicker way to do this:
# number = [value for value in [list]] # We are saying is something similar to what we had above 

number = [num**2 for num in [1, 3, 5, 7, 9]] # numbers = ['The answer' for 'some sort of iteration' in ['a list of things']]
# We can also add if and elif statements here