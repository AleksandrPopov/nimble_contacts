from api import app
from config import SERVER_HOST, SERVER_PORT
from schedulers import run_schedules

if __name__ == '__main__':
    app.run(host=SERVER_HOST, port=SERVER_PORT)
    run_schedules()
