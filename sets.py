# So far: 

# lists = [name1, name2, name3]

# dictionary = {
#    "key": "value",
# }

set = {"Item 1", "Item 2", "Item 3"}
print(set)
# An unique characteristic about sets is that it does not care about the order of items
# Another characteristic is that, unlike tuples, items in a set are changeable
set.add("Item 4")
print(set)
set.remove("Item 3")
print(set)