"""
Group Number: 61, Applied Class 04
Group Members:
1) Pragy Parashar
2) Parnoor Parnoor
3) Joanna Song Chea Lee

Date:
Description:
"""


class Book:
    """
    A class used to represent a book

    Attributes
    —---------
    title : str
      a string to store the book title
    author : str
      a string to store the book author
    release_date : str
      a string to store the release date of the book
    last_update_date : str
      a string to store the last update date of the book
    producer : str
      a string to store the producer of the book
    book_path : str
      a string to store the relative path of the book text file

    """

    def __init__(self,
                 title="",
                 author="",
                 release_date="",
                 last_update_date="",
                 language="",
                 producer="",
                 book_path=""
                 ):
        """
        Constructs a book object

        Parameters
        ----------
        title : str
          The title of the book
        author : str
          The author of the book
        release_date : str
          The release date of the book
        last_update_date : str
          The last update date of the book
        producer : str
          The producer of the book
        book_path : str
          The relative path of the book text file

        """
        self.title = title
        self.author = author
        self.release_date = release_date
        self.last_update_date = last_update_date
        self.language = language
        self.producer = producer
        self.book_path = book_path

    def __str__(self):
        """
        Returns all the book's attributes as a formatted string
        """
        return f"{self.title};;;{self.author};;;{self.release_date};;;{self.last_update_date};;;{self.language};;;{self.producer};;;{self.book_path}"
