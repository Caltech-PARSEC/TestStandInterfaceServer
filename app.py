#!/usr/bin/env python
from queue import Queue
from threading import Lock
from flask import Flask, render_template, request
from flask_socketio import SocketIO, disconnect
from flask_socketio import emit as sio_emit

from messages import emit, emit_message, ServerMessage

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

command_queue = Queue()
command_id = 0

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

@socketio.on('add_to_command_queue')
def add_to_command_queue(commands):
    global command_id
    global command_queue

    ids = []

    for cmd in commands:
        cmd.update({'id': command_id})
        ids.append(command_id)
        command_queue.put(cmd, block=True)
        command_id += 1

    sio_emit('queue_status', {'data': 'added', 'ids': ids})

@socketio.on('remove_from_queue')
def remove_from_command_queue(command_id):
    global command_queue

    temp_cmd = command_queue.get(block=False)
    temp_queue = []

    # Remove items until we find the command to remove. Add each command
    # to our temp queue once we confirm we shouldn't remove it.
    while temp_cmd['id'] != command_id and not command_queue.empty():
        temp_queue.append(temp_cmd)
        temp_cmd = command_queue.get(block=False)
    # If this is true, then the queue got emptied, so this should be added to
    # the temp queue.
    if temp_cmd['id'] != command_id:
        temp_queue.append(temp_cmd)

    while len(temp_queue) > 0:
        command_queue.put(temp_queue.pop())

    if temp_cmd['id'] == command_id:
        sio_emit('queue_status', {'data': 'removed', 'ids': [command_id]})
    else:
        sio_emit('queue_status', {'data': 'remove failed'})


@socketio.on('cl_ping', namespace=namespace)
def ping_pong():
    emit('sv_pong')

@socketio.on('connect', namespace=namespace)
def do_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)

    message = ServerMessage('Connected!')
    emit(message)

@socketio.on('disconnect_request', namespace=namespace)
def disconnect_request():
    message = ServerMessage('Disocnnected!')
    emit(message)
    disconnect()

@socketio.on('disconnect', namespace=namespace)
def do_disconnect():
    print('Client disconnected', request.sid)

if __name__ == '__main__':
    socketio.run(app, debug=True)
