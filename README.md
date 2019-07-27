# JOURNAL APP

### Technologies Used - 
1. Python 3.6

### Dependencies - 
None

### Project Structure
    JournalApp
    |----JournalApp
         |----HomeScreen
              |----__init__.py
              |----home_screen.py
         |----Journals
              |----__init__.py
              |----journal_manager.py
         |----Login
              |----__init__.py
              |----login.py
         |----SignUp
              |----__init__.py
              |----signup.py
         |----Users
              |----__init__.py
              |----user_manager.py
              |----users.json
         |----WelcomeScreen
              |----__init__.py
              |----welcome_screen.py
         |----__init__.py
    |----main.py
    |----settings.py
    |----requirements.txt
    |----README.md

### Description - 
The "Journal App" application is a terminal based application which can be run on terminal of any machine having the required python
version, or higher. The "Journal App" provides the feature of creating and saving upto 50(can be changed from the settings.py file) 
journal entries. After the maximum number of journal entries is reached, the oldest journal is replaced when a new entry is created.
The maximum number of users that can signup is 10(can be changed from settings.py file). A user can list all his journal entries or
create a new one.

### How to run?
Run the main.py file.<br>
On the terminal type - python main.py

### Working
***All the data is saved in json files. No database is used.***

Upon starting the app the user sees the welcome screen. The user is given choice to signup, login or exit.<br>
Sign Up-
1. If the user selects to Sign up the the user is redirected to Signup screen and is asked username and password.
2. When the user enters a username and password, the credentials are validated. If the crdentials are valid the user is signed up.
3. Username is valid if it's length is 8 and is alphanumeric. Password is valid when it's length is 8.
4. When the user signs up, an user entry is created in JournalApp/JournalApp/Users/users.json.
5. The password is hashed before saving.
6. The user is redirected to home screen after signing up successfully and the user session is saved in user_session.json.
7. If the number of registered users is equal to the MAX_USERS_COUNT from settings.py file the a new user can't sign up.

Log In-<br>
1. The user is asked for credentials when login option is selected.
2. The entered credentials are validated. The app checks if the user exists and the password is correct.
3. The provided password is verified against the stored password.
4. Upon successful login the user is redirected to the home screen.
5. The user session is saved in user_session.json

Exit-<br>
The app is closed.

Home Screen-<br>
On the home screen the user is given option to create a journal entry or list all entries.
Create Journal Entry - 
1. The user is asked to enter journal entry text.
2. After the text is entered, if the user has created his first user entry then a journal file with the username oas name
   is created in JournalApp/JournalApp/Journals.
3. The journal entry is saved with it's creation date.
4. If the entry is not the user's first entry then the entry is added in the username.json file which already exists.
5. If the number of journal entries is equal to MAX_JOURNAL_ENTRIES then the oldest entry is replaced if a new entry is added.

List Journal Entries - 
1. Lists all journal entries from user's journal(username.json).

Log Out - 
1. The user session is invalidated by removing data from user_session.json.
2. User is redirected to Welcome screen.