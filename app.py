#!/usr/bin/env python3
from threading import Lock
from flask import Flask, render_template, request
from flask_socketio import SocketIO, disconnect
from flask_socketio import emit
import time

from src.sensors import SensorManager
from src.valves import ValveManager

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

# App setup
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.logger.disabled = True
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

namespace = '/socket'

# Other setup
start_time = time.time()

valve_manager = ValveManager()
sensor_manager = SensorManager()

def client_tester():
    i = 0
    while True:
        # TODO: Add better client test
        # Code to test Client
        send_log_data('Hello World!')
        send_sensor_data(sensor_manager.get_sensor_by_name("Pressure Sensor 1"))
        send_sensor_data(sensor_manager.get_sensor_by_name("Temperature Sensor 1"))
        # socketio.emit('sensor_data', {'time': time.time() - start_time,
        #                               'name': 'sensor1',
        #                               'value': i})
        # socketio.emit('sensor_data', {'time': time.time() - start_time,
        #                               'name': 'sensor2',
        #                               'value': i + 1})
        i += 1
        socketio.sleep(1);

@socketio.on('connect')
def connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(client_tester)

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@socketio.on('cl_ping', namespace=namespace)
def ping():
    emit('sv_pong')

####################
# Message Handling #
####################
@socketio.on('cl_msg', namespace=namespace)
def event(msg):
    print('Message from Client:', msg)

@socketio.on('valve_seq', namespace=namespace)
def valve_seq(valve_seq):
    print('Valve Sequence:', valve_seq)

@socketio.on('set_valve')
def set_valve(data):
    # print("name:", data['name'], "should_open:", data['should_open'])
    # return
    valve = valve_manager.get_valve(data['name'])
    if data['should_open']:
        valve.open()
    else:
        valve.close()

@socketio.on('set_sensor')
def set_sensor(data):
    sensor = sensor_manager.getSensorByName(data['name'])
    sensor.set_sensor_value(data['value'])

@socketio.on('emergency_stop', namespace=namespace)
def emergency_stop():
    print('EMERGENCY STOP REQUESTED!!!')
    print('BUT IT IS NOT YET IMPLEMENTED')

###################
# Message Pushing #
###################

# TODO: replace the datetime.now() call with the time the
# sensor reading was obtained.
def send_sensor_data(sensor):
    socketio.emit('sensor_data', {'time': time.time() - start_time,
                                  'name': sensor.get_name(),
                                  'value': sensor.get_sensor_value()})

# TODO: refactor angle component
def send_valve_data(valve):
    socketio.emit('valve_data', {'time': time.time() - start_time,
                                 'name': valve.get_name(),
                                 'angle': valve.last_value})

def send_log_data(message):
    socketio.emit('log_data', {'message': message})

if __name__ == '__main__':
    socketio.run(app, debug=False)
