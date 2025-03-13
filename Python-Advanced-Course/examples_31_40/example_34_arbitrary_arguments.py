# Example 33 - Arbitrary arguments

def display_name(*args):
    for arg in args:
        print(arg, end=" ")
    print()


def display_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} - {value}", end=" ")
    print()


def display_employee(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for key, value in kwargs.items():
        print(f"{key} - {value}", end=" ")
    print()

display_name("Albus", "Percival", "Wolfrick", "Brian", "Dumbledore")
print("------------------------------------------------")
display_address(street="Baker Street", house="221B", city="London", country="U.K.")
print("------------------------------------------------")
display_employee("Albus", "Percival", "Wolfrick", "Brian", "Dumbledore",
                 street="Baker Street", house="221B", city="London", country="U.K.")
