from book import Book; from user import User; from author import Author
import book_menu, user_menu, author_menu

def validate_menu_option(user_choice, max_menu_options):
    try:
        user_choice = int(user_choice)
        if user_choice < 1 or user_choice > max_menu_options:
            print(f"Invalid menu choice. Please enter a number between 1 and {max_menu_options}.")
            return False
        return True
    except ValueError:
        print("Invalid menu choice. Please enter a number.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def main_menu():
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Quit")
    choice = input("Enter your choice: ")
    return choice if validate_menu_option(choice, 4) else "Invalid choice in main menu"

def book_operations_menu():
    print("1. Add a new Book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")
    choice = input("Enter your choice: ")
    return choice if validate_menu_option(choice, 5) else "Invalid choice in book menu"

def user_operations_menu():
    print("1. Add a new User")
    print("2. View user details")
    print("3. Display all users")
    choice = input("Enter your choice: ")
    return choice if validate_menu_option(choice, 3) else "Invalid choice in user menu"

def author_operations_menu():
    print("1. Add a new Author")
    print("2. View author details")
    print("3. Display all authors")
    choice = input("Enter your choice: ")
    return choice if validate_menu_option(choice, 3) else "Invalid choice in author menu"

def main():
    authors = [Author("J.R.R. Tolkien", "Biography of J.R.R. Tolkien")]
    books = [Book("Lord of the Rings", "J.R.R. Tolkien", "fantasy", "1954")]
    users = [User("John Doe")]
    while True:
        main_menu_choice = main_menu()
        if main_menu_choice == '1':
            book_menu_choice = book_operations_menu()
            if book_menu_choice == '1':
                book_menu.add_book(books)
            elif book_menu_choice == '2':
                book_menu.borrow_book(books, users)
            elif book_menu_choice == '3':
                book_menu.return_book(books, users)
            elif book_menu_choice == '4':
                book_menu.search_book(books)
            elif book_menu_choice == '5':
                book_menu.display_books(books)
            
        elif main_menu_choice == '2':
            user_menu_choice = user_operations_menu()
            if user_menu_choice == '1':
                user_menu.add_user(users)
            elif user_menu_choice == '2':
                user_menu.view_user_details(users)
            elif user_menu_choice == '3':
                user_menu.display_users(users)
                
        elif main_menu_choice == '3':
            author_menu_choice = author_operations_menu()
            if author_menu_choice == '1':
                author_menu.add_author(authors)
            elif author_menu_choice == '2':
                author_menu.view_author_details(authors)
            elif author_menu_choice == '3':
                author_menu.display_authors(authors)
        
        elif main_menu_choice == '4':
            break
            
main()