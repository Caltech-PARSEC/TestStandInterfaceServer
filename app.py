#!/usr/bin/env python3
from threading import Lock
from flask import Flask, render_template, request
from flask_socketio import SocketIO, disconnect
from flask_socketio import emit

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.logger.disabled = True
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

namespace = '/socket'

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@socketio.on('cl_ping', namespace=namespace)
def ping():
    emit('sv_pong')

@socketio.on('event', namespace=namespace)
def event(msg):
    print('EVENT_HANDLE:', msg)

@socketio.on('broadcast_event', namespace=namespace)
def broadcast_event(msg):
    print('BROADCAST_EVENT_HANDLE', msg)

if __name__ == '__main__':
    socketio.run(app, debug=False)
