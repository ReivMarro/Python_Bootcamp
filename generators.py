def my_generator():
    for num in range(50):
        yield num ** num # Yield tells us that this is no longer a function, that this is a generator
# generators will work only one number at a time, so it only deals with the task at hand
# this is code that is memory performing, due to the stated above

for big_num in my_generator():
    print(big_num)

# we can cast this into a list by using
# all numbers = list(my_generator()) # By creating this, the machine does store the numbers in the list, unlike before
# print(all_numbers) 