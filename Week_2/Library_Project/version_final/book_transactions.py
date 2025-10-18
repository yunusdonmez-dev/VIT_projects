## All function about user transactions are here listed
import os
import json

def show_books():
    # Show all books in the library
    # Read books.json file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    json_path = os.path.join(current_dir, 'books.json')

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        books = [item['Kitap_Adi'] for item in data]
        i = 0
        for book in books:
            i += 1
            print(f"{i}. {book}")
    input('Please press enter to cotinue')

def search_book():
    # Take an input from user, barcode or book name. Then list all books that have given string value in the name
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, 'books.json')

    search_word = input("Enter the barcode or the name of the book : ")

    try :
        barcode = int(search_word) # If the input is an integer then we assume its barcode
        name = None
    except :
        name = search_word
        barcode = None
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if name != None:
        books = list(filter(lambda x : name.lower() in x['Kitap_Adi'].lower(), data))
    elif barcode != None:
        books = list(filter(lambda x : barcode == x['Barkod'], data))

    for book in books:
        print(f"{book['Barkod']}- {book['Kitap_Adi']}")

def add_book():
    # Get the book information from user and add the book to our database/library
    try:
        barcode = int(input('Scan the barcode(13 digits) :'))
        book_name = input("Enter book name : ")
        language = input("Enter the language if the book : ")
        price = int(input("Whats the price : "))
        publisher = input("Publisher : ")
        author = input("Who is the author : ")
    except:
        print('Invalid input')

    
    # if the file is there then just read and write
    # If its not there we need to create it first

    current_dir = os.path.dirname(os.path.abspath(__file__))
    books_json_path = os.path.join(current_dir, 'books.json')

    with open(books_json_path, 'r', encoding= 'utf-8') as f:
        data = json.load(f)
        print("OK:", type(data), "items:", len(data) if isinstance(data, list) else "n/a")

        new_book = {
        'Barkod' : int(barcode),
        'Dil' : language,
        'Fiyat' : int(price),
        'Kitap_Adi' : book_name,
        'Yayinevi' : publisher,
        'Yazar' : author
         }
        
        data.append(new_book)

    with open(books_json_path ,'w' , encoding='utf-8') as f:
        json.dump(data,f, ensure_ascii=False, indent=4)
        
        input('Book is succesfully saved. Please press enter to continue...')

def delete_book(barcode):

    current_dir = os.path.dirname(os.path.abspath(__file__))
    books_json_path = os.path.join(current_dir, 'books.json')

    with open(books_json_path, 'r', encoding= 'utf-8') as f:
        data = json.load(f)
        book = filter(lambda x:x['Barkod'] == barcode, data)

        data.remove(book)

    with open(books_json_path ,'w' , encoding='utf-8') as f:
        json.dump(data,f, ensure_ascii=False, indent=4)
        
        # input('Book is succesfully deleted. Please press enter to continue...')    
