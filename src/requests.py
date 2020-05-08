from flask import request, Blueprint
from src.db import API
requests = Blueprint('requests', __name__)

db = API()


@requests.route('/get_data', methods=["GET"])
def get_data():
    key = request.args.get("key")
    resp = db.read_data(key)
    if resp is None:
        resp = {}
    return resp


@requests.route('/write_data', methods=["PUT"])
def upsert_data():
    resp = db.write_data(request.json['key'], request.json['data'])
    if resp is None:
        return {}
    return resp
