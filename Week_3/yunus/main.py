
import library_file
import user_file
import book_file

library_1 = library_file.Library('team_2_lib')

while True:
    selection = int(input('''
          
    1- Login
    2- Add user
    3- Add book
    0- Exit

'''))
    if selection == 0:
        library_1.exit()
        break
    elif selection == 1:

        name = input('Enter username : ') 
        password = input('Enter password : ') 

        library_1.login(name, password)

    elif selection == 2:
        name = input('Enter username : ') 
        password = input('Enter password : ') 
        user = user_file.User(name, password)
        library_1.add_user(user)

    elif selection == 3:
        title = input('Enter book title : ') 
        author = input('Enter author : ') 
        publication_year = input('Publication year : ') 

        book = book_file.Book(title, author , publication_year)
        library_1.add_book(book)