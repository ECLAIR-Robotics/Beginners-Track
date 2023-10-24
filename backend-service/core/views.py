from flask import jsonify, request
from core import app
from flask_cors import cross_origin

@app.route("/", methods=["GET"])
@cross_origin()
def index():
    return jsonify({"message": "Home Automation API is Running!"}), 200

