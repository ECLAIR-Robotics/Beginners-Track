from flask import jsonify, request
from core import app
from flask_cors import cross_origin
from embedded import Relay
import RelayContainer

@app.route("/", methods=["GET"])
@cross_origin()
def index():
    dictionary1 = {
        1: "Hello",
        2: "World"
    }
    print(dictionary1[1])
    r = RelayContainer()
    return jsonify({"message": "Home Automation API is Running!"}), 200


@app.route("/relay/on", methods = ["GET"])


@app.route("/add", methods=["GET"])
def addTwoNumbers(a : int , b : int) -> int:
    return a + b
