class Animal:
    fur_color = "Yellow"
    def speak(self):
        print("Rawwwwrr")
    def eat(self):
        pass # We need 'pass' so the command allows the function and indentation (without creating error)

    def chase(self):
        pass

class Lion(Animal): # This will extend into 'Tiger' all the methods included in the 'Animal' class
    def speak(self):
        print("Roaaar")

class HouseCat(Animal): # Again, it has inherited the 'Animal' methods except for speak which has been overwritten
    
    fur_color = "Black" # We can inherit the class (in this case 'Animal') but overwrite attributes or methods 

    def speak(self):
        print("Meow")

lion = Lion() # Here we have three options now. We can write 'Animal', 'Lion', 'HouseCat' and each will print a different thing
lion.speak()
cat = HouseCat()
cat.speak()
print(cat.fur_color)