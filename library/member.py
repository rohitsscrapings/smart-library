from library.book import Book


class Member:
    """
    Represents a library member.
    """

    def __init__(self, member_id: str, name: str):
        self._member_id = member_id
        self._name = name
        self._borrowed_books = []

    @property
    def member_id(self):
        """Returns the member ID."""
        return self._member_id

    @property
    def name(self):
        """Returns the member name."""
        return self._name

    @property
    def borrowed_books(self):
        """Returns the list of borrowed books."""
        return self._borrowed_books

    def borrow_book(self, book: Book):
        """
        Borrows a book for the member.

        Raises:
            Exception: If the book is already borrowed by the member.
        """
        if book in self._borrowed_books:
            raise Exception("This book is already borrowed by the member")

        book.borrow()
        self._borrowed_books.append(book)

    def return_book(self, book: Book):
        """
        Returns a borrowed book.

        Raises:
            Exception: If the book is not borrowed by the member.
        """
        if book not in self._borrowed_books:
            raise Exception("This book was not borrowed by the member")

        book.return_book()
        self._borrowed_books.remove(book)

    def to_dict(self):
        """
        Converts the member to a dictionary for JSON storage.
        """
        return {
            "member_id": self._member_id,
            "name": self._name,
            "borrowed_books": [book.id for book in self._borrowed_books]
        }

    def __str__(self):
        return f"{self._name} (ID: {self._member_id})"

    def __eq__(self, other):
        if not isinstance(other, Member):
            return False
        return self._member_id == other._member_id
