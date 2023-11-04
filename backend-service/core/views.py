from flask import jsonify, request
from core import app
from flask_cors import cross_origin
from embedded import Relay
import RelayContainer


'''
query_params = test.args
get request should have nonsensitive data in query params
send info in body of a post request (JSON data)
body = request.json (request.get_data()) (for JSON data, but will raise error for non JSON data)

try:
    body = request.get_data
except Exception as e:
    return jsonify({"message": "Error parsing JSON"}), 400
'''


@app.route("/", methods=["GET"])
@cross_origin()
def index():
    return jsonify([{"message": "Home Automation API is Running!"}]), 200

# ?id=17

@app.route("/relay/on", methods=["GET"])
def relayOn():
    id = request.args.get("id")
    con = RelayContainer.RelayContainer()
    if (con.getRelay(id) & con.getRelay(id).getRelayState() == False):
        con.getRelay(id).setState(True)
        return jsonify([{"message": "Relay has been turned on!"}])
    else:
        return jsonify([{"message": "Relay does not exist or is already on!"}])


@app.route("/relay/off", methods=["GET"])
def relayOff():
    id = request.args.get("id")
    con = RelayContainer.RelayContainer()
    if (con.getRelay(id) & con.getRelay(id).getRelayState() == True):
        con.getRelay(id).setState(False)
        return jsonify([{"message": "Relay does not exist or is already off!"}])


@app.route("/relay/add", methods=["POST"])
def addRelay():
    id = request.form.get("id")
    con = RelayContainer.RelayContainer()
    con.addRelay(id, False)
    allRelays = con.getAllRelays()
    return jsonify([{"message": "Relay added."}, {"relays": allRelays}]), 200


@app.route("/relay/delete", methods=["POST"])
def deleteRelay():
    id = request.form.get("id")
    con = RelayContainer.RelayContainer()
    if (con.getRelay(id)):
        i = 0
        for relay in con.relays:
            if (relay.getID() == id):
                con.popRelay(i)
                return jsonify([{"message": "Relay deleted."}])
            i = i+1
    else:
        return jsonify([{"message": "Relay does not exist."}]), 200

@app.route("/con/clear", methods=["POST"])
def clearCon():
    con = RelayContainer.RelayContainer()
    
    return jsonify([{"message": "Container cleared."}])
