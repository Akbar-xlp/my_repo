class Book:
    def __init__(self, title, author):
        self.title = title
        self.__author = author

    def get_title(self):
        return self.title

    def get_author(self):
        return self.__author

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        self.__author = author


book_1 = Book("Python", "User")
print(book_1.title)
book_1.title = "Java"
print(book_1.title)
print(book_1.author)
book_1.author = "Person"
print(book_1.author)

