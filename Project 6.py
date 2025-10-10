library = {
    "Python101": "Available",
    "DataScience": "Available",
    "Algorithms": "Available"
}
borrowed_books = set()

    
while True:
    print("\nLibrary Menu:")
    print("1 - Add Book")
    print("2 - Borrow Book")
    print("3 - Return Book")
    print("4 - View All Books")
    print("5 - Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        book_name = input("Enter the name of the book to add: ")
        book_key = book_name.strip().title()
        if book_key in library:
            print(f"The book '{book_key}' already exists in the library.")
        else:
            library[book_key] = "Available"
            print(f"The book '{book_key.title()}' has been added to the library.")
    elif choice == '2':
        book_name = input("Enter the name of the book to borrow: ")
        book_key = book_name.strip().lower()
        if book_key in library:
            if library[book_key] == "Available":
                library[book_key] = "Borrowed"
                borrowed_books.add(book_key)
                print(f"You have borrowed '{book_key.title()}'.")
            else:
                print(f"Sorry, '{book_key.title()}' is currently borrowed.")
        else:
            print(f"The book '{book_key.title()}' does not exist in the library.")
    elif choice == '3':
        book_name = input("Enter the name of the book to return: ")
        book_key = book_name.strip().lower()
        if book_key in library:
            if library[book_key] == "Borrowed":
                library[book_key] = "Available"
                borrowed_books.remove(book_key)
                print(f"You have returned '{book_key.title()}'.")
            else:
                print(f"The book '{book_key.title()}' was not borrowed.")
        else:
            print(f"The book '{book_key.title()}' does not exist in the library.")
    elif choice == '4':
        print("\nCurrent Books in the Library:")
        for book, status in library.items():
            print(f"{book.title()}: {status}")
        print(f"Total books: {len(library)}")
        print(f"Borrowed books: {len(borrowed_books)}")
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-5).")