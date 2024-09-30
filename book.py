class Book:
    def __init__(self, title, author, genre, publication_date, is_available = True):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__is_available = is_available
        
    @property
    def title(self):
        return self.__title
    
    @property
    def author(self):
        return self.__author
    
    @property
    def genre(self):
        return self.__genre
    
    @property
    def publication_date(self):
        return self.__publication_date
    
    @property
    def is_available(self):
        return self.__is_available
    
    def borrow(self):
        if self.__is_available:
            self.__is_available = False
            print(f"{self.__title} borrowed successfully.")
            return True
        return False
    
    def return_book(self):
        if self.__is_available:
            print(f"{self.__title} is already available.")
            return False
        self.__is_available = True
        print(f"{self.__title} returned successfully.")
        return True