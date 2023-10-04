from flask import jsonify, request
from core import app
from flask_cors import cross_origin
from embedded import Relay
import RelayContainer


@app.route("/", methods=["GET"])
@cross_origin()
def index():
    dictionary1 = {
        "1": "Hello",
        "2": "World"
    }
    # print(dictionary1[1])
    r = RelayContainer.RelayContainer()
    return jsonify({"message": "Home Automation API is Running!"}), 200


@app.route("/relay/on", methods=["GET"])
def relayOn():
    con = RelayContainer.RelayContainer()
    if (con.getRelay(5)):
        con.getRelay(5).setState(True)
        return jsonify({"Relay has been turned on!"})


@app.route("/relay/off", methods=["GET"])
def relayOff():
    con = RelayContainer.RelayContainer()
    if (con.getRelay(5)):
        con.getRelay(5).setState(False)
        return jsonify({"Relay has been turned off!"})


@app.route("/relay/add", methods=["POST"])
def addRelay():
    con = RelayContainer.RelayContainer()
    con.addRelay(5, True)


@app.route("/relay/delete", methods=["POST"])
def deleteRelay():
    con = RelayContainer.RelayContainer()
    if (con.getRelay(5)):
        con.removeRelay(5)
