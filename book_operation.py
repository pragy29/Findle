"""
Group Number: 61, Applied Class 04
Group Members:
1) Pragy Parashar
2) Parnoor Parnoor
3) Joanna Song Chea Lee

Date:
Description:
"""
import os
import re
import math as mat
from book import Book


class BookOperation:
    """
    A class that contains all the operations related to a book.

    Attributes
    ----------
    book_folder_path : str
      a string to store the relative folder path of the books data
    book_info_path : str
      a string to store the relative path of the books info text file.
    book_title_list : list
      a list to store all the book titles
    book_info_dict : dict
      a dictionary to store key-value pairs of a book title and book object.
    book_title : str
      a string to store the title of the book
    page_number : int
      an integer to store the page number
    author_name : str
      a string to store the author's name

    Methods
    -------
    extract_book_info()
      extracts book attributes from each book and writes them as formatted string to books.txt
    load_book_info()
      loads book info from books.txt
    get_counts(book_title)
      returns the number of chapters, words and lines for the specified book_title
    display_titles(page_number)
      displays titles of books listed in book_title_list list
    show_book_content(book_title)
      returns book title with list of contents displayed
    show_book_text(book_title, page_number)
      displays one page of book text includes book title, chapter number, book text and page number
    get_book_author(author_name)
      prints book title followed by full author name
    get_book_release_year()
      prints total number of books for specific release year ranges

    """
    book_folder_path = "./data/books_data/"
    book_info_path = "./data/result_data/books.txt"
    book_title_list = []
    book_info_dict = {}

    def extract_book_info(self):
        """
        extracts book attributes from each book and writes them as formatted string to books.txt
        """

        try:
            book_list = []
            status_flag = False
            for file in os.listdir(self.book_folder_path):
                if file.endswith('.txt'):
                    # setting file path to each new book txt file
                    new_file_path = os.path.join(self.book_folder_path, file)
                    # opening and reading file
                    with open(new_file_path, 'r', encoding='utf-8') as new_file:
                        title_start = 0
                        title_end = 0
                        extended_title = ""
                        authors = ""
                        release_dates = ""
                        update_dates = ""
                        languages = ""
                        producers = ""
                        new_list = new_file.readlines()
                        # extracting the title
                        for lines in new_list:
                            re_title = re.findall('^Title:.*$', lines)
                            if re_title:
                                title_start = new_list.index(lines)
                        # extracting the author
                        for lines in new_list:
                            re_author = re.findall('^Author:.*$', lines)
                            if re_author:
                                title_end = new_list.index(lines)
                                for author in re_author:
                                    authors = re.sub('Author: ', '', author)
                        # extracting the release date
                        for lines in new_list:
                            re_release_date = re.findall('^Release Date:.*$', lines)
                            if re_release_date:
                                for release_date in re_release_date:
                                    release_dates = re.sub('Release Date: ', '', release_date)
                                    release_dates = re.sub(' \[.+#.*]', '', release_dates)
                        # extracting the update date
                        for lines in new_list:
                            re_update_date = re.findall('^\[Most recently+.*]', lines)
                            if re_update_date:
                                for update_date in re_update_date:
                                    update_dates = re.sub('\[Most recently updated: ', '', update_date)
                                    update_dates = re.sub('\]', '', update_dates)
                        # extracting producer
                        for lines in new_list:
                            re_producer = re.findall('^Produced by:.*$', lines)
                            if re_producer:
                                for producer in re_producer:
                                    producers = re.sub('Produced by: ', '', producer)
                        # extracting language
                        for lines in new_list:
                            re_language = re.findall('^Language:.*$', lines)
                            if re_language:
                                for language in re_language:
                                    languages = re.sub('Language: ', '', language)
                        for lines in new_list[title_start:title_end]:
                            if lines.find("Title: ") != -1:
                                index = lines.index(":")
                                extended_title += lines[index + 1:len(lines) - 1].strip()
                            else:
                                if lines != "\n":
                                    extended_title += " " + lines[:len(lines) - 1].strip()
                        book_list.append((extended_title, authors, release_dates, update_dates, languages, producers,
                                          new_file_path.strip()))
            # opening and writing book info to books.txt file
            with open(self.book_info_path, 'w') as book_info_file:
                for book in book_list:
                    title = book[0]
                    author = book[1]
                    release_date = book[2]
                    update_date = book[3]
                    language = book[4]
                    producer = book[5]
                    file_path = book[6]
                    if title == '':
                        title = 'NA'
                    if author == '':
                        author = 'NA'
                    if release_date == '':
                        release_date = 'NA'
                    if update_date == '':
                        update_date = 'NA'
                    if language == '':
                        language = 'NA'
                    if producer == '':
                        producer = 'NA'
                    if file_path == '':
                        file_path = 'NA'

                    book_obj = Book(title, author, release_date, update_date, language, producer, file_path)
                    book_info_file.write(book_obj.__str__() + '\n')
                status_flag = True
        # excception handling for if file is not found
        except FileNotFoundError as e:
            print("File Not Found!"+str(e))
            return False
        except:
            print("Some error occurred!")
            return False
        finally:
            return status_flag

    def load_book_info(self):
        """
        loads book info from books.txt

        Returns
        -------
        status_flag : boolean
          a boolean result indicating success of method

        """

        try:
            status_flag = False
            status_flag = self.extract_book_info()
            # opening and reading books.txt
            with open(self.book_info_path, 'r') as book_data_file:
                book_data = book_data_file.readlines()

                for data in book_data:
                    title = data.split(';;;')[0]
                    author = data.split(';;;')[1]
                    release_date = data.split(';;;')[2]
                    update_date = data.split(';;;')[3]
                    language = data.split(';;;')[4]
                    producer = data.split(';;;')[5]
                    file_path = data.split(';;;')[6]
                    book_obj = Book(title, author, release_date, update_date, language, producer, file_path)
                    self.book_title_list.append(title)
                    self.book_info_dict[title] = book_obj
                status_flag = True
        # exception handling for if file is not found
        except FileNotFoundError as e:
            print("Some error occurred!"+str(e))
            return False
        except:
            return False
        finally:
            return status_flag

    def get_counts(self, book_title):
        """
        returns the number of chapters, words and lines for the specified book_title

        Parameters
        ----------
        book_title : str
          a string to store the title of the book

        Returns
        -------
        tuple
        a tuple consisting of number of chapters, words and lines for the specified book_title

        """

        try:
            book_obj = Book()
            start_index = 0
            end_index = 0
            chapter_count = 0
            start_content = 0
            end_content = 0
            line_count = 0
            for books in self.book_info_dict.keys():
                if book_title.upper() == books.upper():
                    book_obj = self.book_info_dict[books]
            if book_obj is not None:
                book_path = book_obj.book_path
                book_path = book_path[:len(book_path) - 1].strip()
                # opening the book file based on book's title
                with open(book_path, 'r', encoding='utf-8') as new_file:
                    book_content = new_file.readlines()
                    # obtaining number of chapters
                    for lines in book_content:
                        if start_content == 0:
                            if lines.lower().find('content') != -1:
                                start_content = book_content.index(lines)
                        if start_content > 0 and end_content == 0:
                            line_count += 1
                            if lines.lower().find('illustration') != -1:
                                end_content = start_content + line_count
                            if lines == '\n' and line_count > 2:
                                end_content = start_content + line_count
                    chapter_list = book_content[start_content:end_content]
                    for chapter in chapter_list:
                        if chapter != '' or chapter != '\n':
                            chapter_count += 1
                    # finding out where story starts and ends to obtain word and line count
                    for lines in book_content:
                        if lines.find("*** START OF") != -1:
                            start_index = book_content.index(lines)
                        if lines.find("*** END OF") != -1:
                            end_index = book_content.index(lines)
                    book_content = book_content[start_index + 1:end_index]
                    line_count = len(book_content)
                    re_pattern = '[\.\,\:\;\-\_\(\)\{\}\[\]\'\"\!\?]'
                    word_count = 0
                    for lines in book_content:
                        lines = re.sub(re_pattern, " ", lines)
                        if lines != "\n":
                            line_list = lines.split(" ")
                            for lines in line_list:
                                if lines not in ('', ' ', '\n'):
                                    word_count += 1
                    return chapter_count, word_count, line_count
            else:
                print("No such book found!")
                return 0, 0, 0
        # exception handling for if file is not found
        except FileNotFoundError as e:
            print("File not found. " + str(e))
            return 0, 0, 0
        except:
            print("Some error occured.")
            return 0, 0, 0

    def display_titles(self, page_number):
        """
        displays titles of books listed in book_title_list list

        Parameters
        ----------
        page_number : int
          an integer to store the page number

        Returns
        -------
        str
        a string consisting of books listed in book_title_list list.

        """

        try:
            total_pages = 0
            if len(self.book_title_list) % 10 > 0:
                total_pages = (len(self.book_title_list) // 10) + 1
            else:
                total_pages = len(self.book_title_list) // 10
            if page_number <= 0 or page_number > total_pages:
                print("Error! Please enter valid page number.")
            else:
                start_index = 0
                end_index = 0
                if total_pages > 0:
                    start_index = (page_number * 10) - 10
                    end_index = (page_number * 10)
                    title_list = self.book_title_list[start_index:end_index]
                print("List of Book Titles".center(70, '~'))
                for titles in title_list:
                    print(f"{start_index + 1}. {titles}")
                    start_index += 1
                print('\n\n')
                print(f'Current Page: {page_number}')
                print(f'Total Pages: {total_pages}')
                return True
        except:
            print("Some error occurred")
            return False

    def show_book_content(self, book_title):
        """
        returns book title with list of contents displayed

        Parameters
        ----------
        book_title : str
          a string to store the title of the book

        Returns
        -------
        str
        a string consisting of the book title and the contents

        """

        try:
            book_obj = Book()
            chapter_list = []
            start_content = 0
            end_content = 0
            line_count = 0
            for books in self.book_info_dict.keys():
                if book_title.upper() == books.upper():
                    book_obj = self.book_info_dict[books]
            if book_obj is not None:
                book_path = book_obj.book_path
                book_path = book_path[:len(book_path) - 1].strip()

                with open(book_path, 'r', encoding='utf-8') as new_file:
                    book_content = new_file.readlines()
                    for lines in book_content:
                        if start_content == 0:
                            if lines.lower().find('content') != -1:
                                start_content = book_content.index(lines)+1
                        if start_content > 0 and end_content == 0:
                            line_count += 1
                            if lines.lower().find('illustration') != -1:
                                end_content = start_content + line_count
                            if lines == '\n' and line_count > 2:
                                end_content = start_content + line_count
                    chapter_list = book_content[start_content:end_content]
                print("Contents".center(70,'~'))
                if chapter_list:
                    for lines in chapter_list:
                        if lines != '\n':
                            print(lines)
                else:
                    print("Content Not Available")
                print("".center(70,'~'))
            else:
                print("No such book found!")
            return True
        # exception handling for if file is not found
        except FileNotFoundError as e:
            print("File not found!"+str(e))
            return False
        except:
            print("Some Error Occurred!")
            return False

    def show_book_text(self, book_title, page_number):
        """
        displays one page of book text includes book title, chapter number, book text and page number

        Parameters
        ----------
        book_title : str
          a string to store the title of the book
        page_number : int
          an integer to store the page number

        Returns
        -------
        str
        a string consisting of one page of book text with book title, chapter number and page number.
        """

        try:
            book_obj = Book()
            total_pages = 0
            start_index = 0
            end_index = 0
            for books in self.book_info_dict.keys():
                if book_title.upper() == books.upper():
                    book_obj = self.book_info_dict[books]
            if book_obj is not None:
                book_path = book_obj.book_path
                book_path = book_path[:len(book_path) - 1].strip()

                with open(book_path, 'r', encoding='utf-8') as new_file:
                    book_content = new_file.readlines()
                    for lines in book_content:
                        if lines.upper().find("*** START OF") != -1:
                            start_index = book_content.index(lines)
                        if lines.upper().find("*** END OF") != -1:
                            end_index = book_content.index(lines)
                            break
                    book_content = book_content [start_index+1:end_index]
                    total_pages = mat.ceil(len(book_content)/15)
                    if page_number > total_pages:
                        print(f"\nSorry the book has only {total_pages} pages. Please enter an acceptable value\n")
                        return True
                    for content in book_content:
                        if '\n' in book_content:
                            book_content.remove('\n')
                    read_start_index = (page_number*15)-15
                    read_end_index = page_number*15
                    print(f"Start of page {page_number}".center(70, '-'))
                    for lines in book_content[read_start_index:read_end_index]:
                        print(lines)
                    print(f"End of page {page_number}".center(70, '-'))
                    return True
            else:
                print("Book not found!")
                return False
        # exception handling for if file is not found
        except FileNotFoundError as e:
            print("File not found. " + str(e))
            return False
        except:
            print("Some error occurred.")
            return False


    def get_book_by_author(self, author_name):
        """
        prints book title followed by full author name

        Parameters
        ----------
        author_name : str
          a string to store the author's name

        Returns
        -------
        str
        prints book title followed by full author name
        """

        try:
            books_by_authors = []
            for books in self.book_info_dict:
                author = self.book_info_dict[books].author
                if author.lower().find(author_name.lower()) != -1:
                    books_by_authors.append((self.book_info_dict[books].title, self.book_info_dict[books].author))
            print(f"Books by {author_name}".center(70, '~'))
            if books_by_authors:
                count = 1
                for books in books_by_authors:
                    print(f"{count}. {books[0]} _ {books[1]}")
                    count += 1
            else:
                print(f"No books by {author_name}")
            return True

        except:
            print("Some error occurred!")
            return False

    def get_book_release_year(self):
        """
        prints total number of books for specific release year ranges

        Returns
        -------
        str
        prints total number of books for specific release year ranges
        """

        try:
            books_before_1990 = 0
            books_between_1990_2000 = 0
            books_after_2000 = 0
            for books in self.book_info_dict:
                release_year = self.book_info_dict[books].release_date[-4:]
                if int(release_year) < 1990:
                    books_before_1990 += 1
                elif 2000 >= int(release_year) >= 1990:
                    books_between_1990_2000 += 1
                elif int(release_year) > 2000:
                    books_after_2000 += 1
            print("Total Number of Books by Year".center(70, '~'))
            print(f"Number of books released before 1990: {books_before_1990}")
            print(f"Number of books released between 1990 and 2000: {books_between_1990_2000}")
            print(f"Number of books released after 2000: {books_after_2000}")

            return True
        except:
            print("Some error occurred!")
            return False
