# Example 55 - Magic methods

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        if self.title == other.title and self.author == other.author:
            return True
        else:
            return False


book1 = Book("Sherlock Holmes", "Sir Arthur Conan Doyle", 335)
book2 = Book("Herkules Poirot", "Agatha Christine", 210)
book3 = Book("The Lord of The Rings", "J.R.R. Tolkien", 421)
book4 = Book("The Lord of The Rings", "J.R.R. Tolkien", 421)

print(book3 == book4)

