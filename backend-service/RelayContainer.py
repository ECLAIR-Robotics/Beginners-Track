from embedded.Relay import Relay

class RelayContainer:

    def __init__(self):
        self.relays = []
        print("RelayContainer Initialized")

    def str(self):
        print(f"Container Size: {len(self.relays)}")
        print("ID\tState")
        print("-------------------------")

        for relay in self.relays:
            print(f"{relay.getID()}\t{relay.getRelayState()}")

    def addCreatedRelay(self, relay: Relay) -> bool:
        self.relays.append(relay)
        return True

    def addRelay(self, int: id, state: bool) -> bool:
        return self.addRelay(Relay(id, state))

    def initializeLow(self):
        for relay in self.relays:
            relay.setState(0)

    def getRelayIndex(self, index: int) -> Relay:
        return self.relays[index]

    def getRelay(self, id: int) -> Relay:
        for relay in self.relays:
            if relay.getID() == id:
                return relay

    def popRelay(self, index: int) -> Relay:
        return self.relays.pop(index)

    def removeRelay(self, id: int) -> Relay:
        for index, relay in enumerate(self.relays):
            if relay.getID() == id:
                return self.popRelay(index)

    def getAllRelays(self) -> [Relay]:
        return self.relays

    def updateRelays(self, id: int, state: bool) -> bool:
        for relay in self.relays:
            if relay.getID() == id:
                relay.setState(state)
                return True
