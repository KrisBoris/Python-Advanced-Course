# Example 56  - Property

class Rectangle:

    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return f"{self.__height:.1f}cm"

    @property
    def width(self):
        return f"{self.__width:.1f}cm"

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self.__height = new_height
        else:
            print("Height must be greater than zero")

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self.__width = new_width
        else:
            print("Width must be greater than zero")

    @height.getter
    def height(self):
        return self.__height

    @width.getter
    def width(self):
        return self.__width

    @height.deleter
    def height(self):
        del self.__height
        print("Height deleted successfully")

    @width.deleter
    def width(self):
        del self.__width
        print("Width deleted successfully")


rectangle = Rectangle(4, 5)

print(rectangle.height)
print(rectangle.width)

rectangle.height = 5
rectangle.width = 6

print(rectangle.height)
print(rectangle.width)

del rectangle.height
del rectangle.width
