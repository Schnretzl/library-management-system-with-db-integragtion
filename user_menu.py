def add_user(conn):
    name = input("Enter the name of the user: ")
    # users.append(User(name))
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
            print(f"{name} added to the system successfully.")
            conn.commit()
        except Exception as e:
            print(f"Error: {e}")
    print()
    
def view_user_details(conn):
    user_id = get_valid_user_id()
    user_index = find_user_index(conn, user_id)
    if user_index is None:
        print("User not found.")
        return False
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id = %s", (user_index,))
            user = cursor.fetchone()
            print(f"Name: {user[1]}")
            print(f"ID: {user[0]}")
            cursor.execute("SELECT * FROM borrowed_books WHERE user_id = %s AND return_date IS NULL", (user_index,))
            borrowed_books = cursor.fetchall()
            if len(borrowed_books) == 0:
                print("No borrowed books.")
            else:
                print("Borrowed Books:")
                for book in borrowed_books:
                    cursor.execute("SELECT * FROM books WHERE id = %s", (book[2],))
                    book_details = cursor.fetchone()
                    print(f"{book_details[1]}")
            print()
        except Exception as e:
            print(f"Error: {e}")

def display_users(users):
    for user in users:
        print(f"Name: {user.name}")
        print(f"ID: {user.id}")
        print()
        
def find_user_index(conn, user_id):
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            result = cursor.fetchone()
            user_index = result[0] if result else None
            return user_index
        except Exception as e:
            print(f"Error: {e}")    

def get_valid_user_id():
    while True:
        user_id = input("Enter the ID of the user: ")
        if user_id.isdigit():
            return int(user_id)
        print("Invalid user ID. Please try again.")