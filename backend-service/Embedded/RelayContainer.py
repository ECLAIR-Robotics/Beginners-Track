from Relay import Relay

class RelayContainer:
    
    #create our container object
    def __init__(self):
        #our container is an array which will store the Relay objects
        #the goal of this is to have the user access particular Relay and alter it via the array
        self.relay_container = []
    
    
    #implement helper method that returns size
    def get_size(self) -> int:
        return self.relay_container.len()

    #loop through our array and call Relay.toString() 
    def str(self):
        for x in self.relay_container:
            x.to_string()
            print("\n")
    
    #user is asking to create a new relay object with given id and boolean state
    def add_relay(self, input_id, input_state):
        #check to see if the value already exists!
        if (input_id > 27 or input_id < 0):
            return
        for x in self.relay_container:
            if (x.get_id() == input_id):
                x.set_state(input_state)
        self.relay_container.append(Relay(input_id, input_state))

    #intialize all of our Relays to LOW
    def intialize_low(self):
        for x in self.relay_container:
            x.set_state(False)

    #this will return whatever relay is in relay_container[idx]
    def get_relay_index(self, idx) -> Relay:
        #check if it's out of range
        if(idx >= len(self.relay_container) or idx < 0):
            #we we don't want a array index out of bounds error, user gets nothing!
            return None
        return self.relay_container[idx]

    #gets relay given a specified relay id, not the same as array index!
    def get_relay(self, relay_id) -> Relay:
        for x in self.relay_container:
            if(x.get_id() == relay_id):
                return x

        return None

    #remove a relay from the array
    def remove_relay(self, relay_id):
        #turn off GPIO pin when removing
        offRelay = (self.get_relay(relay_id))
        offRelay.set_state(False)
        self.relay_container.remove(offRelay)
