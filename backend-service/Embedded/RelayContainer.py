from Relay import Relay

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges."  
    + "You can achieve this by using 'sudo' to run your script")
class RelayContainer:
    
    #create our container object
    def __init__(self):
        #our container is an array which will store the Relay objects
        #the goal of this is to have the user access particular Relay and alter it via the array
        self.relay_container = []
    
    #lopp through our array and call Relay.toString() 
    #TODO Implement this method
    def str(self):
        for x in self.relay_container:
            x.toString()
            print("\n")
    
    #user is asking to create a new relay object with given id and boolean state
    def addRelay(self, input_id, input_state):
        #check to see if the value already exists!
        for x in self.relay_container:
            if (x.getID() == input_id):
                x.setState(input_state)
        self.relay_container.append(Relay(input_id, input_state))

    #intialize all of our Relays to LOW
    def intializeLow(self):
        for x in self.relay_container:
            x.setState(False)

    #this will return whatever relay is in relay_container[idx]
    def getRelayIndex(self, idx):
        #check if it's out of range
        if(idx >= len(self.relay_container) or idx < 0):
            #we we don't want a array index out of bounds error, user gets nothing!
            return None
        return self.relay_container[idx]

    #gets relay given a specified relay id, not the same as array index!
    def getRelay(self, relay_id):
        for x in self.relay_container:
            if(x.getID() == relay_id):
                return x

        return None

    #remove a relay from the array
    def removeRelay(self, relay_id):
        self.relay_container.remove(self.getRelay(relay_id))
