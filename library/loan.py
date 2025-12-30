from datetime import datetime
from library.book import Book
from library.member import Member


class Loan:
    """
    Represents a loan (borrowing event) in the library system.
    """

    def __init__(self, book: Book, member: Member):
        self._book = book
        self._member = member
        self._date_borrowed = datetime.now()

    @property
    def book(self):
        """Returns the borrowed book."""
        return self._book

    @property
    def member(self):
        """Returns the member who borrowed the book."""
        return self._member

    @property
    def date_borrowed(self):
        """Returns the date when the book was borrowed."""
        return self._date_borrowed

    def to_dict(self):
        """
        Converts the loan to a dictionary for JSON storage.
        """
        return {
            "book_id": self._book.id,
            "member_id": self._member.member_id,
            "date_borrowed": self._date_borrowed.isoformat()
        }

    def __str__(self):
        return f"{self._member.name} borrowed '{self._book.title}' on {self._date_borrowed}"

    def __eq__(self, other):
        if not isinstance(other, Loan):
            return False
        return (
            self._book == other._book
            and self._member == other._member
            and self._date_borrowed == other._date_borrowed
        )
