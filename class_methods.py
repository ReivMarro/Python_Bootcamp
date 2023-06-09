class Drinks: # Brand new class
    this_is_a_property = {
        "key_1": 'Value 1'
    } # Property is a dictionary now
    this_list = ['Pepsi', 'Cola', 'Dr Pepper'] 
# All what is happening with the next lines is that we are encapsulating all that code within the class 'Drinks'
#These are different methods that we can use. They look like functions
# However they are not functions because they are inside a class which makes them a parameter of themselves or 'self'
    def add_name(self, name): # This method links to line 24
        self.this_list.append(name)
        return self.this_list
    
    def this_is_a_method(self):
        print(self.this_list)
# Underneath, we can define properties using methods (we can create a class variable based on a class function)
    @property # This is called a decorator
    def get_pepsi(self):
        return self.this_list[0]

the_drink = Drinks() # This will instantiate the class (meaning it will activate the class)
#the_drink.this_is_a_method() # By using this line and the next two we can choose an item from the list to print
#pepsi = the_drink.get_pepsi # By adding 'pepsi' at the beginning we are storing that bit of info, making it printable
#print("The best drink is", pepsi)
#the_drink.add_name("Fanta") # By using this line and the next one, we can add an item to the list
#print(the_drink.this_list)