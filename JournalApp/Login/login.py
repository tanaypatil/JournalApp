import json
from JournalApp.HomeScreen.home_screen import show_home_screen
from JournalApp.Users.user_manager import User


def show_login_screen():
    """
    Shows the login screen. Asks for login credentials.
    :return: -
    """
    print("\n\n")
    print("****************************************************")
    print("********************** LOG IN **********************")
    print("****************************************************")
    print("\n")
    username = input("Username: ")
    password = input("Password: ")
    user = User(username=username, password=password)
    if user.exists():
        if user.is_valid():
            print("You have successfully logged in.\n")
            login_user(username)
        else:
            print("Invalid User. Enter correct user credentials.\n")
            show_login_screen()
    else:
        print("\nUser doe not exist.\n")
        return


def save_user_session(username):
    """
    Saves user session in file.
    :param username: Username of logged in user.
    :return: -
    """
    session = {'logged_in': True, 'username': username}
    with open('user_session.json', 'w') as file:
        json.dump(session, file)


def login_user(username):
    """
    Saves user session and redirects to home screen.
    :param username: Username
    :return: -
    """
    save_user_session(username)
    show_home_screen()
