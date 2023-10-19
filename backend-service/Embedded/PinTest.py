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



