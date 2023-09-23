#make our imports here
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges."  
    + "You can achieve this by using 'sudo' to run your script")

# This will be where we will create our relay class 
class Relay:

    #define our Relay object
    def __init__(self, id):
        #get initialized with proper values
        self.pin_id = id
        self.state = False
    #switches the state of the pin to its opposite
    def setState(self, input_state):
        self.state = input_state
    
    #gets the pin id
    def getID(self):
        return self.pin_id
    
    def getRelayState(self):
        return self.state



    