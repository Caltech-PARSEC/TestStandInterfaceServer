#import BoardInterface

from enum import Enum

# Valve: class representing an individual valve on the test stand. Needs access
# to the BoardInterface code to implement the open() and close() methods.

class Valve:

    def __init__(self, valveID, boardID, closedAngle, openAngle, name):
        self._valveID = valveID
        self.boardID = boardID
        self._closeAngle = closeAngle
        self._openAngle = openAngle
        self._lastValue = 0.0
        self.name = name

    def getValue(self):
        return lastValue

    def open(self):
        BoardInterface.writeValve(boardID, valveID, openAngle)

    def close(self):
        BoardInterface.writeValve(boardID, valveID, closeAngle)

    def getName(self):
        return name

    def getBoardID(self):
        return boardID

    def getValveID(self):
        return _valveID


# ValveManager: a class to keep a record of every declared valve, as well as
# their associated boards and ID's. Valves will be recorded in dictionary _valves,
# mapping each valve object to a descriptive label of the valve from the ValveEnum class.

class ValveManager:

    def __init__(self):

        _valves = {}
        _valvesByBoard = {1 : [], 2 : [], 3 :[], 4 : [], 5 : []}
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


# TO be written once more info is acquired:
# ValveEnum: embedded enumerator class to keep a descriptive label for every valve on the test stand.
