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

    def __lt__(self, other):
        if self.pages < other.pages:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.pages > other.pages:
            return True
        else:
            return False

    def __add__(self, other):
        return self.pages + other.pages

    def __contains__(self, item):
        if item in self.title or item in self.author:
            return True
        else:
            return False

    def __getitem__(self, key):
        match key:
            case "title":
                return self.title
            case "author":
                return self.author
            case "pages":
                return self.pages
            case _:
                return f"Key {key} is invalid"


book1 = Book("Sherlock Holmes", "Sir Arthur Conan Doyle", 335)
book2 = Book("Herkules Poirot", "Agatha Christine", 210)
book3 = Book("The Lord of The Rings", "J.R.R. Tolkien", 421)
book4 = Book("The Lord of The Rings", "J.R.R. Tolkien", 421)

print(book3)
print(book3 == book4)
print(book1 > book2)
print(book2 < book1)
print(book1 + book2)
print("Rings" in book3)
print(book1["title"])
