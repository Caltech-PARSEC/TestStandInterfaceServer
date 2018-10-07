#import BoardInterface

from enum import Enum


class Valve:
    """
    Class representing an individual valve on the test stand. Needs access
    to the BoardInterface code to implement the open() and close() methods.
    """

    def __init__(self, valveID, boardID, closedAngle, openAngle, name):
        self._valveID = valveID
        self.boardID = boardID
        self._closeAngle = closeAngle
        self._openAngle = openAngle
        self._lastValue = 0.0
        self.name = name

    def is_open(self):
        """
        Returns true if the last known angle was the open angle.
        NOTE: returns false even when there is no last value.
        """

        if (_lastValue == _openAngle):
            return True

        else:
            return False

    def open(self):
        BoardInterface.writeValve(boardID, valveID, openAngle)
        _lastValue = openAngle

    def close(self):
        BoardInterface.writeValve(boardID, valveID, closeAngle)
        _lastValue = closedAngle

    def getName(self):
        return name

    def getBoardID(self):
        return boardID

    def getValveID(self):
        return _valveID



class ValveManager:
    """
    A class to keep a record of every declared valve, as well as their
    associated boards and ID's. Valves will be recorded in dictionary _valves,
    mapping each valve object to a descriptive label of the valve from the ValveEnum class.
    """

    def __init__(self):

        # Dictionary mapping descriptive labels from the ValveEnum class to the corresponding sensor objects.
        _valves = {}

        # Maps each board ID (1 thru 5) to a list of all the valves on the corresponding board.
        _valvesByBoard = {1 : [], 2 : [], 3 :[], 4 : [], 5 : []}

        # Maps a tuple (valve ID, board ID) to the corresponding sensor object.
        _valvesByID = {}


    def addValve(self, vEnum, vObject):
        _valves[vEnum] = vObject
        _valvesByBoard[vObject.getBoardID()].append(vObject)
        _valvesByID[ (vObject.getValveID(), vObject.getBoardID())] = vObject

    def getValve(self, vEnum):
        return _valves[vEnum]

    def getValveByID(self, valveID, boardID):
        return _valvesByID[ (valveID, boardID) ]

    def getAllValves(self):
        return _valves.values()

    class ValveEnum(Enum):
        """
        Embedded enumerator class to keep a descriptive label for every valve on the test standself.
        """

        DEFAULT_VALVE = 1
