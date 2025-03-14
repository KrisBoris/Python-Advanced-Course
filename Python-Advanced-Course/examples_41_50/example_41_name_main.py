# Example 41 - If name == __main__

def favourite_color(color):
    print(f"Your favourite color is {color}")


def main():
    favourite_color("blue")


# This line wil be always executed when imported
favourite_color("blue")


if __name__ == '__main__':
    main()

# To check script's attributes
# print(dir())
