class Animal:
    def __init__ (self, species):
        self.species = species
        
    def makeSound(self):
        print(f"The sound is of {self.species} and it can run")
        
class Bird:
    def __init__(self, BirdType):
        self.BirdType = BirdType
        
    def makeawaaz(self):
            print(f"The sound is of {self.BirdType} can fly")
            
class Dragon(Animal, Bird):
    def __init__(self,name, species, BirdType):
        self.species = species
        self.BirdType = BirdType
        self.name = name
        
    def Mutant(self):
                print(f"The sound is of {self.name} and it is a {self.species} {self.BirdType} ")
                
a = Animal("Lion")
a.makeSound()

b = Bird("Eagle")
b.makeawaaz()

c = Dragon("DRAGON", "Lion", "Eagle")
c.Mutant()
                 
                            