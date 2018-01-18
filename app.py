#!/usr/bin/env python
from threading import Lock
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, disconnect

from messages import emit_message, ServerMessage

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

namespace = '/socket'

def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(10)
        count += 1
        message = ServerMessage('Server generated event')
        emit_message(socketio, message, namespace)

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@socketio.on('ping', namespace=namespace)
def ping_pong():
    emit('pong')

@socketio.on('connect', namespace=namespace)
def do_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)
    emit('server_response', {'data': 'Connected'})

@socketio.on('disconnect_request', namespace=namespace)
def disconnect_request():
    emit('server_response', {'data': 'Disconnected!'})
    disconnect()

@socketio.on('disconnect', namespace=namespace)
def do_disconnect():
    print('Client disconnected', request.sid)

if __name__ == '__main__':
    socketio.run(app, debug=True)
