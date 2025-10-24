import json
import os

class Book():
                
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_borrowed = False            #False=kitap kutuphanede. True=kitap alinmis. False ile baslar
        self.borrowed_by = None             #basta kimse kitap almadigi icin None ile baslatilir. Biri aldiysa ismi yazilir
    
    def show_info(self):
        status = "Borrowed" if self.is_borrowed else "Available"   
        print("Book Info")
        print("Title :", self.title)
        print("Author:", self.author)
        print("Year  :", self.publication_year)
        print("Status:", status)


    def borrow(self, user):
        if not self.is_borrowed:                               #kitap kimse tarafindan alinmamissa, musaitse
            self.is_borrowed = True                            
            self.borrowed_by = user.name                       
            user.borrowed_books.append(self.title)             #basligi ekliyor
            print(f"{user.name} borrowed '{self.title}'.")
        else:                                                  #musait degilse kimin aldigini soyler   
            print(f"'{self.title}' is already borrowed by {self.borrowed_by}.")

    def return_book(self,user):
        if self.is_borrowed and self.borrowed_by == user.name:          #kitap biri tarafinda alinmissa
            self.is_borrowed = False                                    #kitap kutuphaneye geri dondu
            self.borrowed_by = None                                     #artik bir kullanicida degil
            user.borrowed_books.remove(self.title)
            print(f"'{user.name}' has successfully returned '{self.title}'.")
        
        elif not self.is_borrowed:
            print(f"'{self.title}' is already in the library.")
        
        else:
            print(f"'{self.title}' was borrowed by another user.")


    def to_dict(self):         # Kitap bilgisini JSON'a uygun hale getirir. 
        return {
            "title": self.title,
            "author": self.author,
            "publication_year": self.publication_year,
            "is_borrowed": self.is_borrowed,
            "borrowed_by": self.borrowed_by
            }
        

#-----------------------------------------------

class Novel(Book):
    def __init__(self, title, author, publication_year, genre):
        super().__init__(title, author, publication_year)           #book sinifinin __init__ methodunu cagirir
        self.genre = genre                  #genre= tur demek
        
    def to_dict(self):
        data = super().to_dict()            #book daki to_dict cagirilir
        data["genre"] = self.genre 
        return data
    
    
class Magazine(Book):
    def __init__(self, title, author, publication_year, issue):
        super().__init__(title, author, publication_year)
        self.issue = issue
        
    def to_dict(self):
        data = super().to_dict()
        data["issue"] = self.issue
        return data
    
#--------------------------------


class User():
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.borrowed_books = []
        
    def borrow_book(self,book):
        book.borrow(self)

    def return_book(self,book):
        book.return_book(self)

    def list_borrowed_books(self):
        print(f"Borrowed books of user '{self.name}': ")
        if not self.borrowed_books:
            print(" No borrowed books.")
        else:
            for title in self.borrowed_books:
                print(f"   - {title}")

    def to_dict(self):
        return {
            "name": self.name,
            "password": self.password,
            "borrowed_books": self.borrowed_books
        }

#--------------------------

class Library():
        def __init__(self, name):
           self.name = name
           self.books = []
           self.users = []

        def add_book(self,book):
           self.books.append(book)
           print(f"Book '{book.title}' added to the library.")

        
        def add_user(self, user):
            self.users.append(user)
            print(f"User '{user.name}' added to the library '{self.name}'.")


        def show_all_books(self):
            print(f"{self.name} - All Books: ")
            if not self.books:
                print("No books in de library yet.")

            else:
                for book in self.books:
                    book.show_info()

        def login(self, name, password):
            for user in self.users:
                if user.name == name and user.password == password:
                    print(f"Welcome, {name}!")
                    return user
            print("Invalid username or password.")
            return None            
           
#----------------------------
#json a kaydetme ve yukleme

        def save(self, filename="library_data.json"):
            data = {
                "name": self.name,                                          #kutuphanenin adi
                "books": [book.to_dict() for book in self.books],           #self.books içindeki her book nesnesi için book.to_dict() çağrılır.
                "users": [user.to_dict() for user in self.users]
            }
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            print(f"Library data saved to '{filename}'.")



        def load(self, filename="library_data.json"):           #kaydedilmis veriyi geri yukler (self nesnesine) yeniden kullanima sokar
            if not os.path.exists(filename):
                print("No saved data found.")
                return
            with open(filename, "r", encoding="utf-8") as f:
             data = json.load(f)                                #json.load(f) ile JSON formatındaki veri Python sözlüğüne (dict) çevrilir.

            self.name = data["name"]                            #kutuphanenin adi self.name olarak ayarlanir
            
            #Kitapları (books) Yeniden Oluşturma
            self.books = []                                     
            for b in data["books"]:                             
                if "genre" in b:
                    book = Novel(b["title"], b["author"], b["publication_year"], b["genre"])
                elif "issue" in b:
                    book = Magazine(b["title"], b["author"], b["publication_year"], b["issue"])
                else:
                    book = Book(b["title"], b["author"], b["publication_year"])
                book.is_borrowed = b["is_borrowed"]             #kitap oduncte mi
                book.borrowed_by = b["borrowed_by"]             #kim odunc aldi
                self.books.append(book)

            self.users = []
            for u in data["users"]:
                user = User(u["name"], u["password"])
                user.borrowed_books = u["borrowed_books"]
                self.users.append(user)

        def exit(self):
            print('Thanks for using')
            self.save()


#ana menu  
def main():
    library = Library("My Library")
    library.load()               # JSON varsa eski verileri yükle

    print("---Welcome to the Library System---")

    # Login veya yeni hesap oluşturma
    user = None                              #henuz giris yapmis bir kullanici yok
    while not user:                          #kullanıcı başarılı şekilde giriş yapana kadar döngü devam eder.
        print("1 - Log in")
        print("2 - Create new account")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Username: ")
            password = input("Password: ")
            user = library.login(name, password)
        elif choice == "2":                         #yeni hesap olusturma
            name = input("Choose a username: ")
            password = input("Choose a password: ")
            new_user = User(name, password)
            library.add_user(new_user)
            user = new_user
        else:
            print("Invalid choice. Try again.")


    while True:
        print(f"=== Library Menu ({user.name}) ===")
        print("1 - List all books")
        print("2 - Borrow a book")
        print("3 - Return a book")
        print("4 - Show my borrowed books")
        print("5 - Save and exit")

        choice = input("Select an option: ")

        if choice == "1":
            library.show_all_books()

        elif choice == "2":
            title = input("Enter the title of the book to borrow: ")
            for book in library.books:
                if book.title.lower() == title.lower():
                    user.borrow_book(book)              #kitap kutuphanede bulursa kullaniciya eklenir
                    break
            else:
                print("Book not found.")

        elif choice == "3":
            title = input("Enter the title of the book to return: ")
            for book in library.books:
                if book.title.lower() == title.lower():
                    user.return_book(book)                  #kitap kullanici listesinden silinir
                    break
            else:
                print("Book not found.")

        elif choice == "4":
            user.list_borrowed_books()

        elif choice == "5":
            library.exit()
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
