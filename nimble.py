import requests

from config import TOKEN, URL


def get_contact() -> list:
    auth = {'Authorization': TOKEN}
    data = requests.get(URL, headers=auth)
    fields_list = ['first name', 'last name', 'email']
    result = []

    if data.status_code == 200:
        data = data.json().get('resources')
        if data is not None and type(data) == list:
            for i in data:
                i = i.get('fields')
                if all(a in list(i.keys()) for a in fields_list):
                    first_name = i.get('first name')[0]['value']
                    last_name = i.get('last name')[0]['value']
                    email = i.get('email')[0]['value'] if i.get('email') is not None else None
                    result.append((first_name, last_name, email))
    return result
