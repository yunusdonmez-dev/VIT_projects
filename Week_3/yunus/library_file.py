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
    
    def add_book(self, book): # -- > 
        ''''
        This functian takes a book and add this to library.books
        '''
        # Example data > book = ('suc ve ceza' , 'Dostoevsky' , 1895, True, user)
        self.books.append(book)
        print(f"'{book.title}' has been added to the library '{self.name}'.")

    def add_user(self, user):
        ''''
        This functian takes a user and add this to library.users
        '''
        # Example data > user = ('yunus' , [book1, book2] , 123asd)
        self.users.append(user)
        print(f"'{user.name}' has been added to the library '{self.name}'.")


    def login(self, name : str, password: str):
        self.load()
        for user in self.users:
            if user[1] == name and user[2] == password:
                print(f"Welcome, {user.name}! You logged in successfully.")
                return user
        print("Username or password didn't match.")
        return None        

    def show_all_books(self):
        print(f"All books that added to the library '{self.name}':")
        if self.books == []:
            print("  No available books.")
        else:
            for book in self.books:
                print(f" - {book.title}")

    def load(self):
        # load alle detail in json to library object
        current_dir = os.path.dirname(os.path.abspath(__file__)) # This finds current directory to be make it work on every system
        books_json = os.path.join(current_dir, 'books.json') # Add books.json to current path
        users_json = os.path.join(current_dir, 'users.json')
        temp_users=[]
        temp_books=[]                
        with open(users_json, "r",encoding='utf-8') as f: # Save library users to json/database   
            temp_users = json.load(f)
            for user in temp_users:
                self.users.append((user['name'], user['borrowed_books'], user['password']))         

        with open(books_json, "r",encoding='utf-8') as f: # Save library books to json/database
            temp_books = json.load(f)
            for book in temp_books:
                self.books.append((book['title'], book['author'], book['publication_year'], book['is_borrowed'], book['borrowed_by']))

    def save(self):
        current_dir = os.path.dirname(os.path.abspath(__file__)) # This finds current directory to be make it work on every system
        books_json = os.path.join(current_dir, 'books.json') # Add books.json to current path
        users_json = os.path.join(current_dir, 'users.json')
        temp_users=[]
        temp_books=[]
        with open(users_json, "w",encoding='utf-8') as f: # Save library users to json/database
            for u in self.users:
                temp_users.append(u.to_dict())
            json.dump(temp_users,f, indent=4, ensure_ascii=False)   

        with open(books_json, "w",encoding='utf-8') as f: # Save library books to json/database
            for b in self.books:
                temp_books.append(b.to_dict())
            json.dump(temp_books,f, indent=4, ensure_ascii=False) 
        
    def exit(self):
        print('Thanks for using')
        Library.save(self)

