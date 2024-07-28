class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
class classic_book(Book):    
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"classic_book: {super().__str__()}"    
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {super().__str__()}, File Size: {self.file_size} MB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {super().__str__()}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)

# Example usage:
if __name__ == "__main__":
    library = Library()
    classic_book = Book ("Pride and Prejudice", "Jane Austen")
    ebook1 = EBook("Snow Crash", "Neal Stephenson", 500)
    printbook1 = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)
    library.add_book(classic_book)
    library.add_book(ebook1)
    library.add_book(printbook1)
    library.list_books()
