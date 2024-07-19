from library_management import Book, Library

def main():
    library = Library()

    # Adding books to the library
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("1984", "George Orwell")
    book3 = Book("To Kill a Mockingbird", "Harper Lee")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Listing available books
    library.list_available_books()

    # Checking out a book
    if library.check_out_book("1984"):
        print("Checked out '1984'")
    else:
        print("'1984' is not available")

    # Listing available books after checkout
    library.list_available_books()

    # Returning a book
    if library.return_book("1984"):
        print("Returned '1984'")
    else:
        print("'1984' was not checked out")

    # Listing available books after return
    library.list_available_books()

if __name__ == "__main__":
    main()
