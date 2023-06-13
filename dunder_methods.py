# Dunder methods = double underscore

class Animal:
    fur_color = "Yellow"

    def __init__(self, fur_color):
        self.fur_color = fur_color # This will automatically assign fur colour in a different method

    def speak(self):
        raise NotImplementedError 
    def eat(self):
        print("I am eating, yum!") 

    def chase(self, animal="Gazelle"):
        print("I am chasing a ", animal)
    
    def get_fur_color(self):
        print("Getting fur color: ", self.fur_color)

class HouseCat(Animal):
    fur_color = "White"
    def __init__(self, fur_color):
        super().__init__(fur_color)
        print("Fur color was chosen.")
        self.animal_type = "House Cat"
        print(self.animal_type)
    
        
    def speak(self):
        print("Meow") 

    def eat(self):
        super().eat() 
        print("I am eating salmon") 

    def chase(self, animal):
        super().chase(animal)
        print(animal, "was caught")

cat = HouseCat("White")
cat.get_fur_color() # Here we will have to use cat. + whatever property you want to trigger + ("the required positional argument we want to choose")
