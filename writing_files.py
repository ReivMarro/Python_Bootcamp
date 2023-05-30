with open("writing_files.txt", "w") as file:
    file.write("Hello from Python 201") #This will open and create a new .txt file once this file is executed

# We can add append too in order for the file created to be amended (or information be added)
with open("writing_files.txt", "a") as file:
    file.write("\nThis is extra info about Python 201") # We can get the append in a new line by using \n 
    file.write("\n\tThis is tabbed information") # We can get the append tabbed by using \t