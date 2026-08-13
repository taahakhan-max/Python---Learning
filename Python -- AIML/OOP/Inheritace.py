class Employee: 
    def __init__ (self, name, id, skill):
        self.name  = name
        self.id    = id
        self.skill = skill
        
    def showDetails(self):
        print(f"The id of {self.name} is {self.id}")                
        
class Programmer(Employee):
    def showLanguage(self):
            print(f"{self.name} is a programmer with id {self.id}")
            
class Developer(Employee):
    def showSkills(self):
        print(f"{self.name} id is {self.id} and skill is {self.skill}")
        
                
#a = Programmer("Taaha",3400)
#a.showLanguage()  
#b = Employee("Guru",3000)
#b.showDetails()       
c = Developer("Khan", 4333, "Python")
c.showSkills()