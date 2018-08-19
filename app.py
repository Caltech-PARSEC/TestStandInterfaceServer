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

@socketio.on('cl_msg', namespace=namespace)
def event(msg):
    print('Message from Client:', msg)

@socketio.on('valve_seq', namespace=namespace)
def event(valve_seq):
    print('Valve Sequence:', valve_seq)

@socketio.on('emergency_stop', namespace=namespace)
def emergency_stop():
    print('EMERGENCY STOP REQUESTED!!!')

if __name__ == '__main__':
    socketio.run(app, debug=False)
