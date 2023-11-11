
from core.sqlite3.database import Database # With this statement we can grab the database class we made and then use it here
from Embedded.Relay import Relay

GPIO_PIN_HIGHEST = 27
GPIO_PIN_LOWEST = 0

class RelayContainer:
    
    #create our container object
    def __init__(self):
        #our container is an array which will store the Relay objects
        #the goal of this is to have the user access particular Relay and alter it via the array
        self.relay_container = []
        self.db = Database()
        self.relay_container = self.getAllRelays()

    #implement helper method that returns size
    def getSize(self) -> int:
        return len(self.relay_container)

    #loop through our array and call Relay.toString() 
    #Implement this method
    #Returns empty string, only prints x
    def __str__(self):
        for x in self.relay_container:
            #x.to_string()
            # list1 = []
            # list1.append(x.__str__())
            print(x)
        return ' '
    
    #user is asking to create a new relay object with given id and boolean state

    def addRelay(self, input_id: int, input_state, name: str, disctiption: str):
        #check to see if the value already exists!
        if (input_id > GPIO_PIN_HIGHEST or input_id < GPIO_PIN_LOWEST):
            return
        for x in self.relay_container:
            assert isinstance(x, Relay)
            if (x.get_id() == input_id):
                x.set_state(input_state)
                return
        #self.relay_container.append(Relay(input_id, input_state))
        # Now, to see if it is connected to the database, wep need to check if it is already there!
        #TODO
        if self.db.contains(input_id) :
            return False
        self.db.add(input_id, input_state, name, disctiption)
        self.relay_container.append(Relay(input_id, input_state))
        return True

    def setRelay(self, input_id: int, input_state) -> bool:
        r = self.getRelay(input_id)
        if (r != None):
            r.set_state(input_state)
            return self.db.setState(input_id, input_state)
        return False


    #intialize all of our Relays to LOW
    def intializeLow(self):
        for x in self.relay_container:
            x.set_state(False)
            self.db.setState(x.get_id(), False)

    #this will return whatever relay is in relay_container[idx]
    def getRelayIndex(self, idx: int) -> Relay:
        #check if it's out of range
        if(idx >= len(self.relay_container) or idx < 0):
            #we we don't want a array index out of bounds error, user gets nothing!
            return None
        return self.relay_container[idx]

    #gets relay given a specified relay id, not the same as array index!
    def getRelay(self, relay_id: int) -> Relay:
        #check if relay_id is out of bounds!
        if (relay_id > GPIO_PIN_HIGHEST or relay_id < GPIO_PIN_LOWEST):
            return None

        for x in self.relay_container:
            if(x.get_id() == relay_id):
                return x
        #relay doesn't exit yet....
        return None

    #remove a relay from the array
    def removeRelay(self, relay_id:int):
        #turn off GPIO pin when removing
        offRelay = (self.getRelay(relay_id))
        if (offRelay != None):
          offRelay.set_state(False)
          self.relay_container.remove(offRelay)
          if self.db.contains(relay_id):
                return self.db.remove(relay_id)
          
        return None

    def getAllRelays(self):
        self.relays = self.db.getAllDevices()
        self.container = []
        for relay in self.relays:
            self.container.append(Relay(relay[0], relay[1]))
        return self.container
            


