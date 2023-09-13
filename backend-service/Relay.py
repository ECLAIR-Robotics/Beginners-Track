import RPi.GPIO as GPIO

class Relay:
    def __init__(self, id: int, state: bool = False):
        self.id = id
        self.state = state

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.id, GPIO.OUT)

        GPIO.output(self.id, self.state)

    def setState(self, state: bool):
        self.state = state
        GPIO.output(self.id, self.state)
        
    def getID(self):
        return self.id

    def getRelayState(self):
        return self.state
        