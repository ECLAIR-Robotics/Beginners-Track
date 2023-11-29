from flask import jsonify, request
import json
from core import app
from Embedded.RelayContainer import RelayContainer
from speech import speech_to_text
from flask_cors import cross_origin

@app.route("/", methods=["GET"]) # route is a decorator
@cross_origin()
def index():
    return jsonify([{"message": "Home Automation API is Running!"}]), 200

@app.route("/relay/update", methods=["PUT"])
@cross_origin()
def relay():
    data = request.get_json()
    rsc = RelayContainer()
    if rsc.setRelay(data["relayNumber"], data["relayState"]):
        return jsonify({"updatedRelayState": (data["relayState"]), "success" : True}), 200 
    else:
        return jsonify({"updatedRelayState": (data["relayState"]), "success" : False}), 201


@app.route("/getAll", methods=["GET"])
@cross_origin()
def total():
    rsc = RelayContainer()
    devices = rsc.getAllDevices()
    dictList = []
    for device in devices:
        dictList.append({ "id": device[0], "state": device[1], "name": device[2], "description": device[3] })

    return jsonify(dictList), 200

@app.route("/delete", methods=["PUT"])
@cross_origin()
def remove():
    rsc = RelayContainer()
    data = request.get_json()
    result = rsc.removeRelay(data["relayNumber"])
    if(result):
        return jsonify({"deleteRelay": (data["relayState"]), "success" : True}), 200 
    return jsonify({"deleteRelay": (data["relayState"]), "success" : False}), 201
    

   
@app.route("/relay/put", methods=["PUT"]) # Want cahs: Post
@cross_origin() 
def add():
    data = request.get_json()
    rsc = RelayContainer()
    if(rsc.addRelay(data["relayNumber"], data["relay"], data["name"], data["description"])):
        return jsonify({"addRelay": (data["relayNumber"]), "success" : True}), 200 
    else:
        return jsonify({"addRelay": (data["relayNumber"]), "success" : False}), 201
    


'''
    updatedRelayState: true
    success: True
'''
