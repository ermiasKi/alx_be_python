class Book:
    def __init__(self, title:str, author:str) -> None:
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title: str, author: str, file_size:int) -> None:
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count:int) -> None:
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    def __init__(self) -> None:
        self.books =  []

    def add_book(self,book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            typ = type(book).__name__
            if typ == "Book":
                print(f"{typ}: {book.title} by {book.author}")
            elif typ == "EBook":
                print(f"{typ}: {book.title} by {book.author}, File Size: {book.file_size}KB")
            else:
                print(f"{typ}: {book.title} by {book.author}, Page Count: {book.page_count}")