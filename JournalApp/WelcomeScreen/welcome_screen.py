from JournalApp.Login.login import show_login_screen
from JournalApp.SignUp.signup import show_signup_screen


def show_welcome_text():
    """
    Shows the welcome screen. Gives choice to login or signup.
    :return: -
    """
    print("\n")
    print("********************************************************************")
    print("********************** WELCOME to JOURNAL APP **********************")
    print("********************************************************************")
    print("\n")
    while True:
        print("\n\n***********************************************************")
        print("a. Press 1 to 'Sign Up' as a new User")
        print("b. Press 2 to 'Log In' if you are an existing User")
        print("c. Press 3 to exit.")
        starting_action = input("Your response: ")
        if starting_action == "1":
            show_signup_screen()
        elif starting_action == "2":
            show_login_screen()
        elif starting_action == "3":
            print("Exiting...")
            with open('user_session.json', 'w') as file:
                file.write("")
                file.close()
            exit(0)
        else:
            print("\nEnter a valid value.\n")
