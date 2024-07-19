class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        print(f"Deleting {self.title}")

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

# Example usage:
if __name__ == "__main__":
    book = Book("The Catcher in the Rye", "J.D. Salinger", 1951)
    print(book)  # Output: The Catcher in the Rye by J.D. Salinger, published in 1951
