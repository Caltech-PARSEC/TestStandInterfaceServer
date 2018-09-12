#import BoardInterface

from enum import Enum

class Sensor():

    def __init__(self, sensorID, boardID, name):
        self.sensorID = sensorID
        self.boardID = boardID
        self._lastValue = 0.0
        self.name = name

    def getSensorValue():
        return _lastValue

    def setSensorValue(sensorVal):
        _lastValue = sensorVal

    def getName():
        return name

    def _rawToRealValue(rawValue):
        pass

    def getSensorID():
        return sensorID

    def getBoardID():
        return boardID

class PressureSensor(Sensor):

    def _rawToRealValue(rawValue):          #take in as an int value between 0 and 0xFFF
        return rawValue * (1500 / 4095)         #Maps from (0x000,0xFFF) to (0,1500) psi

class TempSensor(Sensor):

    def _rawToRealValue(rawValue):
        integer = int(rawValue >> 5)
        decimal = float(int(rawValue % (2**6))) / 32.0
        return float(integer) + decimal


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

    def getBoardID():
        return boardID

    def getValveID():
        return _valveID


class SensorManager:

    def __init__(self):

        _sensors = {}
        _sensorsByBoard = {1 : [], 2 : [], 3 : [], 4 : [], 5 : [] }
        _sensorsByID = {}


        addSensor(SensorEnum.PRESSURE_1, PressureSensor( 1, 1, "Pressure Sensor 1"))
        addSensor(SensorEnum.TEMPERATURE_1, TemperatureSensor( 1, 2, "Temperature Sensor 1"))
        addSensor(SensorEnum.FORCE_1, ForceSensor( 1, 3, "Force Sensor 1"))

        """
        _sensors[SensorEnum.PRESSURE_1] = PressureSensor(1, 1, "Pressure Sensor 1")
        _sensorsByBoard[1].append( _sensors[SensorEnum.PRESSURE_1] )
        _sensorsByID[ (1, 1) ] = _sensors[SensorEnum.PRESSURE_1]

        _sensors[SensorEnum.TEMPERATURE_1] = TemperatureSensor(1, 2, "Temperature Sensor 1")
        _sensorsByBoard[2].append( _sensors[SensorEnum.TEMPERATURE_1] )
        _sensorsByID[ (1, 2) ] = _sensors[SensorEnum.TEMPERATURE_1]

        _sensors[SensorEnum.FORCE_1] = ForceSensor(1, 3, "Force Sensor 1")
        _sensorsByBoard[3].append( _sensors[SensorEnum.FORCE_1] )
        _sensorsByID[ (1, 3) ] = _sensors[SensorEnum.FORCE_1]

        """

        def addSensor(sEnum, sObject):
            _sensors[sEnum] = sObject
            _sensorsByBoard[sObject.getBoardID()].append(sObject)
            _sensorsByID[ (sObject.getSensorID(), sObject.getBoardID()) ] = sObject


    class SensorEnum(Enum):
        PRESSURE_1 = 1

        TEMPERATURE_1 = 2

        FORCE_1 = 3


    def getSensor( sensorType ):
        return _sensors[sensorType]

    def getSensorByID(sensorID, boardID):
        return _sensorsByID[(sensorID, boardID)]

    def getAllSensors():
        ret = []
        for key in _sensors:
            ret.append( _sensors[key] )
        return ret


class ValveManager:

    def __init__(self):

        _valves = {}
        _valvesByBoard = {1 : [], 2 : [], 3 :[], 4 : [], 5 : []}
        _valvesByID = {}


    def addValve(vEnum, vObject):
        _valves[vEnum] = vObject
        _valvesByBoard[vObject.getBoardID()].append(vObject)
        _valvesByID[ (vObject.getValveID(), vObject.getBoardID())] = vObject

    def getValve(vEnum):
        return _valves[vEnum]

    def getValveByID(valveID, boardID):
        return _valvesByID[ (valveID, boardID) ]

    def getAllValves():
        ret = []
        for v in _valves:
            ret.append( _valves[v] )
        return ret


def __main__():
    test = TemperatureSensor(1, 1, test)
    test._rawToRealValue(input("Enter bin \n"))
