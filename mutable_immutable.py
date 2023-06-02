# Strings are immutable
string = "This is string 1"
string = "Overwritten. This is now string 1"

print(string.upper())
print(string)

# Lists use immutable strings inside but the list itself is mutable
# For example, the order of the list can be changed: we can add to it, we can append it, etc
names = ["JMR", "JRM", "RMJ", "MRJ"]
names.append("JR")
print(names)