# Object Oriented Programming in Python

# 1. Classes and Objects
class Animal:
    def __init__(self, name):
        self.name = name  # Encapsulation

    def speak(self):
        return f"{self.name} makes a sound."

# 2. __init__ and __str__ methods
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} barks."

    def __str__(self):
        return f"Dog(name={self.name}, breed={self.breed})"

# 3. Inheritance and Polymorphism
animals = [Animal("Generic"), Dog("Buddy", "Labrador")]
for a in animals:
    print(a.speak())  # Polymorphism

# 4. Encapsulation and Abstraction
class Vehicle:
    def __init__(self, brand):
        self._brand = brand  # Protected attribute

    def drive(self):
        raise NotImplementedError("Subclasses must implement drive method.")  # Abstraction

class Car(Vehicle):
    def drive(self):
        return f"{self._brand} car is driving."

my_dog = Dog("Max", "Beagle")
print(my_dog)  # Uses __str__

my_car = Car("Toyota")

