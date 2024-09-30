import user_menu
from book import Book
from user import User

def add_book(conn):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    genre = input("Enter the genre of the book: ")
    publication_date = input("Enter the publication date of the book: ")
    # books.append(Book(title, author, genre, publication_date))
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM authors WHERE name = %s", (author,))
            author_id = cursor.fetchone()[0] if cursor.fetchone() else None
            if author_id is None:
                # Add author to Author database if missing
                cursor.execute("INSERT INTO authors (name) VALUES (%s)", (author,))
                conn.commit()
                cursor.execute("SELECT * FROM authors WHERE name = %s", (author,))
                author_id = cursor.fetchone()[0]
            cursor.execute("INSERT INTO books (title, author_id, publication_date, genre) VALUES (%s, %s, %s, %s)", (title, author_id, publication_date, genre))
            print(f"{title} added to the system successfully.\n")
            conn.commit()
        except Exception as e:
            print(f"Error: {e}")
    
def borrow_book(books, users):
    book_title = input("Enter the title of the book you want to borrow: ")
    book_title_index = find_book_index(books, book_title)
    if book_title_index is None:
        print("Book not found.")
        return False
    user_id = user_menu.get_valid_user_id()
    user_index = user_menu.find_user_index(users, user_id)
    if user_index is None:
        print("User not found.")
        return False
    if books[book_title_index].borrow():
        users[user_index].borrowed_books.append(books[book_title_index])
        return True
    else:
        print("Book is not available.")
        return False
        
def return_book(books, users):
    user_id = user_menu.get_valid_user_id()
    user_index = user_menu.find_user_index(users, user_id)
    if user_index is None:
        print("User not found.")
        return False
    book_title = input("Enter the title of the book you want to return: ")
    book_title_index = find_book_index(books, book_title)
    user_book_index = find_book_index(users[user_index].borrowed_books, book_title)
    if book_title_index is None:
        print("Book not found.")
        return False
    elif user_book_index is None:
        print("Book not borrowed.")
        return False
    elif books[book_title_index].return_book():
        users[user_index].borrowed_books.remove(books[book_title_index])
        return True
    else:
        print("Book is already available.")
        return False
    
def search_book(conn):
    title = input("Enter the title of the book: ")
    book_title_index = find_book_index(conn, title)
    if book_title_index is None:
        print("Book not found.")
        return False
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books WHERE id = %s", (book_title_index,))
            book = cursor.fetchone()
            print(f"Title: {book[1]}")
            cursor.execute("SELECT * FROM authors WHERE id = %s", (book[2],))
            author = cursor.fetchone()
            print(f"Author: {author[1]}")
            print(f"Genre: {book[3]}")
            print(f"Publication Date: {book[4]}")
            print(f"Availability: {'Available' if book[5] else 'Not Available'}")
        except Exception as e:
            print(f"Error: {e}")
    return True

def display_books(conn):
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        if not books:
            print("No books in library.")
            return False
        print("\nBooks in library:")
        for index, book in enumerate(books):
            print(f"{index + 1}. {book[1]}")
    print()
    return True

def find_book_index(conn, title):
    #Return the index of the book, or None if the book is not found
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books WHERE title = %s", (title,))
            book = cursor.fetchone()
            if book:
                return book[0]
            else:
                return None
        except Exception as e:
            print(f"Error: {e}")