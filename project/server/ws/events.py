from flask import request

from flask_socketio import send, emit

from project.server import socketio

def ack(msg):
    print('message was received: ', msg)

@socketio.on('connect')
def on_connect():
    print(request.headers)
    send('Welcome to Socket-IO!', callback=ack)

@socketio.on('disconnect')
def test_disconnect():
    print(request.sid, " client disconnected!")

@socketio.on('my message')
def another_event(data):
    print('my message', data)
    emit('my message', data)

@socketio.on('my broadcast message')
def another_event(data):
    print('my broadcast message', data)
    emit('my message', data, broadcast=True)

@socketio.on('message')
def handle_message(message):
    print('incoming message: ', message)