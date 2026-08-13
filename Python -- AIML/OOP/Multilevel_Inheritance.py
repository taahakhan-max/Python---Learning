class Animal:
    def __init__(self,name, species):
        self.species = species
        self.name = name
        
    def showDetails(self):
            print(f"The Animal is {self.species} ")
            print(f"The name is {self.name}")
            
class Dog(Animal):
    def __init__(self,name, breed):
        Animal.__init__(self, name, species = "Dog")
        self.breed = breed
         
    def showDetails(self):
        Animal.showDetails(self)
        print(f"The breed is {self.breed}")
        
class GoldenRetreiver(Dog):
    def __init__(self,name, colour):
        Dog. __init__(self,name , breed = "Golden Retriever")
        self.colour = colour
        
    def showDetails(self):
        Dog.showDetails(self)
        print(f"The colour is {self.colour}")
        
a = GoldenRetreiver("Tommy", "Golden")
a.showDetails()
    
            
            