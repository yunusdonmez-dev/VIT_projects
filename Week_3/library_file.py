import os
import json

class Library():
    '''
    This library class
    '''
    def __init__(self, name):
        self.name = name
        self.users= []
        self.books= []
    
    def add_book(book): # -- > print informatie
        ''''
        This functian takes a book in dictionary format and add this books.json file
        '''
        books_json = os.path.dirname(os.path.abspath(__file__)).join('books.json')
        with open(books_json, 'r+', encoding='utf-8') as file:
            books = json.load(file)
            books.append(book)
            json.dump(books, file, ensure_ascii=False ,indent=4)
        print('Book is added')

    def add_user(self, user):
        users_json = os.path.dirname(os.path.abspath(__file__)).join('users.json')
        with open(users_json, 'r+', encoding='utf-8') as file:
            users = json.load(file)
            users.append(user)
            json.dump(users, file, ensure_ascii=False ,indent=4)
        print('User is added')

    def login(name, password):
        users_json = os.path.dirname(os.path.abspath(__file__)).join('users.json')
        with open(users_json, 'r', encoding='utf-8') as file:
            users = json.load(file)
        user = filter(lambda user: user['name'] == name and user['password'] == password, users)
        if not user['name'] is None:
            print(f"{user['name']} is logged in.")
            return user 