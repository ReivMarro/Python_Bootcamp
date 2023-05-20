# A list is subscriptable
# First item of a list will be item zero
list = ['one', 'two', 'three', 'four', 'five']
print(list[0]) #This is called indexing

# b = True
# print(b[0]) This is an example of a non-subscriptable error and it would not print

print(list[1:4]) #This will print all items in between those values. This is called slicing

print(list[2::]) # The double colon indicates printing to the end of list

print(list[-1]) # This will print the last item of the list, it makes its way backwards
# One can carry on experimenting with this
print (list[-3::])

course = "Python 101"
print(course[5]) #This will take each letter as a single item, item 5 will be printed