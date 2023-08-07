from db import DB
from schedulers import run_schedules
from utils import parse_contacts_data

db = DB()

run_schedules()

while True:
    get_contacts = db.search_contacts(input())
    print(parse_contacts_data(get_contacts))
