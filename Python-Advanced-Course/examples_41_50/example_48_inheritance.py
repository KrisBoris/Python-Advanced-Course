# Example 48 - Inheritance

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} goes bark, bark")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} goes miau, miau")
