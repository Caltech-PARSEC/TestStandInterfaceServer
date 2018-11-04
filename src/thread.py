import sensors
import valves
import threading
import time


class StatusType(Enum):
    RUNNING = 0
    PAUSED = 1
    CHANGING_SEQUENCE = 2
    E_STOP = 3


class SequenceRunner():
    """
    Class to control which sequence runs when.
    """

    def run_sequence(self, sequenceName):
        #thread = Thread(self.sequences[sequenceName].run_sequence)
        #cv.aquire()
        #while not (self.status == E_STOP or self.status == CHANGING_SEQUENCE):
            #cv.wait()
        #if self.status == E_STOP:
        #   self.sequences[sequenceName].run_emergency_stop()
        #cv.release()

class ValveSequence(threading.Thread):
    """
    Abstract class representing valve sequences to be defined later.
    Subclasses will need to override the __init__() and run() methods with
    specific instructions for each sequence.
    To initiate the sequence, the runner must call the sequence's start()
    method, which will call the run() method.

    """

    def __init__(self, sequenceType, sequenceName):
        threading.Thread.__init__(self, name = sequenceName) #do I need the self here?

    def run(self):
        #pretend to be doing something
        pass



class SequenceManager:
    """
    A class to keep a record of every declared sequence. Sequences will be
    recorded in dictionary _sequences, mapping each ValveSequence object to a
    descriptive label of the sequence from the SequenceEnum class.
    """

    def __init__(self):
        # Dictionary mapping descriptive labels from the SequenceEnum class to the corresponding ValveSequence objects.
        _sequences = {}

    def addValve(self, sEnum, sObject):
        #sEnum is the SequenceEnum enumerator type, sObject is the ValveSequence object
        _sequences[sEnum] = sObject

    def getValve(self, sEnum):
        return _sequences[vEnum]

    def getAllValves(self):
        return _valves.values()

    class SequenceEnum(Enum):
        """
        Embedded enumerator class to keep a descriptive label for every sequence.
        """

        EXAMPLE_SEQUENCE = 1
