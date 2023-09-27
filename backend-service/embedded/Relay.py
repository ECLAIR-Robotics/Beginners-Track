import RPi.GPIO as GPIO
import time 

class Relay:
    
    def __init__(self, relay_pin, gpio_pin):
        self.relay_pin = relay_pin
        self.gpio_pin = gpio_pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.gpio_pin, GPIO.OUT)
        GPIO.output(self.gpio_pin, GPIO.LOW)

    def setState (self, state: bool):
        self.state = state
        if (state):
            GPIO.output(self.gpio_pin, GPIO.HIGH)
        else:
            GPIO.output(self.gpio_pin, GPIO.LOW)
        

    def getID(self):
        return self.relay_pin

    def getRelayState(self):
        return self.gpio_pin
        