# Example 53 - Static methods

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        print(f"{self.name} works as {self.position}")

    @staticmethod
    def is_valid(position):
        positions = ("Programmer", "Accountant", "Manager", "Security Guard")
        return positions in positions


employee1 = Employee("Eliot", "Programmer")
employee2 = Employee("Angela", "Accountant")
employee3 = Employee("Darline", "Hackerwoman")

employee1.get_info()
employee2.get_info()
employee3.get_info()
print(Employee.is_valid(employee3.position))
