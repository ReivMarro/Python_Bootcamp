# Reason why we try to catch an except errors is to keep the code running
# Otherwise the code would encounter an error and die (stop working)
num = input("Enter a number: ")
num2 = input("Enter a second number: ")
try:
    num = int(num)
    num2 = int(num2)
    total_num = num / num2
except ValueError:
    print("Num or Num2 were not valid numbers") # This works like an 'if', 'elif', 'else' statement
# If the value entered at 'input' is not what we expect, it can be caught
except ZeroDivisionError: # We can keep catching exceptions for code to be printed
    print("Numbers could not be divided")
except Exception as e:
    print("Exception was caught")
    print(type(e))

print(num)