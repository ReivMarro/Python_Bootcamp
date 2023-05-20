name = "MR"
welcome_message = "Hello %s welcome to Python 101" % name
print(welcome_message) # This is the old way to input the command


# The two most modern ways to format are .format() and f""
name = "JMR"
welcome_message = "Hello {} welcome to Python 101".format(name)

print(welcome_message) # This however is not the most modern way to do this

welcome_message = f"Hello {name} welcome to Python 101".format(name)

print(welcome_message) # This is the most modern/efficient way to do this
