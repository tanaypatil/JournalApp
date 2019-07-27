from JournalApp.Journals.journal_manager import JournalEntry, get_journal, print_journal


def show_home_screen():
    """
    Shows home screen. Gives choice of creating journal entry or listing all journal entries.
    :return: -
    """
    print("\n")
    print("********************** JOURNAL APP ****************************")
    print("***************************************************************")
    print("Create your journal with Journal App and store upto 50 entries.")
    print("***************************************************************")
    while True:
        print("\n\n***********************************************************")
        print("a. Press 1 to list all journal entries.")
        print("b. Press 2 to create a journal entry.")
        print("c. Press 3 to log out.")
        action = input("Your response: ")
        if action == "1":
            journal = get_journal()
            print("\n**************************Listing your journal entries*******************************\n")
            print_journal(journal)
            print("\n*************************************************************************************\n")
        elif action == "2":
            text = input("\nEnter journal text: ")
            journal_entry = JournalEntry(text=text)
            created = journal_entry.save()
            if created:
                print("Journal Entry created successfully.\n")
            else:
                print("Journal entry not created.\n")
        elif action == "3":
            print("Logging Out.")
            with open('user_session.json', 'w') as file:
                file.write("")
                file.close()
            break
        else:
            print("\nEnter a valid value.\n")
