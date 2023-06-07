#First, we create an empty list called moves to store the names of all the moves available for the Pokémon:
moves = [move['move']['name'] for move in data['moves']]

#This list comprehension iterates over each move in the data['moves'] list and retrieves the name of the move using move['move']['name']. It collects all the move names in the moves list.
#Next, we use the random.sample() function to retrieve a random sample of moves from the moves list. The random.sample() function takes two arguments: the population (list) from which to choose the sample and the sample size (k).
random_moves = random.sample(moves, k=min(len(moves), 5))

#In this case, we choose a sample size of 5 or the total number of moves available (whichever is smaller). This ensures that if there are fewer than 5 moves available for the Pokémon, it will still retrieve all of them.
#The random.sample() function randomly selects unique elements from the moves list and returns a new list called random_moves.
#Finally, we iterate over the random_moves list and print each move:
for move in random_moves:
    print(move)

#This loop prints each move name on a separate line, displaying the randomly selected moves.
#By following these steps, you can obtain a random sample of moves from the Pokémon API and display them as desired.

# METHOD EXPLANATION:
#The approach of using random.sample() to obtain a random sample can work with any JSON data obtained from an API, as long as the structure of the JSON allows it.
#The key is to identify the appropriate list or collection of items from which you want to extract a random sample. In the provided code example, we extracted a random sample of moves from the "moves" section of the Pokémon API response.
#If the JSON data you obtain from an API contains a similar structure where you have a list of items from which you want to extract a random sample, you can adapt the code accordingly.
#Here's a general outline of the steps:
Parse the JSON response and access the relevant list or collection of items.
Create a list (let's call it items) that contains the desired attribute or value for each item in the list.
Use random.sample() to obtain a random sample from the items list.
Iterate over the random sample and perform any desired operations on each item.
By following this approach, you can extract a random sample from any JSON data obtained from an API, as long as you correctly identify the target list or collection within the JSON structure.