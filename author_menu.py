def add_author(conn):
    name = input("Enter the name of the author: ")
    bio = input("Enter the biography of the author: ")
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM authors WHERE name = %s", (name,))
            result = cursor.fetchone()
            if result:
                print("Author already exists.")
                return False
            cursor.execute("INSERT INTO authors (name, bio) VALUES (%s, %s)", (name, bio))
            print(f"Added {name} to the list of authors.\n")
            conn.commit()
        except Exception as e:
            print(f"Error: {e}")
    
def view_author_details(conn):
    author_name = input("Enter the name of the author: ")
    author_index = find_author_index(conn, author_name)
    if author_index is None:
        print("Author not found.")
        return False
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM authors WHERE id = %s", (author_index,))
            author = cursor.fetchone()
            print(f"Name: {author[1]}")
            print(f"Biography: {author[2]}")
            cursor.execute("SELECT * FROM books WHERE author_id = %s", (author_index,))
            books = cursor.fetchall()
            if books:
                print("Books:")
                for book in books:
                    status = " (checked out)" if not book[5] else ""
                    print(f"{book[1]}{status}")
            print()
        except Exception as e:
            print(f"Error: {e}")
    
def display_authors(conn):
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM authors")
            authors = cursor.fetchall()
            if len(authors) == 0:
                print("No authors in the system.")
            else:
                print("Authors:")
                for author in authors:
                    print(f"Name: {author[1]}")
                print()
        except Exception as e:
            print(f"Error: {e}")
            
def edit_author_bio(conn):
    author_name = input("Enter the name of the author: ")
    author_index = find_author_index(conn, author_name)
    if author_index is None:
        print("Author not found.")
        return False
    new_bio = input("Enter the new biography: ")
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE authors SET bio = %s WHERE id = %s", (new_bio, author_index))
            print("Biography updated successfully.")
            conn.commit()
        except Exception as e:
            print(f"Error: {e}")
        
def find_author_index(conn, author_name):
    #Return the index of the author, or None if the author is not found
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM authors WHERE name = %s", (author_name,))
            result = cursor.fetchone()
            author_id = result[0] if result else None
            return author_id
        except Exception as e:
            print(f"Error: {e}")
    return None