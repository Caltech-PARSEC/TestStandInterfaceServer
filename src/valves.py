#import BoardInterface

from enum import Enum

class ValveEnum(Enum):
    """
    Embedded enumerator class to keep a descriptive label for every valve on the test standself.
    """
    DEFAULT_VALVE = 1

class Valve:
    """
    Class representing an individual valve on the test stand. Needs access
    to the BoardInterface code to implement the open() and close() methods.
    """

    def __init__(self, valveID, boardID, closeAngle, openAngle, name):
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

        if (self._lastValue == self._openAngle):
            return True

        else:
            return False

    def open(self):
        BoardInterface.writeValve(self.boardID, self._valveID, self._openAngle)
        self._lastValue = self._openAngle

    def close(self):
        BoardInterface.writeValve(self.boardID, self._valveID, self._closeAngle)
        self._lastValue = self._closeAngle

    def get_name(self):
        return self.name

    def get_board_id(self):
        return self.boardID

    def get_valve_id(self):
        return self._valveID

class ValveManager:
    """
    A class to keep a record of every declared valve, as well as their
    associated boards and ID's. Valves will be recorded in dictionary _valves,
    mapping each valve object to a descriptive label of the valve from the ValveEnum class.
    """

    def __init__(self):

        # Dictionary mapping descriptive labels from the ValveEnum class to the corresponding sensor objects.
        self._valves = {}

        # Maps each board ID (1 thru 5) to a list of all the valves on the corresponding board.
        self._valvesByBoard = {1 : [], 2 : [], 3 :[], 4 : [], 5 : []}

        # Maps a tuple (valve ID, board ID) to the corresponding sensor object.
        self._valvesByID = {}


    def add_valve(self, vEnum, vObject):
        self._valves[vEnum] = vObject
        self._valvesByBoard[vObject.getBoardID()].append(vObject)
        self._valvesByID[ (vObject.getValveID(), vObject.getBoardID())] = vObject

    def get_valve(self, vEnum):
        return self._valves[vEnum]

    def get_valve_by_id(self, valveID, boardID):
        return self._valvesByID[ (valveID, boardID) ]

    def get_all_valves(self):
        return self._valves.values()
