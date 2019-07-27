from JournalApp.Login.login import login_user
from JournalApp.Users.user_manager import User
from settings import MAX_USER_COUNT


def show_signup_screen():
    """
    Shows the signup screen. Asks for signup credentials.
    :return: -
    """
    print("\n\n")
    print("*****************************************************")
    print("********************** SIGN UP **********************")
    print("*****************************************************")
    print("\n")
    if User.get_user_count() >= MAX_USER_COUNT:
        print("\nCannot create more than "+str(MAX_USER_COUNT)+" users.\n")
        return
    else:
        username = input("Username (Should be 8 characters long): ")
        password = input("Password (Should be 8 characters long): ")
        if check_credentials(username, password)['valid']:
            user = User(username=username, password=password)
            user.save()
            login_user(username)
        else:
            show_signup_screen()


def check_credentials(username, password):
    """
    Validates the credentials.
    :param username: Username
    :param password: Password
    :return: True if the credentials are valid, else False
    """
    username_check = User.check_username(username)
    password_check = User.check_password(password)
    if username_check['valid'] and password_check['valid']:
        return {'valid': True}
    else:
        if not username_check['valid']:
            print(username_check['error'])
        if not password_check['valid']:
            print(password_check['error'])
        return {'valid': False}
