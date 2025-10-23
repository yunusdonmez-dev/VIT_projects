#book.py

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_borrowed = False
        self.borrewed_by = None

    def show_info(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"{self.title} by {self.author} ({self.publication_year}) - {status}")

    def borrow(self, user):
        if not self.is_borrowed:
            self.is_borrowed = True
            self.borrewed_by = user.name
            user.borrowed_books.append(self, title)
            print(f"{user.name} borrowed {self.title}.")
        else:
            print(f"{self.title} is already borrowed by {self.borrowed_by}.")

    def return_book(self):
        if self.is_borrowed = False
            print(f"{self.title} returned by {self.borrowed_by}.")
            self.is_borrowed = False
            self.borrewed_by = None
    
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "publication_year": self.publication_year,
            "is_borrowed": self.is_borrowed,
            "borrowed_by": self.borrowed_by
        }
