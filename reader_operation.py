"""
Group Number: 61, Applied Class 04
Group Members:
1) Pragy Parashar
2) Parnoor Parnoor
3) Joanna Song Chea Lee

Date:
Description:
"""
from reader import Reader


class ReaderOperation:
    """
    Contains all the operations related to a reader.

    Attributes
    ----------
    book_title : str
      a string to store the title of the book
    page_number : int
      an integer to store the page number
    reader_obj : object
      an object storing the reader object
    num : int
      an integer storing the specified bookmark

    Methods
    -------
    add_bookmark(book_title,page_number, reader_obj)
      add specified reader's bookmark to the bookmark_list list
    delete_bookmark(num, reader_obj)
      delete the specified reader's bookmark based on the index from bookmark_list list
    save_favourite_book(book_title, reader_obj)
      add the specified reader's favourite book in favourite_book_list list
    delete_favourite_book(num, book_title, reader_obj)
      remove specified reader's favourite book from favourite_book_list list
    show_all_favourite_book(reader_obj)
      display all the Reader's favourite books
    show_all_bookmarks(reader_obj)
      display all the Reader's bookmarks
    """

    def add_bookmark(self,
                     book_title="",
                     page_no=0,
                     reader_obj=Reader()):
        """
        add specified reader's bookmark to the bookmark_list list

        Parameters
        ----------
        book_title : str
          a string to store the title of the book
        page_number : int
          an integer to store the page number
        reader_obj : object
          an object storing the reader object

        Returns
        -------
        A tuple with book_title and page, that will be added to the reader's bookmark_list
        """

        try:
            if (book_title, page_no) in reader_obj.bookmark_list:
                print("Bookmark already exists!")
                return 2
            if book_title != "" and page_no != 0:
                reader_obj.bookmark_list.append((book_title, page_no))
            return True
        except:
            return False

    def delete_bookmark(self,
                        num=1,
                        reader_obj=Reader()):
        """
        delete the specified reader's bookmark based on the index from bookmark_list list

        Parameters
        ----------
        reader_obj : object
          an object storing the reader object
        num : int
          an integer storing the specified bookmark

        Returns
        -------
        The corresponding bookmark at position num will be removed from the reader's bookmark_list.

        """

        try:
            if num > 0:
                if reader_obj.bookmark_list:
                    deleted_bookmark = reader_obj.bookmark_list[num - 1]
                    if deleted_bookmark:
                        reader_obj.bookmark_list.remove(deleted_bookmark)
                        print(f"Bookmark for book {deleted_bookmark[0]} page {deleted_bookmark[1]} has been deleted.")
                    else:
                        print("No bookmark found.")
                else:
                    print("You don't have any bookmarks to delete")
            return True
        except:
            return False

    def save_favourite_book(self,
                            book_title="",
                            reader_obj=Reader()):
        """
        add the specified reader's favourite book in favourite_book_list list

        Parameters
        ----------
        book_title : str
          a string to store the title of the book
        reader_obj : object
          an object storing the reader object

        Returns
        -------
        The book_title is saved into the reader's favourite_book_list.
        """

        try:
            if book_title != "":
                reader_obj.favourite_book_list.append(book_title)
            return True
        except:
            return False

    def delete_favourite_book(self,
                              num=0,
                              title="",
                              reader_obj=Reader()):
        """
        remove specified reader's favourite book from favourite_book_list list

        Parameters
        ----------
        num : int
          an integer storing the specified bookmark
        book_title : str
          a string to store the title of the book
        reader_obj : object
          an object storing the reader object

        Returns
        -------
        If the type is int, one item from reader's favourite_book_list is deleted based on index.
        If the type is str, serach the match item in favourite_book_list to perform deletion.
        """

        status_flag = False
        try:
            if num != 0:
                deleted_fav_book = reader_obj.favourite_book_list[num - 1]
                if title != "":
                    if deleted_fav_book:
                        if reader_obj.favourite_book_list[num - 1].upper() == title.upper():
                            reader_obj.favourite_book_list.remove(deleted_fav_book)
                            print(f"{deleted_fav_book} has been successfully deleted from favourites.")
                    else:
                        print("No such favourite book found.")
                else:
                    if deleted_fav_book:
                        reader_obj.favourite_book_list.remove(deleted_fav_book)
                        print(f"{deleted_fav_book} has been successfully deleted from favourites.")
                    else:
                        print("No such favourite book found.")
            else:
                if title != "":
                    for favs in reader_obj.favourite_book_list:
                        if title.upper() == favs.upper():
                            reader_obj.favourite_book_list.remove(title)
                            print(f"{title} has been successfully deleted from favourites.")
                        else:
                            print("No such favourite book found.")
            return True
        except:
            print("Some error occurred!")
            return False

    def show_all_favourite_book(self, reader_obj=Reader()):
        """
        display all the Reader's favourite books

        Parameters
        ----------
        reader_obj : object
          an object storing the reader object

        Returns
        -------
        Prints favourite books with row number shown at beginning of each item for specified reader.

        """

        try:
            book_num = 1
            if reader_obj.favourite_book_list:
                for books in reader_obj.favourite_book_list:
                    print(f"{book_num}: {books}\n")
                    book_num += 1
            else:
                print("You don't have any favourite books!")
            return True
        except:
            print("Some error occurred!")
            return False

    def show_all_bookmarks(self, reader_obj=Reader()):
        """
        display all the Reader's bookmarks

        Parameters
        ---------
        reader_obj : object
          an object storing the reader object

        Returns
        -------
        Prints all bookmarks with row number shown at beginning of each item for specified reader.
        """

        try:
            bookmark_num = 1
            if reader_obj.bookmark_list:
                for bookmarks in reader_obj.bookmark_list:
                    print(f"{bookmark_num:} Book: {bookmarks[0]}  Page: {bookmarks[1]}")
                    bookmark_num += 1
                status_flag = True
            else:
                print("You don't have any bookmarks!")
            return True
        except:
            return False
