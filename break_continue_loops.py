# Using lists

items = ["One", "Two", "Three", "Four", "Five"]
# Example 1
for item in items:
    if item == "Two" or item == "Four":
        continue  # Instruction here is to start printing and skip numbers included, but then continue printing the list
    print(item)

# Example 2
for item in items:
    if item == "Three":
        break # Instruction here is to start printing and 'break'/stop the command at the item selected
    print(item)

# Example 3
num = 0

while num <= 20:
    num = num + 1
    if num % 2 == 0: # This means that if any number divided by 2 has a reminder of 0, it will ignore
        continue
    print(num)

# Example 4
num = 0

while num <= 1_000_000:
    if num == 13:
        break
    print(num)