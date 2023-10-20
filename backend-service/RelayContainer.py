from embedded.Relay import Relay
from db.model import Model


class RelayContainer:

    def __init__(self):
        self.m = Model()
        self.relays = []
        for relay in self.m.getAllRelays():
            self.relays.append(Relay(relay[0], relay[1]))
        print("RelayContainer Initialized")

    def str(self):
        print(f"Container Size: {len(self.relays)}")
        print("ID\tState")
        print("-------------------------")
        for relay in self.relays:
            print(f"{relay.getID()}\t{relay.getRelayState()}")

    #def addCreatedRelay(self, relay: Relay) -> bool:
    #    self.relays.append(relay)
    #    self.m.addRelay(relay.getID(), relay.getRelayState())
    #    return True

    def addRelay(self, id: int, state: bool) -> bool:
        self.relays.append(Relay(id, state))
        self.m.addRelay(id, state)
        return True
    
    def add(self, relay: Relay) -> bool:
        self.relays.append(relay)
        self.m.addRelay(relay.getID(), relay.getRelayState())
        return True

    def initializeLow(self):
        for relay in self.relays:
            self.m.updateRelayState(False, relay.getID())
            relay.setState(False)

    def getRelayIndex(self, index: int) -> Relay:
        return self.relays[index]

    def getRelay(self, id: int) -> Relay:
        for relay in self.relays:
            if relay.getID() == id:
                return relay

    def popRelay(self, index: int) -> Relay:
        for relay in self.relays:
            if relay.getID() == index:
                ret = relay
                self.m.dropRelay(ret.getID())
                self.relays.pop(index)
                return ret

    #def removeRelay(self, id: int) -> Relay:
    #    for index, relay in enumerate(self.relays):
    #        if relay.getID() == id:
    #            return self.popRelay(index)

    def getAllRelays(self) -> [Relay]:
        return self.m.getAllRelays()

    def updateRelays(self, id: int, state: bool) -> bool:
        for relay in self.relays:
            if relay.getID() == id:
                relay.setState(state)
                self.m.updateRelayState(state, id)
                return True
