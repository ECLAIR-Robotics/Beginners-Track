# sudo apt-get install rpi.gpio
import RPi.GPIO as GPIO
# import time


class Relay:

    def __init__(self, relay_pin, gpio_pin):
        self.relay_pin = relay_pin
        self.gpio_pin = gpio_pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.gpio_pin, GPIO.OUT)
        GPIO.output(self.gpio_pin, GPIO.LOW)

    def setState(self, state: bool):
        self.state = state
        if (state):
            GPIO.output(self.gpio_pin, GPIO.HIGH)
        else:
            GPIO.output(self.gpio_pin, GPIO.LOW)

    def getID(self):
        return self.relay_pin

    def getRelayState(self):
        return self.gpio_pin


class RelayContainer:
    def __init__(self):
        self.relays: [Relay] = []

    def str(self):
        print(f"Container Size: {len(self.relays)}")
        print("ID\tState")
        print("-------------------------")

        for relay in self.relays:
            print(f"{relay.getID()}\t{relay.getRelayState()}")

    def addRelay(self, relay: Relay) -> bool:
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
