# Input function helps to ask for information
# When asking for input from user it will always come back as a string

age = input("What is your age? ")
dog_years = age * 7 
print(dog_years) # It will not print a number when prompted as it will take it as a string

#HOWEVER

dog_years = int(age) * 7 # This way it explicitly makes it an integer aka a number
print(dog_years) # This is called casting

name = input('What is your name? ')
print("Hello,", name)