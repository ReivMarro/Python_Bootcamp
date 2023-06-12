class Animal:
    fur_color = "Yellow"
    def speak(self):
        raise NotImplementedError # This is a blueprint that tells us that if you want to use this method you have to implement it yourself
    def eat(self):
        print("I am eating, yum!") 

    def chase(self, animal="Gazelle"):
        print("I am chasing a ", animal)
    
    def nemesis(self):
        pass # We need 'pass' so the command allows the function and indentation (without creating error)

class HouseCat(Animal):
    def speak(self):
        print("Meow") # And so (continue from line 4) it is our job to implement this by overwriting it

    def eat(self):
        super().eat() # This will let us print the 'super' class (Animal) + the new class 'HouseCat'
        print("I am eating salmon") 

    def chase(self, animal):
        super().chase(animal)
        print(animal, "was caught")

cat = HouseCat()
cat.chase("mouse") # Here we will have to use cat. + whatever property you want to trigger + ("the required positional argument we want to choose")
