from flask import Flask, jsonify, request
from db import DB

app = Flask(__name__)


@app.route('/search')
def search_contacts_api():
    """
    "You can try the API at this address http://79.132.137.32:5000/search?name='name'
    """
    contact_name = request.args.get('name')
    return jsonify(DB().search_contacts(contact_name=contact_name)[0])
