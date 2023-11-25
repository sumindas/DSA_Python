class Car:
    def __init__(self, make, model):
        self.make = make  # Public attribute
        self.__model = model  # Private attribute

    def drive(self):
        return f"{self.make} {self.__model} is driving."

    def __engine_start(self):  # Private method
        return "Engine started."

    def start(self):  # Public method
        return self.__engine_start()

# Creating an instance of the Car class
my_car = Car("Toyota", "Camry")

# Accessing public attributes and methods
print(my_car.make)          # Output: Toyota
print(my_car.drive())       # Output: Toyota Camry is driving.
print(my_car.start())       # Output: Engine started.

# Attempting to access a private attribute or method
# This will raise an AttributeError
print(my_car.__model)
print(my_car.__engine_start())
