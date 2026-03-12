class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Новий клас Fish без методу speak
class Fish(Animal):
    pass

animals = [Dog(), Cat(), Fish()]

for animal in animals:
    print(f"{type(animal).__name__} каже: {animal.speak()}")