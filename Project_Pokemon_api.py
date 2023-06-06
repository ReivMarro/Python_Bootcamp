# 1. Ask for user input
# 2. Create a dynamic URL based on step 1
# 3. Fetch the data from the URL in step 2
# 4. Print out the jason data (but because it is jason we need to convert it to a dictionary, not print out yet)
# 5. Print out pokemon data

import requests

pokemon = input("What Pokemon do you want to find? ")
pokemon = pokemon.lower() # Step 1 completed. I need to specify pokemon.lower since we are working with a mutable variable

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}" # Step 2, dynamic URL

req = requests.get(url) # This needs 'import requests' at the beginning
if req.status_code == 200: # This links to line 27. Made in case a non-existent pokemon name is 'input'
    data = req.json() # This covers step 4

    print(f"Name is \t\t{data['name']}") 
    print("Abilities:") 
    for ability in data['abilities']:
        print(ability['ability']['name'])

else:
    print("Pokemon not found")