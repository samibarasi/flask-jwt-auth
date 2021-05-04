
from dotenv import load_dotenv
from project.server import app, socketio

load_dotenv()

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=5000)