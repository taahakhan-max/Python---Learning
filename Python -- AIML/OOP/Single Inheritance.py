class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def makeSound(self):
        print(f"{self.species} make sound like {self.name}")
        
class Cat(Animal):
    def __init__(self, name, breed):
        self.name = name 
        self.breed = breed            \
            
    def makeSound(self):
         
         print(f"{self.breed} make sound like {self.name}")
         
a = Animal("Dog", "Dog")
a.makeSound()

b = Cat("Cat", "Pointer")
b.makeSound()         