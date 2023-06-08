class Drinks: # Brand new class
    this_is_a_property = {
        "key_1": 'Value 1'
    } # Property is a dictionary now
    this_list = ['Pepsi', 'Coca Cola', 'Dr Pepper'] 
the_drink = Drinks() # This will instantiate the class (meaning it will activate the class)
print(the_drink.this_is_a_property['key_1']) # To access the key, as we would with any dictionary, we would use ['DictionaryKeyHere']

# We can also index and slice the list included above
print(the_drink.this_list[2]) # Each item of the list has an index
