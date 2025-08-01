class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False 
    
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        return not self._is_checked_out
    
    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self, title, author):
        new_book = Book(title, author)
        self._books.append(new_book)
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    return True
        return False
    
    def return_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower() and not book.is_available():
                if book.return_book():
                    return True
        return False
    
    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books available in the library.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")