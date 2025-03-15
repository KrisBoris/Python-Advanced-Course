# Example 46 - Object Orientated Programming

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print(f"{self.make} {self.model} is driving")

    def stop(self):
        print(f"{self.make} {self.model} stopped")


car = Car("Tesla", "Model S", "2019")
car.drive()
car.stop()
