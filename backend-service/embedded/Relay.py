import RPi.GPIO as GPIO
import time


class Relay:

    def __init__(self, relay_id: int, gpio_pin: bool):
        self.relay_id = relay_id
        self.gpio_pin = gpio_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.relay_id, GPIO.OUT)
        GPIO.output(self.relay_id, GPIO.LOW)

    def setState(self, input_state: bool):
        self.gpio_pin = input_state
        if (input_state):
            GPIO.output(self.relay_id, GPIO.HIGH)
        else:
            GPIO.output(self.relay_id, GPIO.LOW)

    def getID(self):
        return self.relay_id

    def getRelayState(self):
        return self.gpio_pin
