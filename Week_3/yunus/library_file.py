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
    
    def add_book(self, book : dict): # -- > 
        ''''
        This functian takes a book in dictionary format and add this to books.json file
        '''
        current_dir = os.path.dirname(os.path.abspath(__file__)) # This finds current directory to be make it work on every system
        books_json = os.path.join(current_dir, 'books.json') # Add books.json to current path
        
        if os.path.exists(books_json) == False:
            with open(books_json, 'w',encoding='utf-8') as f: 
                json.dump([], f)

        with open(books_json, 'r', encoding='utf-8') as file:
            books = json.load(file)
            books.append(book)
        with open(books_json, 'w', encoding='utf-8') as file:
            json.dump(books, file, ensure_ascii=False ,indent=4)
        print('Book is added')

    def add_user(self, user : dict):

        current_dir = os.path.dirname(os.path.abspath(__file__))
        users_json = os.path.join(current_dir, 'users.json')

    # Make a transactions.json file if it is not already there
        if os.path.exists(users_json) == False:
            with open(users_json, 'w',encoding='utf-8') as f: 
                json.dump([], f)

        with open(users_json, 'r', encoding='utf-8') as file:
            users = json.load(file)
            users.append(user)
        with open(users_json, 'w', encoding='utf-8') as file:
            json.dump(users, file, ensure_ascii=False ,indent=4)
        print('User is added')

    def login(self, name : str, password: str):

        current_dir = os.path.dirname(os.path.abspath(__file__))
        users_json = os.path.join(current_dir, 'users.json')

        with open(users_json, 'r', encoding='utf-8') as file:
            users = json.load(file)
            user = list(filter(lambda user: user['name'] == name and user['password'] == password, users))
            if not user[0]['name'] is None:
                print(f"{user[0]['name']} is logged in.")
                return user 