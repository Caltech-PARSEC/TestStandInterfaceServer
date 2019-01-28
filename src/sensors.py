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

    def get_sensor_value(self):
        return self._lastValue

    def set_sensor_value( self, sensorVal ):
        self._lastValue = sensorVal

    def get_name(self):
        return self.name

    def _raw_to_real_value(self, rawValue):
        pass

    def get_sensor_id(self):
        return self.sensorID

    def get_board_id(self):
        return self.boardID


class PressureSensor(Sensor):

    def _raw_to_real_value(self, rawValue):
        """
        Takes in an integer value from 0 and 0xFFF, returns
        an integer reading between 0 and 1500 psi
        """
        return rawValue * (1500 / 4095)

class TemperatureSensor(Sensor):

    def _raw_to_real_value(self, rawValue):
        """
        Temperature sensor reading comes in as a 16 bit value:
        11 bits for integer part, 5 bits for decimal part.
        Returns a float value for the temperature reading.
        """
        # Effectively divides by 2^5. Eliminates the last 5 bits and grabs the first 11.
        integer = int(rawValue >> 5)

        # Mod 2^5 grabs the last 5 bits. Take the value as an int, then divide by 32 
        # (because it's after the decimal point)
        decimal = float(int(rawValue % (2**5))) / 32.0

        return float(integer) + decimal


class ForceSensor(Sensor):

    def _raw_to_real_value(self, rawValue):
        pass


class SensorEnum(Enum):
    """
    Embedded enumerator class to keep a descriptive label for every sensor on the test stand.
    """
    PRESSURE_1 = 1
    TEMPERATURE_1 = 2
    FORCE_1 = 3

class SensorManager:
    """
    A class to keep a record of every declared sensor, as well as
    their associated boards and ID's. Sensors will be recorded in dictionary _sensors,
    mapping each sensor object to a descriptive label of the sensor from the SensorEnum class.
    """

    def __init__(self):

        # Dictionary mapping descriptive labels from the SensorEnum class to the corresponding sensor objects.
        self._sensors = {}

        # Maps each board ID (1 thru 5) to a list of all the sensors on the corresponding board.
        self._sensorsByBoard = {1 : [], 2 : [], 3 : [], 4 : [], 5 : [] }

        # Maps a tuple (sensor ID, board ID) to the corresponding sensor object.
        self._sensorsByID = {}

        # Maps a string representation of the sensor to the corresponding sensor object.
        self._sensorsByName = {}

        add_sensor(SensorEnum.PRESSURE_1, PressureSensor( 1, 1, "Pressure Sensor 1"))
        add_sensor(SensorEnum.TEMPERATURE_1, TemperatureSensor( 1, 2, "Temperature Sensor 1"))
        add_sensor(SensorEnum.FORCE_1, ForceSensor( 1, 3, "Force Sensor 1"))

        def add_sensor(self, sEnum, sObject):
            self._sensors[sEnum] = sObject
            self._sensorsByBoard[sObject.get_board_id()].append(sObject)
            self._sensorsByID[ (sObject.get_sensor_id(), sObject.get_board_id()) ] = sObject
            self._sensorsByName[sObject.get_name()] = sObject


    def get_sensor(self, sensorType):
        return self._sensors[sensorType]

    def get_sensor_by_id(self, sensorID, boardID):
        return self._sensorsByID[(sensorID, boardID)]

    def get_sensor_by_name(self, name):
        return self._sensorsByName[name]

    def get_all_sensors(self):
        return self._sensors.values()
