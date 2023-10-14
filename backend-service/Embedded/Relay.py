#make our imports here
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges."  
    + "You can achieve this by using 'sudo' to run your script")

# This will be where we will create our relay class 
class Relay:

    #define our Relay object
    def __init__(self, id, input_state):
        #GPIO pin
        #setup circuit
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        self.pin_id = id
        self.state = input_state

        #set GPIO pin as output pin
        GPIO.setup(self.pin_id, GPIO.OUT)
        #set the GPIO state to either high or low
        GPIO.output(self.pin_id, GPIO.HIGH if self.state else GPIO.LOW)

    #switches the state of the pin to its opposite
    def set_state(self, input_state):
        self.state = input_state
        GPIO.output(self.pin_id, GPIO.HIGH if self.state else GPIO.LOW)
    
    #can you read RelayContainer.py???
    #gets the pin id
    def get_id(self) -> int:
        return self.pin_id
    
    #gets the state of the relay
    def get_relay_state(self) -> bool:
        return self.state

    #prints out the contents of relay
    def to_string(self):
        print("[ID: {0} , State: {1}]".format(self.get_id(), self.get_relay_state()))


    