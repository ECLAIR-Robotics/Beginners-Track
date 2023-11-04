from Embedded.RelayContainer import RelayContainer
import unittest
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

    #loops through all the lights over and over while increasing speed each itteration
    def testQuickSequence(self):
        self.quickSequence(10)

    def quickSequence(self, wait):

        for i in range(1, wait):
            self.con.setRelay(4, True)
            time.sleep(1/i)
            self.con.setRelay(4, False)
            self.con.setRelay(17, True)
            time.sleep(1/i)
            self.con.setRelay(17, False)
            self.con.setRelay(27, True)
            time.sleep(1/i)
            self.con.setRelay(27, False)
            self.con.setRelay(22, True)
            time.sleep(1/i)
            self.con.setRelay(22, False)


    def tearDown(self):
        self.con.removeRelay(4)
        self.con.removeRelay(17)
        self.con.removeRelay(27)
        self.con.removeRelay(22)



