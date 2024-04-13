# Findle E-Book Reader and Analyzer

## Overview
Findle is a Python-based application designed for reading and analyzing e-books. It allows users to perform a variety of operations including registering, logging in, viewing book details, reading books, managing bookmarks, and handling favorite books.

## Getting Started

### Prerequisites
- Python 3.9
- Libraries: `random`, `math`, `os`, `string`

### Installation
- Clone the repository to your local machine: git clone https://github.com/pragy29/Findle
- Navigate to the cloned directory: cd findle
  
### Running the Application
To run the application, execute the main Python script: python main.py


## Features
- **User Registration and Login:** Secure registration and login system for application access.
- **Book Operations:**
  - View detailed information about books such as number of chapters, words, and lines.
  - Display titles of all available books and their contents.
  - Read books and manage reading sessions with bookmarks.
- **Book Management:**
  - Add or remove books from favorites.
  - Show all favorite books in the user’s list.
- **Search and Filters:**
  - Filter books by author and publication year.
  - Search for books within specified criteria.

## File Structure
- `book.py`: Handles the book attributes and basic operations.
- `book_operation.py`: Manages all book-related operations.
- `user.py`: Defines the user model including attributes and methods for user operations.
- `user_operation.py`: Handles user-based actions like registration and login.
- `reader.py`: Extends user functionalities, tailored for a reader.
- `reader_operation.py`: Manages reader-specific actions such as bookmarks and favorites.
- `main.py`: The main executable script that runs the application.

## Contributing
Contributors are welcome to further enhance the application. Please fork the repository and submit a pull request for review.

## License
This project is licensed under the Monash University License.

## Authors
https://github.com/pragy29

## Acknowledgments
- Monash University, Faculty of IT
- All contributors who test, document, and maintain the project.



