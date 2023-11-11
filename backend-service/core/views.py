from flask import jsonify, request
from core import app
from flask_cors import cross_origin
from embedded.RelayControl import RelayContainer


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


@app.route("/relay/add", methods=["POST"])
def addRelay():
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify([{"message": "Error parsing JSON"}]), 400
    con = RelayContainer()
    added = con.addRelay(data["id"], data["state"])
    if added:
        return jsonify([{"message": "Relay added."}, {"relays": con.getAllRelays()}])
    else:
        return jsonify([{"message": "Relay exists."}, {"relays": con.getAllRelays()}])


@app.route("/relay/delete", methods=["PUT"])
def deleteRelay():
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify([{"message": "Error parsing JSON"}]), 400
    con = RelayContainer()
    deleted = con.popRelay(data["id"])
    if deleted:
        return jsonify([{"message": "Relay deleted."}, {"relays": con.getAllRelays()}])
    else:
        return jsonify([{"message": "Relay does not exist."}, {"relays": con.getAllRelays()}])


@app.route("/relay/on", methods=["GET"])
def relayOn():
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify([{"message": "Error parsing JSON"}]), 400
    con = RelayContainer()
    if(con.checkExistence(data["id"])):
        con.updateRelay(data["id"], True)
        return jsonify([{"message": "Relay has been turned on or was already on!"}])
    else:
        return jsonify([{"message": "Relay does not exist!"}])


@app.route("/relay/off", methods=["GET"])
def relayOff():
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify([{"message": "Error parsing JSON"}]), 400
    con = RelayContainer()
    if(con.checkExistence(data["id"])):
        con.updateRelay(data["id"], False)
        return jsonify([{"message": "Relay has been turned off or was already off!"}])
    else:
        return jsonify([{"message": "Relay does not exist!"}])


@app.route("/relay/all", methods=["GET"])
def getAllRelays():
    con = RelayContainer()
    allRelays = con.getAllRelays()
    return jsonify([{"relays": allRelays}])


@app.route("/con/clear", methods=["POST"])
def clearCon():
    con = RelayContainer.RelayContainer()
    con.clearAll()
    allRelays = con.getAllRelays()
    return jsonify([{"message": "Container cleared."}, {"relays": allRelays}]), 200
