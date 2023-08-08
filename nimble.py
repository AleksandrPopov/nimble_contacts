import requests

from config import NIMBLE_TOKEN, NIMBLE_API_URL


def get_nimble_contacts() -> list:
    nimble_authorization = {'Authorization': NIMBLE_TOKEN}
    nimble_contacts = requests.get(NIMBLE_API_URL, headers=nimble_authorization)
    nimble_db_fields_list = ['first name', 'last name', 'email']
    contacts_result_contacts_list = []

    if nimble_contacts.status_code == 200:
        nimble_contacts = nimble_contacts.json().get('resources')

        if nimble_contacts is not None and type(nimble_contacts) == list:

            for i in nimble_contacts:
                i = i.get('fields')

                if all(a in list(i.keys()) for a in nimble_db_fields_list):
                    first_name = i.get('first name')[0]['value']
                    last_name = i.get('last name')[0]['value']
                    email = i.get('email')[0]['value'] if i.get('email') is not None else None
                    contacts_result_contacts_list.append((first_name, last_name, email))

    return contacts_result_contacts_list
