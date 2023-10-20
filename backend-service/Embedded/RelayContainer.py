from Relay import Relay
from core.sqlite3.database import Database # With this statement we can grab the database class we made and then use it here

class RelayContainer:
    
    #create our container object
    def __init__(self):
        #our container is an array which will store the Relay objects
        #the goal of this is to have the user access particular Relay and alter it via the array
        self.relay_container = []
        self.db = Database()
    
    #lopp through our array and call Relay.toString() 
    #TODO Implement this method
    def str(self):
        for x in self.relay_container:
            x.toString()
            print("\n")
    
    #user is asking to create a new relay object with given id and boolean state
    def addRelay(self, input_id, input_state, name, disctiption):
        #check to see if the value already exists!
        for x in self.relay_container:
            if (x.getID() == input_id):
                x.setState(input_state)
        self.relay_container.append(Relay(input_id, input_state))
        # Now, to see if it is connected to the database, we need to check if it is already there!
        #TODO
        self.db.add(input_id, input_state, name, disctiption)

    #intialize all of our Relays to LOW
    def intializeLow(self):
        for x in self.relay_container:
            x.setState(False)

    #this will return whatever relay is in relay_container[idx]
    def getRelayIndex(self, idx) -> Relay:
        #check if it's out of range
        if(idx >= len(self.relay_container) or idx < 0):
            #we we don't want a array index out of bounds error, user gets nothing!
            return None
        return self.relay_container[idx]

    #gets relay given a specified relay id, not the same as array index!
    def getRelay(self, relay_id) -> Relay:
        for x in self.relay_container:
            if(x.getID() == relay_id):
                return x

        return None

    #remove a relay from the array
    def removeRelay(self, relay_id):
        #turn off GPIO pin when removing
        offRelay = (self.getRelay(relay_id))
        offRelay.setState(False)
        self.relay_container.remove(offRelay)
