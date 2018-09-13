#import BoardInterface

from enum import Enum

# Sensor: Abstract class representing an individual sensor on the test stand.
# Subclasses will need to override _rawToRealValue method with specific
# logic to convert the input from the microcontroller board into a sensor measurement.

class Sensor():

    def __init__(self, sensorID, boardID, name):
        self.sensorID = sensorID
        self.boardID = boardID
        self._lastValue = 0.0
        self.name = name

    def getSensorValue(self):
        return _lastValue

    def setSensorValue( self, sensorVal ):
        _lastValue = sensorVal

    def getName(self):
        return name

    def _rawToRealValue(self, rawValue):
        pass

    def getSensorID(self):
        return sensorID

    def getBoardID(self):
        return boardID

class PressureSensor(Sensor):

    def _rawToRealValue(self, rawValue):         #take in as an int value between 0 and 0xFFF
        return rawValue * (1500 / 4095)         #Maps from (0x000,0xFFF) to (0,1500) psi

class TempSensor(Sensor):

    def _rawToRealValue(self, rawValue):                 #temperature sensor reading comes in as a 16 bit value. 11 bits for integer part, 5 bits for decimal part
        integer = int(rawValue >> 5)                     #effectively dividing by 2^5. Eliminates the last 5 bits and grabs the first 11.
        decimal = float(int(rawValue % (2**5))) / 32.0   #mod 2^5 grabs the last 5 bits. Take the value as an int, then divide by 32 (because it's after the decimal point)
        return float(integer) + decimal


class ForceSensor(Sensor):

    def _rawToRealValue(self, rawValue):
        pass


# SensorManager: a class to keep a record of every declared sensor, as well as
# their associated boards and ID's. Sensors will be recorded in dictionary _sensors,
# mapping each sensor object to a descriptive label of the sensor from the SensorEnum class.

class SensorManager:

    def __init__(self):

        _sensors = {}
        _sensorsByBoard = {1 : [], 2 : [], 3 : [], 4 : [], 5 : [] }
        _sensorsByID = {}

        addSensor(SensorEnum.PRESSURE_1, PressureSensor( 1, 1, "Pressure Sensor 1"))
        addSensor(SensorEnum.TEMPERATURE_1, TemperatureSensor( 1, 2, "Temperature Sensor 1"))
        addSensor(SensorEnum.FORCE_1, ForceSensor( 1, 3, "Force Sensor 1"))

        def addSensor(self, sEnum, sObject):
            _sensors[sEnum] = sObject
            _sensorsByBoard[sObject.getBoardID()].append(sObject)
            _sensorsByID[ (sObject.getSensorID(), sObject.getBoardID()) ] = sObject


# SensorEnum: an embedded enumerator class to keep a descriptive label for every sensor on the test stand.

    class SensorEnum(Enum):
        PRESSURE_1 = 1

        TEMPERATURE_1 = 2

        FORCE_1 = 3


    def getSensor(self, sensorType):
        return _sensors[sensorType]

    def getSensorByID(self, sensorID, boardID):
        return _sensorsByID[(sensorID, boardID)]

    def getAllSensors(self):
        return _sensors.values()
