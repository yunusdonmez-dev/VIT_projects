
import library_file

library_1 = library_file.Library('team_2_lib')

while True:
    selection = int(input('''
          
    1- Login
    2- Add user
    3- Add book
    0- Exit

'''))
    if selection == 0:
        break
    if selection == 1:
        name : input('Enter username : ') # type: ignore
        password : input('Enter password : ') # type: ignore

        library_1.login(name, password)

    if selection == 2:
        user = {
            'name' : input("name : "),
            'password' : input("password : ")
        }
        library_1.add_user(user)