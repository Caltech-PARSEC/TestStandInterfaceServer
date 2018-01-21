from socketio import emit as sio_emit

def emit(message, namespace):
    assert(isinstance(message, Message))
    sio_emit(message.message_type, message.data_map(), namespace=namespace)

def emit_message(socketio, message, namespace):
    assert(isinstance(message, Message))
    socketio.emit(message.message_type, message.data_map(), namespace=namespace)

class Message:
    message_type = None

    def data_map(self):
        raise NotImplementedError('This method must be implemented.')

class SensorDataMessage(Message):
    message_type = 'sensor_data'

    def __init__(self, sensor_name, sensor_type):
        self.sensor_name = sensor_name
        self.sensor_type = sensor_type
        self.sensor_value = None

    def set_sensor_value(self, sensor_value):
        self.sensor_value = sensor_value

    def data_map(self):
        return {
            'data': 'Data from {}.'.format(self.sensor_name),
            'sensor_name': self.sensor_name,
            'sensor_type': self.sensor_type,
            'sensor_value': self.sensor_value
        }

class ServerMessage(Message):
    message_type = 'server_message'

    def __init__(self, message):
        self.message = message

    def data_map(self):
        return {
            'data': self.message
        }
