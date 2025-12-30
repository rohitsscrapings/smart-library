# Smart Library Management System

## Project Description
The Smart Library Management System is a console-based Python application developed using Object-Oriented Programming (OOP) principles.

This system helps a small library manage its books, members, borrowing and returning of books, and data persistence. The project demonstrates core OOP concepts such as abstraction, inheritance, encapsulation, association, composition, and polymorphism.

The application uses a simple text-based menu and stores data using JSON files to ensure data is preserved between program runs.

---

## Features
- Add physical books and eBooks to the library
- Register library members
- Borrow and return books with validation rules
- Prevent members from borrowing the same book twice
- Track active loans
- Save and load library data using JSON
- Custom error handling for common scenarios

---

## Project Structure
smart-library/
├── library/
│   ├── book.py
│   ├── member.py
│   ├── loan.py
│   ├── library.py
│   └── exceptions.py
├── tests/
│   └── test_library.py
├── main.py
├── README.md
├── data.json
└── .gitignore

---

## How to Run the Application
1. Open a terminal in the project directory
2. Run the application using:
python3 main.py

---

## Menu Options
1. Add physical book
2. Add eBook
3. Add member
4. Borrow book
5. Return book
6. List books
7. List members
8. Save library data
9. Load library data
0. Exit

---

## Example Usage
1. Add a physical book
2. Add a member
3. Borrow the book using the member ID
4. Return the book
5. Save the library data
6. Reload the data to verify persistence

---

## Saving and Loading Data
- Select option 8 to save all books, members, and loans to data.json
- Select option 9 to load previously saved data from data.json

---

## Technologies Used
- Python
- Object-Oriented Programming (OOP)
- JSON for file storage
- Git and GitHub for version control

---

## Testing
The application was tested manually using the console menu to verify:
- Book creation
- Member registration
- Borrow and return functionality
- Error handling
- JSON save and load operations
