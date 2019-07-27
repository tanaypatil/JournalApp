import json
from datetime import datetime
from settings import MAX_JOURNAL_ENTRY_COUNT


class JournalEntry:
    def __init__(self, text):
        self.text = text
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M%p")

    def save(self):
        """
        Saves journal entry.
        :return: True if entry is saved, else False
        """
        if is_session_valid():
            username = get_session_username()
            try:
                with open('JournalApp/Journals/' + username + ".json", 'r') as file:
                    journal = json.load(file)
                    file.close()
                journal = sorted(journal, key=lambda x: x['created_at'], reverse=True)
            except Exception as e:
                journal = []
            if len(journal) == MAX_JOURNAL_ENTRY_COUNT:
                journal = journal[:MAX_JOURNAL_ENTRY_COUNT-1]
            with open('JournalApp/Journals/' + username + ".json", 'w') as file:
                journal_entry = JournalEntry(text=self.text)
                journal.append(journal_entry.__dict__)
                json.dump(journal, file)
                file.close()
            return True
        else:
            return False


def is_session_valid():
    """
    Checks if session is valid.
    :return: True if session is valid, else False
    """
    try:
        with open('user_session.json', 'r') as file:
            session = json.load(file)
            if session['logged_in'] and "username" in session:
                valid = True
            else:
                valid = False
            file.close()
        return valid
    except Exception as e:
        return False


def get_session_username():
    """
    Get username of logged in user.
    :return: Username.
    """
    with open('user_session.json', 'r') as file:
        session = json.load(file)
        return session['username']


def get_journal():
    """
    Returns list of journal entries.
    :return: Journal entry list.
    """
    if is_session_valid():
        username = get_session_username()
        try:
            with open('JournalApp/Journals/'+username+'.json', 'r') as file:
                journal = json.load(file)
                file.close()
        except:
            journal = []
        return journal
    else:
        return []


def print_journal(journal):
    """
    Prints entries from journal.
    :param journal: Journal
    :return: -
    """
    try:
        journal = sorted(journal, key=lambda x: x['created_at'], reverse=True)
        if len(journal) == 0:
            print("No entries in Journal.")
        else:
            for entry in journal:
                entry_format = f'{entry["created_at"]} ---- {entry["text"]}'
                print(entry_format)
    except Exception as e:
        print("No entries in Journal.")
