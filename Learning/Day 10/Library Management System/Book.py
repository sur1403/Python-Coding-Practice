class Book:
    def __init__(self, title, author, ISBN, genre):
 
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.genre = genre
        self.available = True


    def checkout(self):
        if self.available:
            self.available = False
            return True
        else:
            return False
        
    def return_books(self):
        self.available = True


    def display_info(self):
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("ISBN: ", self.ISBN)
        print("Genre", self.genre)
        print("available", self.available)
     

