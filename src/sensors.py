#import BoardInterface

from enum import Enum


class Sensor():
    """
    Abstract class representing an individual sensor on the test stand.
    Subclasses will need to override _rawToRealValue method with specific logic to
    convert the input from the microcontroller board into a sensor measurement.
    """

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

    def _rawToRealValue(self, rawValue):
        """
        Takes in an integer value from 0 and 0xFFF, returns
        an integer reading between 0 and 1500 psi
        """
        return rawValue * (1500 / 4095)

class TempSensor(Sensor):

    def _rawToRealValue(self, rawValue):
        """
        Temperature sensor reading comes in as a 16 bit value:
        11 bits for integer part, 5 bits for decimal part.
        Returns a float value for the temperature reading.
        """
        # Effectively divides by 2^5. Eliminates the last 5 bits and grabs the first 11.
        integer = int(rawValue >> 5)

        # Mod 2^5 grabs the last 5 bits. Take the value as an int, then divide by 32 (because it's after the decimal point)
        decimal = float(int(rawValue % (2**5))) / 32.0

        return float(integer) + decimal


class ForceSensor(Sensor):

    def _rawToRealValue(self, rawValue):
        pass


class SensorManager:
    """
    A class to keep a record of every declared sensor, as well as
    their associated boards and ID's. Sensors will be recorded in dictionary _sensors,
    mapping each sensor object to a descriptive label of the sensor from the SensorEnum class.
    """

    def __init__(self):

        # Dictionary mapping descriptive labels from the SensorEnum class to the corresponding sensor objects.
        _sensors = {}

        # Maps each board ID (1 thru 5) to a list of all the sensors on the corresponding board.
        _sensorsByBoard = {1 : [], 2 : [], 3 : [], 4 : [], 5 : [] }

        # Maps a tuple (sensor ID, board ID) to the corresponding sensor object.
        _sensorsByID = {}

        # Maps a string representation of the sensor to the corresponding sensor object.
        _sensorsByName = {}

        addSensor(SensorEnum.PRESSURE_1, PressureSensor( 1, 1, "Pressure Sensor 1"))
        addSensor(SensorEnum.TEMPERATURE_1, TemperatureSensor( 1, 2, "Temperature Sensor 1"))
        addSensor(SensorEnum.FORCE_1, ForceSensor( 1, 3, "Force Sensor 1"))

        def addSensor(self, sEnum, sObject):
            _sensors[sEnum] = sObject
            _sensorsByBoard[sObject.getBoardID()].append(sObject)
            _sensorsByID[ (sObject.getSensorID(), sObject.getBoardID()) ] = sObject
            _sensorsByName[sObject.getName()] = sObject


    class SensorEnum(Enum):
        """
        Embedded enumerator class to keep a descriptive label for every sensor on the test stand.
        """

        PRESSURE_1 = 1

        TEMPERATURE_1 = 2

        FORCE_1 = 3


    def getSensor(self, sensorType):
        return _sensors[sensorType]

    def getSensorByID(self, sensorID, boardID):
        return _sensorsByID[(sensorID, boardID)]

    def getSensorByName(self, name):
        return _sensorsByName[name]

    def getAllSensors(self):
        return _sensors.values()
