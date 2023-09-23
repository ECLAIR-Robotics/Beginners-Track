#make our imports here

# This will be where we will create our relay class 
class Relay:

    #define our Relay object
    def __init__(self, id):
        #GPIO pin
        self.pin_id = id
        #Active/Inactive
        self.state = False
    #switches the state of the pin to its opposite
    def setState(self, input_state):
        self.state = input_state
    
    #gets the pin id
    def getID(self):
        return self.pin_id
    
    #gets the state of the relay
    def getRelayState(self):
        return self.state

    #prints out the contents of relay
    def toString(self):
        print("ID: %d , State: %r" % (self.getID(), self.getRelayState()))


    