# try:
#    print("Trying 1 / 0")
#    total = 1 - 0 # This will not execute
#    print("This will not show up")
# except Exception:
#    print("Exception was caught")
#    total = 0
# print(total)

num = input("What is a number? ")
try:
    num = int(num) # This tells that we can't manage the value 'error'
except Exception: # So it throws and catch that exception
    num = "Unknown" # Overwrites it and turns it into 'Unknown'

print(num)