from flask import Flask, request
from db import DB

app = Flask(__name__)


@app.route('/search')
def search_contacts_api():
    """
    "You can try the API at this address http://79.132.137.32:5000/search?name='name'
    """
    contact_name = request.args.get('name')
    get_contacts = DB().search_contacts(contact_name=contact_name)
    return get_contacts if len(get_contacts) != 0 else {'result': f'{contact_name} not found'}
