import json
from datetime import datetime

from library.book import Book, PhysicalBook, EBook
from library.member import Member
from library.loan import Loan
from library.exceptions import (
    BookNotFoundError,
    MemberNotFoundError
)


class Library:
    """
    Represents the library system controller.
    """

    def __init__(self):
        self._books = {}      # book_id -> Book
        self._members = {}    # member_id -> Member
        self._loans = []      # list of Loan objects

    @property
    def books(self):
        """Returns all books in the library."""
        return self._books

    @property
    def members(self):
        """Returns all members in the library."""
        return self._members

    @property
    def loans(self):
        """Returns all active loans."""
        return self._loans

    def add_book(self, book: Book):
        """
        Adds a book to the library.
        """
        self._books[book.id] = book

    def add_member(self, member: Member):
        """
        Adds a member to the library.
        """
        self._members[member.member_id] = member

    def borrow_book(self, member_id: str, book_id: str):
        """
        Borrows a book for a member.

        Raises:
            MemberNotFoundError: If the member does not exist.
            BookNotFoundError: If the book does not exist.
        """
        if member_id not in self._members:
            raise MemberNotFoundError("Member not found")

        if book_id not in self._books:
            raise BookNotFoundError("Book not found")

        member = self._members[member_id]
        book = self._books[book_id]

        member.borrow_book(book)

        loan = Loan(book, member)
        self._loans.append(loan)

    def return_book(self, member_id: str, book_id: str):
        """
        Returns a borrowed book.

        Raises:
            MemberNotFoundError: If the member does not exist.
            BookNotFoundError: If the book does not exist.
        """
        if member_id not in self._members:
            raise MemberNotFoundError("Member not found")

        if book_id not in self._books:
            raise BookNotFoundError("Book not found")

        member = self._members[member_id]
        book = self._books[book_id]

        member.return_book(book)

        for loan in self._loans:
            if loan.book == book and loan.member == member:
                self._loans.remove(loan)
                break

    def save_to_file(self, filename: str):
        """
        Saves the library data to a JSON file.
        """
        data = {
            "books": [book.to_dict() for book in self._books.values()],
            "members": [member.to_dict() for member in self._members.values()],
            "loans": [loan.to_dict() for loan in self._loans]
        }

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_from_file(self, filename: str):
        """
        Loads library data from a JSON file.
        """
        with open(filename, "r") as file:
            data = json.load(file)

        self._books.clear()
        self._members.clear()
        self._loans.clear()

        # Recreate books
        for b in data.get("books", []):
            if b["type"] == "PhysicalBook":
                book = PhysicalBook(
                    b["id"],
                    b["title"],
                    b["author"],
                    b["available_copies"]
                )
            else:
                book = EBook(
                    b["id"],
                    b["title"],
                    b["author"],
                    b["file_size_mb"]
                )
            self._books[book.id] = book

        # Recreate members
        for m in data.get("members", []):
            member = Member(m["member_id"], m["name"])
            self._members[member.member_id] = member

        # Recreate loans
        for l in data.get("loans", []):
            book = self._books[l["book_id"]]
            member = self._members[l["member_id"]]

            loan = Loan(book, member)
            loan._date_borrowed = datetime.fromisoformat(l["date_borrowed"])

            member.borrowed_books.append(book)
            self._loans.append(loan)
