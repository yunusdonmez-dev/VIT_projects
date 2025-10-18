## This module is for all functions related to user

import os
import json
import datetime
import time_module

def transaction_log(id, barcode):
    # This function hold the record of every transaction as log in json file.
    # This function takes many parameters. Which boek, who takes it, when , when due, boek info, user info
    # Or book barcode(unique) user id(unique) 
    current_dir = os.path.dirname(os.path.abspath(__file__))
    users_json_path = os.path.join(current_dir, 'users.json')
    books_json_path = os.path.join(current_dir, 'books.json')

    with open(users_json_path, 'r',encoding='utf-8') as f:
        users_data = json.load(f)
        user_data = list(filter(lambda x: x['Id'] == id, users_data)) # the user is filtered
    
    with open(books_json_path, 'r',encoding='utf-8') as f:
        books_data = json.load(f) 
        book_data = list(filter(lambda x: x['Barkod'] == barcode, books_data)) # the book is filtered

    transactions_json_path = os.path.join(current_dir, 'transactions.json')
    
    # Make a transactions.json file if it is not already there
    if os.path.exists(transactions_json_path) == False:
        with open(transactions_json_path, 'w',encoding='utf-8') as f: 
            json.dump([], f)

    with open(transactions_json_path, 'r',encoding='utf-8') as f:
        transactions_data = json.load(f)
        new_transaction = {
        'Id' : id,
        'User_name' : user_data[0]['User_name'],
        'Tel' : user_data[0]['Tel'],
        'Adres' : user_data[0]['Adres'],
        'barcode' : barcode,
        'Language' : book_data[0]['Dil'],
        'Price' : book_data[0]['Fiyat'],
        'Book_name' : book_data[0]['Kitap_Adi'],
        'publisher' : book_data[0]['Yayinevi'],
        'Author' : book_data[0]['Yazar'],
        'Start_date' : str(datetime.date.today()),
        'Due_date' : str(time_module.two_weeks_ahead())
         }
        transactions_data.append(new_transaction) # Add new transaction to the list

    with open(transactions_json_path ,'w',encoding='utf-8') as f:
        json.dump(transactions_data,f, ensure_ascii=False, indent=4)
def add_user():
    # Get the user information from user
    # Save the user in user.json via append

    user_name = input("Enter username: ")
    tel = input("Enter telefone number: ")
    adres = input("Enter adres: ")
    
    # if the file is there then just read and write
    # If its not there we need to create it first

    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, 'users.json')

    if os.path.exists(json_path) == False:
        with open(json_path, 'w') as f: 
            json.dump([], f)


    with open(json_path, 'r', encoding= 'utf-8') as f:
        data = json.load(f)
        next_id = max((item['Id'] for item in data), default=0) + 1   # A new id is generated bu system
        new_user = {
        'Id' : next_id if next_id > 0 else 1, # For the first
        'User_name' : user_name,
        'Tel' : tel,
        'Adres' : adres
         }
        data.append(new_user)

    with open(json_path ,'w' , encoding='utf-8') as f:
        json.dump(data,f, ensure_ascii=False, indent=4)
        
        input('User is succesfully saved. Please press enter to continue...')
def show_users():
    # This function prints all the users. Takes no argument
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, 'users.json')

    with open(json_path, 'r', encoding= 'utf-8') as f:
        data = json.load(f)
        users = ([item['Id'],item['User_name']] for item in data) # Take id and username to list all users
        for user in users:
            print(f"{user[0]}- {user[1]}")


    input('Please press enter to cotinue')
def search_user():
    # This function searchs and prints all the user that has given argument. 
    # This function takes a string or id(int) to search the realted users
    search = input('Enter the id or name of the user : ')
    try:
        id = int(search)
        search_word = None
    except:
        search_word = search
        id = None

    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, 'users.json')

    with open(json_path, 'r', encoding= 'utf-8') as f:
        data = json.load(f) 
        users = ([item['Id'],item['User_name']] for item in data) # Take id and username to list all users
        for user in users:
            if id != None:
                if id == user[0]:
                    print(f"{user[0]}- {user[1]}")
            elif search_word != None:
                if search_word.lower() in user[1].lower() :
                    print(f"{user[0]}- {user[1]}")
    input('Please press enter to cotinue')
def delete_user():
    input('This function is not ready yet! Press enter to continue')
def lent_book():

    # Lent a boek
    barcode = int(input("Enter the barcode of the book : "))

    current_dir = os.path.dirname(os.path.abspath(__file__))
    books_json_path = os.path.join(current_dir, 'books.json')

    with open(books_json_path, 'r',encoding='utf-8') as f:
        books_data = json.load(f) 
        book_data = list(filter(lambda x: x['Barkod'] == barcode, books_data)) # the book is filtered    
        if book_data[0]['Kitap_Adi'] != None:
            print(book_data[0]['Kitap_Adi'])
        else:
            print('Book is not available')
            # selection = int(input("Select : "))
            lent_book() # Call the function but how to exit ???
    
    user_id = int(input('Enter your user Id : '))

    users_json_path = os.path.join(current_dir, 'users.json')
    with open(users_json_path, 'r',encoding='utf-8') as f:
        users_data = json.load(f)
        user_data = list(filter(lambda x: x['Id'] == user_id, users_data)) # the user is filtered
        if user_data[0]['User_name'] != None:
            print(user_data[0]['User_name'])
        else:
            print('User is unknown. Try to be member')
            # lent_book() # Call the function but how to exit ???    

    transaction_log(user_id,barcode)
    # delete the book from the list
    print(f"Book is succesfully lended, due date is {str(time_module.two_weeks_ahead())}. Enjoy! ")
def return_book():

    barcode = int(input("Enter the barcode : "))

    current_dir = os.path.dirname(os.path.abspath(__file__))
    books_json_path = os.path.join(current_dir, 'books.json')

    with open(books_json_path, 'r', encoding='utf-8') as f:
        books = json.load(f)

        book = list(filter(lambda x:x['Barkod'] == barcode, books))[0]['Kitap_Adi']

    id = int(input("Enter the user id : "))

    users_json_path = os.path.join(current_dir, 'users.json')
    with open(users_json_path, 'r', encoding='utf-8') as f:
        users = json.load(f)

        user = list(filter(lambda x:x['Id'] == id, users))[0]['User_name']    



   
    # Add the book again to the list

return_book()
