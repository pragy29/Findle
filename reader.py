"""
Group Number: 61, Applied Class 04
Group Members:
1) Pragy Parashar
2) Parnoor Parnoor
3) Joanna Song Chea Lee

Date:
Description:
"""
from user import User
class Reader(User):
    """
    Contains all the information about a reader. This class inherits from the user class

    Attributes
    ----------
    user_id : int
      an integer to store the id of the user
    user_name : str
      a string to store the username
    user_password: str
      a string to store the user's password
    user_role : str
      a string to store the user's role
    favourite_book_list : list
      a list to store reader's favourite books
    bookmark_list : list
      a list of tuples where each tuple refers to bookmarked book title and page number

    """

    def __init__(self,
                 user_id="",
                 user_name="",
                 user_password="",
                 user_role='reader',
                 favourite_book_list=[],
                 bookmark_list=[]):
        """
        Constructs a reader object

        Parameters
        ----------
        user_id : int
          an integer to store the id of the user
        user_name : str
          a string to store the username
        user_password: str
          a string to store the user's password
        user_role : str
          a string to store the user's role
        favourite_book_list : list
          a list to store reader's favourite books
        bookmark_list : list
          a list of tuples where each tuple refers to bookmarked book title and page number
        """

        User.__init__(self,user_id, user_name, user_password, user_role)
        self.favourite_book_list = favourite_book_list
        self.bookmark_list = bookmark_list

    def __str__(self):
        """
        Return all the attributes of a reader as a formatted string.
        """

        return f"{self.user_id};;;{self.user_name};;;{self.user_password};;;{self.user_role};;;{self.favourite_book_list};;;{self.bookmark_list} "
