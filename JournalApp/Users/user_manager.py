import binascii
import hashlib
import json
import os


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save(self):
        """
        Saves user in file.
        :return: -
        """
        print("Signing up...")
        with open('JournalApp/Users/users.json', 'r') as file:
            users = json.load(file)
            if users is None or users == "" or len(users) <= 0:
                users = []
            file.close()
        with open('JournalApp/Users/users.json', 'w') as file:
            self.password = User.hash_password(self.password)
            users.append(self.__dict__)
            json.dump(users, file)
            file.close()
        print("User saved successfully.")

    @staticmethod
    def is_unique_username(username):
        """
        Checks if username is unique.
        :param username: Username
        :return: True if username is unique, else False
        """
        with open('JournalApp/Users/users.json', 'r') as file:
            users = json.load(file)
            file.close()
        if users is None or users == "" or len(users) <= 0:
            return True
        else:
            user = list(filter(lambda x: x['username'] == username, users))
            if len(user) > 0:
                return False
            else:
                return True

    @staticmethod
    def check_username(username):
        """
        Checks if username is a valid.
        :param username: Username
        :return: Dict - 'valid' - True if username is valid, else False. 'error': Error string passed if valid is False
        """
        if len(username) != 8:
            return {'valid': False, "error": "Username should be 8 characters long."}
        elif not username.isalnum():
            return {'valid': False, "error": "Username should be alphanumeric."}
        elif not User.is_unique_username(username):
            return {'valid': False, "error": "Username already taken."}
        else:
            return {'valid': True}

    @staticmethod
    def check_password(password):
        """
        Checks if password is valid.
        :param password: Password
        :return: Dict - 'valid' - True if password is valid, else False. 'error': Error string passed if valid is False
        """
        if len(password) != 8:
            return {'valid': False, "error": "Password should be 8 characters long."}
        else:
            return {'valid': True}

    @staticmethod
    def hash_password(password):
        """
        Hashes password.
        :param password: Password
        :return: Hashed password.
        """
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                      salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    @staticmethod
    def verify_password(stored_password, provided_password):
        """
        Verifies stored password against the password provided by user.
        :param stored_password: Stored password.
        :param provided_password: User provided password.
        :return: True if stored password and provided passwords are same, else False
        """
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',
                                      provided_password.encode('utf-8'),
                                      salt.encode('ascii'),
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

    @staticmethod
    def get_user_count():
        """
        Count registered users.
        :return: Number of users.
        """
        with open('JournalApp/Users/users.json', 'r') as file:
            users = json.load(file)
            if users is None or users == "" or len(users) <= 0:
                users = []
            file.close()
        return len(users)

    def exists(self):
        """
        Checks if user exists in file.
        :return: True if user exists, else False
        """
        with open('JournalApp/Users/users.json', 'r') as file:
            users = json.load(file)
            file.close()

        if users is None or users == "" or len(users) <= 0:
            exists = False
            # return {'valid': False, 'error': "User doe not exist."}
        else:
            user = list(filter(lambda x: x['username'] == self.username, users))
            if len(user) > 0:
                exists = True
            else:
                exists = False
        return exists

    def is_valid(self):
        """
        Checks if user is valid by verifying username and password.
        :return: True if user is valid, else False.
        """
        with open('JournalApp/Users/users.json', 'r') as file:
            users = json.load(file)
            file.close()
        if users is None or users == "" or len(users) <= 0:
            return False
        user = list(filter(lambda x: x['username'] == self.username, users))[0]
        if User.verify_password(user['password'], self.password):
            return True
        else:
            return False


