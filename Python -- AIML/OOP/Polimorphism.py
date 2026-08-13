class shape:
    def area(self):
        return "The area of the figure"
    
class rectangle(shape):
    def __init__(self, width, hieght):
            self.width = width
            self.hieght = hieght
            
    def area(self):
         return self.width*self.hieght
        
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius
    
def print_area(shape):              # Using polymorphism
    print(f"The area of shape is {shape.area()}")    
    
Rectangle = rectangle(4,5)
Circle    = circle(4)

print_area(Rectangle)
print_area(Circle)                