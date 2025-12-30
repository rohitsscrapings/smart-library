import pytest

from library.library import Library
from library.book import PhysicalBook
from library.member import Member
from library.exceptions import BookNotAvailableError, BookNotFoundError


def setup_library():
    """
    Helper function to create a library with one book and one member.
    """
    library = Library()
    book = PhysicalBook("B1", "Python OOP", "Author", 1)
    member = Member("M1", "Test User")

    library.add_book(book)
    library.add_member(member)

    return library


def test_add_book():
    library = Library()
    book = PhysicalBook("B2", "Test Book", "Author", 2)

    library.add_book(book)

    assert "B2" in library.books


def test_add_member():
    library = Library()
    member = Member("M2", "Alice")

    library.add_member(member)

    assert "M2" in library.members


def test_borrow_book_success():
    library = setup_library()

    library.borrow_book("M1", "B1")

    assert len(library.loans) == 1
    assert library.books["B1"].available_copies == 0


def test_borrow_same_book_twice_fails():
    library = setup_library()

    library.borrow_book("M1", "B1")

    with pytest.raises(Exception):
        library.borrow_book("M1", "B1")


def test_borrow_nonexistent_book():
    library = setup_library()

    with pytest.raises(BookNotFoundError):
        library.borrow_book("M1", "INVALID")
