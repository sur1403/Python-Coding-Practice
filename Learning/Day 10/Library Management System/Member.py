class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    
    def borrow_book(self, book):
        if len(self.borrowed_books) < 3:
            if book.checkout():
                self.borrowed_books.append(book)
                return True
            else:
                return False
        else:
            print("You have already borrowed the maximum number of books.")
            return False


    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_books()
            self.borrowed_books.remove(book)
            return True
        else:
            print("You have not borrowed this book.")
            return False

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Id: {self.member_id}")
        print("Borrowed Books:")

        for book in self.borrowed_books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.ISBN}, Genre: {book.genre} ")


    