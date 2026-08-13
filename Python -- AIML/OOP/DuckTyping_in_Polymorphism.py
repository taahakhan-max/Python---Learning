class Laptop:
    def build(self):
        print("Building a laptop.")
        
class Desktop:
    def build(self):
        print("Building a desktop.")
        
class Tablet:
    def read_pdf(self):
        print("Reading a PDF on the tablet.")
        
class Alien:
    def code(self, machine : Laptop):
        print("Alien is coding.")
        machine.build()
        
        
hp = Laptop()
sony = Desktop()
tablet = Tablet()
alien = Alien()

#alien.code(hp)
alien.code(sony)
