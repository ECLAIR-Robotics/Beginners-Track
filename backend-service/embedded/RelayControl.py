import RPi.GPIO as GPIO
import time
from db.model import Model


class Relay:

    def __init__(self, relay_id: int, relay_state: bool):
        self.relay_id = relay_id  # 4, 17, 22
        self.relay_state = relay_state  # on true / off false
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.relay_id, GPIO.OUT)
        self.setState(self.relay_state)
        # GPIO.output(self.relay_id, GPIO.HIGH)  # initialize to off

    def setState(self, input_state: bool):
        self.relay_state = input_state
        if (self.relay_state):
            GPIO.output(self.relay_id, GPIO.LOW)  # turn on
        else:
            GPIO.output(self.relay_id, GPIO.HIGH)  # turn off

    def getID(self):
        return self.relay_id  # 4, 17, 22

    def getRelayState(self):
        return self.relay_state  # on true / off false


class RelayContainer:

    allIds = [4, 17, 22]

    def __init__(self):
        self.m = Model()
        self.relays = []
        for relay in self.m.getAllRelays():
            # all relays in db to container
            self.relays.append(Relay(relay[0], relay[1]))
        print("RelayContainer Initialized")

    def str(self):
        print(f"Container Size: {len(self.relays)}")
        print("ID\tState")
        print("-------------------------")
        for relay in self.relays:
            print(f"{relay.getID()}\t{relay.getRelayState()}")

    def addRelay(self, id: int, state: bool) -> bool:
        self.relays.append(Relay(id, state))
        if not self.m.checkIfRelayExists(id):
            self.m.addRelay(id, state)  # add to db if it doesn't already exist
            return True  # true, added
        return False

    def add(self, relay: Relay) -> bool:  # add relay object
        self.relays.append(relay)
        if not self.m.checkIfRelayExists(relay.getID()):
            self.m.addRelay(relay.getID(), relay.getRelayState())
            return True  # true, added
        return False

    def initializeLow(self):
        for relay in self.relays:  # initialize all relays to off
            self.m.updateRelayState(False, relay.getID())
            relay.setState(False)

    def initializeHigh(self):
        for relay in self.relays:  # initialize all relays to on
            self.m.updateRelayState(True, relay.getID())
            relay.setState(True)

    def getRelayAtIndex(self, index: int) -> Relay:
        return self.relays[index]  # get given index

    def getRelay(self, id: int):
        for relay in self.relays:
            if relay.getID() == id:
                return relay  # get given id
        else:
            raise ValueError("Relay does not exist")

    def popRelay(self, id: int):
        print(f"Attempting to remove relay {id}")
        if not self.m.checkIfRelayExists(id):
            return False
        else:
            for index, relay in enumerate(self.relays):
                if relay.getID() == id:
                    self.relays.pop(index)
                    self.m.dropRelay(id)
                    relay.setState(False)  # set removed relay to off
                    return True  # true, popped

    def getAllRelays(self) -> [Relay]:
        return self.m.getAllRelays()

    def updateRelay(self, id: int, state: bool) -> bool:
        for relay in self.relays:
            if relay.getID() == id:
                # set relay of certain id to certain state
                relay.setState(state)
                self.m.updateRelayState(state, id)
                return True

    def checkExistence(self, id: int):
        return self.m.checkIfRelayExists(id)

    def clearAll(self):
        for relay in self.relays:
            relay.setState(False)
        self.relays.clear()
        self.m.clearAll()

    def clearBackend(self):
        for id in self.allIds:
            self.addRelay(id, False)
            self.clearAll()
