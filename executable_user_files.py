# The idea is to create a file over user input
filename = input("What is the filename? ") # We are asking for a file name
content = input("Enter the content: ") # We are asking for some content

with open(filename, 'w') as file: # This makes it dynamic, up to the user
    file.write(content) # Once this is used in a Terminal and once the input has been entered, a txt file will be created with the name and content provided by user

open_file = input("Would you like to read this file? ") # Possible prompts for user interaction
if open_file in ['y', 'n']:
    if open_file == 'y':
        with open(filename, 'r') as file:
            print(file.read())