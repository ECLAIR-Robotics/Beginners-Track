from flask import jsonify, request
import json
from core import app
from Embedded.RelayContainer import RelayContainer
from flask_cors import cross_origin

# @app.before_request
# def before_request():
#   headers = { 'Access-Control-Allow-Origin': '*',
#               'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS', 
#               'Access-Control-Allow-Headers': 'Content-Type' }
  
#   if request.method == 'OPTIONS' or request.method == 'options':
#     return jsonify(headers), 200

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

@app.route("/delete", methods=["DELETE"])
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
    if(rsc.addRelay(data["relayNumber"], data["relay"], data["name"], data["disctiption"])):
        return jsonify({"addRelay": (data["relayNumber"]), "success" : True}), 200 
    else:
        return jsonify({"addRelay": (data["relayNumber"]), "success" : False}), 401
    
@app.route("/relay/add", methods=["POST"])
@cross_origin() 
def create():
    # process the data (request.get_json())
    data = request.get_json()
    rsc = RelayContainer()
    resp = rsc.addRelay(data["id"], False, data["name"], data["desc"])
    if resp:
        # were chillin
        return jsonify({"message": "Added.", "success" : True}), 201
    else:
        return jsonify({"message": "Bad Request.", "success" : False}), 401
        # bad req
        # 401
        pass


'''
    updatedRelayState: true
    success: True
'''
