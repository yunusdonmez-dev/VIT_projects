#library.py

import json
from book import Book
from user import User


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def show_all_books(self):
        for book in self.books:
            book.show_info()

    def login(self, name, password):
        for user in self.users:
            if user.name == name and user.password == password:
                return user
        print("Invalid credentials.")
        return None

    def save(self, file):
        data = {
            "books": [b.to_dict() for b in self.books],
            "users": [u.to_dict() for u in self.users]
        }
        with open(file, "w") as f:
            json.dump(data, f, indent=4)

    def load(self, file):
        try:
            with open(file, "r") as f:
                data = json.load(f)
            print("Library data loaded successfully.")
        except FileNotFoundError:
            print("No previous data found.")
