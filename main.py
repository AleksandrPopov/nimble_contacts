from api import app
from config import HOST, PORT
from schedulers import run_schedules

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
    run_schedules()
