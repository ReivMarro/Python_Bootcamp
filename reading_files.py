# Explanation on how to read files on python:
#with open("filename", "r") as file:
    #print(file.read()) # We would need a file with the name indicated in the same folder

# for example
with open("readme.txt", "r") as file:
    print(file.read())

# Option 2: If we want the file stored in a variable that is accessible outside of the 'with' key word or the indentation that comes after
content = file.read() #This stores the content of the file in a variable called 'content'
#With this python closed the file, it is being efficient, not using much memory
print("the content is", content) 