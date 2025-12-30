from abc import ABC, abstractmethod
from library.exceptions import BookNotAvailableError


class Book(ABC):
    """
    Abstract base class representing a generic book in the library.

    This class defines the common interface for all book types.
    """

    def __init__(self, book_id: str, title: str, author: str):
        self._id = book_id
        self._title = title
        self._author = author

    @property
    def id(self):
        """Returns the book ID."""
        return self._id

    @property
    def title(self):
        """Returns the book title."""
        return self._title

    @property
    def author(self):
        """Returns the book author."""
        return self._author

    @abstractmethod
    def borrow(self):
        """Borrow the book."""
        pass

    @abstractmethod
    def return_book(self):
        """Return the book."""
        pass

    @abstractmethod
    def to_dict(self):
        """Convert the book to a dictionary."""
        pass

    def __str__(self):
        return f"{self._title} by {self._author}"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self._id == other._id


class PhysicalBook(Book):
    """
    Represents a physical book with limited copies.
    """

    def __init__(self, book_id: str, title: str, author: str, available_copies: int):
        super().__init__(book_id, title, author)
        self._available_copies = available_copies

    @property
    def available_copies(self):
        """Returns number of available copies."""
        return self._available_copies

    def borrow(self):
        """
        Borrows a physical book.

        Raises:
            BookNotAvailableError: If no copies are available.
        """
        if self._available_copies <= 0:
            raise BookNotAvailableError("No physical copies available")
        self._available_copies -= 1

    def return_book(self):
        """Returns a physical book."""
        self._available_copies += 1

    def to_dict(self):
        """Convert the physical book to a dictionary."""
        return {
            "type": "PhysicalBook",
            "id": self._id,
            "title": self._title,
            "author": self._author,
            "available_copies": self._available_copies
        }


class EBook(Book):
    """
    Represents an electronic book.
    """

    def __init__(self, book_id: str, title: str, author: str, file_size_mb: float):
        super().__init__(book_id, title, author)
        self._file_size_mb = file_size_mb
        self._is_borrowed = False

    @property
    def file_size_mb(self):
        """Returns the file size in MB."""
        return self._file_size_mb

    def borrow(self):
        """
        Borrows an eBook.

        Raises:
            BookNotAvailableError: If the eBook is already borrowed.
        """
        if self._is_borrowed:
            raise BookNotAvailableError("EBook already borrowed")
        self._is_borrowed = True

    def return_book(self):
        """Returns an eBook."""
        self._is_borrowed = False

    def to_dict(self):
        """Convert the eBook to a dictionary."""
        return {
            "type": "EBook",
            "id": self._id,
            "title": self._title,
            "author": self._author,
            "file_size_mb": self._file_size_mb,
            "is_borrowed": self._is_borrowed
        }
