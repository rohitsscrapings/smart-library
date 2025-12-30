from library.library import Library
from library.book import PhysicalBook, EBook
from library.member import Member
from library.exceptions import (
    BookNotAvailableError,
    BookNotFoundError,
    MemberNotFoundError
)


def print_menu():
    print("\n==== Smart Library Management System ====")
    print("1. Add physical book")
    print("2. Add eBook")
    print("3. Add member")
    print("4. Borrow book")
    print("5. Return book")
    print("6. List books")
    print("7. List members")
    print("8. Save library")
    print("9. Load library")
    print("0. Exit")


def main():
    library = Library()

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                book_id = input("Book ID: ")
                title = input("Title: ")
                author = input("Author: ")
                copies = int(input("Available copies: "))

                book = PhysicalBook(book_id, title, author, copies)
                library.add_book(book)
                print("Physical book added successfully.")

            elif choice == "2":
                book_id = input("Book ID: ")
                title = input("Title: ")
                author = input("Author: ")
                size = float(input("File size (MB): "))

                book = EBook(book_id, title, author, size)
                library.add_book(book)
                print("EBook added successfully.")

            elif choice == "3":
                member_id = input("Member ID: ")
                name = input("Member name: ")

                member = Member(member_id, name)
                library.add_member(member)
                print("Member added successfully.")

            elif choice == "4":
                member_id = input("Member ID: ")
                book_id = input("Book ID: ")

                library.borrow_book(member_id, book_id)
                print("Book borrowed successfully.")

            elif choice == "5":
                member_id = input("Member ID: ")
                book_id = input("Book ID: ")

                library.return_book(member_id, book_id)
                print("Book returned successfully.")

            elif choice == "6":
                if not library.books:
                    print("No books in library.")
                else:
                    for book in library.books.values():
                        print(book)

            elif choice == "7":
                if not library.members:
                    print("No members registered.")
                else:
                    for member in library.members.values():
                        print(member)

            elif choice == "8":
                library.save_to_file("data.json")
                print("Library saved to data.json")

            elif choice == "9":
                library.load_from_file("data.json")
                print("Library loaded from data.json")

            elif choice == "0":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except BookNotAvailableError as e:
            print(f"Error: {e}")
        except BookNotFoundError as e:
            print(f"Error: {e}")
        except MemberNotFoundError as e:
            print(f"Error: {e}")
        except ValueError:
            print("Invalid input type. Please enter correct values.")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
