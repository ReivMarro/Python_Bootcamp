courses = {
    "js": "JavaScript 101",
    "python": ["Python 101", "Python 201"],
    "html": "HTML 101"
} # We do not always necessarily know all the values in a dictionary
#print(courses) # That is to do some print debugging
#course['js']  # Sometimes this is a tedious way to do this
# And so there is an easier way than the shown above

# Example with info found in the dictionary:
print(courses.get("js", None)) # Reason to use None is to set a default in case we cannot get 'js'

# Example with info NOT found in the dictionary:
print(courses.get("css", "The course was not found")) # Adding a default text also work
if courses.get("react", "React 101"): # Without the default 'React 101' the command wouldn't print anything. Reason being is because there is no 'react' information in the dictionary
    print("You are enrolled in React 101")