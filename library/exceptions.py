class LibraryError(Exception):
    """
    Base class for all library-related errors.
    """
    pass


class BookNotAvailableError(LibraryError):
    """
    Raised when a book is not available for borrowing.
    """
    pass


class BookNotFoundError(LibraryError):
    """
    Raised when a book cannot be found in the library.
    """
    pass


class MemberNotFoundError(LibraryError):
    """
    Raised when a member cannot be found in the library.
    """
    pass
