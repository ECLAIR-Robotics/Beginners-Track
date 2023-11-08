from RelayContainer import RelayContainer
from Relay import Relay
import unittest
import RPi.GPIO as GPIO
import time

class PinTestCase(unittest.TestCase):
    def setUp(self):
        self.con = RelayContainer()
        self.con.addRelay(4, False, None, None)
        self.con.addRelay(17, False, None, None)
        self.con.addRelay(27, False, None, None)
        self.con.addRelay(22, False, None, None)

    def testTurnOnSequence(self):
        self.con.setRelay(4, True)
        time.sleep(1)
        self.con.setRelay(17, True)
        time.sleep(1)
        self.con.setRelay(27, True)
        time.sleep(1)
        self.con.setRelay(22, True)

    #represent a 4 digit binary number using LEDS
    def binarySequence(self, n):
        self.con.setRelay(4, n & 1)
        self.con.setRelay(17, n & 2)
        self.con.setRelay(27, n & 4)
        self.con.setRelay(22, n & 8)
    

    def tearDown(self):
        self.con.removeRelay(4)
        self.con.removeRelay(17)
        self.con.removeRelay(27)
        self.con.removeRelay(22)



