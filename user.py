"""
Group Number: 61, Applied Class 04
Group Members:
1) Pragy Parashar
2) Parnoor
3) Joanna Song Chea Lee

Date:
Description:
"""


class User:
    """
    A class that contains all the information about a user

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

    """

    def __init__(self,
                 user_id="",
                 user_name="",
                 user_password="",
                 user_role="user"
                 ):
        """
        Constructs a user object

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
        """

        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.user_role = user_role

    def __str__(self):
        """
        Return all the attributes of a user as a formatted string.
        """
        return f"{self.user_id};;;{self.user_name};;;{self.user_password};;;{self.user_role}"
