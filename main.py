"""
Group Number: 61, Applied Class 04
Group Members:
1) Pragy Parashar
2) Parnoor Parnoor
3) Joanna Song Chea Lee

Date:
Description:
"""
"""
This class contains the main function logic that runs the application.

Attributes
----------
reader_obj : object
  an object storing the reader object


Methods
------
display_start_menu()
  prints the start menu options
display_logged_user_menu(reader_obj)
  prints the main menu options that users see after logging in
display_book_menu(reader_obj)
  prints the book operations menu options
display_bookmark_menu(reader_obj)
  prints the reader operations menu options

"""

import os
# importing book operation class
from book_operation import BookOperation
# importing user class
from user import User
# importing user operation class
from user_operation import UserOperation
# importing reader class
from reader import Reader
# importing reader operation class
from reader_operation import ReaderOperation

# start menu upon launching application
def display_start_menu():
    print("Welcome to Findle".center(70, '-'))
    print("1: Login as Existing User".center(70))
    print("2: Signup as New User    ".center(70))
    print("3: Exit Application      ".center(70))
    print("".center(70, '-'))

# main menu that logged user sees
def display_user_home(reader_obj=Reader()):
    print("Find, Explore and Read".center(70, "~"))
    print(f"Welcome {reader_obj.user_name.upper()}".center(70, '_'))
    print("1: Browse through our library          ".center(70))
    print("2: Bookmarks and Favs                  ".center(70))
    print("3: Log Out                             ".center(70))
    print("".center(70, "~"))

# menu for book operations (reading etc)
def display_browse_books():
    print("Welcome to our ever expanding digital library.".center(70))
    print("1: Browse all books.              ".center(70))
    print("2: Browse books by Authors.       ".center(70))
    print("3: Browse books by year of release".center(70))
    print("4: View Book Info.               ".center(70))
    print("5: View Book Contents.            ".center(70))
    print("6: Read a Book.                   ".center(70))
    print("B: Go back to previous menu.      ".center(70))
    print("".center(70, '-'))

# menu for navigating through a particular book and reader operations
def display_books_menu():
    print("M: Previous Page             N:Next Page")
    print("F: Favourite Book            G: Bookmark Page")
    print("B: Go to previous menu.")

# menu for managing bookmarks and favourites
def display_reader_ops():
    print("Manage your Books".center(70, '-'))
    print("1. Show your bookmarks.")
    print("2. Show your favourites.")
    print("3. Delete your bookmarks.")
    print("4. Delete your favourites.")
    print("5. Go Back to previous menu")

"""
does the validation of user input
"""
def input_validation(user_input='', function=''):
    try:
        status = False
        if function.lower() == 'main menu' or function.lower() == 'user home':
            if user_input.isdigit() and user_input in ('1', '2', '3'):
                status = True
        if function.lower() == 'books':
            if user_input.upper() in ('1', '2', '3', '4', '5', '6', 'B'):
                status = True
        if function.lower() == 'reader':
            if user_input.isdigit() and user_input in ('1', '2', '3', '4', '5'):
                status = True
        if function.lower() == 'book menu':
            if user_input.isalpha() and user_input.upper() in ('N', 'M', 'F', 'G', 'B'):
                status = True
        return status
    except:
        return False

"""
main function logic 
"""
def main():
    try:
        book_op_obj = BookOperation()
        user_op_obj = UserOperation()
        reader_op_obj = ReaderOperation()
        book_op_status_flag = book_op_obj.load_book_info()
        user_op_status_flag = user_op_obj.load_user_info()
        if book_op_status_flag and user_op_status_flag:
            while True:
                logout_flag = False
                display_start_menu()
                menu_input = input("How would you like to proceed? Please enter a valid option: ")
                if input_validation(menu_input, 'main menu'):
                    if int(menu_input) == 1:
                        while True:
                            print("Please enter your login credentials.")
                            username = input("Username: ")
                            password = input("Password: ")
                            user_auth = user_op_obj.user_login(username, password)
                            if user_auth:
                                for user in user_op_obj.user_info_list:
                                    if user.user_name == username and user.user_password == password:
                                        user_obj = user
                                        if isinstance(user, Reader):
                                            reader_obj = user
                                        else:
                                            reader_obj = Reader(user_obj.user_id, user_obj.user_name,
                                                                user_obj.user_password,
                                                                "reader", [], [])
                                        break

                                while True:
                                    display_user_home(reader_obj)
                                    user_input = input("Please choose an option to proceed: ")
                                    if input_validation(user_input, 'user home'):
                                        if int(user_input) == 1:
                                            while True:
                                                display_browse_books()
                                                book_input = input("Please enter your choice.")
                                                if input_validation(book_input, 'books'):
                                                    if book_input.upper() == '1':
                                                        page_input = input("Please enter page number from the "
                                                                           "catalogue to view. ")
                                                        if page_input.isdigit():
                                                            book_op_obj.display_titles(int(page_input))
                                                            print("".center(70, '-'))
                                                            print('\n')
                                                        else:
                                                            print("Please enter a valid input.")
                                                        continue
                                                    elif book_input.upper() == '2':
                                                        author_input = input("Please enter an author name. ")
                                                        book_op_obj.get_book_by_author(author_input)
                                                        print("".center(70, '-'))
                                                        print('\n')
                                                        continue
                                                    elif book_input.upper() == '3':
                                                        book_op_obj.get_book_release_year()
                                                        print("".center(70, '-'))
                                                        print('\n')
                                                    elif book_input.upper() == '4':
                                                        book_input = input("Please enter a book name: ")
                                                        print(f"{book_input.upper()}".center(70, '-'))
                                                        book_info = book_op_obj.get_counts(book_input)
                                                        if book_info != (0, 0, 0):
                                                            print(f"Number of chapter: {book_info[0]}".center(70))
                                                            print(f"Number of words: {book_info[1]}".center(70))
                                                            print(f"Number of lines: {book_info[2]}".center(70))
                                                        print("".center(70, '-'))
                                                        print('\n')
                                                        continue
                                                    elif book_input.upper() == '5':
                                                        book_input = input("Please enter a book name: ")
                                                        book_op_obj.show_book_content(book_input)
                                                        continue
                                                    elif book_input.upper() == '6':
                                                        while True:
                                                            book_title = input(
                                                                "Please enter the book you want to read: ")
                                                            page_number = input(
                                                                "Please enter the page you want to read: ")
                                                            if page_number.isdigit():
                                                                status = book_op_obj.show_book_text(book_title,
                                                                                                    int(page_number))
                                                                if status:
                                                                    while True:
                                                                        display_books_menu()
                                                                        reader_op_input = input("Please enter a your "
                                                                                                "choice to proceed.")
                                                                        if input_validation(reader_op_input,
                                                                                            'book menu'):
                                                                            if reader_op_input.upper() == 'N':
                                                                                book_op_obj.show_book_text(
                                                                                    book_title, int(page_number) + 1)
                                                                                continue
                                                                            elif reader_op_input.upper() == 'M':
                                                                                book_op_obj.show_book_text(
                                                                                    book_title, int(page_number) - 1)
                                                                                continue
                                                                            elif reader_op_input.upper() == 'F':
                                                                                status = reader_op_obj.save_favourite_book(
                                                                                    book_title, reader_obj)
                                                                                if status:
                                                                                    print(
                                                                                        "Book has been saved as favourite ")
                                                                                continue
                                                                            elif reader_op_input.upper() == 'G':
                                                                                bookmark_flag = reader_op_obj.add_bookmark(book_title,
                                                                                                           page_number,
                                                                                                           reader_obj)
                                                                                if bookmark_flag !=2:
                                                                                    print("Bookmark has been added")
                                                                                continue
                                                                            elif reader_op_input.upper() == 'B':
                                                                                break
                                                                        else:
                                                                            print("Please enter a valid input.")
                                                                            continue
                                                                else:
                                                                    print("Please enter a valid input.")
                                                                    continue
                                                                break
                                                            else:
                                                                print("Please enter a valid page number. ")
                                                                continue

                                                    elif book_input.upper() == 'B':
                                                        break
                                                else:
                                                    print("Please enter valid option.")
                                                    continue

                                        elif int(user_input) == 2:
                                            while True:
                                                display_reader_ops()
                                                reader_choice = input("Please enter your choice: ")
                                                if input_validation(reader_choice, 'reader'):
                                                    if int(reader_choice) == 1:
                                                        print("Bookmarks".center(70, '-'))
                                                        reader_op_obj.show_all_bookmarks(reader_obj)
                                                        print("".center(70, '-'))
                                                    elif int(reader_choice) == 2:
                                                        print("Favourites".center(70, '-'))
                                                        reader_op_obj.show_all_favourite_book(reader_obj)
                                                        print("".center(70, '-'))
                                                    elif int(reader_choice) == 3:
                                                        delete_input = input("Please enter bookmark number to delete: ")
                                                        if delete_input.isdigit():
                                                            reader_op_obj.delete_bookmark(int(delete_input), reader_obj)
                                                        else:
                                                            print("Please enter a valid input.")
                                                    elif int(reader_choice) == 4:
                                                        delete_input = input("Please enter favourite to delete: ")
                                                        if delete_input.isdigit():
                                                            reader_op_obj.delete_favourite_book(int(delete_input), '',reader_obj)
                                                        else:
                                                            reader_op_obj.delete_favourite_book(0, delete_input,reader_obj)
                                                    elif int(reader_choice) == 5:
                                                        break

                                                else:
                                                    print("Please enter a valid input")
                                                    continue
                                        elif int(user_input) == 3:
                                            print("You are now logging out.\n")
                                            for users in range(0,len(user_op_obj.user_info_list)):
                                                if user_op_obj.user_info_list[users].user_id == reader_obj.user_id:
                                                    user_op_obj.user_info_list[users] = reader_obj
                                            logout_flag = True
                                            break

                                    else:
                                        print("Please enter a valid option.")
                                        continue
                            if logout_flag:
                                break
                            else:
                                print("Invalid username or password. Please enter your credentials again.")
                                break
                    elif int(menu_input) == 2:
                        while True:
                            print("-------------------Register as a new user-------------------")
                            username = input("Username: ")
                            password = input("Password: ")
                            role = input("Role: ")
                            if username.isalnum() and password.isalnum():
                                user_auth = user_op_obj.user_registration(username, password, role)
                                if user_auth:
                                    break
                                else:
                                    print("Username already exists. Please choose another username.")
                                    continue
                            else:
                                print("Please enter valid values.")
                                continue
                            break
                    elif int(menu_input) == 3:
                        print("You are now exiting the application.\n Thank You!")
                        user_op_obj.write_user_info()
                        break
                    else:
                        print("Please enter a valid option.")
                        continue
                else:
                    print("Please enter a valid option.")
                    continue
    # exception handling for if file is not found
    except FileNotFoundError as e:
        print("File not found. " + str(e))
        return False
    except:
        print("Some error occurred.")
        return False

if __name__ == '__main__':
    main()

