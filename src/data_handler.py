#import BoardInterface
#
from enum import Enum

class Sensor():

    def __init__(self, sensorID, boardID, name):
        self.sensorID = sensorID
        self.boardID = boardID
        self._lastValue = 0.0
        self.name = name

    def getSensorValue():
        return lastValue

    def setSensorValue(sensorVal):
        lastValue = sensorVal

    def getName():
        return name

    @abstractmethod
    def _rawToRealValue(rawValue):
        pass

class PressureSensor(Sensor):

    def _rawToRealValue(rawValue):          #take in as hex value.
        data = int(rawValue, 16)
        return data * (1500 / 4095)         #Maps from (0x000,0xFFF) to (0,1500) psi

class TempSensor(Sensor):

    def _rawToRealValue(rawValue):
        pass

class ForceSensor(Sensor):

    def _rawToRealValue(rawValue):
        pass



class Valve:

    def __init__(self, valveID, boardID, closedAngle, openAngle, name):
        self._valveID = valveID
        self.boardID = boardID
        self._closeAngle = closeAngle
        self._openAngle = openAngle
        self._lastValue = 0.0
        self.name = name

    def _rawToRealValue(rawValue):
        pass #figure out conversion

    def getValue():
        return lastValue

    def open():
        BoardInterface.writeValve(boardID, valveID, openAngle)

    def close():
        BoardInterface.writeValve(boardID, valveID, closeAngle)

    def getName():
        return name


class SensorManager:

    def __init__(self, ):
        sensors = {}

        for s in sensorEnum:
            sensors = {}

###sensors: sensorenum to sens
###sensors by board: int to list[sens]
###sensors by ID: (int,int) to sens


    class SensorEnum(Enum):
        PRESSURE_1 = auto()
    #    PRESSURE_2 = auto()
    #    PRESSURE_3 = auto()
    #    PRESSURE_4 = auto()
    #    PRESSURE_5 = auto()
    #    PRESSURE_6 = auto()
    #    PRESSURE_7 = auto()
    #    PRESSURE_8 = auto()
    #    PRESSURE_9 = auto()
    #    PRESSURE_10 = auto()
        TEMPERATURE_1 = auto()
    #    TEMPERATURE_2 = auto()
    #    TEMPERATURE_3 = auto()
    #    TEMPERATURE_4 = auto()
    #    TEMPERATURE_5 = auto()
    #    TEMPERATURE_6 = auto()
    #    TEMPERATURE_7 = auto()
    #    TEMPERATURE_8 = auto()
    #    TEMPERATURE_9 = auto()
    #    TEMPERATURE_10 = auto()
        FORCE_1 = auto()

    def getSensorByID(sensorID, boardID):
        return _sensorsByBoard[(sensorID, boardID)]

    def getAllSensors():
        ret = []
        for s in SensorEnum:
            ret.append


class ValveManager:
    def __init__(self):

###valveEnum to valve
###int to list[valve]
###getvalve enum to valve
###getallvalves: list[valve]
    class ValveEnum(Enum):
