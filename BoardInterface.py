import can
can.rc['interface'] = 'socketcan'
can.rc['channel'] = 'vcan0'
can.rc['bitrate'] = 500000
from can.interfaces.interface import ThreadSafeBus

class CanListener(can.Listener):
    def message_handler(boardId, sensorId, data):
        print("boardId: ", boardId, "\tsensorId: ", sensorId, "\tdata: ", data)

    def on_message_recieved(self, msg):
        boardId = msg.arbitration_id >> 6
        sensorId = msg.arbitration_id && 0b111111
        data = msg.data
        hander(boardId, sensorId, data)


class BoardInterface:
    bus = ThreadSafeBus()
    listener = CanListener()
    notifier = can.Notifier(bus, [listener])

    @staticmethod
    def write_valve(boardID, valveID, angle):
        arbId = (boardID << 6) | (valveID)
        #TODO: angle should be converted to standard 16 bit representation for float
        message = can.Message(arbitration_id=arbId, data=[angle])

    @staticmethod
    def set_message_handler(messageHandler):
        listener.message_handler = messageHandler
