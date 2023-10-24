from flask import jsonify, request
from core import app
from Embedded.RelayContainer import RelayContainer
from flask_cors import cross_origin

@app.route("/", methods=["GET"]) # route is a decorator
@cross_origin()
def index():
    return jsonify({"message": "Home Automation API is Running!"}), 200

