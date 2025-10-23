import json
import os
class Book():
    def __init__(self,title,author,publication_year,is_borrowed=False):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_borrowed = is_borrowed
        self.borrowed_by = None

    def show_info(self):
        print(f"""
Title: {self.title}      
Author: {self.author}       
Publication Year: {self.publication_year} 
Status: {"Borrowed" if self.is_borrowed else "Available"}  
              """)
        
    def borrow(self,user):
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

class User():
    def __init__(self,name,password):
        self.name = name
        self.password = password
        self.borrowed_books = []

    def borrow_book(self,book):
        book.borrow(self)

    def return_book(self,book):
        book.return_book(self)

    def list_borrowed_books(self):
        print(f"Borrowed books of user '{self.name}':")
        if not self.borrowed_books:
            print("  No borrowed books.")
        else:
            for book in self.borrowed_books:
                print(f"  - {book.title}")

    def to_dict(self):
        return {
            "name" : self.name,
            "password":self.password,
            "borrowed_books":self.borrowed_books
        }
    
class Library:
    def __init__(self,name,books=None,users=None):
        self.name = name
        self.books = books if books is not None else []
        self.users = users if users is not None else []
    
    def add_book(self,book):
        self.books.append(book)
        print(f"'{book.title}' has been added to the library '{self.name}'.")

    def add_user(self,user):
        self.users.append(user)
        print(f"User '{user.name}' has been added to the library '{self.name}'.")

    def show_all_books(self):
        print(f"All books that added to the library '{self.name}':")
        if self.books == []:
            print("  No available books.")
        else:
            for book in self.books:
                print(f" - {book.title}")

    def login(self,name,password):
        for user in self.users:
            if user.name == name and user.password == password:
                print(f"Welcome, {user.name}! You logged in successfully.")
                return user
        print("Username or password didn't match.")
        return None
    
    def save(self):
        current_dir = os.path.dirname(os.path.abspath(__file__)) # This finds current directory to be make it work on every system
        books_json = os.path.join(current_dir, 'books.json') # Add books.json to current path
        users_json = os.path.join(current_dir, 'users.json')
        
        with open(books_json, "w",encoding='utf-8') as f: # Save library books to json/database
            json.dump([], f)
            json.dump(self.books,f, indent=4, ensure_ascii=False)

        with open(users_json, "w",encoding='utf-8') as f: # Save library users to json/database
            json.dump([], f)
            json.dump(self.users,f, indent=4, ensure_ascii=False)

    def exit(self):
        print('Thanks for using')
        Library.save(self)
    
library1 = Library('yunus')
book1 = Book("1984", "berat", 2025)
book2 = Book("2025", "berat", 2025)
user1 = User("berat",12345)
library1.add_book(book1)
library1.add_book(book2)
library1.add_user(user1)
library1.exit()