# Instantiate objects
from Book import Book
from Member import Member
from Library import Library


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565", "Fiction")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084", "Fiction")
member1 = Member("Alice", 1)
library = Library()

# Add books to library
library.add_new_books(book1)
library.add_new_books(book2)

# Register members with library
library.register_members(member1)

# Search for books
search_results = library.search_books("Harper Lee")
for book in search_results:
    print(f"Found: {book.title} by {book.author}")

# Member borrows a book
if member1.borrow_book(book1):
    print("Book borrowed successfully.")
else:
    print("Book is not available.")

# Display member's borrowed books
library.display_member_books(member1)

# Member returns a book
member1.return_book(book1)

# Display available books after return
library.display_available_books()
