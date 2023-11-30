import speech_recognition as sr
import requests as req

# make method that will take in input from microphone and convert it to text

IP = "http://localhost:5000" #NOTE: CHANGE THIS IP WHEN NEEDED!!!!

#ask database what relays exist and put that into a dictionary for acceptable words
gpio_dict = {
    "one": 4,
    "two": 17,
    "three": 27,
    "four": 22,
}


def speech_to_text():
    # initialize the recognizer
    r = sr.Recognizer()

    # open the file
    with sr.Microphone as source:
        # listen for the data (load audio to memory)
        print("Listening...")
        audio = r.record(source)
        # recognize (convert from speech to text)
    try:
        # convert speech to text
        text = r.recognize_google(audio)
        # return text
    except sr.UnknownValueError: text = None
    except sr.RequestError as e: text = None

    #goal is to have it activate a relay
    finally: return text

def main():
    out_text = speech_to_text()
    if (out_text != None): 
        text = out_text.lower().split()
        for i in range(len(text)):
            if text[i] == 'relay':
                id = gpio_dict[text[i+1]]
                action = True if text[i+2] == 'on' else False
                print("relay " + id + " " + action)
        
        #make request to backend api
        r = req.put(IP + "/relay/update", json={"relayNumber": id, "relayState": action})
        #do some error checking
        if (r.status_code == 200):
            print("Success")
        else:
            print("Error")

    


    # Now I need to actually deal with the backend API 
    # I need to make a request to the backend API to update the relay

    # I need to make a request to the backend API to get the state of the relay
    # I need to make a request to the backend API to add a relay

