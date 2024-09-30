from author import Author

def add_author(authors):
    name = input("Enter the name of the author: ")
    bio = input("Enter the biography of the author: ")
    authors.append(Author(name, bio))
    print(f"Added {name} to the list of authors.\n")
    
def view_author_details(authors):
    author_name = input("Enter the name of the author: ")
    author_index = find_author_index(authors, author_name)
    if author_index is None:
        print("Author not found.")
        return False
    print(f"Name: {authors[author_index].name}")
    print(f"Biography: {authors[author_index].biography}")
    print()
    
def display_authors(authors):
    for author in authors:
        print(f"Name: {author.name}")
    print()
        
def find_author_index(authors, author_name):
    #Return the index of the author, or None if the author is not found
    for index, author in enumerate(authors):
        if author.name == author_name:
            return index
    return None