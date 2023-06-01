import requests

req = requests.get("https://swapi.dev/api/people/12") # Simple request
person = req.json() # person will be whatever the respond turns out to be turned into '.json'
print(person) # The result/ information given in the terminal will look like a dictionary
# With the information obtained from above then we can print statements
print(f"Name is \t\t{person['name']}") # the \t is to tab the info
print(f"Birth year is \t\t{person['birth_year']}")

# We can also include this in a 'for' loop
print("Films involved in:") 
for film in person['films']:
    req = requests.get(film)
    film = req.json() # And here we have turned part of the info into a .json
    print("Film is: ", film ['title'])