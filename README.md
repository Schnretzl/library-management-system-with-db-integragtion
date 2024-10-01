# Library Management System
This is a system for managing books, users, and authors in a library.
This is managed in a MySQL database.  Tables are stored in a database titled 'library_db', and are created using the following queries:

    CREATE TABLE books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        author_id INT,
        genre VARCHAR(20) NOT NULL,
        publication_date DATE,
        availability BOOLEAN DEFAULT 1,
        FOREIGN KEY (author_id) REFERENCES authors(id),
    );

    CREATE TABLE authors (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        bio TEXT
    );

    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
    );

    CREATE TABLE borrowed_books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        book_id INT,
        borrow_date DATE NOT NULL,
        return_date DATE,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (book_id) REFERENCES books(id)
    );

## Book Operations
### Add a new book
Prompts the user for necessary information, and adds a new book to the library available for lending.

### Borrow a book
Prompts the user for the book title, and the user ID, and then attempts to borrow the book.

### Return a book
Prompts the user for the user ID and book title, and returns the book, if it is borrowed by the user.

### Search for a book
Prompts the user for the book title, and displays all book information available, or notifies the user that the book was not found.

### Display all books
Displays all titles that exist in the library.

## User Operations
### Add a new user
Prompts the user for a name, and adds a new user to the library.

### View user details
Prompts the user for user ID, and displays the user's name and borrowed books.

### Display all users
Displays the names and IDs of all users.

## Author Operations
### Add a new author
Prompts the user for an author's name and bio, and adds a new author to the library.

### View author details
Prompts the user for an author's name, and displays the author's name and bio, if found.

### Display all authors
Displays a list of names of all authors.

### Edit Author Biography
Prompts the user for an author's name.  If the author is found, prompts the user for a new bio for the author and adds it to the library.