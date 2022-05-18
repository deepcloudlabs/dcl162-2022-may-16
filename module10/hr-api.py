import json

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO
from pymongo import MongoClient

from hr.util import extract_emp_from_req

app = Flask(__name__)
app.config['DEBUG'] = True
cors = CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

mongo_client = MongoClient("mongodb://localhost:27017")
emp_collection = mongo_client['myhrdb'].employees

fields = ["identity", "fullName", "iban", "photo", "salary", "birthYear", "department", "fulltime"]


@app.route("/hr/api/v1/employees", methods=["GET"])
def get_employees():
    return json.dumps([emp for emp in emp_collection.find({})])


@app.route("/hr/api/v1/employees/<identity>", methods=["GET"])
def get_employee_by_identity(identity):
    return jsonify(emp_collection.find_one({"_id": identity}))


@app.route("/hr/api/v1/employees", methods=["POST"])
def add_employee():
    emp = extract_emp_from_req(request, fields)
    emp_collection.insert_one(emp)
    return jsonify({"status": "ok"})


@app.route("/hr/api/v1/employees/<identity>", methods=["PUT", "PATCH"])
def update_employee(identity):
    emp = extract_emp_from_req(request, fields)
    updated_emp = emp_collection.find_one_and_update(
        {"_id": identity},
        {"$set": emp},
        upsert=False)
    return jsonify(updated_emp)


@app.route("/hr/api/v1/employees/<identity>", methods=["DELETE"])
def remove_employee(identity):
    removed_emp = emp_collection.find_one({"_id": identity})
    emp_collection.delete_one({"_id": identity})
    return jsonify(removed_emp)


socketio.run(app, port=7001)
