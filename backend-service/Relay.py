import RPi.GPIO as GPIO

class Relay:
    def __init__(self, id: int):
        self.id = id
        self.state = False

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.id, GPIO.OUT)

        GPIO.output(self.id, self.state)
    
    def __init__(self, id: int, state: bool):
        self(id)
        self.setState(state)

    def setState(self, state: bool):
        self.state = state
        GPIO.output(self.id, self.state)
        
    def getID(self):
        return self.id

    def getRelayState(self):
        return self.state
        