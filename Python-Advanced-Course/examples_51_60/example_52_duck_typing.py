# Example 52 - Duck typing

from abc import ABC, abstractmethod
class Animal:

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):

    is_alive = True

    def speak(self):
        print("Woof!")


class Cat(Animal):

    is_alive = True

    def speak(self):
        print("Miau!")


class Car:

    is_alive = False

    def speak(self):
        print("Ka-Chow!")


animals = [Dog(), Cat(), Car()]
for animal in animals:
    # If class has required method it would work
    animal.speak()
