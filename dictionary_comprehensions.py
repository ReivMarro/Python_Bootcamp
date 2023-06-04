names = [("name", "JMR"), ("occupation", "Learner")] # These are tuples
d = {} # This is to turn the previous tuples with different items into a dictionary
for key, value in names:
    d[key] = value
print(d) # This is the long way to make a dictionary using tuples

d = {key:value for key, value in names} # we are unpacking two items, key and value, from the iterable 'names'
print(d)

# There is another shorter and simpler way to do this
d = dict(names)
print(d)

    # Dictionary comprehensions are not as common as lists comprehensions