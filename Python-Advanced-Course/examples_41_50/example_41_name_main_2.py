# Example 41 - If name == __main__

from example_41_name_main import *


def favourite_animal(animal):
    print(f"Your favourite animal is {animal}")


def main():
    favourite_animal("cat")
    favourite_color("yellow")


if __name__ == '__main__':
    main()