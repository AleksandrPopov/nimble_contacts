def parse_contacts_data(contacts_list: list) -> str:
    """
    To parse raw contacts data from db
    :return str contacts data
    """
    if len(contacts_list) != 0:
        result = f'Find {len(contacts_list)} coincidences:\n\n'
        for i in contacts_list:
            result += f'First name: {i[0]}\n' \
                      f'Last Name: {i[1]}\n' \
                      f'Email: {i[2]}\n\n'
    else:
        result = f'Find {len(contacts_list)} coincidences:\n'

    return result
