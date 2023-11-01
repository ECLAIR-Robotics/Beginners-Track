from RelayContainer import RelayContainer
from Relay import Relay
import unittest
import RPi.GPIO as GPIO
import time

class PinTestCase(unittest.TestCase):
    def setUp(self):
        self.con = RelayContainer()
        self.con.add_relay(4, False)
        self.con.add_relay(17, False)
        self.con.add_relay(27, False)
        self.con.add_relay(22, False)

    def test_turn_on_sequence(self):
        self.con.set_relay(4, True)
        time.sleep(1)
        self.con.set_relay(17, True)
        time.sleep(1)
        self.con.set_relay(27, True)
        time.sleep(1)
        self.con.set_relay(22, True)

    def test_show_binary_sequence(self):
        for i in range(16):
            self.binary_sequence(i)
            time.sleep(1)

    #represent a 4 digit binary number using LEDS
    def binary_sequence(self, n):
        self.con.set_relay(4, n & 1)
        self.con.set_relay(17, n & 2)
        self.con.set_relay(27, n & 4)
        self.con.set_relay(22, n & 8)
    

    def tearDown(self):
        self.con.remove_relay(4)
        self.con.remove_relay(17)
        self.con.remove_relay(27)
        self.con.remove_relay(22)



