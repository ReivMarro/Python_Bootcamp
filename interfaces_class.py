class Animal:
    fur_color = "Yellow"
    def speak(self):
        raise NotImplementedError # This is a blueprint that tells us that if you want to use this method you have to implement it yourself
    def eat(self):
        pass # We need 'pass' so the command allows the function and indentation (without creating error)

    def chase(self):
        pass

class HouseCat(Animal):
    def speak(self):
        print("Meow") # And so (continue from line 4) it is our job to implement this by overwriting it

cat = HouseCat()
cat.speak()
