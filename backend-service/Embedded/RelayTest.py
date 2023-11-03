from RelayContainer import RelayContainer
from Relay import Relay
import unittest

class RelayContainerTestCase(unittest.TestCase): 
    def setUp(self) -> None:
       #create a blank relay container
       self.con = RelayContainer()
    
    def test_con_creation(self):
        self.assertIsInstance(self.con, RelayContainer, "Created container is not instance of RelayContainer")

    def test_add_relay(self):
        prev_size = self.con.get_size()
        self.con.add_relay(1, True)
        self.assertGreater(self.con.get_size(), prev_size, "add_relay FAILED: size did not increase")
        self.assertTrue(self.con.get_relay(1).get_relay_state(), "add_relay FAILED: relay state was incorrectly set")
        #lets see if we attempt to add an ID that exists already
        prev_size = self.con.get_size()
        self.con.add_relay(1, False)
        self.assertEqual(self.con.get_size(), prev_size, "add_relay FAILED: added a duplicate relay")
        self.assertFalse(self.con.get_relay(1).get_relay_state(), "add_relay FAILED: failed to replace existing state")

        #what will happen if I add a ID that is not on the board????
        prev_size = self.con.get_size()
        self.con.add_relay(28, True) #this doesn't exist
        self.assertEqual(self.con.get_size(), prev_size, "add_relay FAILED: attempted to add a relay way outside GPIO board")

    def test_get_relay(self):
        self.con.add_relay(1, True)
        self.con.add_relay(5, False)
        self.con.add_relay(10, True)
        self.con.add_relay(2, False)

        self.relay = self.con.get_relay(5)
        self.assertIsInstance(self.relay, Relay, "get_relay FAILED: did not get Relay instance")
        self.assertEqual(self.relay.get_id(), 5, "get_relay FAILED: did not grab correct relay")
    
    def test_get_relay_index(self):
        self.con.add_relay(1, True)
        self.con.add_relay(5, False)
        self.con.add_relay(10, True)
        self.con.add_relay(2, False)
        self.relay = self.con.get_relay_index(2)
        self.assertIsInstance(self.relay, Relay, "get_relay_index FAILED: did not get Relay instance")
        self.assertNotEqual(self.relay.get_id(), 2, "get_relay_index FAILED: did not get relay at correct index (got relay with ID)")

        #breaking test cases
        self.relay = self.con.get_relay_index(1000)
        self.assertIsNone(self.relay, "get_relay_index FAILED: attempted to get relay at out of bounds index (>)")
        self.relay = self.con.get_relay_index(-1)
        self.assertIsNone(self.relay, "get_relay_index FAILED: attempted to get relay at out of bounds index (<)")

    def test_remove_relay(self):
        self.con.add_relay(1, False)
        prev_size = self.con.get_size()
        self.con.remove_relay(1)
        self.assertLess(self.con.get_size(), prev_size, "remove_relay FAILED: failure to remove relay")
        self.assertIsNone(self.con.get_relay(1), "remove_relay FAILED: failure to remove relay")

        self.con.add_relay(2, False)
        prev_size = self.con.get_size()
        self.con.remove_relay(10000)
        self.assertEqual(self.con.get_size(), prev_size, "remove_relay FAILED: failure to handled out of bounds case (>)")
        self.con.remove_relay(-1)
        self.assertEqual(self.con.get_size(), prev_size, "remove_relay FAILED: failure to handle out of bounds case (<)")
        
    
    def test_intialize_low(self):
        for i in range(10):
            self.con.add_relay(i, True)
        
        self.con.intialize_low()

        for i in range(10):
            self.assertFalse(self.con.get_relay(i).get_relay_state(), "intialize_low FAILED: failure to set relay state to False")


    def tearDown(self):
        
        while(self.con.get_size() > 0):
            r = self.con.get_relay_index(0)
            self.con.remove_relay(r.get_id())
