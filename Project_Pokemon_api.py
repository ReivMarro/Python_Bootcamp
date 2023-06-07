# 1. Ask for user input
# 2. Create a dynamic URL based on step 1
# 3. Fetch the data from the URL in step 2
# 4. Print out the jason data (but because it is jason we need to convert it to a dictionary, not print out yet)
# 5. Print out pokemon data

import requests
import random

while True:
    pokemon = input("What Pokemon do you want to find? ")
    pokemon = pokemon.lower() # Step 1 completed. I need to specify pokemon.lower since we are working with a mutable variable

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}" # Step 2, dynamic URL

    req = requests.get(url) # This needs 'import requests' at the beginning (line 7)
    if req.status_code == 200: # This links to line 25. Made in case a non-existent pokemon name is 'input'
        data = req.json() # This covers step 4

        print(f"Name is {data['name']}")
        print("Type:")
        for type in data['types']:
            print(type['type']['name']) 
        print("Abilities:") 
        for ability in data['abilities']:
            print(ability['ability']['name'])
        print("Moves:") 
        moves = [move['move']['name'] for move in data['moves']]
        random_moves = random.sample(moves, k=min(len(moves), 4))
        for move in random_moves:
            print(move)
        break # This is optional. Added to make the function stop asking for Pokemon

    else:
        print("Pokemon not found")
        