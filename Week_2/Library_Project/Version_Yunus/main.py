## This is main

import book_transactions
import time
import user_transactions
import os
import kitap_islemleri

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear') # Clear terminal

def home_page():
    clear_terminal()
    # This function prints welcomeing page of th the library
    print('-'*80)
    print(f"-   {'WELCOME TO OUR LIBRARY'.center(74,' ')} -")
    print(f"- {' '*76} -")
    print(f"-   {'USER TRANSACTIONS':<20} 1{' ':<52} -" )
    print(f"-   {'BOOK TRANSACTIONS':<20} 2{' ':<52} -" )
    print(f"-   {'EXIT':<20} 0{' ':<52} -" )
    print(f"- {' '*76} -")
    print('-'*80)
    print(' '*80)

def user_page():
        # This function prints welcomeing page of the user section(members)
    clear_terminal()
    print('-'*80)
    print(f"- {' '*76} -")
    print(f"-   {'MEMBERS':<20} = 1{'='.center(20,' ')} {'LENT BOOK':<20} = 5{'-'.rjust(7,' ')}" )
    print(f"-   {'ADD MEMBER':<20} = 2{'='.center(20,' ')} {'RETURN BOOK':<20} = 6{'-'.rjust(7,' ')}" )
    print(f"-   {'SEARCH MEMBER':<20} = 3{'='.center(20,' ')} {'BOOK STATUS':<20} = 7{'-'.rjust(7,' ')}" )
    print(f"-   {'DELETE MEMBER':<20} = 4{'='.center(20,' ')} {'EXIT':<20} = 0{'-'.rjust(7,' ')}" )
    print(f"- {' '*76} -")
    print('-'*80)
    print(' '*80)

def book_page():
        # This function prints welcomeing page of the book section 
    clear_terminal()
    print('-'*80)
    print(f"- {' '*76} -")
    print(f"-   {'SHOW BOOKS':<20} = 1{'-'.rjust(52,' ')}" )
    print(f"-   {'ADD BOOK':<20} = 2{'-'.rjust(52,' ')}" )
    print(f"-   {'SEARCH BOOK':<20} = 3{'-'.rjust(52,' ')}" )
    print(f"-   {'DELETE BOOK':<20} = 4{' '.center(20,' ')} {'EXIT':<10} = 0{'-'.rjust(17,' ')}" )
    print(f"- {' '*76} -")
    print('-'*80)
    print(' '*80)

while True: # 'While' is used to have continuous intereaction till user choose 'exit'
  
    home_page()    # Show homepage
    
    selection = int(input("Please choose the code of your selection: "))   # Take user selection
    if selection == 1: # User transactions

        user_page()
        # Take user selecion 
        selection = int(input("Please choose the code of your selection: "))
        if selection == 1:                      # Show all the members
            user_transactions.show_users()
        elif selection == 2:                      # Add user
            user_transactions.add_user()
        elif selection == 3:                      # Search user
            user_transactions.search_user()
        elif selection == 4:                      # Delete user
            user_transactions.delete_user()
        elif selection == 5:                      # Lent user
            user_transactions.lent_book()
        elif selection == 6:                      # Return user
            user_transactions.return_book()
        elif selection == 0:                      # exit
            # Back to home page or direct exit ???
            continue
        else :
            print('Invalid selection. Choose a valid code!')
            continue

    elif selection == 2: # Book transaction
        book_page()
        # Take user selecion 
        selection = int(input("Please choose the code of your selection: "))
        if selection == 1:
            # book_transactions.show_books()
            kitap_islemleri.kitaplari_listele()
        elif selection == 2:
            book_transactions.add_book()
        elif selection == 3:
            book_transactions.search_book()
        elif selection == 4:
            book_transactions.delete_book()
        elif selection == 0:
            continue
        else:
            print('Invalid code. Please enter a valid code')
            continue
    elif selection == 0:
        print("Thanks for using our library, see you soon ")#print exit messeage
        break
    else :
        print('Invalid selection. Choose a valid code!')
        continue

