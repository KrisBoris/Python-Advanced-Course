# Example 31 - Functions

def add(num_1, num_2):
    return num_1 + num_2


def create_full_name(name: str, surname: str):
    name = name.capitalize()
    surname = surname.capitalize()
    return name + " " + surname


print(add(2, 2))
print(create_full_name("terence", "fletcher"))
