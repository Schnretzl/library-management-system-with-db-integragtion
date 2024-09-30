class User:
    _next_id = 1
    
    def __init__(self, name, borrowed_books = None):
        self.__name = name
        self.__id = User._next_id
        User._next_id += 1
        self.__borrowed_books = borrowed_books if borrowed_books is not None else []
        
    @property
    def name(self):
        return self.__name
    
    @property
    def id(self):
        return self.__id
    
    @property
    def borrowed_books(self):
        return self.__borrowed_books