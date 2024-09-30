from user import User

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
    
def view_user_details(users):
    user_id = get_valid_user_id()
    user_index = find_user_index(users, user_id)
    if user_index is None:
        print("User not found.")
        return False
    print(f"Name: {users[user_index].name}")
    print(f"ID: {users[user_index].id}")
    print("Borrowed Books:")
    for book in users[user_index].borrowed_books:
        print(book.title)
    print()

def display_users(users):
    for user in users:
        print(f"Name: {user.name}")
        print(f"ID: {user.id}")
        print()
        
def find_user_index(users, user_id):
    #Return the index of the user, or None if the user is not found
    for index, user in enumerate(users):
        if user.id == user_id:
            return index
    return None

def get_valid_user_id():
    while True:
        user_id = input("Enter the ID of the user: ")
        if user_id.isdigit():
            return int(user_id)
        print("Invalid user ID. Please try again.")