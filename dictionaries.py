person = {
    "key": "value",
    "name": "JMR",
    "twitter": "@JMR"
} # The first item will likely be a string, then a value which could be a float, integer, string, etc
#print (person['twitter']) # When using print, needs reference to the first item, then the string
print(person)
person ['instagram'] = "@JMR_Python"
print(person)
del person ['key']
print(person) # as print is being used and added different variables, new edited lines will appear