from flask import jsonify, request
import json
from core import app
from Embedded.RelayContainer import RelayContainer
from flask_cors import cross_origin

@app.before_request
def before_request():
  headers = { 'Access-Control-Allow-Origin': '*',
              'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS', 
              'Access-Control-Allow-Headers': 'Content-Type' }
  
  if request.method == 'OPTIONS' or request.method == 'options':
    return jsonify(headers), 200

@app.route("/", methods=["GET"]) # route is a decorator
@cross_origin()
def index():
    return jsonify({"message": "Home Automation API is Running!"}), 200

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
    json_string = rsc.getAllRelays()
    return jsonify({"relayState": json_string, "success" : True}), 200

@app.route("/delete", methods=["PUT"])
@cross_origin()
def remove():
    
   
   
@app.route("/relay/put", methods=["PUT"]) # Want cahs: Post
@cross_origin() 
def add():
    data = request.get_json()
    rsc = RelayContainer()
    if(rsc.addRelay(data["relayNumber"], data["relay"], data["name"], data["disctiption"])):
        return jsonify({"addRelay": (data["relayNumber"]), "success" : True}), 200 
    else:
        return jsonify({"addRelay": (data["relayNumber"]), "failure" : False}), 201
    


'''
    updatedRelayState: true
    success: True
'''
