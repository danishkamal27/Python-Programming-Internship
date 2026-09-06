"""
Assignment 2: Library Management System (OOP)
Demonstrates Object-Oriented Programming principles including class interactions,
encapsulation, state management, and edge-case handling.
"""


class Book:
    """Class representing an individual book in the library."""

    def __init__(self, book_id, title, author):
        """Initialize book details."""
        self.book_id = str(book_id).strip()
        self.title = title.strip()
        self.author = author.strip()
        self.is_issued = False

    def __str__(self):
        """String representation of book status."""
        status = "[ISSUED]" if self.is_issued else "[AVAILABLE]"
        return f"ID: {self.book_id:<6} | Title: '{self.title}' by {self.author:<20} | Status: {status}"


class Library:
    """Class representing the Library system managing book collection and transactions."""

    def __init__(self, name="Central City Library"):
        """Initialize library with a name and empty catalog."""
        self.name = name
        self.books = {}  # Dictionary mapping book_id -> Book object

    def add_book(self, book):
        """Add a Book object to the library catalog."""
        if not isinstance(book, Book):
            print("[FAILED] Only valid Book objects can be added.")
            return False

        if book.book_id in self.books:
            print(f"[FAILED] Book with ID '{book.book_id}' already exists in catalog.")
            return False

        self.books[book.book_id] = book
        print(f"[SUCCESS] Added: '{book.title}' by {book.author} (ID: {book.book_id})")
        return True

    def remove_book(self, book_id):
        """Remove a book from the catalog by its ID."""
        book_id = str(book_id).strip()

        if book_id not in self.books:
            print(f"[FAILED] Remove Failed: Book ID '{book_id}' not found in catalog.")
            return False

        book = self.books[book_id]
        if book.is_issued:
            print(f"[FAILED] Remove Failed: Cannot remove '{book.title}' because it is currently issued.")
            return False

        del self.books[book_id]
        print(f"[SUCCESS] Removed: '{book.title}' (ID: {book_id}) successfully.")
        return True

    def issue_book(self, book_id):
        """Issue a book to a user if it exists and is currently available."""
        book_id = str(book_id).strip()

        if book_id not in self.books:
            print(f"[FAILED] Issue Failed: Book ID '{book_id}' does not exist.")
            return False

        book = self.books[book_id]
        if book.is_issued:
            print(f"[FAILED] Issue Failed: '{book.title}' is already issued.")
            return False

        book.is_issued = True
        print(f"[SUCCESS] Issued: '{book.title}' has been successfully issued.")
        return True

    def return_book(self, book_id):
        """Return an issued book back to the library."""
        book_id = str(book_id).strip()

        if book_id not in self.books:
            print(f"[FAILED] Return Failed: Book ID '{book_id}' does not belong to this library.")
            return False

        book = self.books[book_id]
        if not book.is_issued:
            print(f"[FAILED] Return Failed: '{book.title}' was not issued.")
            return False

        book.is_issued = False
        print(f"[SUCCESS] Returned: '{book.title}' has been successfully returned.")
        return True

    def display_books(self):
        """Display all books currently in the library catalog."""
        print(f"\n==========================================================================")
        print(f"   {self.name.upper()} CATALOG")
        print(f"==========================================================================")

        if not self.books:
            print(" No books currently in catalog.")
            print("==========================================================================\n")
            return

        for book in self.books.values():
            print(f" {book}")
        print("==========================================================================\n")


def demonstrate_library_system():
    """Demonstrate Library System operations, object interaction, and error handling."""
    print("=========================================")
    print("  DEMONSTRATING LIBRARY MANAGEMENT SYSTEM")
    print("=========================================\n")

    city_library = Library("City Central Library")

    # Creating Book objects
    b1 = Book("B101", "To Kill a Mockingbird", "Harper Lee")
    b2 = Book("B102", "1984", "George Orwell")
    b3 = Book("B103", "The Great Gatsby", "F. Scott Fitzgerald")

    print("--- 1. Adding Books ---")
    city_library.add_book(b1)
    city_library.add_book(b2)
    city_library.add_book(b3)

    # Display initial catalog
    city_library.display_books()

    print("--- 2. Issuing Books ---")
    city_library.issue_book("B102")  # Valid issue

    print("\n--- 3. Edge Case: Issue Unavailable / Non-Existent Book ---")
    city_library.issue_book("B102")  # Already issued
    city_library.issue_book("B999")  # Non-existent ID

    city_library.display_books()

    print("--- 4. Returning Books ---")
    city_library.return_book("B102")  # Valid return

    print("\n--- 5. Edge Case: Return Book Not Issued / Non-Existent ---")
    city_library.return_book("B101")  # Not issued
    city_library.return_book("B999")  # Non-existent ID

    print("\n--- 6. Removing Books ---")
    city_library.remove_book("B103")  # Valid remove
    city_library.remove_book("B999")  # Non-existent remove

    city_library.display_books()


if __name__ == "__main__":
    demonstrate_library_system()
