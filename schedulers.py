import threading


from db import DB
from nimble import get_contact


def update_contacts_schedule():
    """ Function to update contacts for run_schedules() """

    db = DB()
    while True:
        print('Add', db.add_contacts(get_contact()), 'contacts.')
        threading.Event().wait(86400)


def run_schedules():
    """ Run schedule tasks in background """

    background_thread = threading.Thread(target=update_contacts_schedule)
    background_thread.start()

