# Encapsulation with Access Modifiers (Private, Public, Protected)

# Private Access Modifier
'''class person:
    # Constructor
    def __init__(self, name, age):
        self.__name = name  # private attribute
        self.__age = age  # private attribute

    def display_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")
        
Person1 = person("Alice", 30)
# Accessing private attributes directly will raise an AttributeError

Person1.display_info()  # This will work and display the information        '''


'''
# Protected Access Modifier
class Employee:
    def __init__(self, name, salary):
        self._name = name  # protected attribute
        self._salary = salary  # protected attribute

        
class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def display_info(self):
        print(f"Name: {self._name}, Salary: {self._salary}")
        
        
Manager1 = Manager("Bob", 50000)
Manager1.display_info()  # This will work and display the information
'''

# Public Access Modifier
class Car:
    def __init__(self, make, model):
        self.make = make  # public attribute
        self.model = model  # public attribute

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}")

Car1 = Car("Toyota", "Camry")
Car1.display_info()  # This will work and display the information