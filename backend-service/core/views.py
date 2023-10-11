from flask import jsonify, request
from core import app
from flask_cors import cross_origin
from embedded import Relay
import RelayContainer


@app.route("/", methods=["GET"])
@cross_origin()
def index():
    con = RelayContainer.RelayContainer()
    return jsonify([{"message": "Home Automation API is Running!"}]), 200


@app.route("/relay/on", methods=["GET"])
def relayOn():
    con = RelayContainer.RelayContainer()
    if (con.getRelay(1)):
        con.getRelay(1).setState(True)
        return jsonify({"Relay has been turned on!"})


@app.route("/relay/off", methods=["GET"])
def relayOff():
    con = RelayContainer.RelayContainer()
    if (con.getRelay(1)):
        con.getRelay(1).setState(False)
        return jsonify({"Relay has been turned off!"})


@app.route("/relay/add", methods=["POST"])
def addRelay():
    con = RelayContainer.RelayContainer()
    con.addRelay(1, True)
    return jsonify({"Relay added."})


@app.route("/relay/delete", methods=["POST"])
def deleteRelay():
    con = RelayContainer.RelayContainer()
    if (con.getRelay(1)):
        con.removeRelay(1)
        return jsonify({"Relay deleted."})
