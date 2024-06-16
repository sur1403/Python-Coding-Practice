class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_new_books(self, book):
        self.books.append(book)

    def register_members(self, members):
        self.members.append(members)
        
    
    def search_books(self, keyword):
        found_books = []
        for book in self.books:
         if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
             found_books.append(book)
        return found_books

    def display_available_books(self):
        for book in self.books:
            if book.available:
                return book
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Genre: {book.genre}")
        

    def display_member_books(self, member):
        print(f"Books borrowed by {member.name}:")
        for book in member.borrowed_books:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.ISBN}, Genre: {book.genre}")



