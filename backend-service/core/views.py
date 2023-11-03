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


@app.route("/relay/on", methods=["GET"])
def relayOn():
    con = RelayContainer.RelayContainer()
    if (con.getRelay(17)):
        con.getRelay(17).setState(True)
        return jsonify({"Relay has been turned on!"})


@app.route("/relay/off", methods=["GET"])
def relayOff():
    con = RelayContainer.RelayContainer()
    if (con.getRelay(17)):
        con.getRelay(17).setState(False)
        return jsonify({"Relay has been turned off!"})


@app.route("/relay/add", methods=["POST"])
def addRelay():
    con = RelayContainer.RelayContainer()
    con.addRelay(17, False)
    return jsonify([{"message": "Relay added."}]), 200


@app.route("/relay/delete", methods=["POST"])
def deleteRelay():
    con = RelayContainer.RelayContainer()
    if (con.getRelay(17)):
        con.removeRelay(17)
        return jsonify({"Relay deleted."})
