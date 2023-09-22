#make our imports here
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges."  
    + "You can achieve this by using 'sudo' to run your script")

# This will be where we will create our relay class 
class Relay:
    #lets make a list of tuples, each tuple will contain a GPIO pin and then it's status
    
    #make empty list
    chan_list = []
    #run for loop
    for x in range(0,26):
        #make our tubles
        chan_list.append((x+2, 0))


    #define our Relay object
    def __init__(self):

        #GPIO already handles the pins as long as we have the list
        
        #this designates our GPIO pins to correspond to the pins
        GPIO.setmode(GPIO.BOARD)


        print("")


    