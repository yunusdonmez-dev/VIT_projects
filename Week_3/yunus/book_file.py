
class Book():
    def __init__(self,title,author,publication_year,is_borrowed=False,borrowed_by=None):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_borrowed = is_borrowed
        self.borrowed_by = borrowed_by

    def show_info(self):
        print(f"""
Title: {self.title}      
Author: {self.author}       
Publication Year: {self.publication_year} 
Status: {"Borrowed" if self.is_borrowed else "Available"}  
              """)
        
    def borrow(self,user): # Odunc verme
        if self.is_borrowed:
            print(f"'{self.title}' is already borrowed by '{self.borrowed_by}'.")
        else:
            self.is_borrowed = True
            self.borrowed_by = user
            user.borrowed_books.append(self)
            print(f"'{user.name}' has successfully borrowed '{self.title}'.")

    def return_book(self,user):
        if self.is_borrowed and self.borrowed_by == user:
            self.is_borrowed = False
            self.borrowed_by = None
            user.borrowed_books.remove(self)
            print(f"'{user.name}' has successfully returned '{self.title}'.")
        elif not self.is_borrowed:
            print(f"'{self.title}' is already in the library.")
        else:
            print(f"'{self.title}' was borrowed by another user.")

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "publication_year": self.publication_year,
            "is_borrowed": self.is_borrowed,
            "borrowed_by": self.borrowed_by.name if self.borrowed_by else None
        }
    

class Novel(Book):
    def __init__(self, title, author, publication_year, genre, is_borrowed=False):
        super().__init__(title, author, publication_year, is_borrowed)
        self.genre = genre

class Magazine(Book):
    def __init__(self, title, author, publication_year, issue, is_borrowed=False):
        super().__init__(title, author, publication_year, is_borrowed)
        self.issue = issue