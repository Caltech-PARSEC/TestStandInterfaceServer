from enum import Enum
from abc import ABC, abstractmethod
import BoardInterface

class Sensor(ABC):

    def __init__(self, sensorID, boardID, name):
        self.sensorID = sensorID
        self.boardID = boardID
        self._lastValue = 0.0
        self.name = name
        super(Sensor,self).__init__()

    def getSensorValue():
        return lastValue

    def setSensorValue(sensorVal):
        lastValue = sensorVal

    def getName():
        return name

    @abstractmethod
    def _rawToRealValue(rawValue):
        pass

class Valve:

    def __init__(self, valveID, boardID, closedAngle, openAngle, name):
        self.valveID = valveID
        self.boardID = boardID
        self.closeAngle = closeAngle
        self.openAngle = openAngle
        self.lastValue = 0.0
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

class SensorType(Enum):
    

class SensorManager:
    def __init__(self):
        pass
