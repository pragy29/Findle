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
from reader import Reader
import os
import random as ran
import re


class UserOperation:
    """
    Contains all the operations related to a user.

    Attributes
    ----------
    user_info_path : str
      a string to store the relative path of the users.txt file
    user_info_list :list
      a list to store all users.
    user_name : str
      a string to store the username
    user_password: str
      a string to store the user's password
    user_role : str
      a string to store the user's role

    Methods
    -------
    load_user_info()
      loads all the registered users information from users.txt into the user_info_list list
    user_registration(user_name, user_password, user_role)
      creates a user object and save it in user_info_list list.
    user_login(user_name, user_password)
      authenticate a user login attempt.
    write_user_info()
      writes all user info in user_info_list and in the provided user_info_path
    """

    user_info_list = []
    user_info_path = "./data/result_data/users.txt"

    def load_user_info(self):
        """
        loads all the registered users information from users.txt into the user_info_list list

        Returns
        ----------
        A boolean result to indicate success of method
        """

        status_flag = False
        try:
            users_file = open(self.user_info_path, 'r')
            users_list = users_file.readlines()
            for user in users_list:
                if len(user.split(';;;')) == 4:
                    user_id = user.split(';;;')[0]
                    user_name = user.split(';;;')[1]
                    user_password = user.split(';;;')[2]
                    user_role = user.split(';;;')[3]
                    user_role = user_role[:len(user_role)-1]
                    user_obj = User(user_id, user_name, user_password, user_role)
                    self.user_info_list.append(user_obj)
                else:
                    user_id = user.split(';;;')[0]
                    user_name = user.split(';;;')[1]
                    user_password = user.split(';;;')[2]
                    user_role = user.split(';;;')[3]
                    favourite_book = eval(user.split(';;;')[4])
                    bookmark_list = eval(user.split(';;;')[5])
                    reader_obj = Reader(user_id, user_name, user_password, user_role, favourite_book, bookmark_list)
                    self.user_info_list.append(reader_obj)
            users_file.close()
            status_flag = True
        except FileNotFoundError as e:
            print("File not found. " + str(e))
        except:
            return False
        finally:
            return status_flag

    def user_registration(self,
                          user_name="",
                          user_password="",
                          user_role=""):
        """
        creates a user object and save it in user_info_list list.

        Parameters
        ----------
        user_name : str
          a string to store the username
        user_password: str
          a string to store the user's password
        user_role : str
          a string to store the user's role

        Returns
        -------
        A boolean result to indicate success of method
        """

        check_user_flag = False
        user_role = "user"
        try:
            existing_user = []
            existing_user_names = []
            new_user_id = str(ran.randint(1000000000, 9999999999))
            for users in self.user_info_list:
                existing_user.append([users.user_id, users.user_name, users.user_password, users.user_role])
            if existing_user:
                for users in existing_user:
                    while True:
                        if new_user_id in users:
                            new_user_id = str(ran.randint(1000000000, 9999999999))
                        else:
                            break
                    existing_user_names.append(users[1])

            if user_name in existing_user_names:
                check_user_flag = False
            else:
                check_user_flag = True

            if check_user_flag:
                user = User(new_user_id, user_name, user_password, user_role)
                self.user_info_list.append(user)
        except:
            return False
        finally:
            return check_user_flag

    def user_login(self, user_name, password):
        """
        Authenticate a user login attempt.

        Parameters
        ----------
        user_name : str
          a string to store the username
        user_password: str
          a string to store the user's password

        Returns
        -------
        A boolean result to indicate success of method
        """

        check_user_authentication = False
        try:
            for user in self.user_info_list:
                if user.user_name == user_name and user.user_password == password:
                    check_user_authentication = True
                    break
                else:
                    check_user_authentication = False
        except:
            return False
        finally:
            return check_user_authentication

    def write_user_info(self):
        """
        writes all user info in user_info_list and in the provided user_info_path

        Returns
        -------
        A boolean result to indicate success of method
        """

        status_flag = False
        try:
            users_file = open(self.user_info_path, 'w')
            for users in self.user_info_list:
                users_file.write(users.__str__()+'\n')
            status_flag = True
            users_file.close()
        except FileNotFoundError as e:
            print("File not found. " + str(e))
        except:
            return False
        finally:
            return status_flag
