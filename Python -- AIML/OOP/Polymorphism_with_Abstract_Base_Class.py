# Polymorphism with Abstract Base Class
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"
    
class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"
    
def start_vehicle(vehicle):  # Using polymorphism
    print(vehicle.start_engine())
    
car = Car()
motorcycle = Motorcycle()

start_vehicle(car)
start_vehicle(motorcycle)                