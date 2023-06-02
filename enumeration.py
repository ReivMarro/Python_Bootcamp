# We are going to loop through a list and we are going to get the index number from it
animals = ["Raphael", "Michaelangelo", "Donatello", "Leonardo"]
for animal in animals:
    print(animal) # This will come up with a normal list (Python 101)

# HOWEVER
animals = ["Raphael", "Michaelangelo", "Donatello", "Leonardo"]
for animal in enumerate(animals): # Enumerate will give us a tuple, or more precisely, a list of tuples
    print(animal)

# We can do some unpacking here
animals = ["Raphael", "Michaelangelo", "Donatello", "Leonardo"]
for index, animal in enumerate(animals):
    print(index, animal)

# We can then tweak and edit what we want it to show
animals = ["Raphael", "Michaelangelo", "Donatello", "Leonardo"]
for index, animal in enumerate(animals):
    if index % 2 == 0:
        continue
    print(index, animal)

# And we can keep editing or adding commands
animals = ["Raphael", "Michaelangelo", "Donatello", "Leonardo"]
for index, animal in enumerate(animals):
    print(f"{+1}.\t{animal}")