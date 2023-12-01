import speech_recognition as sr
import requests as req

# make method that will take in input from microphone and convert it to text

IP = "http://10.159.64.100:5000" #NOTE: CHANGE THIS IP WHEN NEEDED!!!!

#ask database what relays exist and put that into a dictionary for acceptable words
gpio_dict = {
    "one": 4,
    "two": 17,
    "three": 27,
    "four": 22,
    "1": 4,   
    "2": 17,
    "3": 27,
    "4": 22,

}


def speech_to_text():
    # initialize the recognizer
    r = sr.Recognizer()

    # open the file
    with sr.Microphone() as source:
        # listen for the data (load audio to memory)
        print("Listening...")
        audio = r.record(source, duration=5)
        # recognize (convert from speech to text)
    try:
        # convert speech to text
        text = r.recognize_google(audio)
        print("You said: ", text)
        # return text
    except sr.UnknownValueError: text = None
    except sr.RequestError as e: text = None

    #goal is to have it activate a relay
    finally: return text

def make_request(text):
    if 'relay' not in text and 'relays' not in text:
        print("Error: relay keyword not found\n")
        return
    elif 'relays' in text:
        i = text.index('relays')
        state = 'on' in text or 'activate' in text
        for id in list(gpio_dict.values())[:4]:
            update_relay(id, state)
    else:
        i = text.index('relay')
        #check if the word after relay is number form, 1, 2, 3, 4
        if text[i+1] in gpio_dict:
            id = gpio_dict[text[i+1]]
        else:
            print(f"Key '{text[i+1]}' not found in gpio_dict")
            return
        action = True if text[i+2] == 'on' else False
        print("relay {id} is {action}".format(id=id, action=action))

def update_relay(id, action):
    #make request to backend api to update relay
    r = req.put(IP + "/relay/update", json={"relayNumber": id, "relayState": action})
    #do some error checking
    if (r.status_code == 200):
        print("Success")
    else:
        print("Error")
    print("\n")

def main():
    try:
        input("Press enter to start recording...")
        out_text = speech_to_text()
        if (out_text != None): 
            make_request(out_text.lower().split())
    except KeyboardInterrupt:
        return False
        
    return True

    
if __name__ == "__main__":
   program_running = True
   while program_running:
        program_running = main()
    
print("\nProgram ending...")

    # Now I need to actually deal with the backend API 
    # I need to make a request to the backend API to update the relay

    # I need to make a request to the backend API to get the state of the relay
    # I need to make a request to the backend API to add a relay

